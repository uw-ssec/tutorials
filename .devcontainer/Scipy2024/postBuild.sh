# These commands will be run after the devcontainer is built.

# Setup Conda environment
conda env create -f ~/.devcontainer/SciPy2024/environment.yml # Create environment from environment.yml
conda init bash # Initialize conda for bash
source ~/.bashrc # Reload bash
conda activate scipy2024 # Activate the environment