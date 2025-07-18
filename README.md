# Fake Resume and Job Description Alignment Detector using LLMs

This project uses **Language Models and Embedding-based Similarity** to evaluate how well a resume aligns with a job description (JD). It helps detect fake, exaggerated, or irrelevant resumes in hiring pipelines.

> Built using `sentence-transformers`, `scikit-learn`, and `Gradio`, and deployed on **Hugging Face Spaces**.


## Live Demo
[Click here to try the app](https://huggingface.co/spaces/jeevitha-app/Resume-JD-Aligner-Detector-App)  

## Features

-  Detects semantic alignment between Resume and Job Description
-  Uses LLM-based embeddings (`all-MiniLM-L6-v2`)
-  Shows a **similarity score** (0–100%) with interpretation
-  Flags irrelevant or potentially fake resumes
-  User-friendly interface built with Gradio
-  One-click deployment using Hugging Face Spaces


---

## How It Works

1. **Input**: User pastes Resume and Job Description text.
2. **Embedding**: Text is converted to numerical embeddings using `SentenceTransformer`.
3. **Similarity**: Cosine similarity is computed between the two embeddings.
4. **Output**: 
   - A score (e.g., 85%)
   - Text feedback:
     - Highly aligned
     -  Partially aligned
     -  Not aligned (possibly fake)

---

##  Technologies Used

| Tool                    | Purpose                            |
|-------------------------|-------------------------------------|
| Python                  | Core programming language          |
| Sentence Transformers   | Embedding model (`MiniLM`)         |
| scikit-learn            | Cosine similarity calculation      |
| Gradio                  | Web interface                      |
| Hugging Face Spaces     | Hosting and deployment             |

---
## Requirements.txt

gradio
sentence-transformers
scikit-learn

## Example input 
#Resume: 
Experienced Data Scientist with expertise in Python, SQL, NLP, and model deployment. Built recommendation engines and deployed models using Hugging Face and Streamlit.
#Job description: 
We are hiring a Data Scientist with hands-on experience in NLP, Python, and model deployment using Hugging Face or Streamlit. Knowledge of recommendation systems is a plus.
## output
Similarity Score: 86.75%
Resume is highly aligned with the Job Description.

 ## Use Cases
HR departments for resume screening
Final year Data Science projects
Talent validation in freelance/remote hiring
Applicants checking alignment before applying




