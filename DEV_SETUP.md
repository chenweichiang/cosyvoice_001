# 快速上手 — CosyVoice (forked upstream)

這份文件說明如何在本機快速準備環境並執行 CosyVoice 的基本示範。

## 1. 建立 Conda 環境（建議）

在終端執行：

```bash
bash scripts/setup_conda.sh
# 然後
conda activate cosyvoice
```

如果你沒有 Conda，請先安裝 Miniconda/Anaconda。

## 2. Git LFS（如果需要下載大型模型檔）

```bash
brew install git-lfs
git lfs install
```

## 3. 下載預訓練模型（自行選擇）

上游提供了多種模型：`CosyVoice2-0.5B`, `CosyVoice-300M`, `CosyVoice-300M-SFT` 等。你可以使用 `modelscope` 或直接用 git clone（需 git lfs）：

```bash
# 範例：
mkdir -p pretrained_models
git clone https://www.modelscope.cn/iic/CosyVoice-300M.git pretrained_models/CosyVoice-300M
```

或使用 `modelscope` 的 Python API（請先安裝 modelscope）：

```python
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
```

## 4. 嘗試啟動 demo（本地）

進入專案根目錄並依 README 提示執行，例如啟動 web demo：

```bash
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M
```

注意：部分功能需要 GPU / 特殊 runtime（如 triton、TensorRT），請參考上游 README。

## 5. 建議的開發流程

- 在 `main` 之外建立 `dev` 分支來做開發：

```bash
git checkout -b dev
```

- 若要同步上游更新：

```bash
git fetch upstream
git merge upstream/main
```

## 其他
- 如果你想要我幫你新增 CI、或建立一個小 demo script 來產生一段 TTS audio，告訴我你偏好的模型（例如 CosyVoice-300M 或 CosyVoice2-0.5B），我可以幫你寫並測試。 
