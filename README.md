# mental-health-disorder-analysis

A comprehensive research project for mental health condition classification using explainable AI (XAI) techniques. This project implements transformer-based models to classify text into mental health categories including depression, anxiety, stress, PTSD, suicide ideation, and none.

## Overview

This repository contains code for:
- **Data Collection**: Reddit data scraping and preprocessing
- **Model Training**: Fine-tuning RoBERTa models for multi-class mental health classification
- **Model Inference**: Deploying trained models for text classification
- **Explainability Analysis**: Using Captum (Integrated Gradients) to understand model decisions
- **LLM Evaluation**: Zero-shot and few-shot prompting experiments with GPT models
- **Robustness Analysis**: Evaluating model performance across different conditions

## Features

- 🧠 **Multi-class Classification**: Supports 5-class (depression, anxiety, PTSD, suicide, none) and 6-class (including stress) classification
- 🔍 **Explainability**: Integrated Gradients attribution to identify important words/phrases
- 📊 **Comprehensive Datasets**: Integrated data from multiple sources (Reddit, eRisk, CAMS, etc.)
- 🤖 **LLM Integration**: Zero-shot and few-shot prompting experiments
- 🔬 **Data Integrity Evaluation**: Clustering and classification-based label validation

## Models

- **all_roberta_large_v1_multiclass**: 5-class classification (no stress category)
- **all_roberta_large_v1_with_stress**: 6-class classification (includes stress)

Fine-tuned models are available on Hugging Face:

- **[SajjadIslam/multiMentalRoBERTA-5-class](https://huggingface.co/SajjadIslam/multiMentalRoBERTA-5-class)**: 5-class classification (depression, anxiety, PTSD, suicide, none)
- **[SajjadIslam/multiMentalRoBERTA-6-class](https://huggingface.co/SajjadIslam/multiMentalRoBERTA-6-class)**: 6-class classification (includes stress category)

📦 **Model Collection**: [multiMentalRoBERTa-Models](https://huggingface.co/collections/SajjadIslam/multimentalroberta-models)

## Installation

### Requirements

See `reddit_data_proces/requirements.txt` for detailed dependencies. Key packages include:

- `transformers` - Hugging Face transformers for model training and inference
- `torch` - PyTorch (GPU support recommended)
- `captum` - Model interpretability
- `praw` - Reddit API wrapper
- `pandas`, `scikit-learn`, `numpy` - Data processing and evaluation
- `sentence-transformers` - Embedding generation

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd PSS_XAI
```

2. Install dependencies:
```bash
pip install -r reddit_data_proces/requirements.txt
```

3. For GPU support, install PyTorch with CUDA (see requirements.txt for details)

4. For Reddit data collection, set up environment variables in a `.env` file:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
```

## Project Structure

```
mental-health-disorder-analysis/
├── Data_Process/
│   ├── Data_Lake/          # Raw datasets
│   ├── Data_Warehouse/      # Processed datasets
│   ├── Dataset_*.ipynb      # Dataset processing notebooks
│   ├── Model_Traning_*.ipynb  # Model training notebooks
│   ├── Model_Inference_*.ipynb # Inference notebooks
│   ├── Explainability_*.ipynb # XAI analysis notebooks
│   ├── Prompting_*.ipynb    # LLM prompting experiments
│   └── Robustness_Analysis.ipynb
└── reddit_data_proces/      # Reddit data collection scripts
    ├── reddit_scrapper.py
    └── requirements.txt
```

## Usage

### Model Training

Run the training notebooks in `Data_Process/`:
- `Model_Traning_No_Stress.ipynb` - Train 5-class model
- `Model_Traning_With_Stress.ipynb` - Train 6-class model

### Model Inference

Use `Model_Inference_RoBERTa.ipynb` or `Model_Inference_multiMentalRoBERTa.ipynb` to classify text samples.

### Explainability Analysis

Run `Explainability_Analysis_Suicidal.ipynb` or `Explainability_Analysis_Suicidal_Key_Phrase.ipynb` to analyze model attributions.

### Data Collection

Use `reddit_scrapper.py` to collect Reddit posts and comments:

```bash
python reddit_data_proces/reddit_scrapper.py
```

## Datasets

The project integrates data from multiple sources including:
- Reddit mental health subreddits
- eRisk Task 2 dataset
- CAMS dataset
- Suicide detection datasets
- Various depression/anxiety datasets

Processed datasets are stored in `Data_Process/Data_Warehouse/`.

## License

[Apache License 2.0]

## Citation
```bibtex
@inproceedings{islam2025multimentalroberta,
  title={multiMentalRoBERTa: A Fine-tuned Multiclass Classifier for Mental Health Disorder},
  author={Islam, KM Sajjadul and Fields, John and Madiraju, Praveen},
  booktitle={2025 IEEE International Conference on Big Data (BigData)},
  pages={3255--3264},
  year={2025},
  organization={IEEE}
}
```


## Contact

[s.i.sajjad.islam@gmail.com]
