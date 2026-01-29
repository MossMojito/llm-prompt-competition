# 🚀 Build your first LLM and Prompt Engineering until use case (Text classify - Sentiment Analysis using LLM)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-HuggingFace-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Databricks-orange.svg)

## 📌 Project Overview
This project documents the development of a high-precision sentiment analysis system. It tracks the journey from basic LLM hyperparameter tuning to identifying failure points in multi-class classification, ending with a professional **SOTA (State-of-the-Art)** hybrid solution.

**Core Business Goal:** To build a generalized system with the **Lowest False Negative rate on the "Negative" class** to protect brand reputation.

---

## 🛠️ Technical Roadmap

### Phase 1: Foundational LLM Configuration (`01_first_llm_Qwen`)
* **Objective:** Master model control via hyperparameter tuning.
* **Experiments:** Systematic testing of `temperature` and `top_p`.
* **Finding:** Higher temperature (e.g., 1.5) increases creativity but causes "hallucinated" labels in structured sentiment tasks.

### Phase 2: The LLM "Nuance Gap" (`02_llm_sentiment`)
* **The Challenge:** Binary Sentiment (IMDb) vs. 5-Class Granularity (SST-5).
* **The Insight:** While LLMs handle simple polarity well, zero-shot prompting frequently confuses "Neutral" with "Negative" without advanced few-shot examples or fine-tuning.

### Phase 3: SOTA Hybrid Architecture & Error Analysis (`2_patiparn_submit`)
* **Architecture:** Benchmarked **XGBoost** (Multilingual Embeddings), **Fine-tuned BERT** (`wangchanberta`), and Few-Shot LLM baselines.
* **Advanced Engineering:** * Implemented **Class Weighting** (Total / Classes * Count) to handle data imbalance without oversampling.
    * Integrated **Auto-Insight Logic** to automatically diagnose model failure modes.



#### 💡 Error Analysis Insights:
The system automatically identifies and reports why the model failed on specific test cases:
* **Negation Bias:** Detection of missed Thai negations (e.g., "ไม่").
* **Contrastive Logic:** Capturing sentiment shifts caused by "But" (แต่).
* **Question Context:** Identifying ignored question formats (e.g., "ไหม").

---

## 📊 Performance Benchmark
| Approach | Task | Accuracy | Key Strength |
| :--- | :--- | :--- | :--- |
| **Qwen 2.5-3B** | Binary | High | Fast, no training required |
| **Qwen 2.5-3B** | 5-Class | Medium | Struggles with granularity |
| **Fine-tuned BERT**| 5-Class | **Highest** | **Optimized for Business Logic** |

---

## 🔮 Future Roadmap: Agentic RAG
* **Agentic Scraper:** Transitioning to **Crawl4AI** for dynamic web data extraction.
* **GraphRAG:** Integrating GraphDB to enhance document relationship understanding in RAG systems.

---
**Developer:** Patiparn Nualchan  
**Focus:** AI Engineering | Data Science | RAG Specialist
