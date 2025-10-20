#!/usr/bin/env python3
"""Simple demo to run CosyVoice inference and save a WAV output.

Usage:
  python3 scripts/demo_tts.py [MODEL_DIR] [OUT_WAV]

MODEL_DIR defaults to pretrained_models/CosyVoice-300M
"""
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT)
sys.path.append(os.path.join(ROOT, 'third_party', 'Matcha-TTS'))

def main():
    model_dir = sys.argv[1] if len(sys.argv) > 1 else 'pretrained_models/CosyVoice-300M'
    out_wav = sys.argv[2] if len(sys.argv) > 2 else 'demo_out.wav'
    text = '你好，這是 CosyVoice 的測試語音。'
    speaker = '中文女'

    if not os.path.isdir(model_dir):
        print(f"Model directory '{model_dir}' not found.\nPlease download the model and place it under '{model_dir}', see DEV_SETUP.md for instructions.")
        sys.exit(2)

    try:
        from cosyvoice.cli.cosyvoice import CosyVoice
        import torchaudio
    except Exception as e:
        print('Failed to import CosyVoice or torchaudio:', e)
        print('Make sure you activated the conda env and installed requirements (see DEV_SETUP.md).')
        sys.exit(3)

    print('Loading model from', model_dir)
    cosy = CosyVoice(model_dir, load_jit=False, load_trt=False, load_vllm=False, fp16=False)

    print('Running inference...')
    try:
        for i, item in enumerate(cosy.inference_sft(text, speaker, stream=False)):
            wav = item.get('tts_speech')
            if wav is None:
                print('Inference returned no audio for item', i)
                continue
            outfile = out_wav if i == 0 else out_wav.replace('.wav', f'_{i}.wav')
            torchaudio.save(outfile, wav, cosy.sample_rate)
            print('Saved', outfile)
    except Exception as e:
        print('Inference failed:', e)
        sys.exit(4)


if __name__ == '__main__':
    main()
