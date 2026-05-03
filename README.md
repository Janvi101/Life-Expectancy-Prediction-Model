# Life Expectancy Prediction System

This project is a machine learning web application that predicts a country's life expectancy based on key socio-economic and health factors. It uses a Linear Regression model trained on WHO data, wrapped in a Flask backend with a modern, glassmorphism UI.

## Local Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model (Optional):**
   If you want to retrain the model, run:
   ```bash
   python train.py
   ```

3. **Run the web application:**
   ```bash
   python app.py
   ```
   Then navigate to `http://localhost:5000` in your web browser.

## Deployment Instructions

### Docker (Recommended for Universal Deployment)
You can easily deploy the application anywhere using Docker.
1. Build the Docker image:
   ```bash
   docker build -t life-expectancy-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 life-expectancy-app
   ```
3. Open your browser and navigate to `http://localhost:5000`.

### Render (Recommended for Free Hosting)
1. Push this code to a GitHub repository.
2. Sign up on [Render](https://render.com) and create a new **Web Service**.
3. Connect your GitHub repository.
4. Set the **Build Command** to: `pip install -r requirements.txt`
5. Set the **Start Command** to: `gunicorn app:app`
6. Click **Create Web Service**.

### Heroku
1. Install the Heroku CLI and login.
2. Run `heroku create` in the project directory.
3. Push to Heroku: `git push heroku master`
4. Scale the dyno: `heroku ps:scale web=1`
5. Open your app: `heroku open`

## Features Used
- **Schooling:** Number of years of Schooling.
- **Income Composition:** Human Development Index in terms of income composition of resources (index ranging from 0 to 1).
- **Adult Mortality:** Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population).
- **HIV/AIDS:** Deaths per 1000 live births HIV/AIDS (0-4 years).
- **BMI:** Average Body Mass Index of entire population.
