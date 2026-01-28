# 📜 Competition Rules & Guidelines

## 🎯 Competition Overview

**Objective**: Create the best prompt for sentiment analysis classification

**Dataset**: IMDb movie reviews (25,000 train, 1,000 test)

**Task**: Classify reviews as "Positive" or "Negative"

**Prize**: Glory, knowledge, and eternal bragging rights! 🏆

---

## ✅ What's Allowed

### Prompting Techniques
- ✅ Zero-shot prompts (just instructions, no examples)
- ✅ Few-shot prompts (include example reviews with labels)
- ✅ Chain-of-thought reasoning (step-by-step analysis)
- ✅ Role-playing (e.g., "You are a movie critic...")
- ✅ Structured instructions (numbered steps, etc.)
- ✅ Custom output parsing logic
- ✅ Creative prompt engineering approaches

### Data Usage
- ✅ Use training data to design prompts
- ✅ Create your own few-shot examples
- ✅ Analyze patterns in the training data
- ✅ Test on the provided sample dataset

### Collaboration
- ✅ Discuss strategies with other students
- ✅ Learn from example prompts provided
- ✅ Ask instructor for clarification
- ✅ Share insights after submission deadline

---

## ❌ What's NOT Allowed

### Prohibited Actions
- ❌ **No fine-tuning**: You can only use prompting, not model training
- ❌ **No test set access**: The evaluation test set is hidden
- ❌ **No hardcoding**: Don't hardcode specific review texts and their labels
- ❌ **No external APIs**: Use only the provided HuggingFace model
- ❌ **No copying**: Don't copy other students' exact prompts
- ❌ **No cheating**: Play fair, learn genuinely

### Technical Constraints
- ❌ Prompts exceeding 1000 tokens will be truncated
- ❌ Output must be exactly "Positive" or "Negative" (case-sensitive)
- ❌ Don't modify the evaluation code or test data
- ❌ Don't submit after the deadline

---

## 📊 Scoring System

### Primary Metric: Accuracy
Your main score is the **accuracy** on the hidden test set (1,000 reviews).

```
Accuracy = (Correct Predictions) / (Total Predictions)
```

**Example**:
- 850 correct predictions out of 1000 = 85% accuracy

### Secondary Metric: F1 Score
Used for tie-breaking and to ensure balanced performance.

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

### Bonus Points (Optional)

1. **Speed Bonus (+2%)**
   - Fastest average inference time per review
   - Only awarded if accuracy > 80%

2. **Creativity Bonus (+1%)**
   - Most innovative prompting approach
   - Determined by peer voting after reveal

3. **Explanation Bonus (+1%)**
   - Best documentation of prompt strategy
   - Clear explanation in code comments

### Leaderboard Ranking

Rankings are determined by:
1. **Primary**: Accuracy (descending)
2. **Tiebreaker 1**: F1 Score (descending)
3. **Tiebreaker 2**: Submission time (earlier is better)

---

## 📝 Submission Guidelines

### File Requirements

1. **Filename**: `your_name.py` (e.g., `john_doe.py`)
2. **Location**: `src/prompts/student_prompts/`
3. **Format**: Must follow the template structure

### Required Elements

Your submission MUST include:

```python
# Student information
STUDENT_NAME = "Your Full Name"
STUDENT_ID = "your_id"
STRATEGY_DESCRIPTION = "Brief description of your approach"

# Main function
def get_prompt(review_text):
    """Your prompt generation logic"""
    # ... your code ...
    return prompt

# Optional
def parse_output(llm_output):
    """Custom output parsing (optional)"""
    # ... your code ...
    return "Positive" or "Negative"
```

### Testing Before Submission

**Always test locally first!**

```python
# In Databricks notebook
from src.evaluation.evaluator import quick_test

# Test your prompt
results = quick_test('your_name')
```

Expected output:
- Accuracy on sample data
- Confusion matrix
- Inference time

### Submission Process

1. **Create your prompt file**
   ```bash
   cp src/prompts/student_prompts/template.py src/prompts/student_prompts/john_doe.py
   ```

2. **Edit and test**
   - Implement your strategy
   - Test on sample data
   - Iterate and improve

3. **Submit via Pull Request**
   ```bash
   git checkout -b feature/john-doe-submission
   git add src/prompts/student_prompts/john_doe.py
   git commit -m "Submission: John Doe - Few-shot approach"
   git push origin feature/john-doe-submission
   ```

4. **Create PR on GitHub**
   - Title: "Submission: [Your Name]"
   - Description: 
     - Brief strategy explanation
     - Expected accuracy (optional)
     - Any special notes

---

## 📅 Timeline

### Week 1: Learning Phase
- **Monday-Wednesday**: Study LLM basics and prompting techniques
- **Thursday-Friday**: Experiment with sample data
- **Weekend**: Design your strategy

### Week 2: Development Phase
- **Monday-Wednesday**: Implement and refine your prompt
- **Thursday**: Final testing and optimization
- **Friday 5 PM**: **SUBMISSION DEADLINE** ⏰

### Week 3: Evaluation Phase
- **Monday**: Automated evaluation on hidden test set
- **Tuesday**: Leaderboard announcement 🏆
- **Wednesday**: Top 3 present strategies

### Week 4: Knowledge Sharing
- **Monday**: Winner presentation
- **Tuesday-Wednesday**: Group discussion and learning
- **Thursday**: Optional: Improve prompts with new knowledge
- **Friday**: Final showcase

---

## 🎤 Presentation Requirements (Top 3)

If you place in the top 3, you'll present your approach (5-10 minutes):

### What to Cover:
1. **Strategy Overview**: What approach did you use?
2. **Design Decisions**: Why did you make specific choices?
3. **Challenges**: What didn't work initially?
4. **Iterations**: How did you improve?
5. **Key Insights**: What did you learn?

### Format:
- Slides (optional) or live code walkthrough
- Show your actual prompt
- Demonstrate on example reviews
- Q&A from peers

---

## ⚖️ Fair Play & Academic Integrity

### Encouraged Collaboration
- ✅ Discussing general strategies
- ✅ Helping each other debug code
- ✅ Sharing learning resources
- ✅ Studying example prompts together

### Academic Dishonesty
- ❌ Copying someone else's exact prompt
- ❌ Sharing your complete prompt before deadline
- ❌ Having someone else write your prompt
- ❌ Plagiarizing from online sources

**Penalty for cheating**: Disqualification and 0 points

---

## 🆘 Getting Help

### When You're Stuck

1. **Check Resources**:
   - Read example prompts in `src/prompts/example_prompts.py`
   - Review the Prompt Engineering Guide
   - Check documentation in `docs/`

2. **Ask Questions**:
   - Post in Databricks workspace chat
   - Ask instructor during office hours
   - Open GitHub issue for technical problems

3. **Debug**:
   - Test on 1-2 examples first
   - Print your prompt to see what's generated
   - Check error messages carefully

### Common Issues

**Problem**: My prompt generates wrong format
**Solution**: Add explicit output format instructions

**Problem**: Accuracy is too low
**Solution**: Try few-shot examples or chain-of-thought

**Problem**: Prompt is too long
**Solution**: Remove unnecessary words, focus on key instructions

**Problem**: Model is slow
**Solution**: Use shorter prompts, avoid very long examples

---

## 📊 Evaluation Process

### How Your Prompt is Evaluated

1. **Automated System** loads your prompt file
2. **For each test review**:
   - Your `get_prompt()` function generates the prompt
   - LLM processes the prompt
   - Your `parse_output()` extracts the prediction
3. **Metrics calculated**: Accuracy, F1, precision, recall
4. **Results saved** to leaderboard

### What Happens During Evaluation

```
For each of 1,000 test reviews:
  1. Generate prompt using your function
  2. Send to LLM (google/flan-t5-base)
  3. Parse output (Positive or Negative)
  4. Compare with true label
  
Calculate final accuracy and ranking
```

### Hidden Test Set

- 1,000 reviews selected randomly
- Balanced: 500 positive, 500 negative
- Not accessible until after competition
- Same for all students (fair comparison)

---

## 🏆 Prizes & Recognition

### Winner (1st Place)
- 🥇 Gold medal on leaderboard
- Featured in course materials
- Present at future course cohorts
- Certificate of excellence

### Runner-up (2nd Place)
- 🥈 Silver medal on leaderboard
- Spotlight in final showcase
- Certificate of achievement

### Third Place
- 🥉 Bronze medal on leaderboard
- Recognition in final presentation
- Certificate of participation

### Special Awards

- 🚀 **Most Creative**: Most innovative approach
- ⚡ **Speed Demon**: Fastest inference time
- 📚 **Best Explainer**: Clearest strategy documentation
- 💡 **Most Improved**: Biggest improvement from first to final submission

---

## ❓ Frequently Asked Questions

**Q: Can I submit multiple times?**
A: Yes, but only your last submission before deadline counts.

**Q: Can I use GPT-4 or Claude API?**
A: No, only the provided HuggingFace model (google/flan-t5-base).

**Q: How long should my prompt be?**
A: No hard limit, but shorter is often better. Keep under 1000 tokens.

**Q: Can I see others' prompts before submitting?**
A: No, prompts are revealed after the deadline.

**Q: What if I'm not good at coding?**
A: This is about prompting, not complex coding! Start with simple prompts.

**Q: Can I use non-English prompts?**
A: Technically yes, but English works best with the model.

**Q: What if my code has a bug during evaluation?**
A: You'll get 0 accuracy. Test thoroughly before submitting!

**Q: Can I change my prompt after seeing the leaderboard?**
A: No, the competition ends when results are announced.

---

## 🎓 Learning Objectives

By participating, you will:

1. ✅ Understand how LLMs work
2. ✅ Master prompt engineering techniques
3. ✅ Learn evaluation metrics for NLP
4. ✅ Practice iterative development
5. ✅ Experience real-world ML workflows
6. ✅ Collaborate with peers
7. ✅ Build portfolio projects

---

## 📞 Contact

**Questions about rules?**
- Email: [instructor email]
- Databricks chat: @instructor
- GitHub Issues: Technical problems

**Want to give feedback?**
- We're always improving! Share your thoughts on:
  - Competition format
  - Learning materials
  - Evaluation process

---

**Good luck, and may the best prompt win!** 🚀

*Remember: The goal is learning, not just winning. Experiment, fail, learn, and improve!*
