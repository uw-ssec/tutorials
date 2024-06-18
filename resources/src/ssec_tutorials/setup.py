import os
from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile
import requests
from langchain.schema import Document

HOME_DIR = Path.home()
CACHE_DIR = HOME_DIR / ".cache"
TUTORIAL_CACHE = CACHE_DIR / "ssec_tutorials"
TUTORIAL_CACHE.mkdir(parents=True, exist_ok=True)

OLMO_MODEL_FILE = os.environ.get("OLMO_MODEL_FILE", "OLMo-7B-Instruct-Q4_K_M.gguf")
OLMO_MODEL = TUTORIAL_CACHE / OLMO_MODEL_FILE

# Set the URL for tutorials data assets
TUTORIALS_DATA_URL = (
    "https://github.com/uw-ssec/tutorials-data/releases/download/scipy-2024/"
)

# Set the default file name for the astro-ph arXiv abstracts
ASTROPH_ARXIV_ABSTRACTS_FILE = os.environ.get(
    "ASTROPH_ARXIV_ABSTRACTS_FILE", "astro-ph-arXiv-abstracts.pkl"
)
ASTROPH_ARXIV_ABSTRACTS = TUTORIAL_CACHE / ASTROPH_ARXIV_ABSTRACTS_FILE

# Set the default file name for the astropy github documents
ASTROPY_GITHUB_FILE = os.environ.get("ASTROPY_GITHUB_FILE", "astropy-github.jsonl")
ASTROPY_GITHUB = TUTORIAL_CACHE / ASTROPY_GITHUB_FILE

QDRANT_ZIP_FILE = os.environ.get("QDRANT_ZIP_FILE", "scipy_qdrant_100k.zip")
QDRANT_FOLDER_NAME = os.environ.get("QDRANT_FOLDER_NAME", "scipy_qdrant")
QDRANT_PATH = TUTORIAL_CACHE / QDRANT_FOLDER_NAME
QDRANT_COLLECTION_NAME = "arxiv_astro-ph_abstracts_astropy_github_documentation"


def download_all_tutorial_data(force=False):
    """Download all tutorial data assets."""

    download_olmo_model(force=force)
    download_astroph_arxiv_abstracts(force=force)
    download_astropy_github_documents(force=force)
    download_qdrant_data(force=force)


def download_olmo_model(model_file: str | None = None, force=False) -> Path:
    """Download the OLMO model from the Hugging Face model hub.

    Parameters
    ----------
    model_file : str | None, optional
        The name of the model file to download, by default None
    force : bool, optional
        Whether to force the download even if the file already exists, by default False

    Returns
    -------
    pathlib.Path
        The path to the downloaded model file
    """

    if not OLMO_MODEL.exists() or force:
        if model_file is None:
            model_file = OLMO_MODEL_FILE
            olmo_model = OLMO_MODEL
        else:
            olmo_model = TUTORIAL_CACHE / model_file
        olmo_model_url = f"https://huggingface.co/ssec-uw/OLMo-7B-Instruct-GGUF/resolve/main/{model_file}"
        urlretrieve(olmo_model_url, olmo_model)
        return olmo_model
    else:
        print(f"Model already exists at {OLMO_MODEL}")
        return OLMO_MODEL


def download_astroph_arxiv_abstracts(
    abstracts_file: str | None = None, force=False
) -> Path:
    """Download the astro-ph arXiv abstracts from the tutorials data repository.

    Parameters
    ----------
    abstracts_file : str | None, optional
        The name of the abstracts file to download, by default None
    force : bool, optional
        Whether to force the download even if the file already exists, by default False

    Returns
    -------
    pathlib.Path
        The path to the downloaded abstracts file
    """

    if not ASTROPH_ARXIV_ABSTRACTS.exists() or force:
        if abstracts_file is None:
            abstracts_file = ASTROPH_ARXIV_ABSTRACTS_FILE
            astroph_arxiv_abstracts = ASTROPH_ARXIV_ABSTRACTS
        else:
            astroph_arxiv_abstracts = TUTORIAL_CACHE / abstracts_file
        astroph_arxiv_abstracts_url = f"{TUTORIALS_DATA_URL}{abstracts_file}"
        urlretrieve(astroph_arxiv_abstracts_url, astroph_arxiv_abstracts)
        return astroph_arxiv_abstracts
    else:
        print(f"astro-ph arXiv abstracts already exist at {ASTROPH_ARXIV_ABSTRACTS}")
        return ASTROPH_ARXIV_ABSTRACTS


def download_astropy_github_documents(
    github_file: str | None = None, force=False
) -> Path:
    """
    Downloads Astropy GitHub LandChain Documents from the specified file or the default file if not provided.

    Args:
        github_file (str | None, optional): The name of the GitHub file to download. If not provided, the default file will be used. Defaults to None.
        force (bool, optional): If True, the download will be forced even if the file already exists. Defaults to False.

    Returns:
        Path: The path to the downloaded Astropy GitHub file that contains LangChain Documents.

    Raises:
        None

    """

    if not ASTROPY_GITHUB.exists() or force:
        if github_file is None:
            github_file = ASTROPY_GITHUB_FILE
            astropy_github = ASTROPY_GITHUB
        else:
            astropy_github = TUTORIAL_CACHE / github_file
        astropy_github_url = f"{TUTORIALS_DATA_URL}{github_file}"
        urlretrieve(astropy_github_url, astropy_github)
        return astropy_github
    else:
        print(f"Astropy github files already exist at {ASTROPY_GITHUB}")
        return ASTROPY_GITHUB


def download_qdrant_data(qdrant_file: str | None = None, force=False) -> Path:
    """
    Downloads the Qdrant data from the tutorials data repository.

    Parameters
    ----------
    qdrant_file: str | None, optional
        The name of the Qdrant file to download, by default None
    force : bool, optional
        Whether to force the download even if the file already exists, by default False

    Returns
    -------
    pathlib.Path
        The path to the downloaded Qdrant data
    """

    if not QDRANT_PATH.exists() or force:
        if qdrant_file is None:
            qdrant_file = QDRANT_ZIP_FILE
            qdrant_zip = TUTORIAL_CACHE / QDRANT_ZIP_FILE
        else:
            qdrant_zip = TUTORIAL_CACHE / qdrant_file
        qdrant_zip_url = f"{TUTORIALS_DATA_URL}{qdrant_file}"
        urlretrieve(qdrant_zip_url, qdrant_zip)

        with ZipFile(qdrant_zip, "r") as zip_ref:
            zip_ref.extractall(TUTORIAL_CACHE)

        if os.path.exists(qdrant_zip):
            os.remove(qdrant_zip)

        return TUTORIAL_CACHE / qdrant_file.replace(".zip", "")
    else:
        print(f"Qdrant data already exists at {QDRANT_PATH}")
        return QDRANT_PATH


def fetch_and_process_github_rst_files(
    github_repo: str,
    github_branch: str,
    docs_path: str,
    github_personal_access_token: str,
) -> list[Document]:
    """
    Recursively fetch and process RST files from a GitHub repository.

    Args:
        github_repo (str): The name of the GitHub repository.
        github_branch (str): The branch of the GitHub repository.
        docs_path (str): The path to the RST files in the GitHub repository.

    Returns:
        list: A list of LangChain Document objects containing the page content and metadata.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request to the GitHub API fails.
    """
    base_url = f"https://api.github.com/repos/{github_repo}/contents/{docs_path}?ref={github_branch}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_personal_access_token}",
    }
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()  # This will raise an error for failed requests
    files = response.json()

    documents = []
    for file in files:
        if file["type"] == "dir":  # This is a directory; recurse into it
            documents.extend(
                fetch_and_process_github_rst_files(
                    github_repo,
                    github_branch,
                    file["path"],
                    github_personal_access_token,
                )
            )
        elif file["name"].endswith(".rst"):
            file_url = file["download_url"]
            response = requests.get(file_url, headers=headers)
            response.raise_for_status()
            title = file["name"].replace(".rst", "").replace("_", " ").title()
            documents.append(
                Document(
                    page_content=response.text,
                    metadata={"title": title, "url": file_url},
                )
            )

    return documents
