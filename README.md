# 🎯 LLM Prompt Engineering Competition

**Master the Art of Prompt Engineering through Hands-on Competition**

Learn how to build effective prompts for Large Language Models (LLMs) by competing to create the best sentiment analysis classifier using the IMDb movie review dataset.

## 📊 Current Leaderboard

| Rank | Student | Accuracy | F1 Score | Strategy | Submission Date |
|------|---------|----------|----------|----------|----------------|
| 🥇 1 | TBD | - | - | - | - |
| 🥈 2 | TBD | - | - | - | - |
| 🥉 3 | TBD | - | - | - | - |

*Leaderboard updates every Monday*

---

## 🎓 What You'll Learn

- ✅ How LLMs work (decoder-only architecture)
- ✅ Prompt engineering techniques (zero-shot, few-shot, chain-of-thought)
- ✅ Evaluation metrics for NLP tasks
- ✅ Working with HuggingFace Transformers
- ✅ Databricks collaborative development
- ✅ Git workflow for ML projects

---

## 🚀 Quick Start

### Prerequisites
- Databricks workspace access
- Basic Python knowledge
- Git installed

### Setup (5 minutes)

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-org/llm-prompt-engineering-competition.git
   cd llm-prompt-engineering-competition
   ```

2. **Import to Databricks**
   - Go to your Databricks workspace
   - Click "Repos" → "Add Repo"
   - Paste the Git URL
   - Click "Create Repo"

3. **Install dependencies**
   ```python
   # Run in Databricks notebook
   %pip install -r requirements.txt
   ```

4. **Start learning!**
   - Open `notebooks/00_setup_guide.ipynb`
   - Follow the tutorial notebooks in order

---

## 📚 Learning Path

### Week 1: Understanding LLMs
- 📓 Notebook 01: Introduction to LLMs
- 📓 Notebook 02: Prompt Engineering Basics
- 🎯 Goal: Understand how LLMs generate text

### Week 2: Build Your Classifier
- 📓 Notebook 03: Sentiment Analysis Challenge
- 💻 Create your prompt in `src/prompts/student_prompts/`
- 🎯 Goal: Submit your best prompt

### Week 3: Competition & Evaluation
- 📊 Automated evaluation on hidden test set
- 🏆 Leaderboard announcement
- 🎯 Goal: Learn from top performers

### Week 4: Knowledge Sharing
- 🎤 Winners present their strategies
- 📝 Update best practices guide
- 🎯 Goal: Improve everyone's understanding

---

## 🎮 Competition Rules

### The Challenge
**Task**: Classify IMDb movie reviews as "Positive" or "Negative"

**Dataset**: 
- Training: 25,000 labeled reviews (available)
- Test: 1,000 reviews (hidden until evaluation)

**Constraints**:
- ✅ Prompting only (no fine-tuning)
- ✅ Max prompt length: 1000 tokens
- ✅ Output must be exactly "Positive" or "Negative"
- ❌ No hardcoding test data
- ❌ No external APIs

### Scoring
- **Primary Metric**: Accuracy (%)
- **Secondary Metric**: F1 Score
- **Bonus Points**:
  - +2% fastest inference time
  - +1% most creative approach (peer vote)
  - +1% best explanation

### Submission
1. Create file: `src/prompts/student_prompts/your_name.py`
2. Follow the template format
3. Test locally first
4. Submit via Pull Request
5. **Deadline**: Week 2, Friday 5 PM

---

## 📁 Project Structure

```
llm-prompt-engineering-competition/
├── data/               # Dataset loading and samples
├── notebooks/          # Learning notebooks (start here!)
├── src/
│   ├── prompts/       # Your prompts go here
│   ├── evaluation/    # Scoring system
│   └── utils/         # Helper functions
├── configs/           # Configuration files
├── results/           # Leaderboard and outputs
└── docs/              # Detailed documentation
```

---

## 🤝 How to Submit Your Prompt

### Step-by-Step Guide

1. **Create your prompt file**
   ```bash
   cp src/prompts/student_prompts/template.py src/prompts/student_prompts/john_doe.py
   ```

2. **Edit the file with your prompt strategy**
   - Follow the template format
   - Add your classification logic
   - Document your approach

3. **Test locally**
   ```python
   # In Databricks notebook
   from src.evaluation.evaluator import test_prompt
   test_prompt('john_doe')
   ```

4. **Submit via Pull Request**
   ```bash
   git checkout -b feature/john-doe-prompt
   git add src/prompts/student_prompts/john_doe.py
   git commit -m "Add John Doe's sentiment classifier"
   git push origin feature/john-doe-prompt
   ```

5. **Create PR on GitHub**
   - Title: "Submission: [Your Name]"
   - Description: Brief explanation of your strategy

---

## 📖 Resources

### Documentation
- 📄 [Setup Guide](docs/SETUP.md)
- 📄 [Competition Rules](docs/COMPETITION_RULES.md)
- 📄 [Prompt Engineering Guide](docs/PROMPT_ENGINEERING_GUIDE.md)
- 📄 [Evaluation Metrics](docs/EVALUATION.md)

### External Resources
- [HuggingFace Transformers Docs](https://huggingface.co/docs/transformers)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Databricks Documentation](https://docs.databricks.com/)

---

## 🏆 Past Winners

### Round 1 (Current)
*Competition in progress...*

---

## 🤔 FAQ

**Q: Can I use GPT-4 API?**  
A: No, only open-source models from HuggingFace allowed.

**Q: How many examples can I put in my prompt?**  
A: As many as you want, but keep total prompt under 1000 tokens.

**Q: Can I see other students' prompts?**  
A: Yes, after submission deadline all prompts become public for learning.

**Q: What if my prompt doesn't work?**  
A: Check the error logs, ask for help, and keep iterating!

---

## 📞 Support

- **Technical Issues**: Open a GitHub Issue
- **Questions**: Ask in Databricks workspace chat
- **Instructor**: [Your contact info]

---

## 📜 License

MIT License - Feel free to use for educational purposes

---

## 🙏 Acknowledgments

- IMDb dataset from HuggingFace Datasets
- Built for learning prompt engineering
- Inspired by real-world ML competitions

---

**Ready to compete? Start with `notebooks/00_setup_guide.ipynb`** 🚀
