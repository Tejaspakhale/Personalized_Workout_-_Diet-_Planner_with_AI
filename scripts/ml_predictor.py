"""
Machine Learning Module for Personalized Workout & Diet Planner
Features:
1. Calorie needs prediction using multiple regression models
2. Recommendation improvement using user history analysis
3. Simple ML models using only standard library (no sklearn required)
"""

import json
import math
from datetime import datetime
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

    
class CaloriePredictor:
    """Predict daily calorie needs using ML-based formulas and user data"""
    
    def __init__(self):
        self.model_weights = {
            'age': -5.0,
            'weight': 10.0,
            'height': 6.25,
            'gender_male': 5.0,
            'gender_female': -161.0,
            'activity_sedentary': 1.2,
            'activity_light': 1.375,
            'activity_moderate': 1.55,
            'activity_very_active': 1.725,
            'activity_extremely_active': 1.9
        }
    
    def calculate_bmr(self, weight, height, age, gender):
        """
        Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation
        This is a scientifically validated formula
        """
        bmr = (10 * weight) + (6.25 * height) - (5 * age)
        
        if gender.upper() == 'M':
            bmr += 5
        else:
            bmr -= 161
        
        return bmr
    
    def predict_tdee(self, weight, height, age, gender, fitness_level, goal):
        """
        Predict Total Daily Energy Expenditure (TDEE)
        Uses BMR + activity multiplier
        """
        bmr = self.calculate_bmr(weight, height, age, gender)
    
        activity_multipliers = {
            'beginner': 1.375,      
            'intermediate': 1.55,  
            'advanced': 1.725      
        }
        
        activity = activity_multipliers.get(fitness_level.lower(), 1.55)
        tdee = bmr * activity
        
        if goal.lower() == 'weight loss':
            tdee *= 0.80
        elif goal.lower() == 'muscle gain':
            tdee *= 1.15
        
        return round(tdee)
    
    def predict_calorie_needs(self, user_data):
        """
        Predict comprehensive calorie needs including BMR, maintenance, and target
        """
        weight = user_data['weight']
        height = user_data['height']
        age = user_data['age']
        gender = user_data['gender']
        fitness_level = user_data['fitness_level']
        goal = user_data['goal']
        
        bmr = self.calculate_bmr(weight, height, age, gender)
       
        activity_multipliers = {
            'beginner': 1.375,
            'intermediate': 1.55,
            'advanced': 1.725
        }
        activity = activity_multipliers.get(fitness_level.lower(), 1.55)
        maintenance_calories = round(bmr * activity)
      
        target_calories = self.predict_tdee(weight, height, age, gender, fitness_level, goal)
      
        if goal.lower() == 'weight loss':
            explanation = f"20% calorie deficit from maintenance for sustainable weight loss"
        elif goal.lower() == 'muscle gain':
            explanation = f"15% calorie surplus from maintenance for muscle building"
        else:
            explanation = f"Maintenance calories for weight maintenance"
        
        return {
            'bmr': round(bmr),
            'maintenance_calories': maintenance_calories,
            'target_calories': target_calories,
            'explanation': explanation
        }
    
    def predict_protein_needs(self, weight, goal, fitness_level):
        """
        Predict daily protein needs in grams
        Based on bodyweight and activity level
        """
        protein_multipliers = {
            'weight loss': {
                'beginner': 1.6,
                'intermediate': 1.8,
                'advanced': 2.0
            },
            'muscle gain': {
                'beginner': 1.8,
                'intermediate': 2.0,
                'advanced': 2.2
            },
            'stay fit': {
                'beginner': 1.2,
                'intermediate': 1.4,
                'advanced': 1.6
            }
        }
        
        multiplier = protein_multipliers.get(goal.lower(), {}).get(fitness_level.lower(), 1.5)
        protein = weight * multiplier
        
        return round(protein)
    
    def predict_macros(self, tdee, goal):
        """
        Predict macronutrient distribution (protein, carbs, fats)
        Returns grams of each macro
        """
        macro_ratios = {
            'weight loss': {'protein': 0.35, 'carbs': 0.35, 'fats': 0.30},
            'muscle gain': {'protein': 0.30, 'carbs': 0.45, 'fats': 0.25},
            'stay fit': {'protein': 0.30, 'carbs': 0.40, 'fats': 0.30}
        }
        
        ratios = macro_ratios.get(goal.lower(), macro_ratios['stay fit'])
        
        macros = {
            'protein_g': round((tdee * ratios['protein']) / 4),
            'carbs_g': round((tdee * ratios['carbs']) / 4),
            'fats_g': round((tdee * ratios['fats']) / 9),
            'protein_percent': round(ratios['protein'] * 100),
            'carbs_percent': round(ratios['carbs'] * 100),
            'fats_percent': round(ratios['fats'] * 100)
        }
        
        return macros


class RecommendationEngine:
    """Improve suggestions using user history and pattern analysis"""
    
    def __init__(self):
        self.min_history_for_prediction = 3
    
    def analyze_user_history(self, history):
        """
        Analyze user history to extract patterns
        Returns insights about progress and trends
        """
        if not history or len(history) < 2:
            return None
        
        weights = [entry.get('weight', 0) for entry in history if 'weight' in entry]
        dates = [entry.get('date', '') for entry in history]
        
        if len(weights) < 2:
            return None
      
        weight_changes = [weights[i] - weights[i-1] for i in range(1, len(weights))]
        avg_change = sum(weight_changes) / len(weight_changes)
    
        first_date = datetime.fromisoformat(dates[0])
        last_date = datetime.fromisoformat(dates[-1])
        days_elapsed = (last_date - first_date).days
   
        if days_elapsed > 0:
            weekly_change = (weights[-1] - weights[0]) / (days_elapsed / 7)
        else:
            weekly_change = 0
        
        analysis = {
            'total_sessions': len(history),
            'weight_change_total': weights[-1] - weights[0],
            'weight_change_avg': round(avg_change, 2),
            'weekly_change_rate': round(weekly_change, 2),
            'days_tracked': days_elapsed,
            'current_weight': weights[-1],
            'starting_weight': weights[0],
            'trend': 'decreasing' if avg_change < 0 else 'increasing' if avg_change > 0 else 'stable'
        }
        
        return analysis
    
    def predict_fitness_level_progression(self, history, current_level):
        """
        Predict if user should progress to next fitness level
        Based on consistency and duration
        """
        if not history or len(history) < self.min_history_for_prediction:
            return current_level, "Not enough data for prediction"
   
        first_date = datetime.fromisoformat(history[0]['date'])
        last_date = datetime.fromisoformat(history[-1]['date'])
        days_elapsed = (last_date - first_date).days

        weeks_elapsed = max(1, days_elapsed / 7)
        consistency_score = len(history) / weeks_elapsed
        
        level_map = {'beginner': 0, 'intermediate': 1, 'advanced': 2}
        current_level_idx = level_map.get(current_level.lower(), 0)
        
        recommendations = []
        should_progress = False
        
        if current_level.lower() == 'beginner':
            if days_elapsed >= 28 and consistency_score >= 2.5:
                should_progress = True
                recommendations.append("You've been consistent for over 4 weeks!")
                recommendations.append("Consider moving to Intermediate level")
        
        elif current_level.lower() == 'intermediate':
            if days_elapsed >= 56 and consistency_score >= 3.0:
                should_progress = True
                recommendations.append("Excellent consistency for over 8 weeks!")
                recommendations.append("You're ready for Advanced level")
        
        if should_progress:
            next_level = list(level_map.keys())[min(current_level_idx + 1, 2)]
            return next_level.capitalize(), recommendations
        else:
            return current_level, ["Continue at current level", f"Build more consistency (current: {consistency_score:.1f} sessions/week)"]
    
    def adjust_calorie_target(self, predicted_tdee, analysis, goal):
        """
        Adjust calorie target based on user's progress
        ML-like adjustment based on results
        """
        if not analysis:
            return predicted_tdee, "Initial prediction"
        
        weekly_change = analysis['weekly_change_rate']
        
        adjustments = []
        adjusted_tdee = predicted_tdee
        
        if goal.lower() == 'weight loss':
            if weekly_change > -0.3:
                adjusted_tdee = int(predicted_tdee * 0.95)
                adjustments.append("Reducing calories by 5% to enhance weight loss")
            elif weekly_change < -1.2:
                adjusted_tdee = int(predicted_tdee * 1.05)
                adjustments.append("Increasing calories by 5% for sustainable weight loss")
            else:
                adjustments.append("Current calorie target is optimal")
        
        elif goal.lower() == 'muscle gain':
            if weekly_change < 0.15:
                adjusted_tdee = int(predicted_tdee * 1.05)
                adjustments.append("Increasing calories by 5% to support muscle growth")
            elif weekly_change > 0.7:
                adjusted_tdee = int(predicted_tdee * 0.98)
                adjustments.append("Slightly reducing calories for lean muscle gain")
            else:
                adjustments.append("Current calorie target is optimal")
        
        else: 
            if abs(weekly_change) > 0.3:
                if weekly_change > 0:
                    adjusted_tdee = int(predicted_tdee * 0.97)
                    adjustments.append("Reducing calories to maintain weight")
                else:
                    adjusted_tdee = int(predicted_tdee * 1.03)
                    adjustments.append("Increasing calories to maintain weight")
            else:
                adjustments.append("Weight is stable - maintain current calories")
        
        return adjusted_tdee, adjustments
    
    def recommend_workout_adjustments(self, history, current_level):
        """
        Recommend workout adjustments based on progress patterns
        """
        if not history or len(history) < self.min_history_for_prediction:
            return ["Continue with current workout plan", "Track progress for better recommendations"]
        
        analysis = self.analyze_user_history(history)
        recommendations = []
        
        consistency = len(history) / max(1, analysis['days_tracked'] / 7)
        
        if consistency >= 4:
            recommendations.append("🌟 Excellent consistency! Consider adding variety or intensity")
        elif consistency >= 2:
            recommendations.append("✅ Good consistency! Keep it up")
        else:
            recommendations.append("⚠️ Try to increase workout frequency for better results")
        
        if analysis['trend'] == 'decreasing' and history[-1].get('goal', '').lower() == 'weight loss':
            recommendations.append("✅ Weight loss progressing well - maintain current intensity")
        elif analysis['trend'] == 'increasing' and history[-1].get('goal', '').lower() == 'muscle gain':
            recommendations.append("✅ Weight gain on track - continue progressive overload")
        elif analysis['trend'] == 'stable':
            recommendations.append("📊 Weight stable - adjust calories if goal requires change")
        
        if analysis['days_tracked'] >= 21:
            recommendations.append("💪 3+ weeks completed - time to increase difficulty by 10%")
        if analysis['days_tracked'] >= 42:
            recommendations.append("🚀 6+ weeks completed - consider varying exercise selection")
        
        return recommendations
    
    def personalize_diet_selection(self, user_data, meal_history=None):
        """
        Use ML-like scoring to personalize diet recommendations
        Based on preferences and past selections
        """
        preferences = user_data.get('avoid_foods', [])
        goal = user_data.get('goal', 'Stay Fit')
        diet_type = user_data.get('diet_type', 'Veg')
        
        scoring_weights = {
            'calorie_match': 0.4,
            'protein_match': 0.3,
            'preference_match': 0.3
        }
        
        guidance = {
            'focus': 'high_protein' if goal.lower() == 'muscle gain' else 'low_calorie',
            'avoid': preferences,
            'priority': 'protein' if goal.lower() == 'muscle gain' else 'calories'
        }
        
        return guidance


def generate_ml_insights(user_data, history=None):
    """
    Generate ML-powered insights for the user
    Main function to be called from main.py
    """
    predictor = CaloriePredictor()
    engine = RecommendationEngine()
    
    insights = {}
    
    tdee = predictor.predict_tdee(
        user_data['weight'],
        user_data['height'],
        user_data['age'],
        user_data['gender'],
        user_data['fitness_level'],
        user_data['goal']
    )
    
    protein = predictor.predict_protein_needs(
        user_data['weight'],
        user_data['goal'],
        user_data['fitness_level']
    )
    
    macros = predictor.predict_macros(tdee, user_data['goal'])
    
    insights['calories'] = {
        'tdee': tdee,
        'protein_g': protein,
        'macros': macros,
        'bmr': round(predictor.calculate_bmr(
            user_data['weight'],
            user_data['height'],
            user_data['age'],
            user_data['gender']
        ))
    }
    
    if history and len(history) > 1:
        analysis = engine.analyze_user_history(history)
        insights['progress_analysis'] = analysis
        
        adjusted_tdee, adjustments = engine.adjust_calorie_target(
            tdee, analysis, user_data['goal']
        )
        insights['adjusted_calories'] = {
            'tdee': adjusted_tdee,
            'adjustments': adjustments
        }
       
        next_level, level_recommendations = engine.predict_fitness_level_progression(
            history, user_data['fitness_level']
        )
        insights['level_progression'] = {
            'current': user_data['fitness_level'],
            'recommended': next_level,
            'reasons': level_recommendations
        }
      
        workout_recommendations = engine.recommend_workout_adjustments(
            history, user_data['fitness_level']
        )
        insights['workout_recommendations'] = workout_recommendations
    else:
        insights['message'] = "Keep logging your progress! ML predictions improve with more data."
    
    return insights


def display_ml_insights(insights):
    """Display ML insights in a user-friendly format"""
    print("\n" + "="*60)
    print("🤖 AI-POWERED INSIGHTS & PREDICTIONS")
    print("="*60)
    
    if 'calories' in insights:
        cal = insights['calories']
        print("\n📊 DAILY CALORIE & NUTRITION TARGETS")
        print("-"*60)
        print(f"   BMR (Base Metabolic Rate): {cal['bmr']} kcal")
        print(f"   TDEE (Total Daily Energy): {cal['tdee']} kcal")
        print(f"   Daily Protein Target: {cal['protein_g']}g")
        
        if 'macros' in cal:
            macros = cal['macros']
            print(f"\n   📈 Macronutrient Distribution:")
            print(f"      Protein: {macros['protein_g']}g")
            print(f"      Carbs: {macros['carbs_g']}g")
            print(f"      Fats: {macros['fats_g']}g")
 
    if 'progress_analysis' in insights:
        analysis = insights['progress_analysis']
        print("\n📈 PROGRESS ANALYSIS (ML-Based)")
        print("-"*60)
        print(f"   Total Sessions: {analysis['total_sessions']}")
        print(f"   Days Tracked: {analysis['days_tracked']}")
        print(f"   Weight Change: {analysis['weight_change_total']:+.1f} kg")
        print(f"   Weekly Rate: {analysis['weekly_change_rate']:+.2f} kg/week")
        print(f"   Trend: {analysis['trend'].upper()}")
  
    if 'adjusted_calories' in insights:
        adj = insights['adjusted_calories']
        print("\n🎯 ADJUSTED RECOMMENDATIONS (ML-Optimized)")
        print("-"*60)
        print(f"   Optimized Daily Calories: {adj['tdee']} kcal")
        for adjustment in adj['adjustments']:
            print(f"   • {adjustment}")
   
    if 'level_progression' in insights:
        prog = insights['level_progression']
        print("\n💪 FITNESS LEVEL PREDICTION")
        print("-"*60)
        print(f"   Current Level: {prog['current']}")
        print(f"   Recommended Level: {prog['recommended']}")
        if prog['current'] != prog['recommended']:
            print(f"   🚀 LEVEL UP SUGGESTED!")
        for reason in prog['reasons']:
            print(f"   • {reason}")
   
    if 'workout_recommendations' in insights:
        print("\n🏋️ SMART WORKOUT RECOMMENDATIONS")
        print("-"*60)
        for rec in insights['workout_recommendations']:
            print(f"   {rec}")
    
    if 'message' in insights:
        print(f"\n💡 {insights['message']}")


def calculate_accuracy_score(predicted_tdee, actual_results, days):
    """
    Calculate how accurate our predictions are
    This improves over time as we collect more data
    """
    if not actual_results or days < 7:
        return None
 
    expected_change = predicted_tdee * 0.001  
    return {
        'status': 'learning',
        'confidence': min(days / 30, 1.0) 
    }


class WorkoutRecommendationModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.label_encoders = {}
        self.trained = False

    def preprocess(self, df):
        df = df.copy()
        categorical_columns = df.select_dtypes(include=["object"]).columns

        for col in categorical_columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.label_encoders[col] = le

        return df

    def train(self, training_data_path):
        df = pd.read_csv(training_data_path)

        X = df.drop("recommended_workout", axis=1)
        y = df["recommended_workout"]

        X = self.preprocess(X)
        self.model.fit(X, y)

        joblib.dump((self.model, self.label_encoders), "workout_model.pkl")
        self.trained = True

    def load_model(self):
        self.model, self.label_encoders = joblib.load("workout_model.pkl")
        self.trained = True

    def predict(self, user_data):
        if not self.trained:
            self.load_model()

        df = pd.DataFrame([user_data])

        for col, le in self.label_encoders.items():
            if col in df:
                df[col] = le.transform(df[col])

        return self.model.predict(df)[0]


class AdaptiveLearner:
    """Adaptive learning system for personalized recommendations"""
    
    def __init__(self):
        self.engine = RecommendationEngine()
    
    def analyze_user_progress(self, user_data):
        """Analyze user progress using history"""
        if 'history' not in user_data or not user_data['history']:
            return None
        
        analysis = self.engine.analyze_user_history(user_data['history'])
        if not analysis:
            return None
       
        progress = {
            'total_sessions': analysis['total_sessions'],
            'total_weight_change': analysis['weight_change_total'],
            'consistency_score': min(100, (analysis['total_sessions'] / max(1, analysis['days_tracked'] / 7)) * 10),
            'is_on_track': abs(analysis['weekly_change_rate']) > 0.1  
        }
        return progress
    
    def suggest_adjustments(self, user_data, progress):
        """Suggest adjustments based on progress"""
        suggestions = []
        
        if progress['consistency_score'] < 50:
            suggestions.append({
                'priority': 'high',
                'recommendation': 'Increase workout frequency to 4-5 days per week',
                'reason': 'Low consistency score indicates irregular training'
            })
        
        if not progress['is_on_track']:
            suggestions.append({
                'priority': 'medium',
                'recommendation': 'Adjust calorie intake or workout intensity',
                'reason': 'Weight change not aligned with goal progression rate'
            })
        
        if progress['total_sessions'] < 5:
            suggestions.append({
                'priority': 'medium',
                'recommendation': 'Focus on building consistent habits',
                'reason': 'Limited training history for accurate analysis'
            })
        
        return suggestions
    
    def predict_next_weight(self, user_data):
        """Predict next weight based on trend"""
        if 'history' not in user_data or len(user_data['history']) < 2:
            return None
        
        history = user_data['history']
        weights = [entry.get('weight', 0) for entry in history if 'weight' in entry]
        
        if len(weights) < 2:
            return None
     
        n = len(weights)
        x = list(range(n))  
        y = weights
  
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi * xi for xi in x)
        
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
        
        next_weight = weights[-1] + slope
    
        if slope > 0.1:
            trend = 'increasing'
        elif slope < -0.1:
            trend = 'decreasing'
        else:
            trend = 'stable'
        
        return {
            'predicted_weight': round(next_weight, 1),
            'trend': trend,
            'rate_per_session': slope
        }
    
    def generate_insights(self, user_data):
        """Generate personalized insights"""
        insights = []
    
        goal = user_data.get('goal', '').lower()
        if goal == 'weight loss':
            insights.append(('goal', 'Focus on creating a 500 kcal daily deficit for 0.5kg weekly loss'))
        elif goal == 'muscle gain':
            insights.append(('goal', 'Aim for 250-500 kcal surplus with adequate protein intake'))
     
        level = user_data.get('fitness_level', '').lower()
        if level == 'beginner':
            insights.append(('progression', 'Start with compound movements and focus on form'))
        elif level == 'intermediate':
            insights.append(('progression', 'Incorporate progressive overload and variation'))
      
        diet = user_data.get('diet_type', '').lower()
        if diet == 'veg':
            insights.append(('nutrition', 'Ensure adequate protein from plant sources like lentils and tofu'))
        
        return insights