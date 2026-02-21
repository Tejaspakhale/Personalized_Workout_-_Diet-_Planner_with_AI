import json
import os
from datetime import datetime


def load_user_data(filename):
    """Load user data from JSON file"""
    if not os.path.exists(filename):
        return None
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️  Error loading user data: {e}")
        return None


def save_user_data(filename, user_data):
    """Save user data to JSON file with history tracking"""
    existing_data = load_user_data(filename)
  
    history_entry = {
        "date": datetime.now().isoformat(),
        "weight": user_data.get('weight'),
        "fitness_level": user_data.get('fitness_level'),
        "goal": user_data.get('goal')
    }
    
    if existing_data:
        existing_data.update(user_data)
     
        if 'history' not in existing_data:
            existing_data['history'] = []
        existing_data['history'].append(history_entry)
    
        if len(existing_data['history']) > 50:
            existing_data['history'] = existing_data['history'][-50:]
        
        data_to_save = existing_data
    else:
        user_data['history'] = [history_entry]
        data_to_save = user_data
 
    data_to_save['last_modified'] = datetime.now().isoformat()
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"⚠️  Error saving user data: {e}")
        return False


def get_user_profile(filename):
    """Get user profile from JSON file"""
    return load_user_data(filename)


def delete_user_data(filename):
    """Delete user data file"""
    if os.path.exists(filename):
        try:
            os.remove(filename)
            return True
        except OSError as e:
            print(f"⚠️  Error deleting user data: {e}")
            return False
    return False


def export_user_data(filename, export_filename):
    """Export user data to a different file"""
    data = load_user_data(filename)
    if data:
        try:
            with open(export_filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"⚠️  Error exporting user data: {e}")
            return False
    return False


def get_progress_summary(filename):
    """Get a summary of user's progress over time"""
    data = load_user_data(filename)
    
    if not data or 'history' not in data or len(data['history']) < 2:
        return None
    
    history = data['history']
 
    first_weight = history[0]['weight']
    current_weight = history[-1]['weight']
    weight_change = current_weight - first_weight
   
    first_date = datetime.fromisoformat(history[0]['date'])
    current_date = datetime.fromisoformat(history[-1]['date'])
    days_tracked = (current_date - first_date).days
  
    first_level = history[0]['fitness_level']
    current_level = history[-1]['fitness_level']
    level_changed = first_level != current_level
    
    summary = {
        "total_sessions": len(history),
        "days_tracked": days_tracked,
        "weight_change": weight_change,
        "first_weight": first_weight,
        "current_weight": current_weight,
        "fitness_level_progression": {
            "initial": first_level,
            "current": current_level,
            "changed": level_changed
        },
        "first_date": first_date.strftime("%Y-%m-%d"),
        "current_date": current_date.strftime("%Y-%m-%d")
    }
    
    return summary


def update_user_preferences(filename, preferences):
    """Update specific user preferences without changing entire profile"""
    data = load_user_data(filename)
    
    if not data:
        return False
  
    for key, value in preferences.items():
        data[key] = value
   
    return save_user_data(filename, data)


def get_user_statistics(filename):
    """Get statistical insights from user data"""
    data = load_user_data(filename)
    
    if not data or 'history' not in data:
        return None
    
    history = data['history']
    
    if len(history) < 2:
        return None
  
    weights = [entry['weight'] for entry in history if 'weight' in entry]
    
    if len(weights) < 2:
        return None
 
    weight_changes = [weights[i] - weights[i-1] for i in range(1, len(weights))]
    avg_weight_change = sum(weight_changes) / len(weight_changes)
    
    statistics = {
        "total_entries": len(history),
        "weight_history": weights,
        "average_weight_change_per_session": round(avg_weight_change, 2),
        "total_weight_change": round(weights[-1] - weights[0], 2),
        "min_weight": min(weights),
        "max_weight": max(weights),
        "current_weight": weights[-1]
    }
    
    return statistics


def validate_user_data(user_data):
    """Validate user data before saving"""
    required_fields = [
        'name', 'age', 'gender', 'weight', 'height', 
        'goal', 'diet_type', 'fitness_level'
    ]
    
    for field in required_fields:
        if field not in user_data:
            return False, f"Missing required field: {field}"

    if not isinstance(user_data['age'], int) or user_data['age'] < 10 or user_data['age'] > 100:
        return False, "Age must be between 10 and 100"
    
    if not isinstance(user_data['weight'], (int, float)) or user_data['weight'] <= 0:
        return False, "Weight must be a positive number"
    
    if not isinstance(user_data['height'], (int, float)) or user_data['height'] <= 0:
        return False, "Height must be a positive number"
    
    return True, "Valid"


def create_backup(filename, backup_folder="backups"):
    """Create a backup of user data"""
    if not os.path.exists(filename):
        return False
    
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(backup_folder, f"user_data_backup_{timestamp}.json")
    
    return export_user_data(filename, backup_filename)
