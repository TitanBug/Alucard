"""
# KubeAudit TUI

A terminal-based Kubernetes misconfiguration scanner with a TUI interface. Uses `rules.yaml` to perform checks and can optionally explain issues using GPT.

## Features
- Scans Kubernetes pods
- Flags common misconfigurations (privileged, run-as-root, default SA)
- Terminal UI using Textual
- Optional OpenAI explanation for findings
- Colorful banner using Rich
- Beautified output and summary

## Requirements
- Python 3.8+
- Kubernetes cluster access (`kubectl` must be configured and working)
- Linux/macOS/WSL (recommended)
- (Optional) OpenAI API Key for GPT feedback

## Installation
```bash
git clone https://github.com/yourusername/kubeaudit-tui.git
cd kubeaudit-tui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to Run
```bash
# (Optionally set your OpenAI API key)
export OPENAI_API_KEY=your-key-here
python main.py
```

## Usage Manual
1. Ensure you are connected to a Kubernetes cluster and `kubectl` is working.
2. Run the tool: `python main.py`
3. The tool will:
   - Display a banner and notice
   - Scan your cluster for common misconfigurations
   - Show a TUI interface with the results
   - Highlight risky configurations in red
   - If `OPENAI_API_KEY` is set, explain risks inline with GPT

## License & Disclaimer
Created by **Brian Bange**. This tool is provided for **ethical and educational use only**.
Use of this software for unauthorized or malicious purposes is strictly prohibited. The creator holds **no responsibility** for misuse.
"""
