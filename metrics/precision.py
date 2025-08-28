import numpy as np
import torch
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from models import precision_model, precision_tokenizer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

def embed_sentences(sentences):
    inputs = precision_tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = precision_model(**inputs)
    return outputs.last_hidden_state[:, 0].cpu().numpy()

def calculate_semantic_precision(source_text, generated_summary, threshold=0.7, detailed=False):
    source_sentences = nltk.sent_tokenize(source_text)
    summary_sentences = nltk.sent_tokenize(generated_summary)

    source_embeddings = embed_sentences(source_sentences)
    summary_embeddings = embed_sentences(summary_sentences)

    right_claims, wrong_claims = [], []
    for i, summary_vec in enumerate(summary_embeddings):
        sims = cosine_similarity([summary_vec], source_embeddings)[0]
        if np.max(sims) >= threshold:
            right_claims.append(summary_sentences[i])
        else:
            wrong_claims.append(summary_sentences[i])

    total_claims = len(right_claims) + len(wrong_claims)
    precision = len(right_claims) / total_claims if total_claims > 0 else 0.0

    return {"right_claims": right_claims, "wrong_claims": wrong_claims, "precision": precision} if detailed else precision

