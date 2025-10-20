#!/usr/bin/env bash
set -euo pipefail

MODEL_DIR=${1:-pretrained_models/CosyVoice-300M}
OUT_WAV=${2:-demo_out.wav}

echo "Activate your conda env first: conda activate cosyvoice"
echo "Running demo with MODEL_DIR=${MODEL_DIR} OUT_WAV=${OUT_WAV}"
python3 scripts/demo_tts.py "${MODEL_DIR}" "${OUT_WAV}"
