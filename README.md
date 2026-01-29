# 🚀 Evolution of Sentiment Analysis: From Zero-Shot LLMs to SOTA BERT

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Databricks](https://img.shields.io/badge/Platform-Databricks-orange.svg)
![Framework](https://img.shields.io/badge/Framework-HuggingFace-yellow.svg)

## 📌 Executive Summary
This project demonstrates the transition from basic LLM prompting to advanced NLP architecture. I started with a "Zero-Knowledge" approach using **Qwen 2.5**, identified failure points in multi-class sentiment tasks, and finally engineered a high-precision **BERT** solution designed for real-world business constraints.

---

## 🛠️ Technical Roadmap

### Phase 1: Foundational LLM Configuration (`01_first_llm_Qwen`)
* **Objective:** Mastering model control.
* **Techniques:** Systematic testing of `temperature` (randomness) and `top_p` (nucleus sampling).
* **Finding:** Higher temperature works for creative writing but degrades performance in structured classification.

### Phase 2: The LLM "Struggle" with Nuance (`02_llm_sentiment`)
* **Experiment:** Binary Sentiment (IMDb) vs. 5-Class Sentiment (SST-5).
* **The Insight:** While the LLM handled Binary classification easily, it failed to distinguish "Negative" from "Very Negative." 
* **Evaluation:** Used **Confusion Matrices** and **Accuracy-per-Class** charts to visualize the decision boundaries of the model.

### Phase 3: The SOTA Solution (`2_patiparn_submit`)
* **Goal:** Lowest False Negative rate on negative reviews (Critical for business reputation).
* **Architectures:** Compared **XGBoost (Multilingual Embeddings)** vs. **Fine-tuned BERT**.
* **Auto-Insight Logic:** Built a custom logic layer to detect common NLP errors like:
  - **Negation Ignoring:** (e.g., "ไม่ดี" vs "ดี")
  - **Contrastive Logic:** Identifying when a model misses the "But" (แต่) in a sentence.

---

## 📊 Performance Benchmark
| Model | Task | Accuracy | Key Strength |
| :--- | :--- | :--- | :--- |
| **Qwen 2.5-3B** | Binary | High | Fast, no training needed |
| **Qwen 2.5-3B** | 5-Class | Medium | Struggles with nuance |
| **Fine-tuned BERT** | 5-Class | **Highest** | Excellent at context & negations |

---

## 💡 Lessons Learned
1. **Prompt Engineering isn't enough:** For specific multi-class tasks, a smaller fine-tuned model (BERT) often outperforms a larger general LLM.
2. **Context Matters:** Thai language negations require specific embedding considerations which I addressed in the final submission.

## 🔮 Future Work: Agentic RAG
I am currently developing an **Agentic Web Scraper** using **Crawl4AI** to feed a dynamic RAG pipeline for internal Knowledge Management systems.

---
**Author:** Patiparn Nualchan  
**Focus:** AI Engineering & RAG Development
