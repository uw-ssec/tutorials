# Python Environment Setup

This tutorial can be set up in three ways: Nebari, GitHub Codespaces, or Conda.

During the tutorial, to follow along, we recommend using [**Nebari**](#nebari)
for ease of use, as you won't need to worry about setting up the compute
environment. However, if you would like to set up the tutorial on your local
machine, you can use [**Conda**](#conda).

Another option is to use [**GitHub Codespaces**](#github-codespaces), which is a
cloud-based development environment that's hosted in the cloud. This option is
available indefinitely, but you will be limited in the free resources you can
use with GitHub Codespaces.

## 🪴 Nebari

```{note}
Day of Access Only, with a good amount of resources
```

For ease of use, we recommend using **Nebari**. The Nebari platform is a
cloud-based platform that provides a JupyterLab Interface. Nebari is developed
and hosted by [Quansight](https://quansight.com/). It is a great way to run the
tutorial materials without having to install anything on your local machine.
However, this will only be available on the **day of the tutorial ONLY**. You
will receive a coupon code with details to access Nebari.

You can find details about using Nebari in the
[Participant Guide](https://tinyurl.com/nebari-guide-scipy2024).

## 🐱‍💻 GitHub Codespaces

```{note}
Indefinite Access, but Limited Resources
```

This tutorial is available to run within
[Github Codespaces](https://github.com/features/codespaces) - "a development
environment that's hosted in the cloud" - with the conda packages specification
in the
[`conda-lock.yml`](https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/conda-lock.yml)
file. However, you will be **limited in the free resources** you can use with
GitHub Codespaces and you need to have a GitHub account to use GitHub
Codespaces.

A codespace is a development environment that's hosted in the cloud. You are
able to chose from various Dev container configuration, for this specific
workshop, please ensure that `Scipy2024` is selected. GitHub currently gives
every user
[120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts),
beyond that you must pay. **So be sure to explicitly stop or shut down your
codespace when you are done by going to this page
(https://github.com/codespaces).**

<a title="Create New Scipy 2024 Codespaces" href="https://github.com/codespaces/new/uw-ssec/tutorials/tree/main?devcontainer_path=.devcontainer%2FScipy2024%2Fdevcontainer.json&quickstart=1" target="_blank"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"/></a>

☝️ Click the button above to go to options window to launch a Github codespace.

## 🐍 Conda

```{note}
Most Persistent, but requires local setup that take time and may differ from the tutorial environment
```

You can set up the tutorial locally using a Conda environment. Here's how:

0. Downloading and Installing Conda

   If you don't have Conda installed, we recommend following the instruction to
   downloadn and install the
   [Miniforge distribution](https://github.com/conda-forge/miniforge) >=
   `Miniforge3-22.3.1-0` of Conda. This distribution is a minimal installer for
   conda specifically optimized for [conda-forge](https://conda-forge.org/)
   (Community-led recipes, infrastructure and distributions for conda.).

1. Create a new Conda environment called `ssec-scipy2024` with
   [`conda-lock`](https://github.com/conda/conda-lock) package installed. This
   package is used to install the exact versions of the packages in the
   [`conda-lock.yml`](https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/conda-lock.yml)
   file.

   **Note: Ensure that you are using Python Version 3.11. The command below will
   install a clean conda environment with just Python 3.11, conda-lock, and
   their dependencies**

   ```bash
   conda create --yes -n ssec-scipy2024 python=3.11 conda-lock
   ```

2. Activate the conda environment:

   ```bash
   conda activate ssec-scipy2024
   ```

3. Download the
   <a title="SciPy2024 Conda Lock File" href="https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/conda-lock.yml" download>conda
   lock file</a>:

   _The example below uses `wget` to download the file. If you don't have `wget`
   installed, you can download the file directly from
   [github](https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/conda-lock.yml)
   by clicking the download
   (<svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg>)
   button on the right side of page_

   ```bash
   wget https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/conda-lock.yml
   ```

4. Install the packages for the tutorial using `conda-lock`:

   ```bash
   conda-lock install -n ssec-scipy2024 conda-lock.yml
   ```

5. Clone the tutorial repository:

   ```bash
   git clone https://github.com/uw-ssec/tutorials.git
   ```

6. Navigate to the tutorial directory:

   ```bash
   cd tutorials/
   ```

7. Download the tutorial data with the provided
   [`download.py`](../../resources/download_data.py) script in the `resources`
   directory. This includes the OLMo data, copy of the vector database, and
   others. The data are downloaded to `~/.cache/ssec-tutorials/` directory:

   ```bash
   python resources/download_data.py
   ```

8. Navigate to the tutorial directory:

   ```bash
   cd SciPy2024
   ```

9. Run Jupyter Lab:

   ```bash
   jupyter lab
   ```

10. Navigate to the specific tutorial notebook you would like to run. For
    guidance on using the Jupyter Lab interface, see the
    [Jupyter Lab documentation](https://jupyterlab.readthedocs.io/en/stable/user/interface.html).
