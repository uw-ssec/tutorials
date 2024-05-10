#/bin/bash -l

export RESOURCES_DIR=./resources

# Download the OLMo GGUF Model
cd ${RESOURCES_DIR} \
&& wget https://huggingface.co/ssec-uw/OLMo-7B-Instruct-GGUF/resolve/main/OLMo-7B-Instruct-Q4_K_M.gguf \
&& cd -

# Install the tutorials helper package
pip install -e "${RESOURCES_DIR}"
