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
    

 Repository Structure
-----------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   summatrix/  │── summatrix.py        # Main pipeline entry point  │── metrics.py          # Evaluation metrics (semantic, fluency, coherence, etc.)  │── utils.py            # Helper functions (data loading, formatting, etc.)  │── examples/           # Example usage and sample datasets  │── README.md           # Project documentation   `

Installation
---------------

Clone the repository:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/yourusername/summatrix.git  cd summatrix   `

(Optional) install requirements:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

Usage
-----------

### 1\. Evaluate a dataset

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   from summatrix import Summatrix  pipeline = Summatrix("input.csv")    results = pipeline.run(detailed=True)    print(results)   `

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
