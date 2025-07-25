!pip install sentence-transformers scikit-learn gradio

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr

# Load pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Function to convert text to embedding
def get_embedding(text):
    return model.encode([text])[0]

# Function to compute similarity
def compute_similarity(resume, jd):
    resume_emb = get_embedding(resume)
    jd_emb = get_embedding(jd)
    similarity = cosine_similarity([resume_emb], [jd_emb])[0][0]
    return round(similarity * 100, 2)

def check_resume(resume_text, jd_text):
    score = compute_similarity(resume_text, jd_text)
    result = f"Similarity Score: {score}%\n\n"
    if score > 75:
        result += "✅ Resume is highly aligned with the Job Description."
    elif score > 50:
        result += "⚠️ Resume is partially aligned. Consider refining keywords and skills."
    else:
        result += "❌ Resume is not aligned. May contain irrelevant or fake claims."
    return result

interface = gr.Interface(
    fn=check_resume,
    inputs=[
        gr.Textbox(label="Paste Resume Text", lines=20, placeholder="Copy your resume content here..."),
        gr.Textbox(label="Paste Job Description", lines=20, placeholder="Copy the job description here...")
    ],
    outputs=gr.Textbox(label="Analysis Result"),
    title="🧾 Resume-Job description Alignment Detector",
    description="Check if your resume genuinely matches the job description using LLM-based similarity."
)

interface.launch(share=True)  # 'share=True' gives public link
