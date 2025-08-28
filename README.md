Summatrix
============

**Summatrix** is a lightweight, modular pipeline for **automatic summarization evaluation**. It helps researchers and developers assess the quality of generated summaries using multiple metrics such as **semantic precision, fluency, coherence, and recall**.

Features
-----------

*   **Multi-metric evaluation**: Go beyond ROUGE/BLEU with semantic and fluency scoring.
    
*   **Modular design**: Swap in or extend evaluation components easily.
    
*   **Pipeline-based execution**: Run evaluations on large datasets with minimal setup.
    
*   **Customizable prompts**: Adapt fluency/coherence checks to your task/domain.
    
*   **CSV/JSON support**: Works directly with structured summarization datasets.
    

            
Installation
---------------

Clone the repository:

`   git clone https://github.com/yourusername/summatrix.git  cd summatrix   `


Usage
-----------

### 1\. Evaluate a dataset
`   from summatrix.summatrix import Summatrix

pipeline = Summatrix("input.csv")
results = pipeline.run(detailed=True)
print(results)
 `

### 2\. Example CSV format

Your CSV should have at least these two columns:

source\_textgenerated\_summaryOriginal text paragraph...Model-generated summary...

Metrics
----------

*   **Semantic Precision** → How much correct information is preserved.
    
*   **Fluency** → Grammar, readability, and naturalness of text.
    
*   **Coherence** → Logical flow of ideas across sentences.
    
*   **Semantic Recall** → Completeness of content relative to the source.
    

Roadmap
----------

*   Add human evaluation alignment experiments
    
*   Support multilingual datasets
    
*   Integrate more LLM-based scoring metrics
    


License
----------

This project is licensed under the **MIT License**.
