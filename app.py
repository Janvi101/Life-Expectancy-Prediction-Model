from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load("model.joblib")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded on server.'}), 500
        
    try:
        data = request.json
        
        # Create DataFrame from input to match model's expected format
        input_data = pd.DataFrame([{
            'Schooling': float(data['schooling']),
            'Income composition of resources': float(data['income']),
            'Adult Mortality': float(data['adultMortality']),
            'BMI': float(data['bmi']),
            'Alcohol': float(data['alcohol']),
            'Polio': float(data['polio']),
            'GDP': float(data['gdp'])
        }])
        
        prediction = model.predict(input_data)[0]
        return jsonify({'prediction': round(prediction, 2)})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
