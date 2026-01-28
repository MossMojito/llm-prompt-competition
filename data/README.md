# Data Directory

## Overview

This directory contains scripts and sample data for the IMDb sentiment analysis competition.

## Files

- **load_data.py**: Main script to load and process IMDb dataset
- **sample_data/**: Small datasets for quick testing (100 train, 50 test)
- **processed/**: Cached full datasets (gitignored, auto-downloaded)

## Dataset Information

### IMDb Movie Reviews Dataset

- **Source**: HuggingFace Datasets (`imdb`)
- **Task**: Binary sentiment classification
- **Classes**: Positive (1), Negative (0)
- **Train Size**: 25,000 reviews
- **Test Size**: 25,000 reviews (we use 1,000 for competition)

### Sample Data Format

```json
[
  {
    "text": "This movie was absolutely fantastic! The acting was superb...",
    "label": 1
  },
  {
    "text": "Waste of time. Poor script and terrible direction...",
    "label": 0
  }
]
```

## Usage

### Load Full Dataset

```python
from data.load_data import load_imdb_dataset

# This will download and cache the dataset
dataset = load_imdb_dataset()

# Access train/test splits
train_data = dataset['train']
test_data = dataset['test']
```

### Create Sample Files

```python
from data.load_data import create_sample_dataset, load_imdb_dataset

# Load full dataset
dataset = load_imdb_dataset()

# Create smaller samples for testing
create_sample_dataset(
    dataset, 
    output_dir="./data/sample_data",
    train_samples=100,
    test_samples=50
)
```

### Load Sample Data

```python
from data.load_data import load_sample_data

# Quick loading for development
train_sample = load_sample_data('./data/sample_data/train_sample.json')
test_sample = load_sample_data('./data/sample_data/test_sample.json')
```

## For Students

1. **Start with sample data** for quick iteration
2. **Test your prompts** on the small dataset first
3. **Final evaluation** will use hidden test set (1,000 examples)

## Data Storage in Databricks

### Recommended Paths

```python
# Store data in DBFS
dbfs_path = "/dbfs/mnt/llm-course/data/"

# Load from DBFS in notebooks
dataset = load_imdb_dataset(cache_dir=dbfs_path)
```

### Shared Data Location

All students should use the same cached data to save space:
- `/dbfs/mnt/llm-course/data/imdb/`

## Dataset Statistics

| Split | Total | Positive | Negative | Avg Length |
|-------|-------|----------|----------|------------|
| Train | 25,000 | 12,500 | 12,500 | ~230 words |
| Test  | 25,000 | 12,500 | 12,500 | ~230 words |
| Competition Test | 1,000 | 500 | 500 | ~230 words |

## Example Reviews

**Positive Example:**
```
"Brilliant! This film exceeded all expectations. The cinematography 
was stunning and the storyline kept me engaged throughout..."
```

**Negative Example:**
```
"Complete disappointment. The plot made no sense and the acting 
was wooden. I want my two hours back..."
```

## Notes

- ⚠️ Full dataset is ~80MB, will be cached on first load
- ✅ Sample data is pre-created and ready to use
- 🔒 Competition test set is hidden until evaluation
- 📊 Dataset is perfectly balanced (50% positive, 50% negative)

## Citation

```bibtex
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  year      = {2011}
}
```
