import torch
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

# Precision model
precision_model_name = "BAAI/bge-m3"
precision_tokenizer = AutoTokenizer.from_pretrained(precision_model_name)
precision_model = AutoModel.from_pretrained(precision_model_name)

# Coherence model
coherence_model = SentenceTransformer("all-MiniLM-L6-v2")

# Fluency model
fluency_model_name = "Qwen/Qwen2.5-3B-Instruct"
fluency_tokenizer = AutoTokenizer.from_pretrained(fluency_model_name)
fluency_model = AutoModelForCausalLM.from_pretrained(
    fluency_model_name, torch_dtype="auto", device_map="auto"
)
