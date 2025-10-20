#!/usr/bin/env bash
set -euo pipefail

ENV_NAME=cosyvoice
PYTHON_VERSION=3.10

echo "Creating conda environment '${ENV_NAME}' with Python ${PYTHON_VERSION}..."
conda create -n "${ENV_NAME}" -y python="${PYTHON_VERSION}"
echo "Activate it with: conda activate ${ENV_NAME}"
echo "Installing requirements.txt if present..."
if [ -f requirements.txt ]; then
  conda activate "${ENV_NAME}"
  pip install -r requirements.txt
else
  echo "No requirements.txt found in repo root. Please run pip install manually after activating the env."
fi

echo "Ensure git lfs is installed if you need to fetch large model files."
echo "For macOS (homebrew): brew install git-lfs && git lfs install"

echo "Setup complete."
