# 🚀 Databricks Setup Guide

**Get started with the LLM Prompt Engineering Competition in 10 minutes**

---

## Prerequisites

✅ Access to a Databricks workspace
✅ Basic Python knowledge  
✅ GitHub account
✅ Git installed (or use Databricks Git integration)

---

## Step 1: Clone the Repository

### Option A: Using Databricks Repos (Recommended)

1. **Navigate to Repos**
   - In Databricks workspace, click on "Repos" in the left sidebar
   - Click "Add Repo"

2. **Add GitHub Repository**
   - Git repository URL: `https://github.com/your-org/llm-prompt-engineering-competition.git`
   - Click "Create Repo"

3. **Access the Files**
   - Your project is now in: `/Repos/[your-username]/llm-prompt-engineering-competition`

### Option B: Using Git CLI

```bash
# Clone to your local machine
git clone https://github.com/your-org/llm-prompt-engineering-competition.git
cd llm-prompt-engineering-competition

# Then upload to Databricks DBFS
databricks fs cp -r . dbfs:/FileStore/llm-course/
```

---

## Step 2: Create a Cluster

### Cluster Configuration

1. **Go to Compute**
   - Click "Compute" in sidebar
   - Click "Create Cluster"

2. **Cluster Settings**
   ```yaml
   Cluster Name: llm-prompt-competition
   
   Cluster Mode: Standard
   
   Databricks Runtime: 13.3 LTS ML
   (Includes Python 3.10, PyTorch, TensorFlow)
   
   Node Type: 
   - Driver: Standard_DS3_v2 (14 GB Memory, 4 Cores)
   - Worker: Standard_DS3_v2
   
   Workers: 2-4 (Auto-scaling)
   
   Auto Termination: 30 minutes
   ```

3. **Advanced Options** (Optional)
   - **Init Scripts**: None needed
   - **Environment Variables**: None needed
   - **Spark Config**: Default is fine

4. **Click "Create Cluster"**
   - Wait 3-5 minutes for cluster to start

### Cluster Policies (If Required)

If your organization has cluster policies:
- Use the ML runtime policy
- Ensure GPU is NOT required (we use CPU)
- Request access if needed

---

## Step 3: Install Dependencies

### Method 1: Using Notebook (Recommended)

1. **Create a new notebook**
   - Workspace → Create → Notebook
   - Name: "00_Setup"
   - Attach to your cluster

2. **Run installation**
   ```python
   # Cell 1: Install from requirements.txt
   %pip install -r /Repos/[your-username]/llm-prompt-engineering-competition/requirements.txt
   
   # Cell 2: Restart Python
   dbutils.library.restartPython()
   
   # Cell 3: Verify installation
   import transformers
   import datasets
   import torch
   
   print("✅ All packages installed successfully!")
   print(f"Transformers version: {transformers.__version__}")
   print(f"PyTorch version: {torch.__version__}")
   ```

### Method 2: Using Cluster Libraries

1. **Go to your cluster**
2. **Click "Libraries" tab**
3. **Install from PyPI**:
   - transformers
   - datasets
   - scikit-learn
   - pandas
   - (or install from requirements.txt)

---

## Step 4: Download the Dataset

### Run Data Loading Script

Create a new notebook:

```python
# Cell 1: Import data loader
import sys
sys.path.append('/Repos/[your-username]/llm-prompt-engineering-competition')

from data.load_data import load_imdb_dataset, create_sample_dataset

# Cell 2: Load dataset
print("Downloading IMDb dataset...")
dataset = load_imdb_dataset(cache_dir="/dbfs/mnt/llm-course/data")

# Cell 3: Create sample files
print("Creating sample datasets...")
create_sample_dataset(
    dataset,
    output_dir="/dbfs/FileStore/llm-course/sample_data"
)

print("✅ Setup complete!")
```

**Expected Output**:
```
Downloading IMDb dataset...
Train samples: 25000
Test samples: 25000
Creating sample datasets...
✅ Sample datasets created:
   - train_sample.json (100 examples)
   - test_sample.json (50 examples)
✅ Setup complete!
```

---

## Step 5: Verify Installation

### Run Verification Notebook

```python
# Cell 1: Test imports
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
import pandas as pd
import numpy as np
import sklearn

print("✅ All imports successful!")

# Cell 2: Test model loading
model_name = "google/flan-t5-base"
print(f"Loading {model_name}...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("✅ Model loaded successfully!")

# Cell 3: Test inference
test_prompt = "Translate to French: Hello, how are you?"
inputs = tokenizer(test_prompt, return_tensors="pt")
outputs = model.generate(**inputs)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(f"Test inference result: {result}")
print("✅ Model inference working!")

# Cell 4: Test data loading
from data.load_data import load_sample_data

sample_path = "/dbfs/FileStore/llm-course/sample_data/test_sample.json"
samples = load_sample_data(sample_path)

print(f"✅ Loaded {len(samples)} sample reviews")
print(f"Example: {samples[0]['text'][:100]}...")
```

---

## Step 6: Explore the Project Structure

### Open the Project

Navigate to: `/Repos/[your-username]/llm-prompt-engineering-competition`

```
📁 Your Project Structure:

├── 📁 data/                    ← Dataset scripts
│   └── load_data.py
│
├── 📁 notebooks/               ← Learning materials
│   ├── 00_setup_guide.ipynb   ← START HERE
│   ├── 01_introduction_to_llm.ipynb
│   ├── 02_prompt_basics.ipynb
│   └── 03_sentiment_analysis.ipynb
│
├── 📁 src/                     ← Source code
│   ├── prompts/
│   │   ├── example_prompts.py ← Study these!
│   │   └── student_prompts/   ← Your code goes here
│   │       └── template.py
│   └── evaluation/
│       ├── metrics.py
│       └── evaluator.py
│
└── 📁 docs/                    ← Documentation
    ├── COMPETITION_RULES.md
    ├── PROMPT_ENGINEERING_GUIDE.md
    └── SETUP.md (you are here!)
```

### Next Steps

1. **Read the docs**
   - `COMPETITION_RULES.md` - Understand the competition
   - `PROMPT_ENGINEERING_GUIDE.md` - Learn techniques

2. **Study examples**
   - Open `src/prompts/example_prompts.py`
   - Run it to see different prompt strategies

3. **Start learning**
   - Open `notebooks/00_setup_guide.ipynb`
   - Follow the learning path in order

---

## Common Issues & Solutions

### Issue 1: Module Not Found

**Error**: `ModuleNotFoundError: No module named 'transformers'`

**Solution**:
```python
%pip install transformers datasets
dbutils.library.restartPython()
```

### Issue 2: CUDA Not Available

**Error**: `RuntimeError: CUDA not available`

**Solution**: This is OK! We use CPU for this course.
```python
# Verify CPU mode
import torch
print(f"Using device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
# Should print: Using device: cpu
```

### Issue 3: Data Not Found

**Error**: `FileNotFoundError: data/sample_data/test_sample.json`

**Solution**: Run the data loading script again:
```python
from data.load_data import create_sample_dataset, load_imdb_dataset
dataset = load_imdb_dataset()
create_sample_dataset(dataset)
```

### Issue 4: Permission Denied

**Error**: `PermissionError: [Errno 13] Permission denied`

**Solution**: Use DBFS paths instead:
```python
# Instead of:
output_dir = "./data/sample_data"

# Use:
output_dir = "/dbfs/FileStore/llm-course/sample_data"
```

### Issue 5: Cluster Won't Start

**Solution**:
1. Check cluster policies
2. Verify you have quota available
3. Try a smaller instance type
4. Contact workspace admin

### Issue 6: Git Integration Issues

**Solution**:
1. Ensure you have a personal access token
2. Check repository URL is correct
3. Verify you have read access
4. Try cloning via HTTPS instead of SSH

---

## Databricks-Specific Tips

### 💡 Tip 1: Use Databricks File System (DBFS)

Store data in DBFS for persistence:
```python
# DBFS paths start with /dbfs/
data_path = "/dbfs/FileStore/llm-course/data"

# Or use dbfs:// in Databricks
data_path = "dbfs:/FileStore/llm-course/data"
```

### 💡 Tip 2: Collaborative Notebooks

Multiple students can work together:
- Share notebooks via workspace
- Use Git for version control
- Comment code clearly

### 💡 Tip 3: Notebook Widgets

Create interactive parameters:
```python
dbutils.widgets.text("student_name", "john_doe")
student_name = dbutils.widgets.get("student_name")
```

### 💡 Tip 4: Display Rich Output

```python
# Display dataframes nicely
display(df)

# Show plots
import matplotlib.pyplot as plt
plt.plot(...)
display(plt.gcf())
```

### 💡 Tip 5: Use MLflow

Track experiments (optional):
```python
import mlflow

mlflow.log_param("prompt_strategy", "few-shot")
mlflow.log_metric("accuracy", 0.85)
```

---

## Resource Limits

### Free/Community Edition
- ⚠️ Limited compute time
- ⚠️ No cluster auto-scaling
- ⚠️ Shared resources

**Recommendation**: Use local development or get workspace access

### Workspace Edition
- ✅ Full cluster access
- ✅ More storage
- ✅ Better performance

---

## File Paths Reference

### In Databricks Notebooks

```python
# Project root
PROJECT_ROOT = "/Repos/[your-username]/llm-prompt-engineering-competition"

# Data
DATA_DIR = f"{PROJECT_ROOT}/data"
SAMPLE_DATA = f"{PROJECT_ROOT}/data/sample_data"

# Source code
SRC_DIR = f"{PROJECT_ROOT}/src"
PROMPTS_DIR = f"{SRC_DIR}/prompts"

# Your prompt file
YOUR_PROMPT = f"{PROMPTS_DIR}/student_prompts/your_name.py"
```

### In DBFS

```python
# Shared data location
DBFS_DATA = "/dbfs/FileStore/llm-course/data"
DBFS_MODELS = "/dbfs/FileStore/llm-course/models"
DBFS_RESULTS = "/dbfs/FileStore/llm-course/results"
```

---

## Quick Command Reference

```python
# List files
%fs ls /FileStore/llm-course/

# Copy files
dbutils.fs.cp("source", "destination")

# Remove files
dbutils.fs.rm("path", recurse=True)

# Read file
with open("/dbfs/path/to/file.txt", "r") as f:
    content = f.read()

# Install package
%pip install package-name

# Restart Python
dbutils.library.restartPython()

# Get widget value
value = dbutils.widgets.get("widget_name")
```

---

## Getting Help

### Within Databricks
- 📚 Documentation: [docs.databricks.com](https://docs.databricks.com)
- 💬 Community: [community.databricks.com](https://community.databricks.com)
- 🎓 Learning: [databricks.com/learn](https://databricks.com/learn)

### For This Course
- Ask instructor in workspace chat
- Post questions in course discussion
- Open GitHub issue for bugs

---

## ✅ Setup Checklist

Before starting the competition, ensure:

- [ ] Databricks cluster is running
- [ ] Repository cloned to workspace
- [ ] Dependencies installed (`requirements.txt`)
- [ ] IMDb dataset downloaded
- [ ] Sample data created
- [ ] Can run example notebooks
- [ ] Can import project modules
- [ ] Understand file structure
- [ ] Read competition rules
- [ ] Studied prompt engineering guide

---

## Next Steps

1. ✅ **Complete this setup**
2. 📖 **Read**: `COMPETITION_RULES.md`
3. 🎨 **Study**: `PROMPT_ENGINEERING_GUIDE.md`
4. 📓 **Open**: `notebooks/01_introduction_to_llm.ipynb`
5. 🚀 **Start building your prompt!**

---

**You're all set! Time to start learning and competing! 🏆**

Good luck! 🎓
