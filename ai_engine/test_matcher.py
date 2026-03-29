from matcher import compute_scores

data = {
    "resumes": [
        {"id": "R1", "text": "python developer sql machine learning"},
        {"id": "R2", "text": "java developer spring boot backend"}
    ],
    "job_description": "looking for python developer with sql"
}

results = compute_scores(data)

for res in results:
    print(res)