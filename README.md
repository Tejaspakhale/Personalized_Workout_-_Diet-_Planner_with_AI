# 🏋️ Personalized Workout & Diet Planner

A Python-based system that generates customized workout and diet plans using user inputs and basic machine learning.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Tools and Technologies](#tools-and-technologies)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Output](#output)
- [How to Run this Project?](#how-to-run-this-project)
- [Results & Conclusion](#results--conclusion)
- [Future Work](#future-work)
- [Author & Contact](#author--contact)

--- 

## Overview

This project is designed to help users generate personalized workout and diet plans based on their fitness goals, physical details, and preferences. It collects user data, processes it, and produces structured weekly workout routines along with diet suggestions.

---

## Problem Statement 

Most fitness apps give generic workout or diet plans that don’t consider individual student needs, cultural food habits, or available resources. Students require a system that generates personalized routines and meal plans using AI, ensuring they are practical, budget-friendly, and effective. 

---

## Tools and Technologies

- **Python Version:**
  - Python 3
  - pandas

- **Standard Library Modules:**
  - json
  - random
  - datetime
  - typing

- **Machine Learning Libraries:**
  - scikit-learn
  - numpy
  - joblib

---

## Project Structure

```
personalized_workout_diet_planner/
│
├── README.md                  # Project explanation
├── .gitignore                 # Files GitHub should ignore
├── requirements.txt           # Project dependencies
│
├── scripts/
│   ├── main.py                # Entry point (run the project)
│   ├── workout_planner.py     # Handles workout plan generation
│   ├── diet_planner.py        # Handles diet plan generation
│   ├── user_data_manager.py   # Manages user data storage (JSON)
│   └── ml_predictor.py        # Machine learning model for recommendations
│
├── data/
│   └── user_data.json         # Stored user data
│
└── output/
    └── workout_diet_ai_image.png   # Final output image
```

---

## Key Insights

- Uses simple logic to create personalized workout and diet plans
- Works based on user inputs like goal, level, and preferences
- Machine learning adds smarter recommendations
- Stores user data for better future suggestions
- Clean modular structure makes the project easy to understand and extend

---

## Output

- A structured weekly workout plan
- Exercise recommendations based on level and goal
- Stored user data with history tracking

![Personalized Workout & Diet Planner](![alt text](image.png))
---

## How to Run this Project?

- Make sure Python 3 is installed on your system
- Open the project folder in terminal or command prompt
- Install required dependencies using:
- pip install -r requirements.txt
- Run the project using:
- python scripts/main.py
- Enter the required details when prompted
- The personalized workout and diet plan will be displayed in the console

---

## Results & Conclusion

This project is able to generate workout and diet plans based on the user input. It changes the plan according to fitness goal and level, so it feels more useful. The machine learning part also helps to give better suggestions. Overall, this project shows that we can build a simple and helpful fitness planner using Python with proper logic.

---

## Future Work

- Add visualization (images/videos) for exercises to improve user experience
- Improve machine learning model with more data
- Improve the AI model to give more accurate and personalized suggestions

---

## Author & Contact

- **Author:** Tejas Sanjay Pakhale
- 📧 **Email:** pakhaletejas539@gmail.com
- 🔗 **Linkedin:** https://www.linkedin.com/in/tejas-pakhale-41178526 
 
 ---