import os
import torch
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Tuple,List

class BiEncoderRetiever:
    def __init__(self, modele_name : str = "sentence-transformers/all-MiniLM-L6-v2", device : str = None):
        self.device = device
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.model = SentenceTransformer(modele_name,device=self.device)
        self.corpus_embedding = None

    def index_corpus(self,corpus_text: List[str],batch_size: int = 64, cache_path = "cache/corpus_embeddings.pt"):
        if os.path.exists(cache_path):
            self.corpus_embedding = torch.load(cache_path,map_location=self.device)
        else:
            self.corpus_embedding = self.model.encode(
                corpus_text,
                batch_size = batch_size,
                show_progress_bar =True,
                device = self.device
            )

            self.corpus_embedding = torch.tensor(self.corpus_embedding,dtype=torch.float32)
            self.corpus_embedding = torch.nn.functional.normalize(self.corpus_embedding,p=2,dim=1)

            os.makedirs(os.path.dirname(cache_path),exist_ok = True)
            torch.save(self.corpus_embedding,cache_path)

    def retrieve(self,query_text: str, top_k : int=20) -> Tuple[np.ndarray,np.ndarray]:
        query_embedding = self.model.encode(query_text, convert_to_tensor = True, device = self.device)

        score = torch.matmul(query_embedding,self.corpus_embedding.T).squeeze(0)

        actual_k = min(top_k,score.size(0))
        top_score, top_inices = torch.topk(score,k=actual_k)

        return top_inices.cpu().numpy() , top_score.cpu().numpy()
    