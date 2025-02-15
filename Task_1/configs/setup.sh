#!/bin/bash

ENV_FILE_PATH="../environment.yml"
cd $(dirname "$ENV_FILE_PATH")
echo "Creating Conda environment from $ENV_FILE_PATH..."
conda env create -f environment.yml
