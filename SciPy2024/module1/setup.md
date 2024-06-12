# Python Environment Setup

This tutorial can be set up in three ways: using GitHub Codespaces, Docker containers, or Conda environment.

## Using GitHub Codespaces

This tutorial is available to run within [Github Codespaces](https://github.com/features/codespaces) - "a development environment that's hosted in the cloud" - with the conda environment specification in the [`environment.yml`](https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/environment.yml) file.

<a title="Create New Scipy 2024 Codespaces" href="https://github.com/codespaces/new/uw-ssec/tutorials/tree/main?devcontainer_path=.devcontainer%2FScipy2024%2Fdevcontainer.json&quickstart=1" target="_blank"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"/></a>

☝️ Click the button above to go to options window to launch a Github codespace.

A codespace is a development environment that's hosted in the cloud.
You are able to chose from various Dev container configuration, for this specific workshop, please ensure that `Scipy2024` is selected.
GitHub currently gives every user [120 vCPU hours per month for free](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts), beyond that you must pay. **So be sure to explicitly stop or shut down your codespace when you are done by going to this page (https://github.com/codespaces).**

## Using a Conda Environment

You can set up the tutorial locally using a Conda environment. Here's how:

1. Download the environment file by clicking <a title="SciPy2024 Environment File" href="https://raw.githubusercontent.com/uw-ssec/docker-images/main/tutorial-scipy-2024/environment.yml" download>this link</a>.

2. Create the Conda environment:

    ```bash
    conda env create -f environment.yml
    ```

3. Activate the Conda environment:

    ```bash
    conda activate scipy-2024
    ```

4. Clone the tutorial repository:

    ```bash
    git clone https://github.com/uw-ssec/tutorials.git
    ```

5. Navigate to the tutorial directory:

    ```bash
    cd tutorials/SciPy2024
    ```

## Using Docker

Alternatively, you can set up the tutorial locally using Docker. Here's how:

1. Pull the Docker image using the following command:

    ```bash
    docker pull ghcr.io/uw-ssec/tutorial-scipy-2024:latest --platform linux/x86_64
    ```

    > Note: The "no matching manifest for linux/arm64/v8 in the manifest list entries" error occurs if you do not include the platform flag for Apple Silicon systems

2. Once the image is pulled, you can run a container with the image:

    ```bash
    docker run -p 8888:8888 --platform linux/x86_64 -it ghcr.io/uw-ssec/tutorial-scipy-2024:latest bash
    ```

    This command will open an interactive container with a bash shell.

3. Clone the tutorial into the container:

    ```bash
    git clone https://github.com/uw-ssec/tutorials.git
    ```

    > Note: If you exit the container, run `docker ps -l` for the Container ID and `docker start -i <container_id>` to pick up where you left off.

    Now, you can navigate to the tutorial directory and start the tutorial.

> Note: If you would like to share your work with the rest of your team or have a reminder of the work you do in this tutorial, you can write your container to a new docker image. You can do that by running `docker commit <container_id> <new_image_name>` in your terminal.
