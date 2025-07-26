# Text Summarizer Project with T5 Model

## Overview
This project implements an end-to-end text summarization system using the T5-small model. The system generates concise summaries from dialogue text using the SamSum dataset. The pipeline is modular, configurable, and supports both training and inference via a FastAPI web interface.

## Model Architecture
- **Model**: T5-small (Text-to-Text Transfer Transformer)
- **Task**: Text Summarization
- **Input Format**: Dialogue text with `"summarize: "` prefix
- **Output**: Concise summaries

## Key Features
- **T5 Model**: Efficient and flexible text summarization
- **Pipeline Architecture**: Modular stages for ingestion, validation, transformation, training, and evaluation
- **Configuration Management**: YAML-based configuration for easy parameter tuning
- **Logging**: Comprehensive logging throughout the pipeline
- **Evaluation**: ROUGE metrics for model performance assessment
- **API**: FastAPI-based web interface for training and prediction

## Project Structure
```
Text-Summarizer-Project/
├── config/
│   └── config.yaml          # Configuration settings
├── src/textSummarizer/
│   ├── components/          # Core components (data, model, evaluation, etc.)
│   ├── config/              # Configuration management
│   ├── entity/              # Data classes
│   ├── pipeline/            # Pipeline stages
│   └── utils/               # Utility functions
├── research/                # Jupyter notebooks for experimentation
├── artifacts/               # Generated artifacts (models, logs, etc.)
├── main.py                  # Main execution script for the pipeline
├── app.py                   # FastAPI app for training and prediction
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Text-Summarizer-Project.git
   cd Text-Summarizer-Project
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv textS
   # On Windows:
   textS\Scripts\activate
   # On Unix/Mac:
   source textS/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Complete Pipeline
```bash
python main.py
```
This will execute all stages:
1. **Data Ingestion**: Downloads and extracts the SamSum dataset
2. **Data Validation**: Validates dataset integrity
3. **Data Transformation**: Preprocesses data for T5 model
4. **Model Training**: Trains the T5-small model
5. **Model Evaluation**: Evaluates the model using ROUGE metrics

### Running the API Server
Start the FastAPI server for training and prediction:
```bash
uvicorn app:app --reload
```
- Access the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

#### API Endpoints
- `GET /train` — Runs the full training pipeline
- `POST /predict` — Returns a summary for the provided text

### Configuration
Update `config/config.yaml` and `params.yaml` to modify:
- Model parameters
- Training arguments
- File paths
- Dataset settings

## Key Changes from Pegasus to T5

### Data Transformation
- **T5**: Requires `"summarize: "` prefix for input text
- **Pegasus**: Direct text input

### Tokenization
- **T5**: Unified tokenization approach
- **Pegasus**: Separate tokenization for input and target

### Model Benefits
1. **Smaller Size**: T5-small is more memory efficient
2. **Faster Training**: Reduced computational requirements
3. **Flexibility**: Can be adapted to other NLP tasks
4. **Better Resource Usage**: Lower GPU memory requirements

## Evaluation
The model is evaluated using ROUGE metrics:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- ROUGE-Lsum

## Output
- Trained model saved as `artifacts/t5-samsum-model`
- Tokenizer saved as `artifacts/tokenizer`
- Training logs and metrics saved in `artifacts/`

## Research Notebooks
- `research/t5_text_summarization.ipynb`: Complete T5 implementation
- `research/text_summarization(final).ipynb`: Original Pegasus implementation (for reference)
- Additional notebooks for data validation, transformation, and evaluation

## Dependencies
- transformers
- datasets
- torch
- evaluate
- pandas
- nltk
- PyYAML
- fastapi
- uvicorn
- tqdm

## License
This project is licensed under