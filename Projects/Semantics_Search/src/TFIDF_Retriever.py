import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Tuple,List

class TFIDRetiever:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.document_vector = None

    def index_corpus(self, corpus_text : List[str]):
        self.document_vector = self.vectorizer.fit_transform(corpus_text)

    def retrieve(self,query_text:str, top_k : int= 5) -> Tuple[np.ndarray,np.ndarray]:
        query_vector =self.vectorizer.transform([query_text])

        similarity = cosine_similarity(query_vector,self.document_vector)[0]
        top_indices = np.argsort(similarity)[::-1][:top_k]
        top_score = similarity[top_indices]

        return top_indices ,top_score