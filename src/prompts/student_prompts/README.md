# Student Prompt Submissions

## 📝 How to Submit Your Prompt

### Step 1: Copy the Template

```bash
cp template.py your_name.py
```

Replace `your_name` with your actual name (e.g., `john_doe.py`)

### Step 2: Edit Your File

Open `your_name.py` and:

1. **Fill in your information**:
   ```python
   STUDENT_NAME = "Your Full Name"
   STUDENT_ID = "your_id"
   STRATEGY_DESCRIPTION = "Description of your approach"
   ```

2. **Implement your prompt**:
   ```python
   def get_prompt(review_text):
       # Your prompt engineering magic here
       prompt = f"..."
       return prompt
   ```

3. **Optional: Custom parsing**:
   ```python
   def parse_output(llm_output):
       # Your output parsing logic
       return "Positive" or "Negative"
   ```

### Step 3: Test Locally

Before submitting, test your prompt:

```python
# In a Databricks notebook
from src.evaluation.evaluator import quick_test

results = quick_test('your_name')
```

This will show you:
- Accuracy on sample data
- Confusion matrix
- Inference time

### Step 4: Submit via Git

```bash
git checkout -b feature/your-name-submission
git add src/prompts/student_prompts/your_name.py
git commit -m "Submission: Your Name - [strategy description]"
git push origin feature/your-name-submission
```

Then create a Pull Request on GitHub.

---

## 📋 Submission Checklist

Before submitting, verify:

- [ ] File named correctly (your_name.py)
- [ ] `STUDENT_NAME` filled in
- [ ] `STUDENT_ID` filled in
- [ ] `STRATEGY_DESCRIPTION` written
- [ ] `get_prompt()` function implemented
- [ ] Tested on sample data
- [ ] No syntax errors
- [ ] Output format is correct ("Positive" or "Negative")

---

## 📊 Current Submissions

### Submitted:
- `template.py` (example template - do not modify)

### Your Submission:
Add your file here!

---

## 🎯 Prompt Engineering Tips

1. **Start Simple**: Begin with zero-shot, then improve
2. **Test Iteratively**: Test after each change
3. **Study Examples**: Look at `example_prompts.py`
4. **Read the Guide**: Check `docs/PROMPT_ENGINEERING_GUIDE.md`
5. **Ask Questions**: Don't hesitate to ask for help!

---

## ⚠️ Common Mistakes to Avoid

- ❌ Forgetting to specify output format
- ❌ Using inconsistent formatting
- ❌ Making prompts too long
- ❌ Not testing before submitting
- ❌ Hardcoding specific reviews

---

## 🏆 Good Luck!

Remember: This is about learning, not just winning.
Experiment, fail, learn, and improve!

For questions, ask in the course chat or open a GitHub issue.
