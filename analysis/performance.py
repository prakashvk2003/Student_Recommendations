def analyze_performance(current_data, historical_data, quiz_questions):
    # Ensure data is filtered for the provided user before analysis
    performance_summary = {
        "accuracy": current_data.get("accuracy"),
        "speed": current_data.get("speed"),
        "score": current_data.get("final_score"),
        "correct_answers": current_data.get("correct_answers"),
        "incorrect_answers": current_data.get("incorrect_answers"),
        "topic": current_data["quiz"]["topic"]
    }

    if not historical_data:
        performance_summary.update({
            "average_score": 0,
            "score_trend": "No Data",
            "weak_topics": []
        })
        return performance_summary

    # Analyze historical trends
    historical_scores = [float(quiz["final_score"]) for quiz in historical_data]
    performance_summary["average_score"] = sum(historical_scores) / len(historical_scores)
    performance_summary["score_trend"] = "improving" if historical_scores[-1] > historical_scores[0] else "declining"

    # Identify weak topics
    incorrect_responses = {}
    for quiz in historical_data:
        for question_id, selected_option in quiz["response_map"].items():
            question = next((q for q in quiz_questions if q["id"] == int(question_id)), None)
            if question:
                is_correct = any(option["is_correct"] for option in question["options"] if option["id"] == selected_option)
                if not is_correct:
                    topic = question["topic"] if question["topic"] else "Unknown Topic"
                    incorrect_responses[topic] = incorrect_responses.get(topic, 0) + 1

    performance_summary["weak_topics"] = sorted(incorrect_responses, key=incorrect_responses.get, reverse=True)

    return performance_summary
