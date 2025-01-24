def generate_recommendations(performance):
    recommendations = []

    # Weak topics
    if performance["weak_topics"]:
        recommendations.append(f"Focus on these topics: {', '.join(performance['weak_topics'][:3])}.")

    # Score improvement
    if performance["score_trend"] == "declining":
        recommendations.append("Consider revisiting previous quizzes to reinforce foundational topics.")
    else:
        recommendations.append("Keep up the good work and continue practicing similar questions.")

    return recommendations
