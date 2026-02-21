from ml_predictor import WorkoutRecommendationModel

def multiply_workout(workout_list, multiplier):
    """Multiply numeric values in workout descriptions"""
    updated_list = []

    for item in workout_list:
        if "sets" in item.lower() or "reps" in item.lower() or "seconds" in item.lower() or "minutes" in item.lower():
            words = item.split()
            new_words = []

            for word in words:
                if word.isdigit():
                    new_number = int(word) * multiplier
                    new_words.append(str(new_number))
                else:
                    new_words.append(word)

            updated_list.append(" ".join(new_words))
        else:
            updated_list.append(item)

    return updated_list

def recommend_workout_ml(self, user_profile):
    model = WorkoutRecommendationModel()
    workout = model.predict({
        "age": user_profile["age"],
        "weight": user_profile["weight"],
        "goal": user_profile["goal"],
        "experience_level": user_profile["fitness_level"]
    })
    return workout

def get_base_workout(goal, equipment):
    """Get base workout exercises based on goal and equipment"""
    workout_exercises = []

    if goal.lower() == "weight loss":
        if equipment.lower() == "home":
            workout_exercises = [
                "Jumping jacks - 3 sets of 30 seconds",
                "Bodyweight squats - 15 reps",
                "Mountain climbers - 20 reps",
                "Plank - 30 seconds",
                "High knees - 30 seconds",
                "Burpees - 10 reps"
            ]
        elif equipment.lower() == "outdoor":
            workout_exercises = [
                "Sprint intervals - 50 meters x 5",
                "Park bench step-ups - 20 reps",
                "Broad jumps - 10 reps",
                "Mountain climbers - 40 reps",
                "Running - 15 minutes",
                "Jump squats - 15 reps"
            ]
        else: 
            workout_exercises = [
                "Treadmill running - 20 minutes",
                "Cycling - 15 minutes",
                "Leg press - 15 reps",
                "Cable crunches - 15 reps",
                "Elliptical - 10 minutes",
                "Battle ropes - 30 seconds x 3"
            ]

    elif goal.lower() == "muscle gain":
        if equipment.lower() == "home":
            workout_exercises = [
                "Push-ups - 15 reps",
                "Squats - 15 reps",
                "Lunges - 15 reps per leg",
                "Pike push-ups - 12 reps",
                "Bulgarian split squats - 12 reps per leg",
                "Plank to push-up - 10 reps"
            ]
        elif equipment.lower() == "outdoor":
            workout_exercises = [
                "Explosive push-ups - 10 reps",
                "Walking lunges - 20 steps per leg",
                "Pike push-ups - 15 reps",
                "Bulgarian split squats - 15 reps per leg",
                "Pull-ups (if bar available) - 8 reps",
                "Diamond push-ups - 12 reps"
            ]
        else: 
            workout_exercises = [
                "Bench press - 12 reps x 3 sets",
                "Lat pull-down - 12 reps x 3 sets",
                "Shoulder press - 12 reps x 3 sets",
                "Bicep curls - 15 reps x 3 sets",
                "Tricep dips - 12 reps x 3 sets",
                "Leg press - 15 reps x 3 sets"
            ]

    else: 
        if equipment.lower() == "home":
            workout_exercises = [
                "Light jogging in place - 10 minutes",
                "Bodyweight squats - 15 reps",
                "Push-ups - 10 reps",
                "Plank - 30 seconds",
                "Stretching exercises - 10 minutes",
                "Yoga poses - 15 minutes"
            ]
        elif equipment.lower() == "outdoor":
            workout_exercises = [
                "Brisk walking - 20 minutes",
                "Bodyweight squats - 15 reps",
                "Park bench push-ups - 12 reps",
                "Lunges - 10 reps per leg",
                "Stretching - 10 minutes",
                "Light jogging - 10 minutes"
            ]
        else: 
            workout_exercises = [
                "Treadmill walking - 15 minutes",
                "Cycling - 15 minutes",
                "Light weights - full body circuit",
                "Stretching - 10 minutes",
                "Yoga or Pilates - 20 minutes",
                "Swimming - 15 minutes (if available)"
            ]

    return workout_exercises


def create_weekly_workout_structure(exercises, fitness_level, goal):
    """Create a structured weekly workout plan"""
    level = fitness_level.lower()

    if level == "beginner":
        active_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    elif level == "intermediate":
        active_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    else: 
        active_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    weekly_plan = {}
    
    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for day in all_days:
        if day in active_days:
            day_index = active_days.index(day)
            
            if goal.lower() == "muscle gain":
                if day_index % 3 == 0:
                    workout_type = "Upper Body Focus"
                    day_exercises = [ex for ex in exercises if any(word in ex.lower() for word in ['push', 'press', 'pull', 'curl', 'dip'])]
                elif day_index % 3 == 1:
                    workout_type = "Lower Body Focus"
                    day_exercises = [ex for ex in exercises if any(word in ex.lower() for word in ['squat', 'lunge', 'leg', 'jump'])]
                else:
                    workout_type = "Full Body"
                    day_exercises = exercises[:4]
            
            elif goal.lower() == "weight loss":
                workout_type = "Cardio & Fat Burn"
                day_exercises = exercises
            
            else: 
                workout_type = "Balanced Fitness"
                day_exercises = exercises
            
            if not day_exercises:
                day_exercises = exercises
            
            weekly_plan[f"{day} - {workout_type}"] = day_exercises
        else:
            weekly_plan[f"{day} - Rest Day"] = ["Active recovery: Light stretching, walking, or yoga"]
    
    return weekly_plan


def get_advanced_exercises(fitness_level, goal):
    """Get additional advanced exercises based on fitness level"""
    level = fitness_level.lower()
    advanced_exercises = []
    
    if level == "intermediate":
        if goal.lower() == "weight loss":
            advanced_exercises = [
                "Jump rope - 2 minutes",
                "Box jumps - 15 reps",
                "Burpees - 20 reps"
            ]
        elif goal.lower() == "muscle gain":
            advanced_exercises = [
                "Diamond push-ups - 15 reps",
                "Archer push-ups - 10 reps per side",
                "Pistol squat progressions - 8 reps per leg"
            ]
        else:
            advanced_exercises = [
                "High knees - 40 seconds",
                "Plank variations - 45 seconds",
                "Jump squats - 15 reps"
            ]
    
    elif level == "advanced":
        if goal.lower() == "weight loss":
            advanced_exercises = [
                "HIIT sprints - 30 seconds x 8 rounds",
                "Box jumps - 25 reps",
                "Burpee pull-ups - 15 reps",
                "Kettlebell swings - 20 reps (if available)"
            ]
        elif goal.lower() == "muscle gain":
            advanced_exercises = [
                "Archer push-ups - 15 reps per side",
                "Pistol squats - 12 reps per leg",
                "Planche progressions - 30 seconds",
                "One-arm push-ups - 8 reps per side",
                "Explosive pull-ups - 10 reps"
            ]
        else:
            advanced_exercises = [
                "Plank hold - 90 seconds",
                "Jump squats - 25 reps",
                "HIIT sprints - 120 seconds",
                "Advanced yoga flows - 20 minutes"
            ]
    
    return advanced_exercises


def generate_workout_plan(goal, equipment, fitness_level):
    """Generate a comprehensive weekly workout plan"""
    base_exercises = get_base_workout(goal, equipment)
    
    level = fitness_level.lower()
    
    if level == "intermediate":
        base_exercises = multiply_workout(base_exercises, 2)
        advanced_exercises = get_advanced_exercises(fitness_level, goal)
        base_exercises.extend(advanced_exercises)
    
    elif level == "advanced":
        base_exercises = multiply_workout(base_exercises, 3)
        advanced_exercises = get_advanced_exercises(fitness_level, goal)
        base_exercises.extend(advanced_exercises)
    
    weekly_plan = create_weekly_workout_structure(base_exercises, fitness_level, goal)
    
    return weekly_plan


def get_weekly_progression_tip(fitness_level):
    """Get progression tips based on fitness level"""
    level = fitness_level.lower()
    
    tips = {
        "beginner": (
            "Week 1-2: Focus on proper form and consistency. "
            "Week 3-4: Add 5 reps or 10 seconds per exercise. "
            "Listen to your body and rest when needed."
        ),
        "intermediate": (
            "Week 1-2: Increase intensity by 10%. "
            "Week 3-4: Add 10-15 reps or 20 seconds per exercise. "
            "Consider adding one extra workout day or incorporating supersets."
        ),
        "advanced": (
            "Week 1-2: Increase weight/resistance by 5-10%. "
            "Week 3-4: Add 15-20 reps or 30 seconds per exercise. "
            "Focus on explosive movements and advanced progressions."
        )
    }
    
    return tips.get(level, tips["beginner"])


def get_workout_tips(goal, equipment):
    """Get specific workout tips based on goal and equipment"""
    tips = []
    
    if goal.lower() == "weight loss":
        tips.extend([
            "Focus on maintaining high heart rate during workouts",
            "Combine cardio with strength training for best results",
            "Aim for 4-6 workouts per week with progressive intensity"
        ])
    elif goal.lower() == "muscle gain":
        tips.extend([
            "Focus on progressive overload - gradually increase resistance",
            "Ensure adequate protein intake (1.6-2.2g per kg bodyweight)",
            "Rest 48-72 hours between training the same muscle group"
        ])
    else:
        tips.extend([
            "Maintain consistency - regularity is key to staying fit",
            "Balance cardio, strength, and flexibility training",
            "Aim for at least 150 minutes of moderate activity per week"
        ])
    
    if equipment.lower() == "home":
        tips.append("Use household items (water bottles, books) as improvised weights")
    elif equipment.lower() == "gym":
        tips.append("Take advantage of free weights and machines for variety")
    
    return tips
