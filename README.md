# 🚀 LLM Sentiment Journey: From Foundation to Specialized NLP

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-HuggingFace-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Databricks-orange.svg)

## 📌 Project Overview
This repository serves as a step-by-step guide for anyone starting from "Zero" in Large Language Models. Instead of just running code, this project demonstrates the **evolution of an AI solution**: starting with basic configurations, discovering model limitations across different datasets, and finally engineering a specialized system to handle complex linguistic nuances.

---

## 🛠️ The Learning Roadmap

### Step 1: Foundational LLM Configuration (`01_first_llm_Qwen`)
* **The Goal:** Learn how to control LLM behavior through hyperparameters.
* **Technical Focus:** Hands-on experimentation with `temperature` and `top_p` using **Qwen 2.5**.
* **Key Lesson:** Understanding how randomness vs. determinism affects output quality in structured tasks.

### Step 2: Transitioning to Sentiment Use Cases (`02_llm_sentiment`)
* **The Goal:** Apply LLMs to real-world text classification.
* **The Experiment:** * **Easy Task:** Success with Binary Sentiment (Positive/Negative) on the **IMDb dataset**.
    * **Complex Task:** Identifying limitations when moving to 5-class granularity (**SST-5 dataset**).
* **Key Lesson:** Discovering the "Nuance Gap"—where zero-shot LLMs begin to struggle with fine-grained emotional labels like "Neutral" vs. "Slightly Negative."

### Step 3: Professional SOTA & Error Analysis (`2_patiparn_submit`)
* **The Goal:** Build a production-ready system optimized for business logic.
* **The Solution:** Transitioned to specialized architectures (**Fine-tuned BERT** and **XGBoost**) to achieve the lowest False Negative rate on critical classes.
* **Advanced Engineering:** * **Class Weighting:** Managing data imbalance mathematically without needing to oversample or undersample.
    * **Auto-Insight Logic:** A custom diagnostic layer that automatically explains *why* a model failed by identifying:
        * **Negation Bias:** Missed Thai negations (e.g., "ไม่").
        * **Contrastive Logic:** Missed sentiment shifts following "But" (แต่).
        * **Question Context:** Failures in recognizing question-based sentiment (e.g., "ไหม").

---

## 💡 Why This Project?
This project shows that AI Engineering is not just about choosing the biggest model—it is about:
1.  **Configuring** the model correctly for the task.
2.  **Evaluating** performance across different datasets to find failure points.
3.  **Engineering** specific solutions (like BERT or Class Weighting) to solve those failure points.

## 🔮 What's Next?
* **Agentic Scraper:** Integrating **Crawl4AI** for dynamic data collection.
* **RAG System:** Building a specialized knowledge retrieval chatbot.

---
**Developer:** Patiparn Nualchan  
**Focus:** AI Engineering | Data Science | NLP Specialist
