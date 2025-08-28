import numpy as np
from itertools import combinations
from models import coherence_model

def check_global_coherence(generated_summary):
    sentences = [s.strip() for s in generated_summary.split(".") if s.strip()]
    if len(sentences) < 2:
        return []
    embeddings = coherence_model.encode(sentences, convert_to_tensor=True)
    return [(float((embeddings[i] @ embeddings[j]).item()), i, j) for i, j in combinations(range(len(sentences)), 2)]

def evaluate_coherence(generated_summary, detailed=False):
    scores = check_global_coherence(generated_summary)
    if not scores:
        return {"average": 0, "min": 0, "std": 0, "composite": 0, "abrupt_shifts": 0, "Coherence": 0} if detailed else 0
    
    values = [s[0] for s in scores]
    avg, mn, std = np.mean(values), np.min(values), np.std(values)
    shifts = sum(1 for v in values if v < 0.1)
    comp = (0.4*avg + 0.4*mn - 0.2*std - 0.1*shifts)
    coherence = 1 if comp > 0 else 0
    
    return {"average": round(avg,3), "min": round(mn,3), "std": round(std,3), "composite": round(comp,3), "abrupt_shifts": shifts, "Coherence": coherence} if detailed else coherence
