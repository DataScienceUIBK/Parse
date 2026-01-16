# Parse: An Open-Domain Reasoning Question Answering Benchmark for Persian

[![Hugging Face Dataset](https://img.shields.io/badge/HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/JamshidJDMY/Parse)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/Paper-PDF-blue)](interface/An_Open_Domain_Reasoning_Question_Answering_Benchmark_for_Persian.pdf)

Parse is an **open-domain Persian reasoning QA benchmark** designed to evaluate reasoning-capable QA systems and LLMs in a low-resource language setting.  
It includes diverse question formats (Boolean / Multiple-choice / Factoid), reasoning dimensions (Multihop / Reasoning), and difficulty levels (Easy / Medium / Hard).

This repository contains:
- The dataset files (train/test/full)
- Prompt templates used for question generation
- Evaluation scripts for **Zero-shot**, **Few-shot**, and **Chain-of-Thought** prompting
- Fine-tuning utilities (TogetherAI formatting & uploader script)
- Human evaluation interfaces for quality and difficulty validation

---

## 📌 Dataset on HuggingFace

You can download the dataset directly from HuggingFace:

**🤗 HuggingFace Dataset:** `JamshidJDMY/Parse`  
https://huggingface.co/datasets/JamshidJDMY/Parse

---

## 🚀 Quick Start (HuggingFace Datasets)

Install dependencies:

```bash
pip install datasets
```

Load dataset:

```python
from datasets import load_dataset

ds = load_dataset("JamshidJDMY/Parse")

print(ds)
print(ds["train"][0])
```

---

## 🔁 Reproducibility (Minimal Setup)

This repo includes ready-to-run scripts for evaluation under:
- **Zero-shot**
- **Few-shot**
- **Chain-of-Thought**

### 1) Install environment

It is recommended to use Python 3.10+:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows
```

Install core requirements:

```bash
pip install -U pip
pip install datasets numpy tqdm pandas scikit-learn
```

> If you use API-based models (Together / OpenAI / etc.), you may need to install additional SDKs
> and set the corresponding API keys depending on your setup.

---

### 2) Run evaluation scripts

#### ✅ Zero-shot
```bash
cd evaluation/zero_shot
bash boolean_sh.sh
bash multichoice_sh.sh
bash factoid_sh.sh
```

#### ✅ Few-shot
```bash
cd evaluation/few_shot
bash boolean_sh.sh
bash multichoice_sh.sh
bash factoid_sh.sh
```

#### ✅ Chain-of-Thought (CoT)
```bash
cd evaluation/chain_of_thought
bash boolean_sh.sh
bash multichoice_sh.sh
bash factoid_sh.sh
```

---

### 3) Evaluate the generated predictions

Each evaluation setup contains:
- `evaluate_results.py`
- `evaluate_finetuned_results.py`

Example:

```bash
python evaluate_results.py
```

---

### 4) Output format

Outputs are saved as JSON files in:

```bash
evaluation/<setting>/prompt_results/<task>/<language>/
```

Example:

```bash
evaluation/chain_of_thought/prompt_results/boolean/persian/answers_llama-3-70b.json
```

---

## 📂 Repository Structure

```bash
.
├── LICENSE
├── README.md
│
├── dataset/
│   ├── full.json
│   ├── train.json
│   └── test.json
│
├── prompts/
│   ├── Boolean_*.txt
│   ├── Factoid_*.txt
│   └── Multichoice_*.txt
│
├── evaluation/
│   ├── zero_shot/
│   ├── few_shot/
│   ├── chain_of_thought/
│   ├── human_quality_evaluation/
│   └── human_difficulty_validation/
│
├── finetune/
│   ├── to_together_ai.py
│   ├── english_prompt/
│   ├── persian_prompt/
│   └── together_ai_data_format/
│       └── train_together.jsonl
│
└── interface/
    ├── difficulty_evalation_interface.html
    ├── quality_evaluation_interface.html
    └── QA_Annotation_Guide.pdf
```

---

## 📜 Citation

If you use Parse, please cite our paper:

```bibtex
@inproceedings{mozafari2026parse,
  title={Parse: An Open-Domain Reasoning Question Answering Benchmark for Persian},
  author={Mozafari, Jamshid and Mousavinasab, Seyed Parsa and Jatowt, Adam},
  booktitle={Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)},
  year={2026}
}
```

---

## 📄 License
This project is released under the license provided in the repository. See [LICENSE](LICENSE).
