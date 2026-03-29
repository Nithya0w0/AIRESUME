from app import rank_results, display_results

data = [
    {"id": "R1", "score": 0.4},
    {"id": "R2", "score": 0.9},
    {"id": "R3", "score": 0.6}
]

ranked = rank_results(data)
display_results(ranked)