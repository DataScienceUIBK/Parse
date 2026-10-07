<!-- ===================== -->
<!--        PARSE          -->
<!-- ===================== -->

<div align="center">

# 🌟 Parse: An Open-Domain Reasoning QA Benchmark for Persian

**A reasoning-focused open-domain Question Answering benchmark for Persian (FA)**  
covering **Boolean**, **Factoid**, and **Multiple-choice** questions with **Reasoning** + **Multi-hop** settings.

<!-- <a href="https://huggingface.co/datasets/JamshidJDMY/Parse"><img src="https://img.shields.io/static/v1?label=Dataset&message=HuggingFace&color=yellow&logo=huggingface"></a> -->
<a href="https://arxiv.org/pdf/2602.01246"><img src="https://img.shields.io/static/v1?label=Paper&message=ArXiv&color=green&logo=arXiv"></a>
<a href="https://opensource.org/license/apache-2-0"><img src="https://img.shields.io/static/v1?label=License&message=MIT&color=red"></a>

</div>

## ✨ Highlights

- 🧠 Designed to evaluate **reasoning capabilities** of LLMs in a **low-resource language**
- ✅ Supports **Zero-shot**, **Few-shot**, and **Chain-of-Thought (CoT)** evaluation
- 🧪 Includes scripts for **automatic evaluation** + **fine-tuning utilities**
- 👥 Comes with **human evaluation interfaces** (quality + difficulty validation)

## 🤗 Dataset

[//]: <> (Parse is publicly available on HuggingFace:)

[//]: <> (- **Dataset:** `JamshidJDMY/Parse`)
[//]: <> (- Link: https://huggingface.co/datasets/JamshidJDMY/Parse)

### Local dataset files (`dataset/`)

This repository also contains the dataset as JSON files under `dataset/`:

- `full.json` → the complete Parse benchmark
- `train.json` → training split (used for fine-tuning experiments)
- `test.json` → test split (used for fine-tuning evaluation)

> Note: `train.json` and `test.json` are provided for reproducibility of fine-tuning experiments.


## 📌 Task Coverage

### Question Types & Subtypes

| Question Type | Subtypes (Categories) |
|---|---|
| **Boolean** | Reasoning: *Simple, Negation, Comparative*  <br> Multihop: *Simple, Negation, Comparative* |
| **Factoid** | Reasoning: *Simple, NonAnswerable, ListBased* <br> Multihop: *Simple, NonAnswerable, ListBased* |
| **Multiple-choice** | Reasoning: *SingleAnswer, MultiAnswer, NonAnswerable* <br> Multihop: *SingleAnswer, MultiAnswer, NonAnswerable* |

### Benchmark Dimensions

| Dimension | Values |
|---|---|
| **Reasoning Types** | Reasoning, Multihop |
| **Difficulty** | Easy, Medium, Hard |
| **Languages** | Persian + English prompts supported |

## 📈 Benchmark Statistics

Parse contains **10,800 questions**, designed with a balanced and fully-controlled taxonomy. 

### Dataset Size & Balance

- **Total questions:** 10,800 
- **Uniform coverage:** **18 configuration families**, each with **600 questions** 
- Difficulty is balanced inside each configuration: **200 Easy / 200 Medium / 200 Hard** 

### Taxonomy Breakdown (Table 2 in the paper)

| QA Type | Dimension | Subtypes | # per subtype | Total |
|---|---|---|---:|---:|
| Boolean | Reasoning | Simple / Negation / Comparative | 600 | 1,800 |
| Boolean | Multihop | Simple / Negation / Comparative | 600 | 1,800 |
| Multiple-choice | Reasoning | Single-Ans / Multi-Ans / Non-Ans | 600 | 1,800 |
| Multiple-choice | Multihop | Single-Ans / Multi-Ans / Non-Ans | 600 | 1,800 |
| Factoid | Reasoning | Simple / List-based / Non-Ans | 600 | 1,800 |
| Factoid | Multihop | Simple / List-based / Non-Ans | 600 | 1,800 |

> Overall: 6 blocks × 1,800 = **10,800 questions**. 

## 🧪 Benchmarking Results (Paper Summary)

We benchmark multilingual and Persian LLMs under:
- **Zero-shot**
- **Few-shot**
- **Chain-of-Thought (CoT)** 

Key findings:
- **Persian prompts** generally improve results compared to English prompts.
- **Structured prompting** helps:
  - **CoT** is most effective for **Boolean** and **Multiple-choice**
  - **Few-shot** is most effective for **Factoid**
- **Fine-tuning improves performance**, particularly for Persian-specialized models. 

> Full result tables are provided in the paper (e.g., Table 4 for Boolean and Table 5 for Multiple-choice). 

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

## 📦 Repository Overview

### `prompts/`
Contains all prompt templates used during benchmark creation (question generation), organized by:
- question type (Boolean / Factoid / Multichoice)
- reasoning type (Reasoning / Multihop)
- sub-category (e.g., Simple, Negation, Comparative, ListBased, NonAnswerable)

### `evaluation/`
Includes all automatic evaluation code:
- `zero_shot/`
- `few_shot/`
- `chain_of_thought/`

Each evaluation setting contains:
- `boolean_sh.sh`
- `factoid_sh.sh`
- `multichoice_sh.sh`

### `finetune/`
Utilities to convert Parse into TogetherAI fine-tuning format:
- `to_together_ai.py`
- output example: `finetune/together_ai_data_format/train_together.jsonl`

### Human evaluation data
- `evaluation/human_difficulty_validation/` → difficulty validation study
- `evaluation/human_quality_evaluation/` → quality evaluation study

### `interface/`
Annotation interfaces and guide:
- `quality_evaluation_interface.html`
- `difficulty_evalation_interface.html`
- `QA_Annotation_Guide.pdf`

## 🔁 Reproducibility (Minimal Setup)

Recommended: **Python 3.10+**

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows
```

Install dependencies:

```bash
pip install -U pip
pip install prettytable termcolor together tenacity datasets
```

> If you use API-based models, ensure you have your TogetherAI API key configured.


## 🧪 Evaluation (TogetherAI)

All evaluation scripts follow the same structure and produce JSON predictions under `prompt_results/`.

### Running experiments

#### ✅ Zero-shot
```bash
cd evaluation/zero_shot
bash boolean_sh.sh
bash factoid_sh.sh
bash multichoice_sh.sh
```

#### ✅ Few-shot
```bash
cd evaluation/few_shot
bash boolean_sh.sh
bash factoid_sh.sh
bash multichoice_sh.sh
```

#### ✅ Chain-of-Thought (CoT)
```bash
cd evaluation/chain_of_thought
bash boolean_sh.sh
bash factoid_sh.sh
bash multichoice_sh.sh
```

### Output format

Predictions are stored here:

```bash
evaluation/<setting>/prompt_results/<task>/<language>/
```

Example:

```bash
evaluation/chain_of_thought/prompt_results/boolean/persian/answers_llama-3-70b.json
```

## 📊 Scoring

Each evaluation setting includes the scoring scripts:

- `evaluate_results.py`
- `evaluate_finetuned_results.py`

Example:

```bash
python evaluate_results.py
```

## 🔧 Fine-tuning

Fine-tuning helper scripts and prompts are available in:

```bash
finetune/
```

Key script:
- `to_together_ai.py` → converts Parse into TogetherAI-compatible JSONL

Output example:
- `finetune/together_ai_data_format/train_together.jsonl`

## 👥 Human Evaluation Summary

We conducted two human evaluation studies to validate benchmark quality and difficulty labels. 

### ✅ Quality Evaluation (1–5 rating)

Annotators evaluated:
- **Ambiguity**
- **Readability**
- **Correctness**

Average scores across groups:

| Metric | Avg. Score (1–5) |
|---|---:|
| Ambiguity | **4.404** |
| Readability | **4.669** |
| Correctness | **4.389** |

These results indicate high linguistic quality and strong factual correctness. 

### ✅ Difficulty Validation

Human accuracy aligns with our difficulty labels (**Easy > Medium > Hard**) consistently across Boolean, Multiple-choice, and Factoid. 

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


## 📜 Citation

If you use Parse, please cite:

```bibtex
@article{mozafari2026parse,
  title={PARSE: An Open-Domain Reasoning Question Answering Benchmark for Persian},
  author={Mozafari, Jamshid and Mousavinasab, Seyed Parsa and Jatowt, Adam},
  journal={arXiv preprint arXiv:2602.01246},
  year={2026}
}
```

## 📄 License

See [LICENSE](LICENSE).
