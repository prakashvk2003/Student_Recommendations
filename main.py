from data.loader import load_data
from analysis.performance import analyze_performance
from analysis.recommendations import generate_recommendations
from analysis.persona import define_persona

def main(user_id=None):
    # Load the datasets
    current_quiz_data, quiz_endpoint_data, historical_quiz_data = load_data()

    if user_id:
        # Filter historical data and current quiz data for the specific user
        historical_quiz_data = [quiz for quiz in historical_quiz_data if quiz["user_id"] == user_id]
        if not historical_quiz_data:
            print(f"No data found for user_id: {user_id}")
            return
        print(f"Generating report for user_id: {user_id}")

        # Filter current quiz data for the user if needed
        # (You can add logic here if `current_quiz_data` supports multiple users)
    else:
        # Generate reports for all users
        user_ids = set(quiz["user_id"] for quiz in historical_quiz_data)
        print(f"Generating reports for all users: {', '.join(user_ids)}")

    # Process data for each user
    for user in ([user_id] if user_id else user_ids):
        print("\n===============================")
        print(f"User ID: {user}")
        print("===============================")

        # Filter the historical data for this user
        user_historical_data = [quiz for quiz in historical_quiz_data if quiz["user_id"] == user]

        # Analyze performance
        performance_summary = analyze_performance(
            current_quiz_data,
            user_historical_data,
            quiz_endpoint_data["quiz"]["questions"]
        )

        # Generate recommendations
        recommendations = generate_recommendations(performance_summary)

        # Define persona
        student_persona = define_persona(performance_summary)

        # Display results
        print("\nPerformance Summary:")
        for key, value in performance_summary.items():
            print(f"{key}: {value}")

        print("\nRecommendations:")
        for rec in recommendations:
            print(f"- {rec}")

        print(f"\nStudent Persona: {student_persona}")


if __name__ == "__main__":
    # Change the `user_id` here for a specific user, or leave it as None for all users
    main(user_id="YcDFSO4ZukTJnnFMgRNVwZTE4j42")
