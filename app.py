from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Age selection landing page
@app.route('/select_age_group')
def landing():
    return render_template('landing.html')

# Main calorie tracker page
@app.route('/calorie_tracker', methods=['GET', 'POST'])
def calorie_tracker():
    if request.method == 'POST':
        name = request.form['name']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        activity_level = request.form['activity']
        age_group = request.form['age_group']
        
        # Calculate calories
        calories = calculate_calories(weight, height, activity_level)
        
        # Redirect to results page with data
        return redirect(url_for('results', name=name, calories=calories, age_group=age_group))
    
    # Default behavior for GET requests
    age_group = request.args.get('age_group', '20-30')  # Default to '20-30' if not specified
    return render_template('index.html', age_group=age_group)

# Results page
@app.route('/results')
def results():
    name = request.args.get('name')
    calories = request.args.get('calories')
    age_group = request.args.get('age_group')
    return render_template('results.html', name=name, calories=calories, age_group=age_group)

# Exercise plan page
@app.route('/exercise_plan')
def exercise_plan():
    return render_template('exercise_plan.html')

# Diet plan page
@app.route('/diet_plan')
def diet_plan():
    return render_template('diet_plan.html')

# Utility function for calculating calories
def calculate_calories(weight, height, activity_level):
    bmr = 10 * weight + 6.25 * height - 5 * 25 + 5  # Default age is 25 for simplicity
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }
    daily_calories = bmr * activity_factors[activity_level]
    calories_to_burn = daily_calories - 500  # 500-calorie deficit for weight loss
    return round(calories_to_burn, 2)

if __name__ == '__main__':
    app.run(debug=True)
