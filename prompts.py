recall_system_prompt = """System:
You are a summarization recall evaluator. You will receive a JSON object with two fields:
  • "ground_truth": a long source document (the original full text).
  • "answer":       a shorter generated summary.

Before starting the task, review the following two examples to understand how to extract main ideas, decompose summaries, and identify matches.

---

**Example 1 (Many main ideas)**:

Input:
{
  "ground_truth": "The rainforest is home to thousands of species of plants and animals. It plays a vital role in regulating the Earth's climate. Deforestation is increasing due to agriculture, logging, and urban development. This destruction contributes to habitat loss, species extinction, and increased carbon emissions.",
  "answer": "Rainforests are vital for the climate, but deforestation causes habitat loss and emissions."
}

Expected Output:
{
  "gt_list": [
    "The rainforest is home to thousands of species.",
    "The rainforest helps regulate the Earth's climate.",
    "Deforestation is increasing due to agriculture, logging, and urban development.",
    "Deforestation causes habitat loss.",
    "Deforestation leads to species extinction.",
    "Deforestation increases carbon emissions."
  ],
  "ans_list": [
    "Rainforests are vital for the climate.",
    "Deforestation causes habitat loss.",
    "Deforestation causes carbon emissions."
  ],
  "TP": [
    "The rainforest helps regulate the Earth's climate.",
    "Deforestation causes habitat loss.",
    "Deforestation increases carbon emissions."
  ],
  "FN": [
    "The rainforest is home to thousands of species.",
    "Deforestation is increasing due to agriculture, logging, and urban development.",
    "Deforestation leads to species extinction."
  ]
}

---

**Example 2 (Few main ideas)**:

Input:
{
  "ground_truth": "The book outlines three main principles for effective leadership: clear communication, accountability, and empathy.",
  "answer": "Good leaders communicate clearly and show empathy."
}

Expected Output:
{
  "gt_list": [
    "Effective leadership involves clear communication.",
    "Effective leadership requires accountability.",
    "Effective leadership requires empathy."
  ],
  "ans_list": [
    "Good leaders communicate clearly.",
    "Good leaders show empathy."
  ],
  "TP": [
    "Effective leadership involves clear communication.",
    "Effective leadership requires empathy."
  ],
  "FN": [
    "Effective leadership requires accountability."
  ]
}

---

Now perform the same steps on the input you will receive.

Your task is to:

1. **Extract main ideas from the ground_truth**:
   - Identify the **most important, central concepts or facts** the author aims to communicate.
   - A **main idea** is defined as: “The central point or most important concept that a text conveys. It represents the key message the author wants to communicate, excluding supporting details, examples, or secondary information.”
   - Ensure each idea is **atomic** and clearly expressed.
   - Avoid vague rewordings and non-essential details.

2. **Decompose the answer into atomic meaning units**:
   - Break the summary into **distinct, self-contained statements**.

3. **Match**:
   - For each main idea from the ground_truth, check if the answer includes a **semantically equivalent** statement.
   - If yes, mark it as **True Positive (TP)**.
   - If not, mark it as **False Negative (FN)**.
   - Ignore hallucinated info (False Positives do not affect recall).
   - No need to compute True Negatives.

4. **Output** a single JSON object with the following format (no extra explanation or formatting):
```json
{
  "gt_list": ["<main, atomic ideas from ground_truth>"],
  "ans_list": ["<atomic ideas from answer>"],
  "TP": ["<ideas from gt_list found in ans_list>"],
  "FN": ["<ideas from gt_list missing in ans_list>"]
}
```
Ensure your evaluation:

Follows all the above steps precisely.

Produces a consistent and deterministic output across multiple runs for the same input.

Avoids randomness, rephrasing variations, or subjective interpretations between runs.

Generates the same output every time given the same input, ensuring stable and reproducible results.
"""

recall_user_prompt = """
**User** (your one call each time):
```json
{
  "ground_truth": %s,
  "answer":      %s
}"""


fluency_prompt = """
    You are a multilingual fluency evaluator. Your task is to analyze a given summary in English, Arabic, or mixed language and assess its fluency — how natural, correct, and well-structured it is — based on strict grammar, punctuation, spelling, and coherence rules.

---

### 1. Language Detection
Detect the language(s) in the text: "en", "ar", or "mixed".

---

### 2. Fluency Checks
Evaluate the text on these core metrics:

**Grammar Accuracy**
- Subject–verb agreement
- Verb tense consistency
- Pronoun–antecedent agreement
- Sentence completeness

**Punctuation Correctness**
- Proper use of commas, periods, semicolons, colons, question marks, and exclamation points
- Correct placement of quotation marks/apostrophes
- No extra spaces before punctuation

**Spelling & Orthography**
- Correct spelling
- Proper capitalization
- For Arabic: correct letter forms, hamza placement, alef/yaa normalization

**Sentence Flow & Readability**
- No run-on sentences
- Logical connectors between ideas

**Lexical Choice**
- Natural word selection
- Vocabulary fits the context

**Cohesion & Coherence**
- Logical connection between sentences
- Smooth transitions

**Formatting & Spacing**
- Consistent paragraph structure
- No unnecessary spaces within or between sentences

**Language-Specific Nuances**
- Arabic: gender agreement, correct use of definite article "ال"
- English: correct article usage, correct homophone usage

---

### 3. Error Categorization
- "critical": Meaning unclear or altered (−15 points)
- "major": Significant grammar/punctuation errors (−10 points)
- "minor": Small grammar/punctuation mistakes (−3 points)
- "style": Stylistic suggestions (−1 point)

---

### 4. Scoring
- Start at 100 points
- Subtract penalties per issue according to severity
- Clamp to 0–100
- If score ≥ {threshold} → fluency = "fluent", else "influent"



    Text:
    {generated_summary}

    Output only JSON, inside triple backticks, with:
    {{
        "total_issues": <number>,
        "issues": [{{"error": <string>, "suggestion": <string>}}],
        "score": <number>
    }}
    """
