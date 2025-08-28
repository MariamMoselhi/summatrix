import re, json, torch
from models import fluency_model, fluency_tokenizer
from prompts import fluency_prompt

def evaluate_fluency(generated_summary, threshold=80, detailed=False):
    prompt = fluency_prompt.format(generated_summary=generated_summary, threshold=threshold)
    
    inputs = fluency_tokenizer(prompt, return_tensors="pt").to(fluency_model.device)
    output = fluency_model.generate(**inputs, max_new_tokens=512, temperature=0.0)
    response = fluency_tokenizer.decode(output[0], skip_special_tokens=True)

    match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", response, re.DOTALL)
    data = json.loads(match.group(1)) if match else {}

    score = data.get("score", 100)
    fluency = 1 if score >= threshold else 0
    
    return {"total_issues": data.get("total_issues",0), "issues": data.get("issues", []), "score": score, "fluency": fluency} if detailed else fluency
