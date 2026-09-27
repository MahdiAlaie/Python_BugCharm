from typing import Set,Tuple

def compute_recall_precision(retrieved_ids , relevant_ids , k = 5) -> Tuple[float,float]:
    if not relevant_ids:
        return 0.0 ,0.0

    hits = len(relevant_ids & retrieved_ids)
    recall = hits / len(relevant_ids)
    precision = hits / k

    return recall , precision