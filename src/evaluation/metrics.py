"""
Evaluation Metrics for Sentiment Classification
================================================

This module provides metrics for evaluating prompt performance.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report
)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_metrics(y_true, y_pred):
    """
    Calculate comprehensive evaluation metrics.
    
    Args:
        y_true (list): True labels (0 or 1, or "Negative"/"Positive")
        y_pred (list): Predicted labels
        
    Returns:
        dict: Dictionary containing all metrics
    """
    # Convert string labels to binary if needed
    if isinstance(y_true[0], str):
        y_true = [1 if label == "Positive" else 0 for label in y_true]
    if isinstance(y_pred[0], str):
        y_pred = [1 if label == "Positive" else 0 for label in y_pred]
    
    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average='binary'
    )
    
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'true_positives': int(tp),
        'true_negatives': int(tn),
        'false_positives': int(fp),
        'false_negatives': int(fn),
        'confusion_matrix': cm
    }
    
    return metrics


def print_metrics(metrics, student_name="Unknown"):
    """
    Pretty print evaluation metrics.
    
    Args:
        metrics (dict): Metrics dictionary from calculate_metrics
        student_name (str): Student name for display
    """
    print("=" * 70)
    print(f"EVALUATION RESULTS: {student_name}")
    print("=" * 70)
    
    print(f"\n📊 Overall Performance:")
    print(f"   Accuracy:  {metrics['accuracy']:.4f} ({metrics['accuracy']*100:.2f}%)")
    print(f"   F1 Score:  {metrics['f1_score']:.4f}")
    print(f"   Precision: {metrics['precision']:.4f}")
    print(f"   Recall:    {metrics['recall']:.4f}")
    
    print(f"\n📈 Confusion Matrix:")
    print(f"   True Positives:  {metrics['true_positives']}")
    print(f"   True Negatives:  {metrics['true_negatives']}")
    print(f"   False Positives: {metrics['false_positives']}")
    print(f"   False Negatives: {metrics['false_negatives']}")
    
    print("\n" + "=" * 70)


def plot_confusion_matrix(cm, student_name="Unknown", save_path=None):
    """
    Plot confusion matrix as a heatmap.
    
    Args:
        cm (np.array): Confusion matrix
        student_name (str): Student name for title
        save_path (str): Path to save figure (optional)
    """
    plt.figure(figsize=(8, 6))
    
    sns.heatmap(
        cm, 
        annot=True, 
        fmt='d', 
        cmap='Blues',
        xticklabels=['Negative', 'Positive'],
        yticklabels=['Negative', 'Positive'],
        cbar_kws={'label': 'Count'}
    )
    
    plt.title(f'Confusion Matrix - {student_name}', fontsize=14, fontweight='bold')
    plt.ylabel('True Label', fontsize=12)
    plt.xlabel('Predicted Label', fontsize=12)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Confusion matrix saved to: {save_path}")
    
    plt.show()


def compare_prompts(results_dict):
    """
    Compare multiple prompt strategies side by side.
    
    Args:
        results_dict (dict): Dictionary mapping student names to metrics
        
    Example:
        results = {
            'John Doe': {'accuracy': 0.85, 'f1_score': 0.84, ...},
            'Jane Smith': {'accuracy': 0.88, 'f1_score': 0.87, ...}
        }
        compare_prompts(results)
    """
    import pandas as pd
    
    # Create comparison dataframe
    comparison = []
    for name, metrics in results_dict.items():
        comparison.append({
            'Student': name,
            'Accuracy': f"{metrics['accuracy']:.4f}",
            'F1 Score': f"{metrics['f1_score']:.4f}",
            'Precision': f"{metrics['precision']:.4f}",
            'Recall': f"{metrics['recall']:.4f}"
        })
    
    df = pd.DataFrame(comparison)
    df = df.sort_values('Accuracy', ascending=False).reset_index(drop=True)
    df.index = df.index + 1  # Start ranking from 1
    
    print("\n" + "=" * 80)
    print("LEADERBOARD - PROMPT COMPARISON")
    print("=" * 80)
    print(df.to_string(index=True))
    print("=" * 80)
    
    return df


def calculate_leaderboard_score(metrics, inference_time=None):
    """
    Calculate final leaderboard score with bonuses.
    
    Base score: Accuracy (0-100)
    Bonuses:
    - Fastest inference: +2%
    - Creative approach (manual): +1%
    - Best explanation (manual): +1%
    
    Args:
        metrics (dict): Evaluation metrics
        inference_time (float): Average inference time per example (seconds)
        
    Returns:
        float: Final score
    """
    base_score = metrics['accuracy'] * 100
    
    # Time bonus (fastest gets +2%)
    time_bonus = 0
    if inference_time is not None and inference_time < 1.0:
        time_bonus = 2
    
    # Manual bonuses would be added by instructor
    
    final_score = base_score + time_bonus
    
    return final_score


def generate_classification_report(y_true, y_pred, save_path=None):
    """
    Generate detailed sklearn classification report.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        save_path: Optional path to save report
        
    Returns:
        str: Classification report
    """
    # Convert to binary if needed
    if isinstance(y_true[0], str):
        y_true = [1 if label == "Positive" else 0 for label in y_true]
    if isinstance(y_pred[0], str):
        y_pred = [1 if label == "Positive" else 0 for label in y_pred]
    
    report = classification_report(
        y_true, 
        y_pred,
        target_names=['Negative', 'Positive'],
        digits=4
    )
    
    if save_path:
        with open(save_path, 'w') as f:
            f.write(report)
        print(f"✅ Classification report saved to: {save_path}")
    
    return report


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Example evaluation
    print("Testing Evaluation Metrics Module\n")
    
    # Simulated predictions
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # True labels
    y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels
    
    # Calculate metrics
    metrics = calculate_metrics(y_true, y_pred)
    
    # Print results
    print_metrics(metrics, student_name="Example Student")
    
    # Print classification report
    print("\n📋 Detailed Classification Report:")
    print(generate_classification_report(y_true, y_pred))
    
    # Example comparison
    print("\n" + "=" * 80)
    print("Example Leaderboard Comparison:")
    
    results = {
        'Alice (Few-shot)': {'accuracy': 0.88, 'f1_score': 0.87, 'precision': 0.86, 'recall': 0.89},
        'Bob (Zero-shot)': {'accuracy': 0.82, 'f1_score': 0.81, 'precision': 0.80, 'recall': 0.82},
        'Charlie (CoT)': {'accuracy': 0.91, 'f1_score': 0.90, 'precision': 0.89, 'recall': 0.91}
    }
    
    compare_prompts(results)
