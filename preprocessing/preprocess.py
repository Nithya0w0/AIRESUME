import os
import string

# Simple stopwords list
STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "for", "on", "with", "a", "an"
}


def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]

    return " ".join(words)


def read_resumes(folder_path):
    resumes = []
    files = os.listdir(folder_path)

    for i, file in enumerate(files):
        file_path = os.path.join(folder_path, file)

        # Skip non-text files (safety)
        if not file.endswith(".txt"):
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned = clean_text(text)

        resumes.append({
            "id": f"R{i+1}",
            "text": cleaned
        })

    return resumes


def read_job_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    return clean_text(text)


def process_data():
    # 🔥 FIXED: Absolute paths (no more errors)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    resumes_path = os.path.join(base_dir, "data", "resumes")
    job_desc_path = os.path.join(base_dir, "data", "job_description.txt")

    resumes = read_resumes(resumes_path)
    job_description = read_job_description(job_desc_path)

    return {
        "resumes": resumes,
        "job_description": job_description
    }