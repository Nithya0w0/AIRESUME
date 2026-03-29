from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing.preprocess import clean_text
from ai_engine.matcher import compute_scores

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload():
    job_desc = request.form["job_description"]
    files = request.files.getlist("resumes")

    resumes = []

    for i, file in enumerate(files):
        text = file.read().decode("utf-8")
        cleaned = clean_text(text)

        resumes.append({
            "id": f"R{i+1}",
            "text": cleaned
        })

    data = {
        "resumes": resumes,
        "job_description": clean_text(job_desc)
    }

    scores = compute_scores(data)

    return jsonify(scores)

if __name__ == "__main__":
    app.run(debug=True)