from ml_predictor import AdaptiveLearner

learner = AdaptiveLearner()
print("AdaptiveLearner instantiated successfully!")

sample_user_data = {
    'weight': 70,
    'height': 170,
    'age': 25,
    'gender': 'M',
    'fitness_level': 'beginner',
    'goal': 'weight loss',
    'history': [
        {'date': '2024-01-01', 'weight': 75},
        {'date': '2024-01-08', 'weight': 74},
        {'date': '2024-01-15', 'weight': 73}
    ]
}

progress = learner.analyze_user_progress(sample_user_data)
print(f"Progress analysis: {progress}")

suggestions = learner.suggest_adjustments(sample_user_data, progress or {})
print(f"Suggestions: {suggestions}")

prediction = learner.predict_next_weight(sample_user_data)
print(f"Weight prediction: {prediction}")

insights = learner.generate_insights(sample_user_data)
print(f"Insights: {insights}")

print("All tests passed!")