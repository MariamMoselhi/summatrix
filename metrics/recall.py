import json
import openai
from prompts import recall_system_prompt, recall_user_prompt

def calculate_semantic_recall(source_text, generated_summary, detailed=False):
    message = [{"role":"system","content":recall_system_prompt + "\n" + recall_user_prompt%(source_text, generated_summary)}]
    
    completion = openai.OpenAI(
        api_key="b888fc8181372eafecc0328c0ceb79a56d7061791d8a1aa650293aea1e9b1e70",
        base_url="https://api.together.xyz/v1"
    )
    
    response = completion.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=message,
        temperature=0,
        max_tokens=3000
    )

    output = response.choices[0].message.content
    if output.startswith("```json"): output = output[7:]
    if output.endswith("```"): output = output[:-3]

    parsed = json.loads(output)
    tp, fn, gt_list = parsed["TP"], parsed["FN"], parsed["gt_list"]
    recall = len(tp) / len(gt_list) if len(gt_list) > 0 else 0.0

    return {"recall": recall, "tp": tp, "fn": fn, "gt_list": gt_list} if detailed else recall
