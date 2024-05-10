import os
from pathlib import Path
from urllib.request import urlretrieve

HOME_DIR = Path.home()
CACHE_DIR = HOME_DIR / ".cache"
TUTORIAL_CACHE = CACHE_DIR / "ssec_tutorials"
TUTORIAL_CACHE.mkdir(parents=True, exist_ok=True)

OLMO_MODEL_FILE = os.environ.get("OLMO_MODEL_FILE", "OLMo-7B-Instruct-Q4_K_M.gguf")
OLMO_MODEL = TUTORIAL_CACHE / OLMO_MODEL_FILE

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

