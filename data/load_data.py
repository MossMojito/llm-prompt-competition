"""
Data loading utilities for IMDb sentiment analysis dataset
"""

from datasets import load_dataset
import json
import os
from pathlib import Path


def load_imdb_dataset(cache_dir="./data/processed"):
    """
    Load the IMDb dataset from HuggingFace
    
    Returns:
        dict: Dictionary with 'train' and 'test' splits
    """
    print("Loading IMDb dataset from HuggingFace...")
    dataset = load_dataset("imdb", cache_dir=cache_dir)
    
    print(f"Train samples: {len(dataset['train'])}")
    print(f"Test samples: {len(dataset['test'])}")
    
    return dataset


def create_sample_dataset(dataset, output_dir="./data/sample_data", 
                         train_samples=100, test_samples=50):
    """
    Create smaller sample datasets for quick testing
    
    Args:
        dataset: HuggingFace dataset object
        output_dir: Where to save sample files
        train_samples: Number of training samples
        test_samples: Number of test samples
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Create balanced samples (50% positive, 50% negative)
    train_pos = [ex for ex in dataset['train'] if ex['label'] == 1][:train_samples//2]
    train_neg = [ex for ex in dataset['train'] if ex['label'] == 0][:train_samples//2]
    train_sample = train_pos + train_neg
    
    test_pos = [ex for ex in dataset['test'] if ex['label'] == 1][:test_samples//2]
    test_neg = [ex for ex in dataset['test'] if ex['label'] == 0][:test_samples//2]
    test_sample = test_pos + test_neg
    
    # Save as JSON
    with open(f"{output_dir}/train_sample.json", 'w', encoding='utf-8') as f:
        json.dump(train_sample, f, indent=2, ensure_ascii=False)
    
    with open(f"{output_dir}/test_sample.json", 'w', encoding='utf-8') as f:
        json.dump(test_sample, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Sample datasets created:")
    print(f"   - {output_dir}/train_sample.json ({len(train_sample)} examples)")
    print(f"   - {output_dir}/test_sample.json ({len(test_sample)} examples)")


def load_sample_data(sample_file):
    """
    Load sample data from JSON file
    
    Args:
        sample_file: Path to JSON file
        
    Returns:
        list: List of examples
    """
    with open(sample_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_test_split(dataset, size=1000, seed=42):
    """
    Create a held-out test set for competition evaluation
    
    Args:
        dataset: HuggingFace dataset
        size: Number of test examples
        seed: Random seed for reproducibility
        
    Returns:
        list: Test examples
    """
    from random import Random
    rng = Random(seed)
    
    # Get balanced positive and negative samples
    positives = [ex for ex in dataset['test'] if ex['label'] == 1]
    negatives = [ex for ex in dataset['test'] if ex['label'] == 0]
    
    # Sample half from each class
    test_set = (
        rng.sample(positives, size//2) + 
        rng.sample(negatives, size//2)
    )
    
    # Shuffle
    rng.shuffle(test_set)
    
    return test_set


if __name__ == "__main__":
    # Example usage
    print("=" * 60)
    print("IMDb Dataset Loader - Demo")
    print("=" * 60)
    
    # Load full dataset
    dataset = load_imdb_dataset()
    
    # Create sample files for students
    create_sample_dataset(dataset)
    
    # Show example
    print("\n📝 Example review:")
    example = dataset['train'][0]
    print(f"Text: {example['text'][:200]}...")
    print(f"Label: {'Positive' if example['label'] == 1 else 'Negative'}")
    
    print("\n✅ Data loading complete!")
