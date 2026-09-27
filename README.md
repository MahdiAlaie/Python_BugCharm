# 🚀 Python & Machine Learning Bootcamp Projects

This repository tracks my hands-on journey through Python programming, Machine Learning, Deep Learning, and NLP concepts. It contains core exercises, notebook explorations, and end-to-end modular mini-projects.

---

## 📌 Featured Projects

| Project | Domain | Core Tech / Concepts | Direct Link |
| :--- | :--- | :--- | :--- |
| **Scientific Semantic Search** | NLP / IR | TF-IDF, Sentence Transformers, Cross-Encoder, SciFact Benchmark | [📂 View Project](./projects/01_scientific_semantic_search) |
| **Computer Vision Experiments** | CV | OpenCV, Image Processing, Face Detection | [📂 View Project](./projects/02_computer_vision_experiments) |
| **Graph Network Analysis** | Network Science | NetworkX, Graph Theory, Anomaly Detection | [📂 View Project](./projects/03_graph_analysis) |

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

---

## 🛠️ Tech Stack & Libraries

- **Languages:** Python
- **Data & Scientific Computing:** NumPy, Pandas, Scikit-learn
- **Deep Learning & NLP:** PyTorch, Sentence-Transformers
- **Analysis & Vision:** NetworkX, Matplotlib, OpenCV

---

