# Use the latest version of the pangeo/base-image
FROM pangeo/base-image:latest

# Define the user
USER root

# Copy the environment and requirements files into the Docker image
COPY environment.yml /tmp/environment.yml

# Create a new Conda environment from the environment.yml file
RUN conda env create -f /tmp/environment.yml

# Install wget, git, ncdu, and curl
RUN apt-get update && apt-get install -y \
    wget \
    git \
    ncdu \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
