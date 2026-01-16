<!-- ===================== -->
<!--        PARSE          -->
<!-- ===================== -->

<div align="center">

# 🌟 Parse: An Open-Domain Reasoning QA Benchmark for Persian

**A reasoning-focused open-domain Question Answering benchmark for Persian (FA)**  
covering **Boolean**, **Factoid**, and **Multiple-choice** questions with **Reasoning** + **Multi-hop** settings.

[![Hugging Face Dataset](https://img.shields.io/badge/HuggingFace-Dataset-yellow)](https://huggingface.co/datasets/JamshidJDMY/Parse)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/badge/Language-Persian%20(FA)-informational)](#)

</div>

---

## ✨ Highlights

- 🧠 Designed to evaluate **reasoning capabilities** of LLMs in a **low-resource language**
- ✅ Supports **Zero-shot**, **Few-shot**, and **Chain-of-Thought (CoT)** evaluation
- 🧪 Includes scripts for **automatic evaluation** + **fine-tuning utilities**
- 👥 Comes with **human evaluation interfaces** (quality + difficulty validation)

---

## 🚀 Quick Start

### Install

```bash
pip install datasets
```

### Load with 🤗 Datasets

```python
from datasets import load_dataset

ds = load_dataset("JamshidJDMY/Parse")
print(ds)

example = ds["train"][0]
print(example)
```

---

## 📦 What’s Inside This Repository?

This repository contains the dataset, evaluation scripts, fine-tuning utilities, and human evaluation materials used in our Parse benchmark experiments.

### `dataset/`
This directory includes three JSON files:

- `full.json` → the complete Parse benchmark
- `train.json` → training split used for fine-tuning experiments
- `test.json` → test split used for evaluation in fine-tuning experiments

> Note: `train.json` and `test.json` are mainly provided for reproducibility of fine-tuning experiments.

---

### `evaluation/`
This directory contains all scripts required to reproduce our evaluation results under three settings:

- **Zero-shot**
- **Few-shot**
- **Chain-of-Thought (CoT)**

Each evaluation setting contains:
- `boolean_sh.sh`
- `factoid_sh.sh`
- `multichoice_sh.sh`

These scripts evaluate Parse for each question type using the **TogetherAI platform**, which we use both for **inference** and **fine-tuning**.

Results are stored under:

```bash
prompt_results/<task>/<language>/
```

If you want to reproduce the experiments, simply rerun the corresponding `.sh` files.

To compute final scores and aggregate evaluation results, use:
- `evaluate_results.py`
- `evaluate_finetuned_results.py`

---

### 👥 Human Evaluations

In addition to automatic evaluation, the repository includes two human-based validation experiments:

#### `human_difficulty_validation/`
Human validation of **question difficulty**, including shuffled evaluation questions and collected human responses.

#### `human_quality_evaluation/`
Human-based assessment of benchmark **quality**, where participants evaluate question-answer correctness and overall quality.

---

### `finetune/`
This directory includes scripts and prompts needed to fine-tune models on Parse using TogetherAI.

Main script:
- `to_together_ai.py` → converts the benchmark into TogetherAI-compatible fine-tuning format

Output format example:
- `together_ai_data_format/train_together.jsonl`

---

### `interface/`
Contains the web interfaces used for human evaluation/validation, including the annotation guide:

- `quality_evaluation_interface.html`
- `difficulty_evalation_interface.html`
- `QA_Annotation_Guide.pdf`

---

### `prompts/`
Contains all prompt templates used during benchmark creation (question generation), organized by:

- Question type (Boolean / Factoid / Multichoice)
- Reasoning type (Reasoning / Multihop)
- Sub-category (e.g., Simple, Negation, Comparative, ListBased, NonAnswerable)

---

## 📌 Task Coverage

| Dimension | Values |
|----------|--------|
| **Question Types** | Boolean, Factoid, Multiple-choice |
| **Reasoning Types** | Reasoning, Multihop |
| **Difficulty** | Easy, Medium, Hard |
| **Languages** | Persian + English prompts supported |

---

## 🔁 Reproducibility (Minimal Setup)

This repository provides ready-to-run evaluation pipelines under:
- **Zero-shot**
- **Few-shot**
- **Chain-of-Thought (CoT)**

### 1) Environment

Recommended: **Python 3.10+**

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

> If you use API-based models (Together / OpenAI / etc.), you may need extra SDKs and API keys depending on your setup.

---

## 🧪 Evaluation

All evaluation scripts follow the same structure and produce JSON predictions under `prompt_results/`.

### ✅ Zero-shot

```bash
cd evaluation/zero_shot
bash boolean_sh.sh
bash multichoice_sh.sh
bash factoid_sh.sh
```

### ✅ Few-shot

```bash
cd evaluation/few_shot
bash boolean_sh.sh
bash multichoice_sh.sh
bash factoid_sh.sh
```

### ✅ Chain-of-Thought (CoT)

```bash
cd evaluation/chain_of_thought
bash boolean_sh.sh
bash multichoice_sh.sh
bash factoid_sh.sh
```

---

## 📊 Scoring

Each evaluation setting contains:

- `evaluate_results.py`
- `evaluate_finetuned_results.py`

Example:

```bash
python evaluate_results.py
```

---

## 🗂️ Output Format

Predictions are stored here:

```bash
evaluation/<setting>/prompt_results/<task>/<language>/
```

Example:

```bash
evaluation/chain_of_thought/prompt_results/boolean/persian/answers_llama-3-70b.json
```

---

## 🔧 Fine-tuning

Fine-tuning helper scripts and prompts are available in:

```bash
finetune/
```

Key script:
- `to_together_ai.py` → converts dataset into TogetherAI-compatible JSONL

Output example:

```bash
finetune/together_ai_data_format/train_together.jsonl
```

---

## 👥 Human Evaluation Interfaces

Annotation interfaces used in our human evaluations:

- `interface/quality_evaluation_interface.html`
- `interface/difficulty_evalation_interface.html`

Annotation guide:

- `interface/QA_Annotation_Guide.pdf`

---

## 📁 Repository Structure (Short)

```bash
.
├── dataset/
├── prompts/
├── evaluation/
├── finetune/
├── interface/
├── LICENSE
└── README.md
```

---

## 📜 Citation

If you use Parse, please cite:

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

See [LICENSE](LICENSE).
