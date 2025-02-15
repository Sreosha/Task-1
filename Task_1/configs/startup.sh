#!/bin/bash
cd ../

echo "Activating the Conda environment..."
conda activate task_1
echo "Starting Ollama..."
ollama start
echo "Pulling the llama3 model from Ollama..."
ollama pull llama3
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
