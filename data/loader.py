import json


def load_data():
    # Load current quiz data
    with open('data/Quiz_Submission.json', 'r') as file:
        current_quiz_data = json.load(file)

    # Load quiz endpoint data
    with open('data/Quiz_Endpoint.json', 'r') as file:
        quiz_endpoint_data = json.load(file)

    # Load historical quiz data
    with open('data/Historical_Quiz_Data.json', 'r') as file:
        historical_quiz_data = json.load(file)

    return current_quiz_data, quiz_endpoint_data, historical_quiz_data
