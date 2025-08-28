import pandas as pd
import time
from metrics import (
    calculate_semantic_precision,
    calculate_semantic_recall,
    evaluate_coherence,
    evaluate_fluency,
)

def evaluate_summarization(input_csv, detailed=False, output_csv="outputs/Summarization_Evaluation.csv"):
    """
    Run the full evaluation pipeline on a CSV file.
    Columns required: 'id', 'source_text', 'generated_summary'
    """
    df = pd.read_csv(input_csv).dropna()
    scores = []

    for _, row in df.iterrows():
        print(f"\n=== Evaluating ID {row['id']} ===")
        try:
            precision = calculate_semantic_precision(row["source_text"], row["generated_summary"], detailed=detailed)
            recall = calculate_semantic_recall(row["source_text"], row["generated_summary"], detailed=detailed)
            coherence = evaluate_coherence(row["generated_summary"], detailed=detailed)
            fluency = evaluate_fluency(row["generated_summary"], detailed=detailed)
            scores.append([precision, recall, coherence, fluency])
        except Exception as e:
            print(f"⚠️ Error at ID {row['id']}: {e}")
            scores.append([None, None, None, None])
        time.sleep(5)

    df[["precision", "recall", "coherence", "fluency"]] = scores
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"\n✅ Evaluation complete. Results saved to {output_csv}")
