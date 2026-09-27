import os 
import pandas as pd
from typing import Set,Tuple,Dict


def load_scifact_data (data_dir :  str = "data/scifact") -> Tuple[pd.DataFrame,pd.DataFrame,Dict[str,Set[str]]]:

    corpus_path = os.path.join(data_dir , "corpus.jsonl")
    queries_path = os.path.join(data_dir , "queries.jsonl")
    qrels_path = os.path.join(data_dir , "qrels" , "test.tsv")


    if not os.path.exists(corpus_path):
        raise FileNotFoundError(f"File not found st: {corpus_path}")

    corpus = pd.read_json(corpus_path,lines=True)
    corpus["content"] = corpus["title"] + " " + corpus["text"]


    queries = pd.read_json(queries_path, lines=True)


    qrels = pd.read_csv(qrels_path,sep="\t")

    relevant_map = qrels.groupby("query-id")["corpus-id"].apply(set).to_dict()

    return corpus , queries , relevant_map