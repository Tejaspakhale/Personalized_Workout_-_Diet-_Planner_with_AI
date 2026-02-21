import json
import os
from datetime import datetime
from workout_planner import generate_workout_plan, get_weekly_progression_tip
from diet_planner import generate_diet_plan, filter_meals_by_preferences
from user_data_manager import load_user_data, save_user_data, get_user_profile
from ml_predictor import generate_ml_insights, display_ml_insights
from ml_predictor import CaloriePredictor
from ml_predictor import AdaptiveLearner

DATA_FILE = "user_data.json"

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display application header"""
    print("=" * 60)
    print("    🏋️ PERSONALIZED WORKOUT & DIET PLANNER 🥗")
    print("=" * 60)
    print()

def get_user_input():
    """Collect user information with validation"""
    print("📋 USER INFORMATION")
    print("-" * 60)
    
    name = input("Enter your name: ").strip()
    
    while True:
        try:
            age = int(input("Enter your age: "))
            if 10 <= age <= 100:
                break
            print("⚠️  Age must be between 10 and 100")
        except ValueError:
            print("⚠️  Please enter a valid number")
    
    gender = input("Gender (M/F/Other): ").strip()
    
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if weight > 0:
                break
            print("⚠️  Weight must be positive")
        except ValueError:
            print("⚠️  Please enter a valid number")
    
    while True:
        try:
            height = float(input("Enter your height (cm): "))
            if height > 0:
                break
            print("⚠️  Height must be positive")
        except ValueError:
            print("⚠️  Please enter a valid number")
    
    print("\n🎯 FITNESS GOALS")
    print("1. Weight Loss")
    print("2. Muscle Gain")
    print("3. Stay Fit")
    goal_choice = input("Choose your goal (1-3): ").strip()
    goal_map = {"1": "Weight Loss", "2": "Muscle Gain", "3": "Stay Fit"}
    goal = goal_map.get(goal_choice, "Stay Fit")
    
    print("\n🍽️  DIET PREFERENCES")
    print("1. Vegetarian")
    print("2. Non-Vegetarian")
    diet_choice = input("Choose your diet type (1-2): ").strip()
    diet_type = "Veg" if diet_choice == "1" else "Non-Veg"
    
    print("\n📍 WORKOUT LOCATION")
    print("1. Home")
    print("2. Gym")
    print("3. Outdoor")
    location_choice = input("Choose workout location (1-3): ").strip()
    location_map = {"1": "Home", "2": "Gym", "3": "Outdoor"}
    workout_location = location_map.get(location_choice, "Home")
    
    while True:
        try:
            workout_time = int(input("\n⏱️  Available workout time per day (minutes): "))
            if workout_time > 0:
                break
            print("⚠️  Time must be positive")
        except ValueError:
            print("⚠️  Please enter a valid number")
    
    print("\n💪 FITNESS LEVEL")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    level_choice = input("Choose your fitness level (1-3): ").strip()
    level_map = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
    fitness_level = level_map.get(level_choice, "Beginner")
    
    medical_conditions = input("\n🩺 Any medical conditions/injuries (or 'none'): ").strip()
    
    equipment = input("\n🧰 Available Equipment (or 'none'): ").strip()
    
    print("\n🚫 FOOD PREFERENCES")
    print("Enter foods you want to avoid (comma-separated, or press Enter to skip):")
    avoid_foods = input("Foods to avoid: ").strip()
    avoid_list = [food.strip().lower() for food in avoid_foods.split(",") if food.strip()]
    
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "goal": goal,
        "diet_type": diet_type,
        "workout_location": workout_location,
        "workout_time_minutes": workout_time,
        "fitness_level": fitness_level,
        "medical_conditions": medical_conditions,
        "equipment": equipment,
        "avoid_foods": avoid_list,
        "created_at": datetime.now().isoformat()
    }

def display_workout_plan(workout_plan, week_number=1):
    """Display the workout plan with weekly structure"""
    print("\n" + "=" * 60)
    print(f"🏋️  WORKOUT PLAN - WEEK {week_number}")
    print("=" * 60)
    
    for day, exercises in workout_plan.items():
        print(f"\n📅 {day}:")
        for exercise in exercises:
            print(f"   • {exercise}")

def display_diet_plan(diet_plan, avoid_foods):
    """Display the diet plan with alternatives"""
    print("\n" + "=" * 60)
    print("🥗 DIET PLAN - AI-OPTIMIZED RECOMMENDATIONS")
    print("=" * 60)
    
    try:
        from ml_predictor import AdaptiveLearner
        learner = AdaptiveLearner()
        use_ml = True
    except:
        use_ml = False
    
    for meal_time, meals in diet_plan.items():
        available_meals = filter_meals_by_preferences(meals, avoid_foods)
        
        if not available_meals:
            available_meals = meals  
        
        primary_meal = available_meals[0]
        print(f"\n🍽️  {meal_time.upper()}:")
        print(f"   ✓ {primary_meal['name']}")
        print(f"     Calories: {primary_meal['calories']} kcal | Protein: {primary_meal['protein']}g")
        
        if len(available_meals) > 1:
            print(f"\n   📋 Alternatives:")
            for i, meal in enumerate(available_meals[1:3], 1):
                print(f"      {i}. {meal['name']} ({meal['calories']} kcal, {meal['protein']}g protein)")
        

def display_diet_plan_original(diet_plan, avoid_foods):
    """Display the diet plan with alternatives"""
    print("\n" + "=" * 60)
    print("🥗 DIET PLAN - TODAY'S RECOMMENDATIONS")
    print("=" * 60)
    
    for meal_time, meals in diet_plan.items():
        
        available_meals = filter_meals_by_preferences(meals, avoid_foods)
        
        if not available_meals:
            available_meals = meals  
        
        primary_meal = available_meals[0]
        print(f"\n🍽️  {meal_time.upper()}:")
        print(f"   ✓ {primary_meal['name']}")
        print(f"     Calories: {primary_meal['calories']} kcal | Protein: {primary_meal['protein']}g")
        
        if len(available_meals) > 1:
            print(f"\n   📋 Alternatives:")
            for i, meal in enumerate(available_meals[1:3], 1):
                print(f"      {i}. {meal['name']} ({meal['calories']} kcal, {meal['protein']}g protein)")

def display_ml_predictions(user_data):
    """Display ML-powered calorie predictions and insights"""
    print("\n" + "=" * 60)
    print("🤖 AI/ML POWERED PREDICTIONS")
    print("=" * 60)
    
    predictor = CaloriePredictor()
    calorie_needs = predictor.predict_calorie_needs(user_data)
    
    print("\n📊 Calorie Needs Prediction (ML Model):")
    print(f"   Basal Metabolic Rate: {calorie_needs['bmr']} kcal/day")
    print(f"   Maintenance (TDEE): {calorie_needs['maintenance_calories']} kcal/day")
    print(f"   🎯 Target: {calorie_needs['target_calories']} kcal/day")
    print(f"\n   💡 {calorie_needs['explanation']}")
 
    macros = predictor.predict_macros(
        calorie_needs['target_calories'],
        user_data['goal']
    )
    
    print(f"\n🥗 Optimal Macros (ML Calculated):")
    print(f"   Protein: {macros['protein_g']}g ({macros['protein_percent']}%) daily")
    print(f"   Carbs: {macros['carbs_g']}g ({macros['carbs_percent']}%) daily")
    print(f"   Fats: {macros['fats_g']}g ({macros['fats_percent']}%) daily")
 
    learner = AdaptiveLearner()
 
    if 'history' in user_data and len(user_data['history']) >= 2:
        progress = learner.analyze_user_progress(user_data)
        
        if progress:
            print(f"\n📈 Progress Analysis (ML-based):")
            print(f"   Sessions Completed: {progress['total_sessions']}")
            print(f"   Weight Change: {progress['total_weight_change']:+.1f} kg")
            print(f"   Consistency Score: {progress['consistency_score']}%")
            print(f"   Goal Progress: {'✅ On Track' if progress['is_on_track'] else '⚠️ Needs Adjustment'}")
            
            suggestions = learner.suggest_adjustments(user_data, progress)
            if suggestions:
                print(f"\n🎯 AI Recommendations (from your data):")
                high_priority = [s for s in suggestions if s['priority'] == 'high']
                medium_priority = [s for s in suggestions if s['priority'] == 'medium']
                
                if high_priority:
                    print(f"   🔴 High Priority:")
                    for suggestion in high_priority:
                        print(f"      • {suggestion['recommendation']}")
                        print(f"        Reason: {suggestion['reason']}")
                
                if medium_priority:
                    print(f"   🟡 Medium Priority:")
                    for suggestion in medium_priority:
                        print(f"      • {suggestion['recommendation']}")
            
            prediction = learner.predict_next_weight(user_data)
            if prediction:
                print(f"\n🔮 Weight Prediction (Linear Regression):")
                print(f"   Current: {user_data['weight']} kg")
                print(f"   Predicted Next: {prediction['predicted_weight']} kg")
                print(f"   Trend: {prediction['trend'].capitalize()} at {abs(prediction['rate_per_session']):.2f} kg/session")
   
    insights = learner.generate_insights(user_data)
    if insights:
        print(f"\n💡 ML-Generated Insights:")
        for category, insight in insights:
            print(f"   • {insight}")

def display_progress_tracking(user_profile):
    """Display user's progress and history"""
    print("\n" + "=" * 60)
    print("📊 PROGRESS TRACKING")
    print("=" * 60)
    
    if "history" in user_profile and user_profile["history"]:
        history = user_profile["history"]
        print(f"\n📅 Plan created: {len(history)} session(s) recorded")
        print(f"🗓️  First session: {history[0]['date'][:10]}")
        print(f"🗓️  Latest session: {history[-1]['date'][:10]}")
     
        if len(history) > 1:
            initial_bmi = calculate_bmi(history[0]['weight'], user_profile['height'])
            current_bmi = calculate_bmi(history[-1]['weight'], user_profile['height'])
            bmi_change = current_bmi - initial_bmi
            
            print(f"\n📈 BMI Trend:")
            print(f"   Initial BMI: {initial_bmi:.2f}")
            print(f"   Current BMI: {current_bmi:.2f}")
            print(f"   Change: {bmi_change:+.2f}")
    else:
        print("\n🆕 This is your first session! Keep tracking your progress.")

def calculate_bmi(weight, height):
    """Calculate BMI"""
    height_m = height / 100
    return weight / (height_m ** 2)

def display_health_tips(user_data):
    """Display personalized health and safety tips"""
    print("\n" + "=" * 60)
    print("💡 PERSONALIZED HEALTH TIPS")
    print("=" * 60)

    progression_tip = get_weekly_progression_tip(user_data['fitness_level'])
    print(f"\n📌 Weekly Progress Tip:")
    print(f"   {progression_tip}")
  
    print(f"\n🧰 Equipment Tip:")
    if user_data['equipment'].lower() != "none":
        print(f"   Your available equipment: {user_data['equipment']}")
        print("   Incorporate equipment-based exercises using the suggested")
        print("   repetitions or duration from your workout plan.")
    else:
        print("   No equipment needed! Bodyweight exercises are highly effective")
        print("   and can be done anywhere.")
  
    print(f"\n🩺 Health & Safety Note:")
    condition = user_data['medical_conditions'].strip().lower()
    if condition != "none" and condition != "":
        print(f"   ⚠️  Medical condition noted: {user_data['medical_conditions']}")
        print("   • Perform all exercises carefully")
        print("   • Stop immediately if you feel pain or discomfort")
        print("   • Consult a doctor before increasing intensity")
    else:
        print("   ✓ No medical conditions reported")
        print("   • Follow the plan as suggested")
        print("   • Maintain proper form and rest")
        print("   • Discontinue any exercise causing pain")
  
    print(f"\n🌟 Personal Health Tips:")
    print("   • Stay consistent with workouts and aim to exercise regularly")
    print("   • Drink 2-3 liters of water daily")
    print("   • Get 7-8 hours of quality sleep")
    print("   • Include at least one fruit in your daily diet")
    print("   • Avoid junk foods and sugary drinks")
    print("   • Track your progress weekly")
  
    bmi = calculate_bmi(user_data['weight'], user_data['height'])
    print(f"\n📊 Your Current Stats:")
    print(f"   BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("   Status: Underweight - Focus on muscle gain with proper nutrition")
    elif 18.5 <= bmi < 25:
        print("   Status: Normal weight - Maintain with balanced diet and exercise")
    elif 25 <= bmi < 30:
        print("   Status: Overweight - Focus on calorie deficit and cardio")
    else:
        print("   Status: Obese - Consult a doctor, start with low-impact exercises")

def main():
    """Main application logic"""
    clear_screen()
    display_header()
  
    existing_profile = get_user_profile(DATA_FILE)
    
    if existing_profile:
        print(f"👋 Welcome back, {existing_profile['name']}!")
        print("\nWould you like to:")
        print("1. Use existing profile and update data")
        print("2. Create a new profile")
        choice = input("\nChoose option (1-2): ").strip()
        
        if choice == "1":
            print("\n📝 Update your current information:")
            print(f"Current weight: {existing_profile['weight']} kg")
            new_weight = input("Enter new weight (or press Enter to keep current): ").strip()
            if new_weight:
                try:
                    existing_profile['weight'] = float(new_weight)
                except ValueError:
                    print("Invalid weight, keeping existing value")
            
            print(f"\nCurrent fitness level: {existing_profile['fitness_level']}")
            print("Has your fitness level changed? (y/n): ", end="")
            if input().strip().lower() == 'y':
                print("1. Beginner")
                print("2. Intermediate")
                print("3. Advanced")
                level_choice = input("New fitness level (1-3): ").strip()
                level_map = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
                existing_profile['fitness_level'] = level_map.get(level_choice, existing_profile['fitness_level'])
            
            user_data = existing_profile
        else:
            user_data = get_user_input()
    else:
        print("🆕 New user detected. Let's create your profile!\n")
        user_data = get_user_input()
 
    save_user_data(DATA_FILE, user_data)
   
    print("\n⏳ Generating your personalized plan...")
    
    workout_plan = generate_workout_plan(
        user_data['goal'],
        user_data['workout_location'],
        user_data['fitness_level']
    )
    
    diet_plan = generate_diet_plan(
        user_data['goal'],
        user_data['diet_type']
    )
   
    clear_screen()
    display_header()
    print(f"Hello {user_data['name']}! 👋\n")
  
    display_ml_predictions(user_data)
    
    display_workout_plan(workout_plan)
    display_diet_plan(diet_plan, user_data.get('avoid_foods', []))
    display_progress_tracking(user_data)
  
    ml_insights = generate_ml_insights(user_data, user_data.get('history'))
    display_ml_insights(ml_insights)
    
    display_health_tips(user_data)
    
    print("\n" + "=" * 60)
    print("✅ Your personalized plan is ready!")
    print("💾 All data has been saved for future reference.")
    print("=" * 60)
    print()

if __name__ == "__main__":
    main()
