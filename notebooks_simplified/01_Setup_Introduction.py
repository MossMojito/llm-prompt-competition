# Databricks notebook source
# MAGIC %md
# MAGIC # 🎓 Notebook 1: Setup & Introduction
# MAGIC 
# MAGIC **Welcome to the LLM Prompt Engineering Competition!**
# MAGIC 
# MAGIC This notebook will get you ready in 10 minutes.
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## What You'll Learn
# MAGIC 
# MAGIC 1. What is an LLM (Large Language Model)?
# MAGIC 2. What is Prompt Engineering?
# MAGIC 3. How this competition works
# MAGIC 4. Setup your environment
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 🤖 What is an LLM?
# MAGIC 
# MAGIC **Simple explanation:**
# MAGIC - LLM = A very smart AI that understands and generates text
# MAGIC - Like ChatGPT, but you control it with "prompts"
# MAGIC - Same input → Same output (predictable)
# MAGIC 
# MAGIC **Example:**
# MAGIC - You give it: "Classify this review as Positive or Negative: This movie was great!"
# MAGIC - It responds: "Positive"
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 🎨 What is Prompt Engineering?
# MAGIC 
# MAGIC **It's how you "talk" to the AI to get better results.**
# MAGIC 
# MAGIC **Bad prompt:**
# MAGIC ```
# MAGIC "What about this review?"
# MAGIC ```
# MAGIC → AI is confused, gives random answer
# MAGIC 
# MAGIC **Good prompt:**
# MAGIC ```
# MAGIC "Classify this movie review as Positive or Negative.
# MAGIC Review: This movie was great!
# MAGIC Answer:"
# MAGIC ```
# MAGIC → AI understands, gives correct answer
# MAGIC 
# MAGIC **Your job:** Write better prompts to get higher accuracy!
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 🏆 How the Competition Works
# MAGIC 
# MAGIC 1. **Dataset**: 100 movie reviews (50 positive, 50 negative)
# MAGIC 2. **Your task**: Write a prompt that classifies them correctly
# MAGIC 3. **Scoring**: Accuracy % (how many you got right)
# MAGIC 4. **Winner**: Highest accuracy wins! 🥇
# MAGIC 
# MAGIC **Timeline:**
# MAGIC - Today: Learn and setup
# MAGIC - This week: Build your prompt
# MAGIC - Next week: Submit and compete
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 📊 Example Competition
# MAGIC 
# MAGIC | Student | Accuracy | Strategy |
# MAGIC |---------|----------|----------|
# MAGIC | Alice   | 87%      | Used examples in prompt |
# MAGIC | Bob     | 79%      | Simple instructions |
# MAGIC | Charlie | 91%      | Step-by-step reasoning |
# MAGIC 
# MAGIC **You can beat them!** 🎯

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🚀 Step 1: Install Required Packages
# MAGIC 
# MAGIC Run this cell (it takes 1-2 minutes):

# COMMAND ----------

# Install packages
%pip install transformers datasets scikit-learn pandas --quiet

# Restart Python to use new packages
dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Step 2: Verify Installation
# MAGIC 
# MAGIC Run this cell to check everything is working:

# COMMAND ----------

# Test imports
print("Testing imports...")

try:
    import transformers
    import datasets
    import sklearn
    import pandas as pd
    import numpy as np
    
    print("✅ All packages installed successfully!")
    print(f"   - Transformers version: {transformers.__version__}")
    print(f"   - Datasets version: {datasets.__version__}")
    print(f"   - Scikit-learn version: {sklearn.__version__}")
    
except ImportError as e:
    print(f"❌ Error: {e}")
    print("Please re-run the installation cell above")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📥 Step 3: Download Dataset
# MAGIC 
# MAGIC This downloads the IMDb movie reviews dataset (takes 2-3 minutes):

# COMMAND ----------

from datasets import load_dataset

print("📥 Downloading IMDb movie reviews dataset...")
print("(This might take 2-3 minutes on first run)")

# Load dataset - we'll use first 100 examples for quick testing
dataset = load_dataset("imdb", split="test")

print(f"\n✅ Dataset loaded successfully!")
print(f"   Total reviews available: {len(dataset)}")

# Show example
print("\n📝 Example review:")
example = dataset[0]
print(f"Review: {example['text'][:200]}...")
print(f"Label: {'Positive' if example['label'] == 1 else 'Negative'}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🎯 Step 4: Load the AI Model
# MAGIC 
# MAGIC This loads the language model (takes 3-5 minutes):

# COMMAND ----------

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("🤖 Loading AI model (FLAN-T5-Small)...")
print("This will take 3-5 minutes...")

model_name = "google/flan-t5-small"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("\n✅ Model loaded successfully!")
print(f"   Model: {model_name}")
print(f"   Size: ~80MB (CPU-friendly)")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🧪 Step 5: Test the Model
# MAGIC 
# MAGIC Let's see how the AI responds to a simple prompt:

# COMMAND ----------

def test_model(prompt):
    """Test the model with a prompt"""
    # Convert text to tokens
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    
    # Generate response
    outputs = model.generate(**inputs, max_length=10)
    
    # Convert tokens back to text
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return result

# Test with a simple prompt
test_prompt = "Is this review positive or negative? Review: This movie was amazing! Answer:"

print("Testing model...")
print(f"\nPrompt:\n{test_prompt}")
print(f"\nModel Response: {test_model(test_prompt)}")

print("\n✅ Model is working! You're ready to compete!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📊 Step 6: Prepare Competition Dataset
# MAGIC 
# MAGIC Let's create our competition dataset (100 reviews):

# COMMAND ----------

# Create balanced dataset: 50 positive, 50 negative
positive_reviews = [ex for ex in dataset if ex['label'] == 1][:50]
negative_reviews = [ex for ex in dataset if ex['label'] == 0][:50]

competition_dataset = positive_reviews + negative_reviews

# Shuffle
import random
random.seed(42)
random.shuffle(competition_dataset)

print(f"✅ Competition dataset ready!")
print(f"   Total reviews: {len(competition_dataset)}")
print(f"   Positive: 50 (50%)")
print(f"   Negative: 50 (50%)")

# Show statistics
import pandas as pd

sample_reviews = pd.DataFrame({
    'Preview': [ex['text'][:100] + '...' for ex in competition_dataset[:5]],
    'Label': ['Positive' if ex['label'] == 1 else 'Negative' for ex in competition_dataset[:5]]
})

print("\n📝 First 5 reviews:")
display(sample_reviews)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🎉 Setup Complete!
# MAGIC 
# MAGIC **You're ready to compete!**
# MAGIC 
# MAGIC ### ✅ What You Have Now:
# MAGIC - AI model loaded and working
# MAGIC - Dataset ready (100 movie reviews)
# MAGIC - Understanding of how it works
# MAGIC 
# MAGIC ### 📚 Next Steps:
# MAGIC 
# MAGIC 1. **Open Notebook 2**: Learn prompt engineering techniques
# MAGIC 2. **Open Notebook 3**: Build your prompt and compete!
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 💡 Key Concepts to Remember
# MAGIC 
# MAGIC 1. **LLM** = AI that understands text
# MAGIC 2. **Prompt** = Instructions you give the AI
# MAGIC 3. **Better prompts** = Higher accuracy
# MAGIC 4. **Goal** = Get highest accuracy score
# MAGIC 
# MAGIC **Ready to learn prompt engineering?** → Go to Notebook 2! 🚀

# COMMAND ----------

# MAGIC %md
# MAGIC ## 📝 Notes Section (Optional)
# MAGIC 
# MAGIC Use this space for your notes:
# MAGIC 
# MAGIC **Things I learned:**
# MAGIC - 
# MAGIC 
# MAGIC **Questions I have:**
# MAGIC - 
# MAGIC 
# MAGIC **Ideas to try:**
# MAGIC -
