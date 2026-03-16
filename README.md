# Health Risk — Predictive Health Risk Detection

A Machine Learning-powered web application that analyzes your daily lifestyle data to predict potential health risks and deliver personalized recommendations.

## Features

| Feature | Description |
|---------|-------------|
| **ML Risk Assessment** | RandomForest model trained on 70,000+ medical records |
| **501 Disease Analyser** | Rule-based analysis across 27 medical categories |
| **Symptom Checker** | Match symptoms against 25+ disease profiles with recovery plans |
| **Health Tracker** | Log daily diet, exercise, and symptom severity with 7-day charts |
| **Nearby Hospitals** | Google Maps integration to find hospitals & pharmacies |
| **PDF Reports** | Download branded health reports for your doctor |
| **Emergency Alerts** | Auto-notify emergency contacts for high-risk scores |
| **BMI & BP Calculators** | Built-in health calculators |
| **Health Encyclopedia** | Browse disease information and prevention tips |
| **PWA Support** | Install as a Progressive Web App on mobile |

## Tech Stack

- **Backend**: Python 3, Flask, Flask-Mail, Flask-CORS
- **ML**: Scikit-Learn (RandomForest), Pandas, NumPy
- **Database**: PostgreSQL (psycopg2)
- **Maps**: Google Maps API (Places, Geocoding)
- **PDF**: FPDF2
- **Frontend**: Bootstrap 5, Font Awesome, Vanilla JS
- **Auth**: SHA-256 hashed passwords, OTP email verification

## Setup

### 1. Clone & Install
```bash
git clone <repo-url>
cd train_health_risk1.py
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file:
```env
SECRET_KEY=your_secret_key
DB_HOST=localhost
DB_NAME=health_db
DB_USER=postgres
DB_PASS=your_password
DB_PORT=5432
DB_SSLMODE=prefer
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
GOOGLE_MAPS_API_KEY=your_google_maps_key
```

### 3. Database
Create a PostgreSQL database. Tables are auto-created on first run.

### 4. Run
```bash
python app.py
```
Visit `http://localhost:5000`

## Project Structure

```
├── app.py                      # Main Flask application (1680 lines)
├── disease_prediction/
│   ├── disease_predictor.py    # Prediction engine (imports 501 rules)
│   └── disease_rules.py        # 501 disease rules across 27 categories
├── data/                        # 12+ health datasets (CSV)
├── ml_models/                   # Trained ML models (.pkl)
├── templates/
│   ├── base.html               # Base template with navbar/footer
│   ├── home.html               # Landing page
│   ├── auth/                   # Login, Register, Password Reset
│   ├── dashboard/              # User dashboard
│   ├── pages/                  # Symptom checker, Nearby, About, etc.
│   ├── prediction/             # Find Disease form & results
│   └── profile/                # User profile with Google Maps
├── static/                     # CSS, JS, images, manifest
├── .env                        # Environment variables (not committed)
└── requirements.txt            # Python dependencies
```

## How It Works

1. **User enters daily routine data** — sleep, activity, stress, BMI, BP, etc.
2. **ML model predicts risks** — RandomForest classifier processes the input
3. **Rule engine analyses 501 diseases** — Matches user data against condition rules
4. **Results delivered** — Risk score, disease predictions, lifestyle recommendations
5. **PDF report generated** — Downloadable branded health report

## Datasets

12 health datasets in `data/` covering: diabetes risk, heart disease, sleep quality, mental health, BMI analysis, blood pressure, respiratory health, nutrition, exercise, kidney function, liver health, and bone density.

## Disclaimer

This application is for **educational and informational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.
