import torch
import numpy as np
from sentence_transformers import CrossEncoder
from typing import Tuple,List

class CrossEncoderReranker:
    def __init__(self, model_name : str = "cross-encoder/ms-marco-MiniLM-L-6-v2", device :str = None):
        self.device = device
        if torch.cuda.is_available() :
            self.device = "cuda"
        else:
            self.device = "cpu"

        self.model = CrossEncoder(
            model_name,
            activation_fn = torch.nn.Sigmoid(),
            device = self.device
        )

    def rerank (
            self,
            query_text : str,
            candidate_docs : List[str],
            candidate_indices: np.ndarray,
            final_top_k :int = 5
    )-> Tuple[np.ndarray,np.ndarray]:
        pair = []
        for doc in candidate_docs:
            pair.append([query_text,doc])

        score = np.array(self.model.predict(pair))

        reranked_order = np.argsort(score)[::-1][:final_top_k]

        top_indices = candidate_indices[reranked_order]
        top_score = score[reranked_order]

        return top_indices , top_score