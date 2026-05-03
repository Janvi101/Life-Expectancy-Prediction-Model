# 🌟 Life Expectancy AI

![Life Expectancy AI Banner](banner.png)

## 📖 Overview

**Life Expectancy AI** is a state-of-the-art machine learning web application designed to predict a country's life expectancy based on key socio-economic and health indicators. Built with a sleek **glassmorphism** UI and a robust **Flask** backend, this tool leverages global health data to provide instant, data-driven insights.

## 🚀 Key Features

The model analyzes several critical factors to generate its predictions:

-   📚 **Schooling:** Average number of years of education.
-   💰 **Income Composition:** Human Development Index in terms of resource composition.
-   📉 **Adult Mortality:** Probability of dying between 15 and 60 years per 1000 population.
-   💪 **BMI:** Average Body Mass Index of the entire population.
-   🍷 **Alcohol:** Per capita (15+) consumption (in liters of pure alcohol).
-   💉 **Polio:** Polio (Pol3) immunization coverage among 1-year-olds (%).
-   📈 **GDP:** Gross Domestic Product per capita (in USD).

## 🛠️ Tech Stack

-   **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
-   **Machine Learning:** [Scikit-learn](https://scikit-learn.org/), [Pandas](https://pandas.pydata.org/), [Joblib](https://joblib.readthedocs.io/)
-   **Frontend:** HTML5, CSS3 (Glassmorphism design), JavaScript
-   **Deployment:** Docker, Gunicorn, Heroku/Render support

## 💻 Local Setup

Get the project running on your local machine in minutes:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Life-Expectancy-Prediction-Model.git
    cd Life-Expectancy-Prediction-Model
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Train the model (Optional):**
    ```bash
    python train.py
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
    Visit `http://localhost:5000` in your browser.

## 🐳 Docker Deployment

For a consistent environment across any platform:

1.  **Build the image:**
    ```bash
    docker build -t life-expectancy-ai .
    ```

2.  **Launch the container:**
    ```bash
    docker run -d -p 5000:5000 life-expectancy-ai
    ```

## 🌐 Cloud Deployment

### Render / Heroku
-   **Build Command:** `pip install -r requirements.txt`
-   **Start Command:** `gunicorn app:app`

## 📂 Project Structure

```text
├── app.py              # Flask server & API routes
├── train.py            # Model training & evaluation script
├── data.csv            # WHO Life Expectancy dataset
├── model.joblib        # Trained Scikit-learn model
├── Dockerfile          # Container configuration
├── Procfile            # Deployment script for Heroku
├── requirements.txt    # Python dependencies
├── static/             # CSS and JavaScript assets
└── templates/          # HTML templates (index.html)
```

---
*Developed with ❤️ for global health data analysis.*
