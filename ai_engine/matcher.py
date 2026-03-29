from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes):

    texts = [job_description] + [r["text"] for r in resumes]

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(texts)

    job_vector = vectors[0]
    resume_vectors = vectors[1:]

    similarity_scores = cosine_similarity(job_vector, resume_vectors)[0]

    # 🔥 KEYWORDS (simple AI)
    keywords = job_description.lower().split()

    results = []

    for i, resume in enumerate(resumes):
        text = resume["text"].lower()

        # MATCH %
        score = similarity_scores[i]
        match_percent = int(score * 100)

        # SKILL BREAKDOWN
        skill_scores = {}
        important_skills = ["python", "sql", "machine learning", "java", "react"]

        for skill in important_skills:
            skill_scores[skill] = 100 if skill in text else 0

        # MISSING SKILLS
        missing = [skill for skill in important_skills if skill not in text]

        # RECOMMENDATIONS
        recommendations = []
        if "python" not in text:
            recommendations.append("Add Python experience")
        if "sql" not in text:
            recommendations.append("Include SQL/database skills")
        if "machine learning" not in text:
            recommendations.append("Mention ML projects")
        if "react" not in text:
            recommendations.append("Add frontend frameworks")
        if "java" not in text:
            recommendations.append("Include backend experience")

        results.append({
            "id": resume["id"],
            "score": score,
            "match": match_percent,
            "skills": skill_scores,
            "missing": missing,
            "recommendations": recommendations
        })

    # SORT
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results