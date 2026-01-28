# 🚀 QUICK START - Read This First!

**Welcome to the LLM Prompt Engineering Competition!**

You've downloaded a complete, production-ready project for teaching prompt engineering through hands-on competition.

---

## 📦 What's Included

This project contains **everything** you need:

✅ **Complete Documentation** - Setup guides, competition rules, learning materials
✅ **Working Code** - Data loaders, evaluation system, example prompts  
✅ **Sample Data** - Ready-to-use IMDb sentiment analysis dataset
✅ **Example Submissions** - Learn from real examples
✅ **Databricks Integration** - Notebooks and configuration for collaborative learning

---

## 🎯 For Instructors

### Getting Started (15 minutes)

1. **Upload to GitHub**
   ```bash
   cd llm-prompt-engineering-competition
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Set Up Databricks**
   - Import repository to Databricks workspace
   - Create shared cluster (see `docs/SETUP.md`)
   - Install dependencies from `requirements.txt`

3. **Prepare Data**
   ```python
   # Run in Databricks notebook
   from data.load_data import load_imdb_dataset, create_sample_dataset
   
   dataset = load_imdb_dataset()
   create_sample_dataset(dataset)
   ```

4. **Share with Students**
   - Give them repository access
   - Direct them to `docs/SETUP.md`
   - Point them to `docs/COMPETITION_RULES.md`

### Customization

**Change the model**: Edit `configs/model_config.yaml`
**Adjust timeline**: Update `docs/COMPETITION_RULES.md`
**Modify scoring**: Edit `src/evaluation/metrics.py`
**Add datasets**: Extend `data/load_data.py`

---

## 👨‍🎓 For Students

### Your Learning Path

1. **Week 1: Learn**
   - Read `docs/SETUP.md` - Get environment ready
   - Read `docs/PROMPT_ENGINEERING_GUIDE.md` - Learn techniques
   - Study `src/prompts/example_prompts.py` - See examples
   - Explore `src/prompts/student_prompts/alice_example.py`

2. **Week 2: Build**
   - Copy `src/prompts/student_prompts/template.py`
   - Implement your prompt strategy
   - Test with sample data
   - Submit via Pull Request

3. **Week 3: Compete**
   - Automated evaluation runs
   - Leaderboard announced
   - Learn from winners

4. **Week 4: Share**
   - Winners present strategies
   - Everyone improves
   - Celebrate learning!

### Quick Test

```python
# Test your prompt in Databricks
from src.evaluation.evaluator import quick_test

results = quick_test('your_name')
# Shows accuracy, F1 score, confusion matrix
```

---

## 📁 Project Structure

```
llm-prompt-engineering-competition/
│
├── 📄 README.md                    ← Project overview, start here!
├── 📄 requirements.txt             ← Python dependencies
├── 📄 .gitignore                   ← Git ignore rules
│
├── 📁 data/                        ← Dataset management
│   ├── load_data.py                ← Load IMDb dataset
│   ├── sample_data/                ← Small test datasets
│   └── README.md                   ← Data documentation
│
├── 📁 src/                         ← Source code
│   ├── prompts/                    
│   │   ├── example_prompts.py      ← Learn from these!
│   │   └── student_prompts/        
│   │       ├── template.py         ← Copy this to start
│   │       ├── alice_example.py    ← Example submission
│   │       └── README.md           ← How to submit
│   │
│   └── evaluation/                 
│       ├── metrics.py              ← Scoring functions
│       └── evaluator.py            ← Main evaluation engine
│
├── 📁 docs/                        ← Full documentation
│   ├── SETUP.md                    ← Databricks setup guide
│   ├── COMPETITION_RULES.md        ← Rules and timeline
│   └── PROMPT_ENGINEERING_GUIDE.md ← Learn prompt engineering
│
├── 📁 configs/                     ← Configuration files
│   └── model_config.yaml           ← Model and eval settings
│
└── 📁 results/                     ← Competition results
    └── leaderboard.md              ← Current rankings
```

---

## 🎓 Key Concepts You'll Learn

1. **How LLMs Work** - Decoder-only models, text generation
2. **Prompt Engineering** - Zero-shot, few-shot, chain-of-thought
3. **Evaluation Metrics** - Accuracy, F1, precision, recall
4. **Real ML Workflows** - Data → Model → Evaluation → Iteration

---

## 🔥 Ready to Start?

### Option 1: Read Everything First (Recommended)
1. `README.md` ← You are here
2. `docs/SETUP.md` ← Set up environment
3. `docs/COMPETITION_RULES.md` ← Understand the game
4. `docs/PROMPT_ENGINEERING_GUIDE.md` ← Master the techniques
5. Start building!

### Option 2: Jump Right In (For Brave Souls)
1. Copy `template.py` to `your_name.py`
2. Write your prompt
3. Run `quick_test('your_name')`
4. Iterate until good
5. Submit!

---

## 📚 Additional Resources

**Inside This Project:**
- `src/prompts/example_prompts.py` - Good vs bad prompts
- `src/prompts/student_prompts/alice_example.py` - Full example
- All documentation in `docs/`

**External Resources:**
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [HuggingFace Docs](https://huggingface.co/docs/transformers)
- [Databricks Learning](https://databricks.com/learn)

---

## 💡 Pro Tips

1. **Start Simple** - Don't overcomplicate your first prompt
2. **Test Often** - Use sample data for quick iteration
3. **Learn from Examples** - Study `example_prompts.py`
4. **Ask Questions** - Use GitHub issues or course chat
5. **Have Fun!** - This is about learning, not just winning

---

## 🆘 Need Help?

**Technical Issues**
- Check `docs/SETUP.md` troubleshooting section
- Open GitHub issue with error details

**Prompt Engineering Questions**
- Read `docs/PROMPT_ENGINEERING_GUIDE.md`
- Study example prompts
- Ask instructor in workspace chat

**Competition Rules**
- Read `docs/COMPETITION_RULES.md`
- Check FAQs section
- Ask instructor for clarification

---

## 🏆 Competition Goals

**Learning Objectives:**
- ✅ Understand LLMs and text generation
- ✅ Master prompt engineering techniques
- ✅ Practice ML evaluation and iteration
- ✅ Build real-world ML projects

**Not Just About Winning:**
- 🎯 Experiment and learn
- 🎯 Help each other grow
- 🎯 Share knowledge
- 🎯 Have fun with AI!

---

## 📞 Support

- **GitHub Issues**: Technical problems
- **Course Chat**: Questions and discussion
- **Instructor**: Direct help and guidance

---

## ✅ Pre-Flight Checklist

Before you start competing:

- [ ] Read this file (you're doing it!)
- [ ] Understand project structure
- [ ] Review `docs/SETUP.md`
- [ ] Read `docs/COMPETITION_RULES.md`
- [ ] Study `docs/PROMPT_ENGINEERING_GUIDE.md`
- [ ] Look at example prompts
- [ ] Set up Databricks environment
- [ ] Test that you can run code
- [ ] Feel excited! 🚀

---

**You're all set! Welcome to the competition!**

**May the best prompt win!** 🏆

*Remember: The goal is to learn and have fun. Experiment boldly!*

---

## 📝 What to Do Next

1. **Read** `README.md` in the main folder
2. **Follow** `docs/SETUP.md` to set up Databricks
3. **Study** `docs/PROMPT_ENGINEERING_GUIDE.md`
4. **Build** your first prompt
5. **Compete** and learn!

**Good luck!** 🎓
