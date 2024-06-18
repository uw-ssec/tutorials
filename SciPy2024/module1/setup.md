# Python Environment Setup

This tutorial can be set up in two ways: using GitHub Codespaces or Conda
environment. For ease of use, we recommend using GitHub Codespaces. However, you
will be limited in the free resources you can use with GitHub Codespaces, see
below for details.

## Using GitHub Codespaces

This tutorial is available to run within
[Github Codespaces](https://github.com/features/codespaces) - "a development
environment that's hosted in the cloud" - with the conda environment
specification in the
[`environment.yml`](https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/environment.yml)
file.

<a title="Create New Scipy 2024 Codespaces" href="https://github.com/codespaces/new/uw-ssec/tutorials/tree/main?devcontainer_path=.devcontainer%2FScipy2024%2Fdevcontainer.json&quickstart=1" target="_blank"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"/></a>

☝️ Click the button above to go to options window to launch a Github codespace.

A codespace is a development environment that's hosted in the cloud. You are
able to chose from various Dev container configuration, for this specific
workshop, please ensure that `Scipy2024` is selected. GitHub currently gives
every user
[120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts),
beyond that you must pay. **So be sure to explicitly stop or shut down your
codespace when you are done by going to this page
(https://github.com/codespaces).**

## Using a Conda Environment

You can set up the tutorial locally using a Conda environment. Here's how:

1. Download the
   <a title="SciPy2024 Environment File" href="https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/environment.yml" download>environment
   file</a>:

   _The example below uses `wget` to download the file. If you don't have `wget`
   installed, you can download the file directly from
   [github](https://github.com/uw-ssec/docker-images/blob/main/tutorial-scipy-2024/environment.yml)
   by clicking the download
   (<svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg>)
   button on the right side of page_

   ```bash
   wget https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/environment.yml
   ```

2. Create the Conda environment:

   ```bash
   conda env create -f environment.yml
   ```

3. Activate the Conda environment:

   ```bash
   conda activate ssec-scipy2024
   ```

4. Clone the tutorial repository:

   ```bash
   git clone https://github.com/uw-ssec/tutorials.git
   ```

5. Navigate to the tutorial directory:

   ```bash
   cd tutorials/
   ```

6. Install internal package:

   ```bash
   pip install -e './resources'
   ```

7. Navigate to the tutorial directory:

   ```bash
   cd SciPy2024
   ```

8. Run Jupyter Lab:

   ```bash
   jupyter lab
   ```
