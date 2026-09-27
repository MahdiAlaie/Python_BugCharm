import numpy as np 
from tqdm.auto import tqdm
from src.data_loader import load_scifact_data
from src.TFIDF_Retriever import TFIDRetiever
from src.Biencoder_retiever import BiEncoderRetiever
from src.CrossEncoderReranker import CrossEncoderReranker
from src.evaluation import compute_recall_precision

def run_pipeline():
    corpus , queries , relevant_map = load_scifact_data(data_dir="data/scifact")

    corpus_contents = corpus["content"].tolist()


    tfidf_retriever = TFIDRetiever()
    tfidf_retriever.index_corpus(corpus_text=corpus_contents)


    dense_retiever = BiEncoderRetiever()
    dense_retiever.index_corpus(corpus_text=corpus_contents)

    reranker = CrossEncoderReranker()


    valid_queries = []
    for idx , row in queries.iterrows():
        if row["_id"] in relevant_map:
            valid_queries.append((idx,row["_id"],row["text"]))

    eval_queries = valid_queries[:100]

    recalls_tfidf , precision_tfidf = [],[]
    recalls_dense , precision_dense = [],[]
    recalls_rerank , precision_rerank = [],[]

    for q_idx , q_id , q_text in tqdm(eval_queries):
        gold_ids = relevant_map[q_id]

        tfidf_indices , _ = tfidf_retriever.retrieve(q_text)
        tfidf_top5_ids = set(corpus.iloc[tfidf_indices]["_id"])
        r_tfidf , p_tfidf = compute_recall_precision(tfidf_top5_ids,gold_ids)
        recalls_tfidf.append(r_tfidf)
        precision_tfidf.append(p_tfidf)

              
        dense_indices , _ = dense_retiever.retrieve(q_text)
        dense_top5_ids = set(corpus.iloc[dense_indices]["_id"][:5])
        r_dense , p_dense = compute_recall_precision(dense_top5_ids,gold_ids)
        recalls_dense.append(r_dense)
        precision_dense.append(p_dense)

        candidate_docs = corpus.iloc[dense_indices]["content"].tolist()
        rerank_indices , _ = reranker.rerank(q_text,candidate_docs,dense_indices)
        rerank_top5_ids = set(corpus.iloc[rerank_indices]["_id"])
        r_rerank , p_rerank = compute_recall_precision(rerank_top5_ids,gold_ids)
        recalls_rerank.append(r_rerank)
        precision_rerank.append(p_rerank)

    print("\n" + "*" *33)
    print("------ Evaluation Results -------")
    print("\n" + "*" *33)
    print(f"TF-IDF           |Recall@5: {np.mean(recalls_tfidf):.4f}  | Precision: {np.mean(precision_tfidf):.4f}")
    print(f"Bi-Encoder       |Recall@5: {np.mean(recalls_dense):.4f}  | Precision: {np.mean(precision_dense):.4f}")
    print(f"Cross-Encoder    |Recall@5: {np.mean(recalls_rerank):.4f} | Precision: {np.mean(precision_rerank):.4f}")

if __name__ == "__main__":
    run_pipeline()