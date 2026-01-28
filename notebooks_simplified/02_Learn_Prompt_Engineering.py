# Databricks notebook source
# MAGIC %md
# MAGIC # 🎨 Notebook 2: Learn Prompt Engineering
# MAGIC 
# MAGIC **In this notebook, you'll learn how to write effective prompts.**
# MAGIC 
# MAGIC We'll show you:
# MAGIC 1. Bad vs Good prompts
# MAGIC 2. Three main strategies
# MAGIC 3. How to test your prompts
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 📚 Prerequisites
# MAGIC 
# MAGIC Make sure you completed Notebook 1 first!

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🔄 Quick Setup
# MAGIC 
# MAGIC Run this to reload the model and data:

# COMMAND ----------

# Reload packages
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
import random

# Load model
print("Loading model...")
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Load data
dataset = load_dataset("imdb", split="test")
positive_reviews = [ex for ex in dataset if ex['label'] == 1][:50]
negative_reviews = [ex for ex in dataset if ex['label'] == 0][:50]
competition_dataset = positive_reviews + negative_reviews
random.seed(42)
random.shuffle(competition_dataset)

print("✅ Ready!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🧪 Testing Function
# MAGIC 
# MAGIC This function tests any prompt on a few examples:

# COMMAND ----------

def test_prompt_strategy(prompt_function, num_tests=10):
    """
    Test a prompt strategy on sample reviews
    
    Args:
        prompt_function: Function that takes review_text and returns a prompt
        num_tests: Number of reviews to test (default 10)
    """
    from sklearn.metrics import accuracy_score
    
    correct = 0
    test_samples = competition_dataset[:num_tests]
    
    print(f"Testing on {num_tests} reviews...")
    print("=" * 60)
    
    for i, example in enumerate(test_samples):
        review = example['text']
        true_label = "Positive" if example['label'] == 1 else "Negative"
        
        # Generate prompt
        prompt = prompt_function(review)
        
        # Get model response
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(**inputs, max_length=10)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Parse response
        if "Positive" in result or "positive" in result:
            predicted = "Positive"
        elif "Negative" in result or "negative" in result:
            predicted = "Negative"
        else:
            predicted = "Positive"  # Default
        
        # Check correctness
        is_correct = (predicted == true_label)
        if is_correct:
            correct += 1
        
        # Show first 3 examples
        if i < 3:
            print(f"\nExample {i+1}:")
            print(f"Review: {review[:80]}...")
            print(f"True: {true_label} | Predicted: {predicted} | {'✅' if is_correct else '❌'}")
    
    accuracy = correct / num_tests
    print("\n" + "=" * 60)
    print(f"📊 Accuracy: {accuracy:.1%} ({correct}/{num_tests} correct)")
    print("=" * 60)
    
    return accuracy

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 📖 Part 1: Bad vs Good Prompts
# MAGIC 
# MAGIC Let's see the difference!

# COMMAND ----------

# MAGIC %md
# MAGIC ## ❌ Bad Prompt #1: Too Vague

# COMMAND ----------

def bad_prompt_vague(review_text):
    """This prompt is too vague"""
    return f"What about this? {review_text}"

print("Testing BAD prompt (vague):")
test_prompt_strategy(bad_prompt_vague, num_tests=10)

# COMMAND ----------

# MAGIC %md
# MAGIC **Why it's bad:**
# MAGIC - AI doesn't know what you want
# MAGIC - No clear output format
# MAGIC - Random results
# MAGIC 
# MAGIC **Expected accuracy: ~50% (random guessing)**

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Good Prompt #1: Clear Instructions

# COMMAND ----------

def good_prompt_clear(review_text):
    """Clear prompt with specific instructions"""
    return f"""Classify this movie review as Positive or Negative.

Review: {review_text}

Answer with ONLY one word - Positive or Negative:"""

print("Testing GOOD prompt (clear):")
test_prompt_strategy(good_prompt_clear, num_tests=10)

# COMMAND ----------

# MAGIC %md
# MAGIC **Why it's good:**
# MAGIC - Clear task: "Classify as Positive or Negative"
# MAGIC - Clear output: "ONLY one word"
# MAGIC - Specific format
# MAGIC 
# MAGIC **Expected accuracy: ~75-80%**

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 📖 Part 2: Three Main Strategies
# MAGIC 
# MAGIC Learn the three most effective approaches:

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🎯 Strategy 1: Zero-Shot (No Examples)
# MAGIC 
# MAGIC **Idea**: Just give clear instructions, no examples

# COMMAND ----------

def strategy_zero_shot(review_text):
    """Zero-shot: Instructions only, no examples"""
    return f"""Task: Classify movie review sentiment.

Review: {review_text}

Classification (Positive or Negative):"""

print("Testing STRATEGY 1: Zero-Shot")
accuracy_zero = test_prompt_strategy(strategy_zero_shot, num_tests=20)

# COMMAND ----------

# MAGIC %md
# MAGIC **Strategy 1 Summary:**
# MAGIC - ✅ Simple and fast
# MAGIC - ✅ Good for clear cases
# MAGIC - ❌ Less accurate on complex reviews
# MAGIC - **Typical accuracy: 75-80%**

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🎯 Strategy 2: Few-Shot (With Examples)
# MAGIC 
# MAGIC **Idea**: Show the AI a few examples first

# COMMAND ----------

def strategy_few_shot(review_text):
    """Few-shot: Include examples"""
    return f"""Classify movie reviews as Positive or Negative.

Example 1:
Review: "Brilliant film! Loved every minute of it."
Classification: Positive

Example 2:
Review: "Waste of time. Boring and poorly acted."
Classification: Negative

Example 3:
Review: "Masterpiece! Best movie this year!"
Classification: Positive

Now classify this review:

Review: {review_text}

Classification:"""

print("Testing STRATEGY 2: Few-Shot")
accuracy_few = test_prompt_strategy(strategy_few_shot, num_tests=20)

# COMMAND ----------

# MAGIC %md
# MAGIC **Strategy 2 Summary:**
# MAGIC - ✅ More accurate than zero-shot
# MAGIC - ✅ Shows the AI what you want
# MAGIC - ❌ Longer prompts (slower)
# MAGIC - **Typical accuracy: 82-88%**

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🎯 Strategy 3: Chain-of-Thought (Step-by-Step)
# MAGIC 
# MAGIC **Idea**: Ask the AI to think step-by-step

# COMMAND ----------

def strategy_chain_of_thought(review_text):
    """Chain-of-thought: Ask for reasoning"""
    return f"""Analyze this movie review step by step.

Review: {review_text}

Step 1: What positive words are present?
Step 2: What negative words are present?
Step 3: What is the overall sentiment?

Final Classification (Positive or Negative):"""

print("Testing STRATEGY 3: Chain-of-Thought")
accuracy_cot = test_prompt_strategy(strategy_chain_of_thought, num_tests=20)

# COMMAND ----------

# MAGIC %md
# MAGIC **Strategy 3 Summary:**
# MAGIC - ✅ Best for complex/mixed reviews
# MAGIC - ✅ More reliable
# MAGIC - ❌ Slowest (more generation)
# MAGIC - **Typical accuracy: 85-90%**

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 📊 Part 3: Compare All Strategies

# COMMAND ----------

import pandas as pd

# Create comparison
comparison = pd.DataFrame({
    'Strategy': ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought'],
    'Accuracy': [
        f"{accuracy_zero:.1%}",
        f"{accuracy_few:.1%}",
        f"{accuracy_cot:.1%}"
    ],
    'Speed': ['Fast ⚡', 'Medium 🚶', 'Slow 🐢'],
    'Complexity': ['Simple', 'Medium', 'Complex']
})

print("\n📊 STRATEGY COMPARISON")
print("=" * 60)
display(comparison)

# Find best
accuracies = [accuracy_zero, accuracy_few, accuracy_cot]
strategies = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
best_idx = accuracies.index(max(accuracies))

print(f"\n🏆 Best strategy: {strategies[best_idx]} ({max(accuracies):.1%})")

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 💡 Part 4: Pro Tips
# MAGIC 
# MAGIC **Key Lessons:**
# MAGIC 
# MAGIC 1. **Be Specific**: Tell the AI exactly what format you want
# MAGIC    - ❌ "Tell me the sentiment"
# MAGIC    - ✅ "Answer with ONLY: Positive or Negative"
# MAGIC 
# MAGIC 2. **Use Examples**: Show, don't just tell
# MAGIC    - Add 2-4 clear examples
# MAGIC    - Balance positive and negative examples
# MAGIC 
# MAGIC 3. **Test Iteratively**: 
# MAGIC    - Try something → Test → Improve → Repeat
# MAGIC 
# MAGIC 4. **Keep It Simple**:
# MAGIC    - Longer ≠ Better
# MAGIC    - Remove unnecessary words
# MAGIC 
# MAGIC 5. **Watch Output Format**:
# MAGIC    - "Positive" ≠ "positive" (case matters)
# MAGIC    - Specify exact format you want

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🎯 Part 5: Your Turn to Experiment!
# MAGIC 
# MAGIC Try creating your own prompt:

# COMMAND ----------

def my_experimental_prompt(review_text):
    """
    TODO: Try your own prompt here!
    
    Tips:
    - Start with one of the strategies above
    - Modify it to make it better
    - Test it!
    """
    
    # Example: Start with few-shot and customize
    my_prompt = f"""
    Classify as Positive or Negative.
    
    Example: "Great!" → Positive
    Example: "Terrible!" → Negative
    
    Review: {review_text}
    
    Answer:
    """
    
    return my_prompt

# Test your prompt
print("Testing YOUR experimental prompt:")
test_prompt_strategy(my_experimental_prompt, num_tests=10)

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🎉 Summary
# MAGIC 
# MAGIC **You learned:**
# MAGIC 
# MAGIC ✅ What makes a good vs bad prompt
# MAGIC ✅ Three main strategies:
# MAGIC    - Zero-shot (simple)
# MAGIC    - Few-shot (with examples)
# MAGIC    - Chain-of-thought (step-by-step)
# MAGIC ✅ How to test your prompts
# MAGIC ✅ Pro tips for better results
# MAGIC 
# MAGIC **Next Step:**
# MAGIC 
# MAGIC → **Go to Notebook 3** to compete! Build your best prompt and see how you rank! 🏆

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📝 Your Notes
# MAGIC 
# MAGIC **What strategy worked best for you?**
# MAGIC - 
# MAGIC 
# MAGIC **Ideas to try in the competition:**
# MAGIC - 
# MAGIC 
# MAGIC **Questions:**
# MAGIC -
