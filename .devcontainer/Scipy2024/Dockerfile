# # Use the Pangeo base image
# ARG PANGEO_BASE_IMAGE_TAG=master
# FROM pangeo/base-image:${PANGEO_BASE_IMAGE_TAG}

# # Copy the environment.yaml file into the Docker image
# COPY environment.yaml /tmp/environment.yaml

# # Use the conda command to create a new environment from the environment.yaml file
# RUN conda env create -f ~/.devcontainer/environment.yaml
# RUN conda init bash
# RUN echo "conda activate ssec-scipy2024" >> ~/.bashrc

# Use the latest version of the pangeo/base-image
FROM pangeo/base-image:latest

USER root

# Copy the environment and requirements files into the Docker image
COPY environment.yml /tmp/environment.yml
COPY requirements.txt /tmp/requirements.txt

# Create a new Conda environment from the environment.yml file
RUN conda env create -f /tmp/environment.yml

# Make RUN commands use the new environment:
# SHELL ["conda", "run", "-n", "swarm-data-science", "/bin/bash", "-c"]

# Install wget, git, ncdu, and curl
RUN apt-get update && apt-get install -y \
    wget \
    git \
    ncdu \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set jovyan as the owner of everything under ${HOME}
# RUN chown -R jovyan:jovyan ${HOME}

# USER ${NB_USER}
