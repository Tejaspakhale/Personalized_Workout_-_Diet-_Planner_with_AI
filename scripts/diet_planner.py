def get_weight_loss_diet(diet_type):
    """Get weight loss diet plan based on diet type"""
    if diet_type.lower() == "veg":
        return {
            'breakfast': [
                {'name': 'Oats with Almond Milk & Chia Seeds', 'calories': 220, 'protein': 10},
                {'name': 'Greek Yogurt (Low Fat) with Berries', 'calories': 180, 'protein': 15},
                {'name': 'Moong Dal Chilla with Mint Chutney', 'calories': 250, 'protein': 15},
                {'name': 'Vegetable Poha (Less Oil)', 'calories': 240, 'protein': 6},
                {'name': 'Sprouts Salad with Lemon', 'calories': 150, 'protein': 12},
                {'name': 'Quinoa Upma with Vegetables', 'calories': 230, 'protein': 8}
            ],
            'lunch': [
                {'name': 'Dal, Brown Rice, Mixed Veg Sabzi, Salad', 'calories': 500, 'protein': 18},
                {'name': '2 Multigrain Roti + Mixed Veg + Paneer', 'calories': 400, 'protein': 12},
                {'name': 'Masoor Dal + 1 Multigrain Roti', 'calories': 320, 'protein': 15},
                {'name': 'Rajma (1 bowl) + 1 Roti', 'calories': 370, 'protein': 15},
                {'name': 'Chickpea Curry + Brown Rice (3/4 cup)', 'calories': 420, 'protein': 16},
                {'name': 'Vegetable Khichdi with Curd', 'calories': 380, 'protein': 14}
            ],
            'dinner': [
                {'name': 'Paneer Bhurji (75g) + Salad', 'calories': 280, 'protein': 20},
                {'name': 'Mixed Vegetable Soup + Roasted Chana', 'calories': 180, 'protein': 10},
                {'name': 'Vegetable Soup + Sprouts Salad', 'calories': 200, 'protein': 12},
                {'name': 'Palak Paneer (Less oil) + 1 Chapati', 'calories': 460, 'protein': 22},
                {'name': 'Tofu Stir Fry with Vegetables', 'calories': 260, 'protein': 18},
                {'name': 'Grilled Paneer Tikka + Salad', 'calories': 300, 'protein': 24}
            ]
        }
    else: 
        return {
            'breakfast': [
                {'name': 'Oats + Whey Protein + Almonds', 'calories': 300, 'protein': 25},
                {'name': 'Boiled Eggs (3 whole)', 'calories': 210, 'protein': 20},
                {'name': 'Egg White Omelette (4 whites + veggies)', 'calories': 160, 'protein': 20},
                {'name': 'Egg Bhurji (2 eggs, less oil) + 1 Multigrain Roti', 'calories': 300, 'protein': 20},
                {'name': 'Scrambled Eggs (2) with Spinach', 'calories': 190, 'protein': 16},
                {'name': 'Poached Eggs (2) with Whole Wheat Toast', 'calories': 280, 'protein': 18}
            ],
            'lunch': [
                {'name': 'Grilled Chicken (150g) + Salad', 'calories': 300, 'protein': 35},
                {'name': 'Chicken Curry (Less Oil) + 1 Roti', 'calories': 350, 'protein': 30},
                {'name': 'Egg Curry (2 eggs) + 1 Roti', 'calories': 360, 'protein': 22},
                {'name': 'Fish Curry (100g) + 1 Roti', 'calories': 330, 'protein': 28},
                {'name': 'Grilled Fish (120g) + Brown Rice (1/2 cup)', 'calories': 340, 'protein': 32},
                {'name': 'Turkey Breast (100g) + Quinoa Salad', 'calories': 320, 'protein': 36}
            ],
            'dinner': [
                {'name': 'Grilled Fish (120g) + Vegetables', 'calories': 280, 'protein': 30},
                {'name': 'Chicken Soup (Clear, no cream)', 'calories': 200, 'protein': 25},
                {'name': 'Boiled Eggs (2) + Salad', 'calories': 180, 'protein': 12},
                {'name': 'Tandoori Chicken (150g)', 'calories': 320, 'protein': 20},
                {'name': 'Baked Salmon (100g) + Steamed Broccoli', 'calories': 290, 'protein': 28},
                {'name': 'Chicken Tikka (120g) + Mixed Salad', 'calories': 270, 'protein': 32}
            ]
        }


def get_muscle_gain_diet(diet_type):
    """Get muscle gain diet plan based on diet type"""
    if diet_type.lower() == "veg":
        return {
            'breakfast': [
                {'name': 'Oats with Almond Milk & Nuts', 'calories': 350, 'protein': 22},
                {'name': 'Vegetable Upma + Sprouts', 'calories': 380, 'protein': 20},
                {'name': 'Moong Dal Chilla + Curd', 'calories': 350, 'protein': 22},
                {'name': 'Paneer Bhurji (100g)', 'calories': 300, 'protein': 20},
                {'name': 'Peanut Butter Banana Smoothie', 'calories': 420, 'protein': 18},
                {'name': 'Besan Chilla (2) + Greek Yogurt', 'calories': 390, 'protein': 24}
            ],
            'lunch': [
                {'name': 'Soya Chunk Curry (60g dry) + Rice', 'calories': 540, 'protein': 40},
                {'name': 'Chole (1 bowl) + 2 Rotis', 'calories': 560, 'protein': 24},
                {'name': 'Dal (Mixed) + Ghee Roti + Veg', 'calories': 500, 'protein': 25},
                {'name': 'Rajma (1 bowl) + Brown Rice (1 cup)', 'calories': 520, 'protein': 22},
                {'name': 'Paneer Butter Masala + 2 Rotis', 'calories': 580, 'protein': 28},
                {'name': 'Tofu Curry (150g) + Quinoa (1 cup)', 'calories': 550, 'protein': 32}
            ],
            'dinner': [
                {'name': 'Chana Stir Fry (1 bowl)', 'calories': 330, 'protein': 22},
                {'name': 'Brown Rice (3/4 cup) + Dal Tadka', 'calories': 430, 'protein': 24},
                {'name': 'Soya Chunk Stir Fry (50g dry)', 'calories': 350, 'protein': 32},
                {'name': 'Dal + Veg Soup Combo', 'calories': 320, 'protein': 22},
                {'name': 'Paneer Tikka (150g) + Veg Salad', 'calories': 420, 'protein': 30},
                {'name': 'Mixed Lentil Curry + 1 Roti', 'calories': 400, 'protein': 26}
            ]
        }
    else:  
        return {
            'breakfast': [
                {'name': 'Whole Eggs (4 eggs)', 'calories': 320, 'protein': 25},
                {'name': 'Chicken Keema (100g, dry)', 'calories': 330, 'protein': 30},
                {'name': 'Oats (40g) + 3 Egg Whites', 'calories': 350, 'protein': 28},
                {'name': 'Egg Bhurji (3 eggs, minimal oil) + 1 Multigrain Roti', 'calories': 400, 'protein': 26},
                {'name': 'Protein Pancakes (2 eggs + oats)', 'calories': 380, 'protein': 24},
                {'name': 'Tuna Sandwich (Whole Wheat)', 'calories': 360, 'protein': 28}
            ],
            'lunch': [
                {'name': 'Grilled Chicken Breast (200g) + Rice (1 cup)', 'calories': 550, 'protein': 40},
                {'name': 'Chicken Curry (150g, low oil) + 2 Rotis', 'calories': 520, 'protein': 40},
                {'name': 'Fish Curry (Surmai/Rohu 150g) + Rice', 'calories': 500, 'protein': 38},
                {'name': 'Mutton (Lean, 120g) + 2 Rotis', 'calories': 600, 'protein': 35},
                {'name': 'Grilled Salmon (150g) + Sweet Potato', 'calories': 530, 'protein': 42},
                {'name': 'Turkey Meatballs (150g) + Pasta', 'calories': 560, 'protein': 38}
            ],
            'dinner': [
                {'name': 'Tandoori Chicken (200g)', 'calories': 420, 'protein': 45},
                {'name': 'Grilled Fish (180g) + Veggies', 'calories': 380, 'protein': 45},
                {'name': 'Egg Whites Omelette (6 whites)', 'calories': 210, 'protein': 36},
                {'name': 'Chicken Soup (thick, homemade)', 'calories': 320, 'protein': 30},
                {'name': 'Baked Chicken Thighs (150g)', 'calories': 400, 'protein': 38},
                {'name': 'Prawn Curry (150g) + 1 Roti', 'calories': 360, 'protein': 34}
            ]
        }


def get_stay_fit_diet(diet_type):
    """Get stay fit diet plan based on diet type"""
    if diet_type.lower() == "veg":
        return {
            'breakfast': [
                {'name': 'Oats with Almond Milk & Nuts', 'calories': 350, 'protein': 22},
                {'name': 'Moong Dal Chilla + Curd', 'calories': 350, 'protein': 22},
                {'name': 'Vegetable Poha (Less Oil)', 'calories': 240, 'protein': 6},
                {'name': 'Vegetable Upma + Sprouts', 'calories': 380, 'protein': 20},
                {'name': 'Fruit Smoothie with Yogurt', 'calories': 280, 'protein': 12},
                {'name': 'Idli (3) with Sambar', 'calories': 300, 'protein': 10}
            ],
            'lunch': [
                {'name': 'Masoor Dal + 1 Multigrain Roti', 'calories': 320, 'protein': 15},
                {'name': 'Paneer Sabzi (120g) + 2 Rotis', 'calories': 560, 'protein': 28},
                {'name': 'Dal (Mixed) + Ghee Roti + Veg', 'calories': 500, 'protein': 25},
                {'name': 'Rajma (1 bowl) + Brown Rice (1 cup)', 'calories': 520, 'protein': 22},
                {'name': 'Vegetable Biryani with Raita', 'calories': 480, 'protein': 14},
                {'name': 'Chole + 1 Roti + Salad', 'calories': 450, 'protein': 18}
            ],
            'dinner': [
                {'name': 'Mixed Vegetable Soup + Roasted Chana', 'calories': 180, 'protein': 10},
                {'name': 'Brown Rice (3/4 cup) + Dal Tadka', 'calories': 430, 'protein': 24},
                {'name': 'Dal + Veg Soup Combo', 'calories': 320, 'protein': 22},
                {'name': 'Soya Chunk Stir Fry (50g dry)', 'calories': 350, 'protein': 32},
                {'name': 'Grilled Vegetables + Hummus', 'calories': 280, 'protein': 12},
                {'name': 'Paneer Tikka + Mixed Salad', 'calories': 340, 'protein': 26}
            ]
        }
    else: 
        return {
            'breakfast': [
                {'name': 'Oats + Whey Protein + Almonds', 'calories': 300, 'protein': 25},
                {'name': 'Boiled Eggs (3 whole)', 'calories': 210, 'protein': 20},
                {'name': 'Moong Dal Chilla + Curd', 'calories': 350, 'protein': 22},
                {'name': 'Egg Bhurji (2 eggs, less oil) + 1 Multigrain Roti', 'calories': 300, 'protein': 20},
                {'name': 'Greek Yogurt with Berries & Honey', 'calories': 260, 'protein': 18},
                {'name': 'Egg Sandwich (Whole Wheat)', 'calories': 320, 'protein': 22}
            ],
            'lunch': [
                {'name': 'Fish Curry (100g) + 1 Roti', 'calories': 330, 'protein': 28},
                {'name': 'Grilled Chicken (150g) + Salad', 'calories': 300, 'protein': 35},
                {'name': 'Palak Paneer (Less oil) + Chapati', 'calories': 460, 'protein': 22},
                {'name': 'Egg Curry (2 eggs) + 1 Roti', 'calories': 360, 'protein': 22},
                {'name': 'Chicken Pulao (1 bowl)', 'calories': 420, 'protein': 26},
                {'name': 'Fish Tikka + Brown Rice', 'calories': 390, 'protein': 32}
            ],
            'dinner': [
                {'name': 'Grilled Fish (180g) + Veggies', 'calories': 380, 'protein': 45},
                {'name': 'Chicken Soup (Clear, no cream)', 'calories': 200, 'protein': 25},
                {'name': 'Paneer Tikka (120g) + Salad', 'calories': 380, 'protein': 26},
                {'name': 'Tandoori Chicken (150g)', 'calories': 320, 'protein': 20},
                {'name': 'Baked Fish + Steamed Vegetables', 'calories': 310, 'protein': 36},
                {'name': 'Chicken Stir Fry with Vegetables', 'calories': 340, 'protein': 30}
            ]
        }


def generate_diet_plan(goal, diet_type):
    """Generate diet plan based on goal and diet preference"""
    if goal.lower() == "weight loss":
        return get_weight_loss_diet(diet_type)
    elif goal.lower() == "muscle gain":
        return get_muscle_gain_diet(diet_type)
    else: 
        return get_stay_fit_diet(diet_type)


def filter_meals_by_preferences(meals, avoid_foods):
    """Filter meals based on user's food preferences"""
    if not avoid_foods:
        return meals
    
    filtered_meals = []
    
    for meal in meals:
        meal_name_lower = meal['name'].lower()
    
        contains_avoided = False
        for avoided_food in avoid_foods:
            if avoided_food in meal_name_lower:
                contains_avoided = True
                break
        
        if not contains_avoided:
            filtered_meals.append(meal)
    
    return filtered_meals if filtered_meals else meals


def calculate_daily_calories(meals_dict):
    """Calculate total daily calories from selected meals"""
    total_calories = 0
    total_protein = 0
    
    for meal_time, meals in meals_dict.items():
        if meals:
            meal = meals[0] 
            total_calories += meal['calories']
            total_protein += meal['protein']
    
    return total_calories, total_protein


def get_nutrition_tips(goal, diet_type):
    """Get personalized nutrition tips"""
    tips = []
    
    if goal.lower() == "weight loss":
        tips.extend([
            "Maintain a calorie deficit of 300-500 kcal per day",
            "Eat protein with every meal to preserve muscle mass",
            "Drink water before meals to control portion sizes",
            "Avoid liquid calories (sodas, juices, alcohol)"
        ])
    elif goal.lower() == "muscle gain":
        tips.extend([
            "Consume 1.6-2.2g protein per kg bodyweight daily",
            "Eat in a calorie surplus of 200-400 kcal per day",
            "Have protein within 2 hours post-workout",
            "Include complex carbs for energy and recovery"
        ])
    else:
        tips.extend([
            "Balance your macros: 40% carbs, 30% protein, 30% fats",
            "Eat whole, unprocessed foods whenever possible",
            "Include variety for complete nutrition",
            "Stay hydrated throughout the day"
        ])
    
    if diet_type.lower() == "veg":
        tips.append("Combine different protein sources (dal + rice, beans + grains)")
        tips.append("Consider B12 supplementation if fully vegetarian")
    else:
        tips.append("Choose lean proteins (chicken, fish) over red meat")
    
    return tips


def get_meal_timing_suggestions(goal):
    """Get meal timing suggestions based on goal"""
    suggestions = {
        "weight loss": {
            "breakfast": "7:00 AM - 9:00 AM",
            "lunch": "12:30 PM - 1:30 PM",
            "snack": "4:00 PM - 5:00 PM (Optional: Fruit or nuts)",
            "dinner": "7:00 PM - 8:00 PM (Eat light)"
        },
        "muscle gain": {
            "breakfast": "7:00 AM - 8:00 AM",
            "mid_morning": "10:00 AM (Protein shake or nuts)",
            "lunch": "12:30 PM - 1:30 PM",
            "pre_workout": "4:00 PM (Banana or oats)",
            "post_workout": "6:00 PM (Protein shake)",
            "dinner": "8:00 PM - 9:00 PM"
        },
        "stay fit": {
            "breakfast": "7:00 AM - 9:00 AM",
            "lunch": "12:30 PM - 1:30 PM",
            "snack": "4:00 PM - 5:00 PM (Optional)",
            "dinner": "7:30 PM - 8:30 PM"
        }
    }
    
    return suggestions.get(goal.lower(), suggestions["stay fit"])
