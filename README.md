# 🚀 Python & Machine Learning Bootcamp Projects

This repository tracks my hands-on journey through Python programming, Machine Learning, Deep Learning, and NLP concepts. It contains core exercises, notebook explorations, and end-to-end modular mini-projects.

---

## 📌 Featured Projects

| Project | Domain | Core Tech / Concepts | Direct Link |
| :--- | :--- | :--- | :--- |
| **Scientific Semantic Search** | NLP / IR | TF-IDF, Sentence Transformers, Cross-Encoder, SciFact Benchmark | [📂 View Project](./projects/Semantics_Search) |
| **Exploratory Data Analysis & Preprocessing** (MidTerm) | Data Analysis | Pandas, NumPy, Data Cleaning, Matplotlib Visualizations | [📂 View Project](./projects/MidTerm_Project)
| **Computer Vision Experiments** | CV | OpenCV, Image Processing, Face Detection | [📂 View Project](./Computer_Vision)
| **Machine Learning Pipelines** | ML / Predictive Modeling | Scikit-learn, Classification, Regression, Model Evaluation | [📂 View Module](./Projects/Machine_learning)


---

### 🔍 Spotlight: Scientific Semantic Search Pipeline

An end-to-end comparison of traditional keyword retrieval vs. dense neural representations over the **SciFact** dataset.

* **Key Implementations:**
  * **Sparse Retrieval:** TF-IDF baseline (`scikit-learn`)
  * **Dense Retrieval (Bi-Encoder):** `all-MiniLM-L6-v2` with normalized embeddings & cosine similarity
  * **Re-ranking (Cross-Encoder):** `ms-marco-MiniLM-L-6-v2` for high-precision top-k scoring
* **Benchmark Evaluation (Top-100 SciFact queries @ k=5):**
  * `TF-IDF`: Recall@5: **0.7323** | Precision@5: **0.1620**
  * `Bi-Encoder`: Recall@5: **0.7860** | Precision@5: **0.1780**
  * `Bi-Encoder + Cross-Encoder`: Recall@5: **0.7902** | Precision@5: **0.1780**

## 🤖 Spotlight: Spam Classification Pipeline
An end-to-end classification study comparing classical machine learning (Scikit-Learn) with deep learning architectures (PyTorch) to identify spam vs. ham emails.

### Benchmark Results (Test Set)

| Model | Accuracy | Spam Precision | Spam Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest (Best)** | **97.5%** | **1.00** | 0.80 | **0.89** |
| **PyTorch Deep Learning** | 95.0% | 0.95* | 0.80* | 0.85* |
| **Naive Bayes** | 95.7% | **1.00** | 0.66 | 0.79 |

### 📊 Spotlight: MidTerm EDA & Preprocessing Project

An end-to-end exploratory data analysis (EDA) and data wrangling pipeline:

* **Data Cleaning & Handling:** Handling missing/null values, duplicate detection, and outlier filtering.
* **Feature Engineering:** Aggregation, grouping, and feature structuring with **Pandas & NumPy**.
* **Visual Storytelling:** Trend analysis, correlation heatmaps, and distribution plots using **Matplotlib**.

### 📸 Spotlight: Computer Vision Experiments
Implementation of foundational computer vision techniques:
* **Preprocessing:** Grayscale conversion, Thresholding.
* **Feature Detection:** Canny Edge Detection and Contour Analysis.
* **Recognition:** Face detection using Haar Cascades and OpenCV.

---

## 🛠️ Tech Stack & Libraries

- **Languages:** Python
- **Data & Scientific Computing:** NumPy, Pandas, Scikit-learn
- **Deep Learning & NLP:** PyTorch, Sentence-Transformers
- **Analysis & Vision:** NetworkX, Matplotlib, OpenCV

---

