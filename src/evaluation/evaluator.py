"""
Main Evaluator - Run and Score All Student Prompts
===================================================

This script evaluates all submitted prompts against the test dataset.
"""

import os
import sys
import importlib
import time
from pathlib import Path
from datetime import datetime
import json

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.evaluation.metrics import (
    calculate_metrics, 
    print_metrics,
    compare_prompts,
    plot_confusion_matrix
)
from data.load_data import load_sample_data, get_test_split, load_imdb_dataset


class PromptEvaluator:
    """Main evaluator for student prompts"""
    
    def __init__(self, model_name="google/flan-t5-base", use_sample=True):
        """
        Initialize the evaluator.
        
        Args:
            model_name: HuggingFace model to use
            use_sample: If True, use sample data; else use full test set
        """
        self.model_name = model_name
        self.use_sample = use_sample
        self.model = None
        self.tokenizer = None
        self.test_data = None
        
        print(f"🚀 Initializing Prompt Evaluator")
        print(f"   Model: {model_name}")
        print(f"   Mode: {'Sample Data' if use_sample else 'Full Test Set'}")
    
    def load_model(self):
        """Load the LLM model"""
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        
        print(f"\n📥 Loading model: {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        print("✅ Model loaded successfully")
    
    def load_test_data(self):
        """Load test dataset"""
        print(f"\n📊 Loading test data...")
        
        if self.use_sample:
            # Use sample data
            sample_path = "./data/sample_data/test_sample.json"
            if os.path.exists(sample_path):
                self.test_data = load_sample_data(sample_path)
            else:
                print("⚠️  Sample data not found, creating it...")
                from data.load_data import create_sample_dataset, load_imdb_dataset
                dataset = load_imdb_dataset()
                create_sample_dataset(dataset)
                self.test_data = load_sample_data(sample_path)
        else:
            # Use full test set
            dataset = load_imdb_dataset()
            self.test_data = get_test_split(dataset, size=1000)
        
        print(f"✅ Loaded {len(self.test_data)} test examples")
    
    def run_inference(self, prompt, max_length=10):
        """
        Run inference on a single prompt.
        
        Args:
            prompt: The complete prompt string
            max_length: Max tokens to generate
            
        Returns:
            str: Model's output
        """
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model.generate(**inputs, max_length=max_length, num_beams=1)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result
    
    def evaluate_student_prompt(self, student_module, student_name):
        """
        Evaluate a single student's prompt.
        
        Args:
            student_module: Imported student module
            student_name: Student's name
            
        Returns:
            dict: Evaluation results
        """
        print(f"\n{'='*70}")
        print(f"Evaluating: {student_name}")
        print(f"{'='*70}")
        
        predictions = []
        true_labels = []
        inference_times = []
        
        # Get the prompt function
        get_prompt = student_module.get_prompt
        
        # Optional: get parse_output function if exists
        parse_output = getattr(student_module, 'parse_output', None)
        
        # Run on all test examples
        for i, example in enumerate(self.test_data):
            review = example['text']
            true_label = example['label']
            
            # Generate prompt
            prompt = get_prompt(review)
            
            # Run inference
            start_time = time.time()
            output = self.run_inference(prompt)
            inference_time = time.time() - start_time
            inference_times.append(inference_time)
            
            # Parse output
            if parse_output:
                prediction = parse_output(output)
            else:
                # Default parsing
                if "Positive" in output:
                    prediction = "Positive"
                elif "Negative" in output:
                    prediction = "Negative"
                else:
                    prediction = "Positive"  # Default fallback
            
            # Convert to binary
            pred_binary = 1 if prediction == "Positive" else 0
            
            predictions.append(pred_binary)
            true_labels.append(true_label)
            
            # Progress indicator
            if (i + 1) % 10 == 0:
                print(f"   Progress: {i+1}/{len(self.test_data)} examples processed")
        
        # Calculate metrics
        metrics = calculate_metrics(true_labels, predictions)
        metrics['avg_inference_time'] = sum(inference_times) / len(inference_times)
        metrics['total_inference_time'] = sum(inference_times)
        
        # Print results
        print_metrics(metrics, student_name=student_name)
        print(f"\n⏱️  Average inference time: {metrics['avg_inference_time']:.3f}s per example")
        print(f"   Total time: {metrics['total_inference_time']:.1f}s")
        
        return metrics
    
    def find_student_prompts(self):
        """
        Find all student prompt submissions.
        
        Returns:
            list: List of (student_name, module_path) tuples
        """
        prompts_dir = Path("./src/prompts/student_prompts")
        student_prompts = []
        
        for file in prompts_dir.glob("*.py"):
            if file.name not in ['__init__.py', 'template.py']:
                student_name = file.stem.replace('_', ' ').title()
                student_prompts.append((student_name, file))
        
        return student_prompts
    
    def evaluate_all_students(self):
        """
        Evaluate all submitted student prompts and generate leaderboard.
        
        Returns:
            dict: Results for all students
        """
        # Load model and data
        if self.model is None:
            self.load_model()
        if self.test_data is None:
            self.load_test_data()
        
        # Find all student submissions
        student_prompts = self.find_student_prompts()
        
        if not student_prompts:
            print("⚠️  No student submissions found!")
            print("   Students should submit their prompts to src/prompts/student_prompts/")
            return {}
        
        print(f"\n📝 Found {len(student_prompts)} student submissions")
        
        # Evaluate each student
        all_results = {}
        
        for student_name, module_path in student_prompts:
            try:
                # Import student module
                spec = importlib.util.spec_from_file_location(student_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Evaluate
                results = self.evaluate_student_prompt(module, student_name)
                all_results[student_name] = results
                
            except Exception as e:
                print(f"\n❌ Error evaluating {student_name}: {str(e)}")
                continue
        
        # Generate comparison
        if all_results:
            print("\n" + "="*80)
            print("FINAL LEADERBOARD")
            print("="*80)
            leaderboard_df = compare_prompts(all_results)
            
            # Save results
            self.save_results(all_results, leaderboard_df)
        
        return all_results
    
    def save_results(self, all_results, leaderboard_df):
        """
        Save evaluation results and leaderboard.
        
        Args:
            all_results: Dictionary of all student results
            leaderboard_df: Pandas DataFrame with rankings
        """
        # Create results directory
        results_dir = Path("./results/submissions")
        results_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save detailed results as JSON
        results_file = results_dir / f"evaluation_{timestamp}.json"
        
        # Convert numpy types to Python types for JSON serialization
        json_results = {}
        for name, metrics in all_results.items():
            json_results[name] = {
                k: float(v) if isinstance(v, (float, int)) else str(v)
                for k, v in metrics.items()
                if k != 'confusion_matrix'
            }
        
        with open(results_file, 'w') as f:
            json.dump(json_results, f, indent=2)
        
        print(f"\n✅ Results saved to: {results_file}")
        
        # Save leaderboard as markdown
        leaderboard_file = Path("./results/leaderboard.md")
        with open(leaderboard_file, 'w') as f:
            f.write("# 🏆 Competition Leaderboard\n\n")
            f.write(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write(leaderboard_df.to_markdown())
        
        print(f"✅ Leaderboard saved to: {leaderboard_file}")


def quick_test(student_name):
    """
    Quick test of a single student's prompt on sample data.
    
    Args:
        student_name: Name of the student file (without .py)
        
    Example:
        quick_test('john_doe')
    """
    evaluator = PromptEvaluator(use_sample=True)
    evaluator.load_model()
    evaluator.load_test_data()
    
    # Import student module
    module_path = f"./src/prompts/student_prompts/{student_name}.py"
    spec = importlib.util.spec_from_file_location(student_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Evaluate
    results = evaluator.evaluate_student_prompt(module, student_name)
    
    return results


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Evaluate student prompts")
    parser.add_argument(
        '--mode', 
        choices=['all', 'single', 'sample'],
        default='sample',
        help='Evaluation mode'
    )
    parser.add_argument(
        '--student',
        type=str,
        help='Student name for single evaluation'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='google/flan-t5-base',
        help='HuggingFace model name'
    )
    
    args = parser.parse_args()
    
    if args.mode == 'all':
        # Evaluate all students on full test set
        evaluator = PromptEvaluator(model_name=args.model, use_sample=False)
        evaluator.evaluate_all_students()
    
    elif args.mode == 'single':
        # Evaluate single student
        if not args.student:
            print("❌ Please specify --student name")
        else:
            quick_test(args.student)
    
    else:
        # Sample mode - quick test
        print("Running in SAMPLE mode - using sample data for quick testing")
        evaluator = PromptEvaluator(model_name=args.model, use_sample=True)
        evaluator.evaluate_all_students()
