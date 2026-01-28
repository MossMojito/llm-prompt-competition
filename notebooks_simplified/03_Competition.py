# Databricks notebook source
# MAGIC %md
# MAGIC # 🏆 Notebook 3: The Competition!
# MAGIC 
# MAGIC **This is where you compete!**
# MAGIC 
# MAGIC In this notebook you will:
# MAGIC 1. Create your best prompt
# MAGIC 2. Test it on 100 reviews
# MAGIC 3. Get your score
# MAGIC 4. See the leaderboard
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 🎯 Competition Rules
# MAGIC 
# MAGIC - **Dataset**: 100 movie reviews (50 positive, 50 negative)
# MAGIC - **Task**: Classify each as Positive or Negative
# MAGIC - **Scoring**: Accuracy % (higher is better)
# MAGIC - **Winner**: Highest accuracy wins! 🥇
# MAGIC 
# MAGIC **Ready? Let's go!** 🚀

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🔄 Setup (Run This First)

# COMMAND ----------

# Import libraries
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import pandas as pd
import numpy as np
import random
import time

print("Loading model and data...")

# Load model
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Load competition dataset
dataset = load_dataset("imdb", split="test")
positive_reviews = [ex for ex in dataset if ex['label'] == 1][:50]
negative_reviews = [ex for ex in dataset if ex['label'] == 0][:50]
competition_dataset = positive_reviews + negative_reviews

# Shuffle with fixed seed (everyone gets same order)
random.seed(42)
random.shuffle(competition_dataset)

print(f"✅ Ready! Competition dataset: {len(competition_dataset)} reviews")

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 👤 YOUR INFORMATION
# MAGIC 
# MAGIC **Fill in your details:**

# COMMAND ----------

# ==========================================
# YOUR INFORMATION - EDIT HERE
# ==========================================

YOUR_NAME = "John Doe"  # ← Change to your name

YOUR_STRATEGY = "Few-shot with examples"  # ← Describe your approach

# ==========================================

print(f"Competitor: {YOUR_NAME}")
print(f"Strategy: {YOUR_STRATEGY}")

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🎨 YOUR PROMPT
# MAGIC 
# MAGIC **This is the most important part!**
# MAGIC 
# MAGIC Edit the function below to create your best prompt.

# COMMAND ----------

# ==========================================
# YOUR PROMPT FUNCTION - EDIT HERE
# ==========================================

def get_my_prompt(review_text):
    """
    This function creates your prompt.
    
    You can use any strategy you learned:
    - Zero-shot (just instructions)
    - Few-shot (with examples)
    - Chain-of-thought (step-by-step)
    - Or create your own!
    
    Args:
        review_text: The movie review to classify
        
    Returns:
        Your complete prompt as a string
    """
    
    # ⬇️⬇️⬇️ EDIT YOUR PROMPT BELOW ⬇️⬇️⬇️
    
    my_prompt = f"""Classify this movie review as Positive or Negative.

Review: {review_text}

Classification:"""
    
    # ⬆️⬆️⬆️ EDIT YOUR PROMPT ABOVE ⬆️⬆️⬆️
    
    return my_prompt

# ==========================================

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🧪 Test Your Prompt
# MAGIC 
# MAGIC Let's see what your prompt looks like:

# COMMAND ----------

# Show example of your prompt
test_review = "This movie was absolutely amazing! Best film of the year."

print("=" * 70)
print("EXAMPLE: What your prompt looks like")
print("=" * 70)
print(get_my_prompt(test_review))
print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC **Does your prompt look good?**
# MAGIC - ✅ Clear instructions?
# MAGIC - ✅ Specifies output format?
# MAGIC - ✅ Includes examples (if using few-shot)?
# MAGIC 
# MAGIC If yes → Continue!  
# MAGIC If no → Go back and edit!

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🏁 RUN THE COMPETITION
# MAGIC 
# MAGIC This will test your prompt on all 100 reviews.
# MAGIC 
# MAGIC **Takes ~5-10 minutes. Go grab a coffee! ☕**

# COMMAND ----------

def run_competition(prompt_function, dataset):
    """
    Run the competition with your prompt
    
    Args:
        prompt_function: Your get_my_prompt function
        dataset: Competition dataset
        
    Returns:
        Dictionary with results
    """
    print(f"🏁 Starting competition for {YOUR_NAME}...")
    print(f"Testing on {len(dataset)} reviews")
    print("=" * 70)
    
    predictions = []
    true_labels = []
    start_time = time.time()
    
    for i, example in enumerate(dataset):
        review = example['text']
        true_label = example['label']
        
        # Generate prompt
        prompt = prompt_function(review)
        
        # Run model
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(**inputs, max_length=10, num_beams=1)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Parse result
        if "Positive" in result or "positive" in result:
            pred = 1
        elif "Negative" in result or "negative" in result:
            pred = 0
        else:
            pred = 1  # Default to positive
        
        predictions.append(pred)
        true_labels.append(true_label)
        
        # Progress update
        if (i + 1) % 20 == 0:
            print(f"   Processed {i+1}/{len(dataset)} reviews...")
    
    # Calculate metrics
    accuracy = accuracy_score(true_labels, predictions)
    f1 = f1_score(true_labels, predictions)
    cm = confusion_matrix(true_labels, predictions)
    
    elapsed_time = time.time() - start_time
    
    results = {
        'name': YOUR_NAME,
        'strategy': YOUR_STRATEGY,
        'accuracy': accuracy,
        'f1_score': f1,
        'confusion_matrix': cm,
        'time': elapsed_time,
        'predictions': predictions,
        'true_labels': true_labels
    }
    
    return results

# Run it!
my_results = run_competition(get_my_prompt, competition_dataset)

print("\n" + "=" * 70)
print("✅ Competition complete!")
print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 📊 YOUR RESULTS

# COMMAND ----------

# Display results
print("\n" + "=" * 70)
print(f"🏆 RESULTS FOR {my_results['name']}")
print("=" * 70)

print(f"\n✨ Strategy: {my_results['strategy']}")
print(f"\n📈 SCORES:")
print(f"   Accuracy:  {my_results['accuracy']:.2%}")
print(f"   F1 Score:  {my_results['f1_score']:.3f}")
print(f"\n⏱️  Time: {my_results['time']:.1f} seconds")

# Confusion Matrix
cm = my_results['confusion_matrix']
tn, fp, fn, tp = cm.ravel()

print(f"\n📊 DETAILED BREAKDOWN:")
print(f"   Correct Positive: {tp}/50 ({tp/50:.1%})")
print(f"   Correct Negative: {tn}/50 ({tn/50:.1%})")
print(f"   Wrong Positive:   {fp} (said Positive, was Negative)")
print(f"   Wrong Negative:   {fn} (said Negative, was Positive)")

print("\n" + "=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📈 Visualize Your Results

# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns

# Confusion Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm, 
    annot=True, 
    fmt='d', 
    cmap='Blues',
    xticklabels=['Negative', 'Positive'],
    yticklabels=['Negative', 'Positive']
)
plt.title(f'Confusion Matrix - {YOUR_NAME}', fontsize=14, fontweight='bold')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.tight_layout()
plt.show()

# Accuracy Bar Chart
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# Overall accuracy
categories = ['Your Score', 'Perfect Score']
scores = [my_results['accuracy'] * 100, 100]
colors = ['#3498db', '#2ecc71']

ax[0].bar(categories, scores, color=colors, alpha=0.8)
ax[0].set_ylabel('Accuracy (%)')
ax[0].set_title('Your Accuracy vs Perfect')
ax[0].set_ylim([0, 100])
ax[0].axhline(y=50, color='r', linestyle='--', label='Random Guess (50%)')
ax[0].legend()

# Add value labels
for i, v in enumerate(scores):
    ax[0].text(i, v + 2, f'{v:.1f}%', ha='center', fontweight='bold')

# Breakdown by sentiment
sentiments = ['Negative Reviews', 'Positive Reviews']
correct_by_sentiment = [tn, tp]
total_by_sentiment = [50, 50]
accuracy_by_sentiment = [c/t*100 for c, t in zip(correct_by_sentiment, total_by_sentiment)]

ax[1].bar(sentiments, accuracy_by_sentiment, color=['#e74c3c', '#2ecc71'], alpha=0.8)
ax[1].set_ylabel('Accuracy (%)')
ax[1].set_title('Accuracy by Sentiment Type')
ax[1].set_ylim([0, 100])
ax[1].axhline(y=my_results['accuracy']*100, color='b', linestyle='--', label='Overall Avg')
ax[1].legend()

# Add value labels
for i, v in enumerate(accuracy_by_sentiment):
    ax[1].text(i, v + 2, f'{v:.1f}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🎯 How Do You Compare?
# MAGIC 
# MAGIC **Benchmark Scores:**

# COMMAND ----------

# Create benchmark comparison
benchmark_data = {
    'Approach': [
        'Random Guess',
        'Simple Prompt',
        'Zero-Shot',
        'Few-Shot',
        'Chain-of-Thought',
        f'**{YOUR_NAME}**'
    ],
    'Accuracy': [
        '50%',
        '70-75%',
        '75-80%',
        '82-88%',
        '85-90%',
        f'**{my_results["accuracy"]:.1%}**'
    ],
    'Level': [
        'Baseline',
        'Beginner',
        'Intermediate',
        'Advanced',
        'Expert',
        '**YOUR SCORE**'
    ]
}

benchmark_df = pd.DataFrame(benchmark_data)

print("\n📊 BENCHMARK COMPARISON")
print("=" * 70)
display(benchmark_df)

# Determine rank
accuracy_pct = my_results['accuracy'] * 100
if accuracy_pct >= 90:
    rank = "🏆 EXPERT - Top Tier!"
elif accuracy_pct >= 85:
    rank = "🥇 ADVANCED - Excellent!"
elif accuracy_pct >= 80:
    rank = "🥈 SOLID - Good job!"
elif accuracy_pct >= 75:
    rank = "🥉 INTERMEDIATE - Keep improving!"
elif accuracy_pct >= 70:
    rank = "📚 BEGINNER - Nice start!"
else:
    rank = "💪 KEEP TRYING - You can do better!"

print(f"\nYour Level: {rank}")
print("=" * 70)

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 💾 Save Your Results

# COMMAND ----------

# Save results to a DataFrame
results_df = pd.DataFrame({
    'Name': [my_results['name']],
    'Strategy': [my_results['strategy']],
    'Accuracy': [f"{my_results['accuracy']:.2%}"],
    'F1 Score': [f"{my_results['f1_score']:.3f}"],
    'Time (sec)': [f"{my_results['time']:.1f}"]
})

print("Your submission summary:")
display(results_df)

# You can save this to share with others
# results_df.to_csv(f"/dbfs/FileStore/llm-course/{YOUR_NAME}_results.csv", index=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🤔 Want to Improve?
# MAGIC 
# MAGIC **If your score isn't what you wanted:**
# MAGIC 
# MAGIC 1. **Go back** to the prompt cell
# MAGIC 2. **Try a different strategy**:
# MAGIC    - Add examples if you didn't have them
# MAGIC    - Try chain-of-thought
# MAGIC    - Be more specific about output format
# MAGIC 3. **Re-run** the competition
# MAGIC 4. **Compare** your new score
# MAGIC 
# MAGIC **Tips to improve:**
# MAGIC - 📚 Review Notebook 2 (strategies)
# MAGIC - 👀 Look at where you made mistakes (confusion matrix)
# MAGIC - 🎯 Did you get more Positive or Negative wrong?
# MAGIC - 💡 Adjust your prompt accordingly

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC 
# MAGIC # 🎉 Congratulations!
# MAGIC 
# MAGIC **You completed the competition!**
# MAGIC 
# MAGIC ### ✅ What You Achieved:
# MAGIC - Built a working prompt for sentiment analysis
# MAGIC - Tested it on 100 real movie reviews
# MAGIC - Got a measurable accuracy score
# MAGIC - Learned prompt engineering hands-on
# MAGIC 
# MAGIC ### 📊 Your Score:
# MAGIC - **Accuracy: {:.2%}**
# MAGIC - **Rank: {}**
# MAGIC 
# MAGIC ### 🚀 Next Steps:
# MAGIC - Share your results with the group
# MAGIC - Learn from others' strategies
# MAGIC - Try to beat your own score
# MAGIC - Apply these skills to real projects!
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC **Great job! You're now a prompt engineer!** 🎓

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📝 Your Reflections
# MAGIC 
# MAGIC **What worked well in your prompt?**
# MAGIC - 
# MAGIC 
# MAGIC **What would you try differently next time?**
# MAGIC - 
# MAGIC 
# MAGIC **Most interesting thing you learned:**
# MAGIC -
