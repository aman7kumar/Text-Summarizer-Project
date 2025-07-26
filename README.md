# Text Summarizer Project with T5 Model

## Overview
This project implements an end-to-end text summarization system using the T5-small model. The system is designed to generate concise summaries from dialogue text using the SamSum dataset.

## Model Architecture
- **Model**: T5-small (Text-to-Text Transfer Transformer)
- **Task**: Text Summarization
- **Input Format**: Dialogue text with "summarize: " prefix
- **Output**: Concise summaries

## Key Features
- **T5 Model**: Uses T5-small for efficient text summarization
- **Pipeline Architecture**: Modular design with separate stages for data ingestion, validation, transformation, and model training
- **Configuration Management**: YAML-based configuration for easy parameter tuning
- **Logging**: Comprehensive logging throughout the pipeline
- **Evaluation**: ROUGE metrics for model performance assessment

## Project Structure
```
Text-Summarizer-Project/
├── config/
│   └── config.yaml          # Configuration settings
├── src/textSummarizer/
│   ├── components/          # Core components
│   ├── config/             # Configuration management
│   ├── entity/             # Data classes
│   ├── pipeline/           # Pipeline stages
│   └── utils/              # Utility functions
├── research/               # Jupyter notebooks
├── artifacts/              # Generated artifacts
├── main.py                 # Main execution script
└── requirements.txt        # Dependencies
```

## Installation
1. Clone the repository
2. Install dependencies:
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

### Configuration
Update `config/config.yaml` and `params.yaml` to modify:
- Model parameters
- Training arguments
- File paths
- Dataset settings

## Key Changes from Pegasus to T5

### Data Transformation
- **T5**: Requires "summarize: " prefix for input text
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
- Trained model saved as `t5-samsum-model`
- Tokenizer saved as `tokenizer`
- Training logs and metrics

## Research Notebooks
- `research/t5_text_summarization.ipynb`: Complete T5 implementation
- `research/text_summarization(final).ipynb`: Original Pegasus implementation (for reference)

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

## License
This project is licensed under the MIT License.