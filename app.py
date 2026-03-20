"""
=================================================================================
COMPLETE HEALTH RISK PREDICTION SYSTEM - INTEGRATED VERSION
=================================================================================
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash, make_response
from flask_cors import CORS
import hashlib
from datetime import datetime, date
import json
from flask_mail import Mail, Message
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import pickle
import numpy as np
import os
from dotenv import load_dotenv
from io import BytesIO
import psycopg  # instead of import psycopg2

# =============================================================================
# DISEASE PREDICTOR — flexible import (subfolder OR root)
# =============================================================================
try:
    from disease_prediction.disease_predictor import get_top_diseases, get_by_category  # type: ignore
    print("✅ Disease Predictor Loaded from disease_prediction/")
except ImportError:
    try:
        from disease_predictor import get_top_diseases, get_by_category  # type: ignore
        print("✅ Disease Predictor Loaded from root")
    except ImportError:
        print("❌ Disease Predictor NOT found — /find-disease will show error")
        get_top_diseases = None
        get_by_category  = None

load_dotenv()

# =============================================================================
# FLASK APP
# =============================================================================
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key_change_in_production')

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

# =============================================================================
# BP ESTIMATOR
# =============================================================================
try:
    from bp_estimator import estimate_blood_pressure, interpret_bp_result  # type: ignore
    BP_ESTIMATOR_AVAILABLE = True
    print("✅ BP Estimator Loaded Successfully")
except ImportError:
    BP_ESTIMATOR_AVAILABLE = False
    print("⚠️  BP Estimator not available")
except Exception as e:
    BP_ESTIMATOR_AVAILABLE = False
    print(f"⚠️  BP Estimator error: {e}")

# =============================================================================
# DATABASE
# =============================================================================
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME,
            user=DB_USER, password=DB_PASS,
            port=os.getenv('DB_PORT', '5432'),
            sslmode=os.getenv('DB_SSLMODE', 'prefer')
        )
        return conn
    except Exception as e:
        print(f"❌ DB Connection Error: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if not conn:
        print("❌ Database setup skipped.")
        return
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY, name TEXT, email TEXT UNIQUE,
            password TEXT, age INTEGER, emergency_contact TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS assessments (
            id SERIAL PRIMARY KEY, user_id INTEGER,
            bp_sys INTEGER, bp_dias INTEGER,
            bp_estimated BOOLEAN DEFAULT FALSE, bp_confidence INTEGER,
            glucose REAL, bmi REAL, smoking INTEGER, alcohol TEXT,
            sleep_hours REAL, screen_time REAL, activity_mins INTEGER,
            stress_level INTEGER, risk_heart_rate TEXT, risk_diabetes TEXT,
            risk_hypertension TEXT, risk_sleep_apnea TEXT, risk_anxiety TEXT,
            risk_obesity TEXT, overall_score INTEGER, overall_risk TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY, user_id INTEGER, name TEXT,
            rating INTEGER, comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS recovery_logs (
            id SERIAL PRIMARY KEY, user_id INTEGER, disease_name TEXT,
            date DATE, diet_quality INTEGER, exercise_mins INTEGER,
            symptom_severity INTEGER, notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        print("✅ Database Initialized Successfully")
    except Exception as e:
        print(f"❌ Database initialization error: {e}")
        conn.rollback()
    finally:
        conn.close()

# =============================================================================
# ML MODEL
# =============================================================================
try:
    with open('health_model.pkl', 'rb') as f:
        artifacts     = pickle.load(f)
        ml_model      = artifacts['model']
        label_encoder = artifacts['encoder']
    print("✅ ML Model Loaded")
except FileNotFoundError:
    print("⚠️  health_model.pkl not found. Using rule-based fallback.")
    ml_model = None; label_encoder = None
except Exception as e:
    print(f"⚠️  ML Model loading error: {e}")
    ml_model = None; label_encoder = None

# =============================================================================
# HEALTH KNOWLEDGE BASE
# =============================================================================
HEALTH_KNOWLEDGE_BASE = {
    'Diabetes Type 2': {
        'title': 'Type 2 Diabetes', 'icon': 'fa-tint', 'color': 'warning',
        'symptoms': ['Thirst', 'Frequent Urination', 'Blurry Vision', 'Fatigue', 'Slow Healing Wounds', 'Tingling in Hands'],
        'struggle': 'Energy crashes, dizziness, constant hunger.',
        'daily_plan': {
            'Phase 1': 'Strict Low Carb Diet. 15 mins walking.',
            'Phase 2': 'Intermittent Fasting (16:8).',
            'Phase 3': 'Strength training 3x week.'
        },
        'recovery': {
            'yoga': [{'name': 'Kapalbhati'}, {'name': 'Dhanurasana'}],
            'diet': {'good': ['Leafy Greens', 'Bitter Gourd', 'Whole Grains'], 'bad': ['Sugar', 'White Rice', 'Soda']}
        }
    },
    'Heart Disease': {
        'title': 'Heart Disease', 'icon': 'fa-heartbeat', 'color': 'danger',
        'symptoms': ['Chest Pain', 'Shortness of Breath', 'Palpitations', 'Fatigue', 'Swelling in Legs', 'Dizziness'],
        'struggle': 'Difficulty climbing stairs, tiredness.',
        'daily_plan': {
            'Phase 1': 'Complete Rest. No salt.',
            'Phase 2': 'Light Yoga (Pranayama).',
            'Phase 3': 'Brisk walking 45 mins.'
        },
        'recovery': {
            'yoga': [{'name': 'Tadasana'}, {'name': 'Shavasana'}],
            'diet': {'good': ['Oats', 'Salmon', 'Berries'], 'bad': ['Fried foods', 'Salt', 'Red Meat']}
        }
    },
    'Sleep Insomnia': {
        'title': 'Insomnia', 'icon': 'fa-bed', 'color': 'primary',
        'symptoms': ["Can't Sleep", 'Irritability', 'Headaches', 'Focus issues', 'Daytime Drowsiness', 'Mood Swings'],
        'struggle': 'Chronic fatigue, brain fog.',
        'daily_plan': {
            'Phase 1': 'No Screens after 8 PM.',
            'Phase 2': 'Wake up at same time daily.',
            'Phase 3': 'Magnesium supplements.'
        },
        'recovery': {
            'yoga': [{'name': 'Yoga Nidra'}, {'name': 'Viparita Karani'}],
            'diet': {'good': ['Warm Milk', 'Almonds', 'Chamomile Tea'], 'bad': ['Caffeine', 'Alcohol', 'Heavy Meals']}
        }
    },
    'Hypertension': {
        'title': 'Hypertension', 'icon': 'fa-tachometer-alt', 'color': 'danger',
        'symptoms': ['Headache', 'Nosebleed', 'Vision issues', 'Chest pain', 'Dizziness', 'Ringing in Ears'],
        'struggle': 'Dizziness, flushing.',
        'daily_plan': {
            'Phase 1': 'DASH Diet (Low Sodium).',
            'Phase 2': 'Slow breathing exercises.',
            'Phase 3': 'Weight management.'
        },
        'recovery': {
            'yoga': [{'name': 'Balasana'}, {'name': 'Sukhasana'}],
            'diet': {'good': ['Bananas', 'Beetroot', 'Spinach'], 'bad': ['Pickles', 'Salt', 'Canned Food']}
        }
    },
    'Migraine': {
        'title': 'Migraine', 'icon': 'fa-brain', 'color': 'info',
        'symptoms': ['Throbbing Headache', 'Sensitivity to Light', 'Nausea', 'Aura', 'Sensitivity to Sound'],
        'struggle': 'Cannot tolerate light/sound.',
        'daily_plan': {
            'Phase 1': 'Dark room rest. Hydration.',
            'Phase 2': 'Avoid caffeine/chocolate.',
            'Phase 3': 'Regular sleep schedule.'
        },
        'recovery': {
            'yoga': [{'name': 'Shishuasana'}, {'name': 'Setu Bandhasana'}],
            'diet': {'good': ['Ginger Tea', 'Water', 'Magnesium-rich foods'], 'bad': ['Cheese', 'Wine', 'Chocolate']}
        }
    },
    'Obesity': {
        'title': 'Obesity', 'icon': 'fa-weight', 'color': 'warning',
        'symptoms': ['Breathlessness', 'Joint pain', 'Snoring', 'Excessive Sweating', 'Back Pain', 'Low Energy'],
        'struggle': 'Low stamina, body pain.',
        'daily_plan': {
            'Phase 1': 'Calorie Deficit. High Protein.',
            'Phase 2': '10k Steps Daily.',
            'Phase 3': 'Strength Training.'
        },
        'recovery': {
            'yoga': [{'name': 'Surya Namaskar'}, {'name': 'Virabhadrasana'}],
            'diet': {'good': ['High Protein', 'Fiber', 'Green Vegetables'], 'bad': ['Sugary drinks', 'Junk Food', 'Processed Food']}
        }
    },
    'Common Cold': {
        'title': 'Common Cold', 'icon': 'fa-snowflake', 'color': 'info',
        'symptoms': ['Runny Nose', 'Sore Throat', 'Fever', 'Cough', 'Sneezing', 'Body Aches'],
        'struggle': 'Weakness, congestion.',
        'daily_plan': {
            'Phase 1': 'Bed rest. Ginger tea.',
            'Phase 2': 'Steam inhalation.',
            'Phase 3': 'Vitamin C supplements.'
        },
        'recovery': {
            'yoga': [{'name': 'Matsyasana'}, {'name': 'Viparita Karani'}],
            'diet': {'good': ['Soup', 'Garlic', 'Honey'], 'bad': ['Cold drinks', 'Dairy', 'Fried Food']}
        }
    },
    'Asthma': {
        'title': 'Asthma', 'icon': 'fa-lungs', 'color': 'warning',
        'symptoms': ['Wheezing', 'Shortness of Breath', 'Chest Tightness', 'Cough', 'Difficulty Breathing at Night'],
        'struggle': 'Breathing difficulty during exercise or cold weather.',
        'daily_plan': {
            'Phase 1': 'Avoid triggers (dust, smoke, pollen).',
            'Phase 2': 'Use prescribed inhaler. Breathing exercises.',
            'Phase 3': 'Gradual physical activity increase.'
        },
        'recovery': {
            'yoga': [{'name': 'Pranayama'}, {'name': 'Sukhasana'}],
            'diet': {'good': ['Ginger', 'Turmeric', 'Omega-3 Fish'], 'bad': ['Sulfite foods', 'Cold drinks', 'Processed food']}
        }
    },
    'Anxiety Disorder': {
        'title': 'Anxiety Disorder', 'icon': 'fa-brain', 'color': 'warning',
        'symptoms': ['Restlessness', 'Rapid Heartbeat', 'Excessive Worry', 'Muscle Tension', 'Panic Attacks', 'Difficulty Concentrating'],
        'struggle': 'Constant worry, difficulty relaxing.',
        'daily_plan': {
            'Phase 1': 'Deep breathing exercises. Limit news.',
            'Phase 2': 'CBT journaling. Regular exercise.',
            'Phase 3': 'Meditation 20 mins daily.'
        },
        'recovery': {
            'yoga': [{'name': 'Shavasana'}, {'name': 'Balasana'}],
            'diet': {'good': ['Green Tea', 'Dark Chocolate', 'Salmon'], 'bad': ['Caffeine', 'Alcohol', 'Sugar']}
        }
    },
    'Depression': {
        'title': 'Depression', 'icon': 'fa-cloud-rain', 'color': 'primary',
        'symptoms': ['Persistent Sadness', 'Loss of Interest', 'Fatigue', 'Sleep Changes', 'Appetite Changes', 'Difficulty Concentrating'],
        'struggle': 'No motivation, emotional numbness.',
        'daily_plan': {
            'Phase 1': 'Reach out to someone. Walk 10 mins.',
            'Phase 2': 'Establish routine. Sunlight exposure.',
            'Phase 3': 'Regular exercise. Social activities.'
        },
        'recovery': {
            'yoga': [{'name': 'Surya Namaskar'}, {'name': 'Viparita Karani'}],
            'diet': {'good': ['Omega-3 foods', 'Nuts', 'Berries'], 'bad': ['Alcohol', 'Processed food', 'Excessive sugar']}
        }
    },
    'Chronic Back Pain': {
        'title': 'Chronic Back Pain', 'icon': 'fa-procedures', 'color': 'danger',
        'symptoms': ['Lower Back Pain', 'Stiffness', 'Muscle Spasms', 'Radiating Leg Pain', 'Difficulty Standing'],
        'struggle': 'Cannot sit or stand for long periods.',
        'daily_plan': {
            'Phase 1': 'Hot/cold therapy. Gentle stretching.',
            'Phase 2': 'Core strengthening exercises.',
            'Phase 3': 'Ergonomic workspace setup.'
        },
        'recovery': {
            'yoga': [{'name': 'Bhujangasana'}, {'name': 'Marjaryasana'}],
            'diet': {'good': ['Anti-inflammatory foods', 'Calcium-rich food', 'Turmeric'], 'bad': ['Processed food', 'Sugary drinks', 'Excessive sitting']}
        }
    },
    'Arthritis': {
        'title': 'Arthritis', 'icon': 'fa-bone', 'color': 'warning',
        'symptoms': ['Joint pain', 'Joint Swelling', 'Stiffness', 'Reduced Range of Motion', 'Joint Redness'],
        'struggle': 'Morning stiffness, difficulty with daily tasks.',
        'daily_plan': {
            'Phase 1': 'Gentle joint mobilization. Anti-inflammatory diet.',
            'Phase 2': 'Low-impact exercise (swimming, cycling).',
            'Phase 3': 'Strength training around joints.'
        },
        'recovery': {
            'yoga': [{'name': 'Virabhadrasana'}, {'name': 'Trikonasana'}],
            'diet': {'good': ['Fish', 'Olive Oil', 'Berries'], 'bad': ['Red Meat', 'Sugar', 'Fried Food']}
        }
    },
    'GERD (Acid Reflux)': {
        'title': 'GERD / Acid Reflux', 'icon': 'fa-fire', 'color': 'danger',
        'symptoms': ['Heartburn', 'Acid Taste in Mouth', 'Difficulty Swallowing', 'Chest Pain After Eating', 'Bloating'],
        'struggle': 'Burning sensation after meals, disrupted sleep.',
        'daily_plan': {
            'Phase 1': 'Elevate head while sleeping. Small meals.',
            'Phase 2': 'Avoid trigger foods. No eating 3hrs before bed.',
            'Phase 3': 'Weight management. Stress reduction.'
        },
        'recovery': {
            'yoga': [{'name': 'Vajrasana'}, {'name': 'Pawanmuktasana'}],
            'diet': {'good': ['Banana', 'Oatmeal', 'Green Vegetables'], 'bad': ['Spicy Food', 'Citrus', 'Coffee']}
        }
    },
    'Anemia': {
        'title': 'Anemia', 'icon': 'fa-tint', 'color': 'danger',
        'symptoms': ['Fatigue', 'Pale Skin', 'Dizziness', 'Cold Hands and Feet', 'Brittle Nails', 'Shortness of Breath'],
        'struggle': 'Extreme tiredness, weakness.',
        'daily_plan': {
            'Phase 1': 'Iron-rich diet. Vitamin C with meals.',
            'Phase 2': 'Iron supplements (if prescribed).',
            'Phase 3': 'Regular blood tests. Moderate exercise.'
        },
        'recovery': {
            'yoga': [{'name': 'Pranayama'}, {'name': 'Shavasana'}],
            'diet': {'good': ['Spinach', 'Lentils', 'Red Meat', 'Pomegranate'], 'bad': ['Tea with meals', 'Calcium with iron', 'Junk food']}
        }
    },
    'Thyroid Disorder': {
        'title': 'Thyroid Disorder', 'icon': 'fa-procedures', 'color': 'warning',
        'symptoms': ['Weight Changes', 'Fatigue', 'Hair Loss', 'Mood Swings', 'Temperature Sensitivity', 'Neck Swelling'],
        'struggle': 'Unexplained weight gain/loss, constant tiredness.',
        'daily_plan': {
            'Phase 1': 'Get thyroid panel tested. Medication.',
            'Phase 2': 'Balanced iodine diet. Regular exercise.',
            'Phase 3': 'Stress management. Regular monitoring.'
        },
        'recovery': {
            'yoga': [{'name': 'Sarvangasana'}, {'name': 'Halasana'}],
            'diet': {'good': ['Iodized Salt', 'Selenium-rich foods', 'Coconut Oil'], 'bad': ['Soy products', 'Gluten (if sensitive)', 'Processed food']}
        }
    },
    'Kidney Disease': {
        'title': 'Chronic Kidney Disease', 'icon': 'fa-kidneys', 'color': 'danger',
        'symptoms': ['Swelling in Legs', 'Frequent Urination', 'Fatigue', 'Nausea', 'Back Pain', 'Foamy Urine'],
        'struggle': 'Fluid retention, exhaustion.',
        'daily_plan': {
            'Phase 1': 'Low sodium, low potassium diet.',
            'Phase 2': 'Monitor BP and blood sugar strictly.',
            'Phase 3': 'Regular kidney function tests.'
        },
        'recovery': {
            'yoga': [{'name': 'Ardha Matsyendrasana'}, {'name': 'Bhujangasana'}],
            'diet': {'good': ['Cabbage', 'Bell Peppers', 'Cauliflower'], 'bad': ['High-potassium foods', 'Processed Meat', 'Excessive protein']}
        }
    },
    'UTI (Urinary Tract Infection)': {
        'title': 'Urinary Tract Infection', 'icon': 'fa-thermometer', 'color': 'warning',
        'symptoms': ['Burning Urination', 'Frequent Urination', 'Cloudy Urine', 'Lower Abdominal Pain', 'Fever'],
        'struggle': 'Pain and urgency disrupting daily life.',
        'daily_plan': {
            'Phase 1': 'Drink 3L water daily. See doctor.',
            'Phase 2': 'Complete antibiotic course.',
            'Phase 3': 'Probiotics. Cranberry juice.'
        },
        'recovery': {
            'yoga': [{'name': 'Malasana'}, {'name': 'Supta Baddha Konasana'}],
            'diet': {'good': ['Water', 'Cranberry', 'Probiotics'], 'bad': ['Caffeine', 'Alcohol', 'Spicy Food']}
        }
    },
    'PCOS': {
        'title': 'Polycystic Ovary Syndrome', 'icon': 'fa-female', 'color': 'warning',
        'symptoms': ['Irregular Periods', 'Weight Gain', 'Acne', 'Hair Loss', 'Excessive Hair Growth', 'Mood Swings'],
        'struggle': 'Hormonal imbalance, fertility concerns.',
        'daily_plan': {
            'Phase 1': 'Anti-inflammatory, low glycemic diet.',
            'Phase 2': 'Regular exercise 45 mins daily.',
            'Phase 3': 'Hormone management with doctor.'
        },
        'recovery': {
            'yoga': [{'name': 'Butterfly Pose'}, {'name': 'Supta Baddha Konasana'}],
            'diet': {'good': ['Whole grains', 'Lean protein', 'Berries'], 'bad': ['Refined carbs', 'Sugar', 'Dairy']}
        }
    },
    'Bronchitis': {
        'title': 'Bronchitis', 'icon': 'fa-lungs', 'color': 'warning',
        'symptoms': ['Persistent Cough', 'Mucus Production', 'Chest Discomfort', 'Fatigue', 'Sore Throat', 'Body Aches'],
        'struggle': 'Constant coughing, difficulty breathing.',
        'daily_plan': {
            'Phase 1': 'Rest. Steam inhalation. Fluids.',
            'Phase 2': 'Prescribed medications. Avoid irritants.',
            'Phase 3': 'Gradual activity increase. No smoking.'
        },
        'recovery': {
            'yoga': [{'name': 'Pranayama'}, {'name': 'Ustrasana'}],
            'diet': {'good': ['Honey', 'Ginger', 'Warm Fluids'], 'bad': ['Smoking', 'Cold Foods', 'Dairy']}
        }
    },
    'Gastric Ulcer': {
        'title': 'Gastric Ulcer', 'icon': 'fa-stomach', 'color': 'danger',
        'symptoms': ['Stomach Pain', 'Bloating', 'Nausea', 'Loss of Appetite', 'Heartburn', 'Dark Stool'],
        'struggle': 'Stomach pain worsened by eating.',
        'daily_plan': {
            'Phase 1': 'Bland diet. Small frequent meals.',
            'Phase 2': 'Take prescribed antacids/PPIs.',
            'Phase 3': 'Stress management. Avoid NSAIDs.'
        },
        'recovery': {
            'yoga': [{'name': 'Vajrasana'}, {'name': 'Pawanmuktasana'}],
            'diet': {'good': ['Bananas', 'Cabbage Juice', 'Probiotics'], 'bad': ['Spicy Food', 'Alcohol', 'Coffee']}
        }
    },
    'Eye Strain': {
        'title': 'Digital Eye Strain', 'icon': 'fa-eye', 'color': 'info',
        'symptoms': ['Eye Pain', 'Blurry Vision', 'Headaches', 'Dry Eyes', 'Neck Pain', 'Difficulty Focusing'],
        'struggle': 'Cannot work long hours on screen.',
        'daily_plan': {
            'Phase 1': '20-20-20 rule (every 20 min, look 20 ft away for 20 sec).',
            'Phase 2': 'Blue light filter glasses. Proper lighting.',
            'Phase 3': 'Eye exercises. Reduce screen time to < 6 hrs.'
        },
        'recovery': {
            'yoga': [{'name': 'Trataka'}, {'name': 'Palming'}],
            'diet': {'good': ['Carrots', 'Fish', 'Eggs'], 'bad': ['Excessive screen time', 'Dim lighting', 'Dehydration']}
        }
    },
    'Dehydration': {
        'title': 'Dehydration', 'icon': 'fa-tint', 'color': 'warning',
        'symptoms': ['Thirst', 'Dark Urine', 'Dizziness', 'Fatigue', 'Dry Mouth', 'Headaches'],
        'struggle': 'Weakness, dry skin, low energy.',
        'daily_plan': {
            'Phase 1': 'Drink 3L water daily. Electrolytes.',
            'Phase 2': 'Eat water-rich fruits and vegetables.',
            'Phase 3': 'Set hydration reminders.'
        },
        'recovery': {
            'yoga': [{'name': 'Shavasana'}, {'name': 'Sukhasana'}],
            'diet': {'good': ['Water', 'Watermelon', 'Coconut Water', 'Cucumber'], 'bad': ['Caffeine', 'Alcohol', 'Salty food']}
        }
    },
    'Vitamin D Deficiency': {
        'title': 'Vitamin D Deficiency', 'icon': 'fa-sun', 'color': 'warning',
        'symptoms': ['Fatigue', 'Bone Pain', 'Muscle Weakness', 'Depression', 'Hair Loss', 'Slow Healing Wounds'],
        'struggle': 'Tired constantly, weak bones.',
        'daily_plan': {
            'Phase 1': '20 mins sunlight daily (morning).',
            'Phase 2': 'Vitamin D supplements (as prescribed).',
            'Phase 3': 'Calcium + Vitamin D rich diet.'
        },
        'recovery': {
            'yoga': [{'name': 'Surya Namaskar'}, {'name': 'Tadasana'}],
            'diet': {'good': ['Fatty Fish', 'Egg Yolks', 'Fortified Milk'], 'bad': ['Indoor lifestyle', 'Excessive sunscreen', 'Processed food']}
        }
    },
    'Sleep Apnea': {
        'title': 'Sleep Apnea', 'icon': 'fa-bed', 'color': 'danger',
        'symptoms': ['Loud Snoring', 'Gasping During Sleep', 'Daytime Drowsiness', 'Morning Headaches', 'Irritability'],
        'struggle': 'Disturbed sleep, daytime fatigue.',
        'daily_plan': {
            'Phase 1': 'Sleep on side. Avoid alcohol before bed.',
            'Phase 2': 'CPAP machine (if prescribed). Weight loss.',
            'Phase 3': 'Regular sleep schedule. Throat exercises.'
        },
        'recovery': {
            'yoga': [{'name': 'Pranayama'}, {'name': 'Simhasana'}],
            'diet': {'good': ['Anti-inflammatory foods', 'Lean protein', 'Fruits'], 'bad': ['Alcohol', 'Sedatives', 'Heavy meals at night']}
        }
    },
    'Pneumonia Risk': {
        'title': 'Pneumonia', 'icon': 'fa-lungs', 'color': 'danger',
        'symptoms': ['High Fever', 'Cough', 'Difficulty Breathing', 'Chest Pain', 'Chills', 'Fatigue'],
        'struggle': 'Severe breathing difficulty, high fever.',
        'daily_plan': {
            'Phase 1': 'Immediate medical attention. Rest.',
            'Phase 2': 'Complete antibiotic course. Fluids.',
            'Phase 3': 'Gradual recovery. Breathing exercises.'
        },
        'recovery': {
            'yoga': [{'name': 'Pranayama'}, {'name': 'Bhujangasana'}],
            'diet': {'good': ['Warm Soup', 'Honey', 'Citrus Fruits'], 'bad': ['Cold Foods', 'Smoking', 'Dairy']}
        }
    },
}

# =============================================================================
# HEALTH PREDICTOR ENGINE
# =============================================================================
class HealthPredictor:
    def predict(self, data):
        risks = {}
        score = 0
        if data.get('bmi', 0) > 30:
            risks['obesity'] = {'level': 'High', 'color': 'red'}; score += 15
        if data.get('bp_sys', 120) > 140:
            risks['hypertension'] = {'level': 'High', 'color': 'red'}; score += 20
        elif data.get('bp_sys', 120) > 130:
            risks['hypertension'] = {'level': 'Medium', 'color': 'orange'}; score += 10
        if data.get('stress', 0) > 7:
            risks['mental'] = {'level': 'High', 'color': 'orange'}; score += 15
        if data.get('sleep_hours', 7) < 6:
            risks['sleep'] = {'level': 'High', 'color': 'red'}; score += 15
        if ml_model and label_encoder:
            try:
                df = pd.DataFrame([{
                    'age': data.get('age', 30), 'bmi': data.get('bmi', 25),
                    'sleep_hours': data.get('sleep_hours', 7),
                    'activity_mins': data.get('activity_mins', 30),
                    'stress_level': data.get('stress', 5),
                    'bp_sys': data.get('bp_sys', 120), 'bp_dias': data.get('bp_dias', 80),
                    'screen_time': data.get('screen_time', 6)
                }])
                pred = label_encoder.inverse_transform([ml_model.predict(df)[0]])[0]
                if pred == 'Diabetes Type 2':
                    risks['diabetes'] = {'level': 'High', 'color': 'red'}; score += 25
                elif pred == 'Heart Disease':
                    risks['heart'] = {'level': 'High', 'color': 'red'}; score += 30
                elif pred == 'Sleep Insomnia':
                    risks['sleep'] = {'level': 'High', 'color': 'red'}; score += 20
            except Exception as e:
                print(f"ML prediction error: {e}")
        for risk_type in ['diabetes', 'heart', 'sleep', 'hypertension', 'obesity', 'mental']:
            if risk_type not in risks:
                risks[risk_type] = {'level': 'Low', 'color': 'green'}
        return risks, min(score + 10, 100), {}

predictor = HealthPredictor()

# =============================================================================
# MAIL
# =============================================================================
app.config['MAIL_SERVER']  = 'smtp.gmail.com'
app.config['MAIL_PORT']    = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
mail = Mail(app)

# =============================================================================
# ROUTES — AUTHENTICATION
# =============================================================================
@app.route('/')
def home():
    return render_template('home.html')

# =============================================================================
# ROUTES — FORGOT PASSWORD (OTP via Email)
# =============================================================================
import random

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        conn  = get_db_connection()
        user  = None
        if conn:
            try:
                c = conn.cursor()
                c.execute("SELECT id, name FROM users WHERE LOWER(email)=%s", (email,))
                user = c.fetchone()
            finally:
                conn.close()
        if user:
            otp = str(random.randint(100000, 999999))
            session['otp']            = otp
            session['otp_email']      = email
            session['otp_user_id']    = user[0]
            session['otp_user_name']  = user[1]
            try:
                msg = Message(
                    subject='HealthPredict AI — Password Reset OTP',
                    sender=os.getenv('MAIL_USERNAME'),
                    recipients=[email]
                )
                msg.html = f"""
                <div style="font-family:Inter,Arial,sans-serif;max-width:520px;margin:auto;border:1px solid #e2e8f0;border-radius:16px;overflow:hidden">
                    <div style="background:linear-gradient(135deg,#312e81,#4c1d95);padding:28px;text-align:center">
                        <h2 style="color:white;margin:0">&#128274; Password Reset</h2>
                    </div>
                    <div style="padding:28px">
                        <p>Hi <strong>{user[1]}</strong>,</p>
                        <p>Use this one-time code to reset your password:</p>
                        <div style="background:#f8fafc;border:2px solid #7c3aed;border-radius:12px;padding:24px;text-align:center;margin:20px 0">
                            <span style="font-size:2.5rem;font-weight:900;letter-spacing:0.2em;color:#7c3aed">{otp}</span>
                        </div>
                        <p style="color:#64748b;font-size:14px">This code is valid for <strong>10 minutes</strong>.</p>
                        <p style="color:#94a3b8;font-size:12px">If you didn't request this, ignore this email.</p>
                    </div>
                </div>
                """
                mail.send(msg)
                flash(f'A 6-digit OTP has been sent to {email}. Check your inbox.', 'success')
            except Exception as e:
                flash(f'Email could not be sent: {str(e)}. Check MAIL_USERNAME/MAIL_PASSWORD in .env', 'danger')
                print(f"OTP email error: {e}")
        else:
            flash('No account found with that email address.', 'danger')
        return redirect(url_for('verify_otp'))
    return render_template('auth/forgot_password.html')

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered = request.form.get('otp', '').strip()
        if entered == session.get('otp'):
            session.pop('otp', None)
            flash('OTP verified! Set your new password.', 'success')
            return redirect(url_for('reset_password'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
    return render_template('auth/verify_otp.html')

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if 'otp_user_id' not in session:
        flash('Session expired. Please start over.', 'warning')
        return redirect(url_for('forgot_password'))
    if request.method == 'POST':
        new_pass  = request.form.get('password', '')
        confirm   = request.form.get('confirm', '')
        if new_pass != confirm:
            flash('Passwords do not match.', 'danger')
            return render_template('auth/reset_password.html')
        if len(new_pass) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return render_template('auth/reset_password.html')
        hashed = hashlib.sha256(new_pass.encode()).hexdigest()
        conn   = get_db_connection()
        if conn:
            try:
                c = conn.cursor()
                c.execute("UPDATE users SET password=%s WHERE id=%s",
                          (hashed, session.pop('otp_user_id')))
                conn.commit()
                session.pop('otp_email', None)
                session.pop('otp_user_name', None)
                flash('Password reset successful! Please login.', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                flash('Could not reset password. Database error.', 'danger')
                print(f"Reset password error: {e}")
            finally:
                conn.close()
    return render_template('auth/reset_password.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = get_db_connection()
        if not conn:
            flash("System Error: Cannot connect to Database.", "danger")
            return render_template('auth/register.html')
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (name, email, password, age, emergency_contact) VALUES (%s,%s,%s,%s,%s)",
                (request.form['name'], request.form['email'],
                 hashlib.sha256(request.form['password'].encode()).hexdigest(),
                 request.form['age'], request.form.get('emergency_contact'))
            )
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            conn.rollback()
            flash('Email already registered or database error.', 'danger')
            print(f"Registration error: {e}")
        finally:
            conn.close()
    return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db_connection()
        if not conn:
            flash("Database connection failed.", "danger")
            return render_template('auth/login.html')
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE email=%s AND password=%s",
                      (request.form['email'],
                       hashlib.sha256(request.form['password'].encode()).hexdigest()))
            user = c.fetchone()
            if user:
                session['user_id']   = user[0]
                session['user_name'] = user[1]
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials!', 'danger')
        except Exception as e:
            flash('Login error occurred.', 'danger')
            print(f"Login error: {e}")
        finally:
            conn.close()
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))

# =============================================================================
# ROUTES — DASHBOARD
# =============================================================================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    dates, scores, history = [], [], []
    recovery_plan = None
    if conn:
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM assessments WHERE user_id=%s ORDER BY created_at DESC LIMIT 10",
                      (session['user_id'],))
            history = c.fetchall()
            if history:
                dates  = [h[22].strftime("%Y-%m-%d") for h in reversed(history)]
                scores = [h[20] for h in reversed(history)]
                latest = history[0]
                primary = None
                if latest[15] == 'High':   primary = 'Diabetes Type 2'
                elif latest[14] == 'High': primary = 'Heart Disease'
                elif latest[17] == 'High': primary = 'Sleep Insomnia'
                elif latest[16] == 'High': primary = 'Hypertension'
                if primary and primary in HEALTH_KNOWLEDGE_BASE:
                    data = HEALTH_KNOWLEDGE_BASE[primary]
                    recovery_plan = {
                        'issue':   data['title'],
                        'insight': f"High risk detected. Recommended Plan: {data['title']}",
                        'yoga':    [y['name'] for y in data['recovery']['yoga']],
                        'diet':    data['recovery']['diet']['good']
                    }
        except Exception as e:
            print(f"Dashboard data error: {e}")
        finally:
            conn.close()
    return render_template(
        'dashboard/index.html',
        user={'name': session['user_name']},
        dates=dates, scores=scores,
        last_risk=history[0][21] if history else 'N/A',
        avg_score=sum(scores) / len(scores) if scores else 0,
        total_assessments=len(history),
        recovery=recovery_plan
    )

# =============================================================================
# ROUTES — FIND DISEASE  (500+ Disease Analyser)
# =============================================================================
# ✅ BOTH hyphen AND underscore routes — covers all link formats
@app.route('/find-disease', methods=['GET'])
@app.route('/find_disease',  methods=['GET'])
def find_disease():
    """
    GET /find-disease  OR  /find_disease
    Shows the 500+ disease analysis input form.
    Template must be at:  templates/find_disease.html
    """
    if 'user_id' not in session:
        flash("Please login to use the Disease Finder.", "warning")
        return redirect(url_for('login'))

    # ── Helpful debug: confirm template exists ───────────────────────────────
    import os as _os
    tpl_path = _os.path.join(app.root_path, 'templates', 'find_disease.html')
    if not _os.path.exists(tpl_path):
        print(f"❌ TEMPLATE MISSING: {tpl_path}")
        flash(
            "Setup Error: templates/find_disease.html is missing. "
            "Please create this file in your templates/ folder.",
            "danger"
        )
        return redirect(url_for('dashboard'))

    return render_template('find_disease.html')


# ✅ Disease analysis — POST handler
@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    """
    POST /predict_disease
    Receives form from find_disease.html → calls disease_predictor.py → shows disease_result.html
    Template must be at:  templates/disease_result.html
    """
    if 'user_id' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('login'))

    if get_top_diseases is None or get_by_category is None:
        flash(
            "Disease Predictor module not loaded. "
            "Check that disease_prediction/disease_predictor.py exists and has no errors.",
            "danger"
        )
        return redirect(url_for('find_disease'))

    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi    = round(weight / ((height / 100) ** 2), 1)

        user_data = {
            'age':           float(request.form['age']),
            'bmi':           bmi,
            'bp_sys':        float(request.form['bp_sys']),
            'bp_dias':       float(request.form['bp_dias']),
            'glucose':       float(request.form['glucose']),
            'sleep_hours':   float(request.form['sleep_hours']),
            'screen_time':   float(request.form['screen_time']),
            'activity_mins': float(request.form['activity_mins']),
            'smoking':       1 if request.form.get('smoking') == 'yes' else 0,
            'alcohol':       request.form.get('alcohol', 'none'),
            'stress_level':  request.form.get('stress_level', 'Low'),
        }

        print(f"[Disease Analyser] Inputs → {user_data}")

        top_diseases = get_top_diseases(user_data, top_n=10)
        by_category  = get_by_category(user_data)

        print(f"[Disease Analyser] ✅ Top diseases: {len(top_diseases)}")
        print(f"[Disease Analyser] ✅ Categories:   {list(by_category.keys()) if by_category else 'None'}")

        # ── Confirm result template exists ───────────────────────────────────
        import os as _os
        res_tpl = _os.path.join(app.root_path, 'templates', 'disease_result.html')
        if not _os.path.exists(res_tpl):
            print(f"❌ TEMPLATE MISSING: {res_tpl}")
            flash(
                "Setup Error: templates/disease_result.html is missing. "
                "Please create this file in your templates/ folder.",
                "danger"
            )
            return redirect(url_for('find_disease'))

        return render_template(
            'disease_result.html',
            user_data    = user_data,
            top_diseases = top_diseases,
            by_category  = by_category
        )

    except KeyError as e:
        flash(f"Missing form field: {e}. Please fill all fields.", "danger")
        return redirect(url_for('find_disease'))

    except ValueError as e:
        flash(f"Invalid number entered: {e}. Please check your inputs.", "danger")
        return redirect(url_for('find_disease'))

    except Exception as e:
        flash(f"Disease analysis error: {str(e)}", "danger")
        print(f"[Disease Analyser] ❌ ERROR: {e}")
        import traceback; traceback.print_exc()
        return redirect(url_for('find_disease'))

# =============================================================================
# ROUTES — HEALTH ASSESSMENT
# =============================================================================
@app.route('/assess', methods=['GET', 'POST'])
def assess():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            form_data     = {k: request.form[k] for k in request.form}
            has_bp        = form_data.get('has_bp_measurement') == 'yes'
            bp_estimated  = False
            bp_confidence = 100
            if has_bp and form_data.get('bp_sys') and form_data.get('bp_dias'):
                bp_sys  = int(form_data['bp_sys'])
                bp_dias = int(form_data['bp_dias'])
            else:
                if BP_ESTIMATOR_AVAILABLE:
                    bp_input = {
                        'age':                         int(form_data.get('age', 30)),
                        'weight':                      float(form_data.get('weight', 70)),
                        'height':                      float(form_data.get('height', 170)),
                        'exercise_minutes':            int(form_data.get('activity_mins', 30)),
                        'sleep_hours':                 float(form_data.get('sleep_hours', 7)),
                        'stress_level':                int(form_data.get('stress', 5)),
                        'smoking':                     form_data.get('smoking') == 'yes',
                        'alcohol_frequency':           form_data.get('alcohol', 'never'),
                        'salt_intake':                 form_data.get('salt_intake', 'medium'),
                        'family_history_hypertension': form_data.get('family_history_bp') == 'yes',
                        'sedentary_hours':             int(form_data.get('sedentary_hours', 8)),
                        'water_intake':                int(form_data.get('water_intake', 8))
                    }
                    bp_result     = estimate_blood_pressure(bp_input)
                    bp_sys        = bp_result['systolic']
                    bp_dias       = bp_result['diastolic']
                    bp_estimated  = True
                    bp_confidence = bp_result['confidence']
                    flash(f'BP estimated: {bp_sys}/{bp_dias} mmHg (Confidence: {bp_confidence}%)', 'info')
                else:
                    bp_sys = 120; bp_dias = 80
                    flash('BP estimation not available. Using default values.', 'warning')
            prediction_data = {
                'bmi':           float(form_data.get('bmi', 25)),
                'sleep_hours':   float(form_data.get('sleep_hours', 7)),
                'activity_mins': int(form_data.get('activity_mins', 30)),
                'stress':        int(form_data.get('stress', 5)),
                'bp_sys':        bp_sys, 'bp_dias': bp_dias,
                'screen_time':   float(form_data.get('screen_time', 6)),
                'age':           int(form_data.get('age', 30))
            }
            risks, score, recs = predictor.predict(prediction_data)
            conn = get_db_connection()
            if conn:
                try:
                    cur = conn.cursor()
                    cur.execute(
                        """INSERT INTO assessments
                        (user_id, bp_sys, bp_dias, bp_estimated, bp_confidence, bmi,
                        sleep_hours, screen_time, activity_mins, stress_level,
                        overall_score, overall_risk, risk_heart_rate, risk_diabetes,
                        risk_hypertension, risk_sleep_apnea, risk_obesity, created_at)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())""",
                        (session['user_id'], bp_sys, bp_dias, bp_estimated, bp_confidence,
                         prediction_data['bmi'], prediction_data['sleep_hours'],
                         prediction_data['screen_time'], prediction_data['activity_mins'],
                         prediction_data['stress'], score,
                         'High' if score > 70 else 'Medium' if score > 40 else 'Low',
                         risks['heart']['level'], risks['diabetes']['level'],
                         risks['hypertension']['level'], risks['sleep']['level'],
                         risks['obesity']['level'])
                    )
                    conn.commit()
                except Exception as e:
                    conn.rollback(); print(f"Database save error: {e}")
                finally:
                    conn.close()
            overall_risk_level = 'High' if score > 70 else 'Medium' if score > 40 else 'Low'
            overall_color_val   = '#ef4444' if score > 70 else '#f59e0b' if score > 40 else '#10b981'

            # ── Emergency contact alert on HIGH risk ─────────────────────────────
            if overall_risk_level == 'High':
                try:
                    conn2 = get_db_connection()
                    if conn2:
                        ec_cur = conn2.cursor()
                        ec_cur.execute("SELECT name, emergency_contact FROM users WHERE id=%s",
                                       (session['user_id'],))
                        u_row = ec_cur.fetchone()
                        conn2.close()
                        if u_row and u_row[1]:           # emergency_contact is email or phone stored as text
                            ec_contact = u_row[1]
                            u_name     = u_row[0]
                            # Send email alert to emergency contact
                            try:
                                msg = Message(
                                    subject=f'[HealthPredict AI] URGENT: {u_name} has HIGH Health Risk',
                                    sender=os.getenv('MAIL_USERNAME'),
                                    recipients=[ec_contact] if '@' in ec_contact else [os.getenv('MAIL_USERNAME')]
                                )
                                msg.html = f"""
                                <div style="font-family:Arial,sans-serif;max-width:560px;margin:auto;border:1px solid #e2e8f0;border-radius:16px;overflow:hidden">
                                    <div style="background:#ef4444;padding:24px;text-align:center">
                                        <h2 style="color:white;margin:0">&#9888; URGENT HEALTH ALERT</h2>
                                    </div>
                                    <div style="padding:24px">
                                        <p style="font-size:16px">Dear Emergency Contact,</p>
                                        <p>This is an automated alert from <strong>HealthPredict AI</strong>.</p>
                                        <p><strong>{u_name}</strong> has just received a <span style="color:#ef4444;font-weight:bold">HIGH health risk score of {score}/100</span>
                                        after completing their health assessment.</p>
                                        <div style="background:#fef2f2;border-left:4px solid #ef4444;padding:14px;border-radius:8px;margin:16px 0">
                                            <strong>Risk Score:</strong> {score}/100 &nbsp;|&nbsp;
                                            <strong>Risk Level:</strong> HIGH
                                        </div>
                                        <p>Please check in with <strong>{u_name}</strong> and encourage them to visit a doctor.</p>
                                        <p style="color:#94a3b8;font-size:12px">This is an automated message from HealthPredict AI. Do not reply.</p>
                                    </div>
                                </div>
                                """
                                mail.send(msg)
                                flash(f'Emergency contact alerted about your high risk score.', 'warning')
                            except Exception as me:
                                print(f"Emergency email error: {me}")
                except Exception as ec_err:
                    print(f"Emergency contact lookup error: {ec_err}")

            diseases_view = [
                {'name': 'Heart Disease',   'icon': 'fa-heartbeat',   'risk_level': risks['heart']['level'],        'color': risks['heart']['color'],        'probability': 80 if risks['heart']['level']=='High' else 40 if risks['heart']['level']=='Medium' else 15,       'recommendation': 'Check cholesterol & BP regularly'},
                {'name': 'Diabetes',        'icon': 'fa-tint',        'risk_level': risks['diabetes']['level'],     'color': risks['diabetes']['color'],     'probability': 80 if risks['diabetes']['level']=='High' else 40 if risks['diabetes']['level']=='Medium' else 15,    'recommendation': 'Reduce sugar & refined carbs'},
                {'name': 'Hypertension',    'icon': 'fa-thermometer', 'risk_level': risks['hypertension']['level'],'color': risks['hypertension']['color'], 'probability': 80 if risks['hypertension']['level']=='High' else 40 if risks['hypertension']['level']=='Medium' else 15,'recommendation': 'Limit sodium, manage stress'},
                {'name': 'Sleep Disorder',  'icon': 'fa-bed',         'risk_level': risks['sleep']['level'],        'color': risks['sleep']['color'],        'probability': 80 if risks['sleep']['level']=='High' else 40 if risks['sleep']['level']=='Medium' else 15,       'recommendation': 'Sleep 7-8 hrs, avoid screens before bed'},
                {'name': 'Obesity',         'icon': 'fa-weight',      'risk_level': risks['obesity']['level'],      'color': risks['obesity']['color'],      'probability': 80 if risks['obesity']['level']=='High' else 40 if risks['obesity']['level']=='Medium' else 15,     'recommendation': 'Walk 10,000 steps daily'},
            ]
            return render_template(
                'prediction/result.html',
                overall_score=score,
                overall_risk=overall_risk_level,
                overall_status=overall_risk_level,
                overall_color=overall_color_val,
                diseases=diseases_view,
                bp_sys=bp_sys, bp_dias=bp_dias,
                bp_estimated=bp_estimated, bp_confidence=bp_confidence,
                recommendations=recs if isinstance(recs, dict) else {'foods': ['Fruits & vegetables', 'Whole grains', 'Lean protein'], 'habits': ['Exercise 30min/day', 'Sleep 7-8 hours', 'Drink 8 glasses water']}
            )
        except Exception as e:
            flash(f'Assessment error: {str(e)}', 'danger')
            print(f"Assessment error: {e}")
            import traceback; traceback.print_exc()
            return redirect(url_for('assess'))
    pre = session.get('pre_checkup', {})
    return render_template('prediction/form.html', bp_estimator_available=BP_ESTIMATOR_AVAILABLE, pre=pre)

# =============================================================================
# ROUTES — OTHER PAGES
# =============================================================================
@app.route('/who-regulations')
def who_regulations():
    return render_template('pages/who.html')

@app.route('/recommendations')
def recommendations():
    return render_template('pages/recommendations.html')

@app.route('/calculators', methods=['GET', 'POST'])
def calculators():
    if request.method == 'POST':
        try:
            age      = int(request.form.get('age', 30))
            weight   = float(request.form.get('weight', 70))
            height   = float(request.form.get('height', 170))
            sleep    = float(request.form.get('sleep_hours', 7))
            exercise = int(request.form.get('activity_mins', 30))
            screen   = float(request.form.get('screen_time', 6))
            stress   = int(request.form.get('stress', 5))
            smoking  = request.form.get('smoking', 'no')
            alcohol  = request.form.get('alcohol', 'never')
            salt     = request.form.get('salt_intake', 'medium')
            family_bp = request.form.get('family_history_bp', 'no')
            glucose_fasting = float(request.form.get('glucose', 0) or 0)
            h_m = height / 100
            bmi = round(weight / (h_m * h_m), 1)
            if bmi < 18.5:   bmi_cat = 'Underweight'
            elif bmi < 25:   bmi_cat = 'Normal'
            elif bmi < 30:   bmi_cat = 'Overweight'
            else:            bmi_cat = 'Obese'
            if glucose_fasting == 0:       glucose_cat = 'Not Provided'
            elif glucose_fasting < 70:     glucose_cat = 'Low (Hypoglycemia)'
            elif glucose_fasting <= 99:    glucose_cat = 'Normal'
            elif glucose_fasting <= 125:   glucose_cat = 'Pre-Diabetic'
            else:                          glucose_cat = 'Diabetic Range'
            bp_sys, bp_dias = 120, 80
            if BP_ESTIMATOR_AVAILABLE:
                try:
                    bp_result = estimate_blood_pressure({
                        'age': age, 'weight': weight, 'height': height,
                        'exercise_minutes': exercise, 'sleep_hours': sleep,
                        'stress_level': stress, 'smoking': smoking == 'yes',
                        'alcohol_frequency': alcohol, 'salt_intake': salt,
                        'family_history_hypertension': family_bp == 'yes',
                        'sedentary_hours': max(0, 16 - exercise // 60 - int(sleep)),
                        'water_intake': 8
                    })
                    bp_sys  = bp_result['systolic']
                    bp_dias = bp_result['diastolic']
                except:
                    pass
            if bp_sys >= 140:   bp_cat = 'High (Hypertension Stage 2)'
            elif bp_sys >= 130: bp_cat = 'Elevated (Stage 1)'
            elif bp_sys >= 120: bp_cat = 'Elevated'
            else:               bp_cat = 'Normal'
            session['pre_checkup'] = {
                'age': age, 'weight': weight, 'height': height,
                'bmi': bmi, 'bmi_cat': bmi_cat,
                'bp_sys': bp_sys, 'bp_dias': bp_dias, 'bp_cat': bp_cat,
                'glucose': glucose_fasting, 'glucose_cat': glucose_cat,
                'sleep_hours': sleep, 'activity_mins': exercise,
                'screen_time': screen, 'stress': stress,
                'smoking': smoking, 'alcohol': alcohol,
                'salt_intake': salt, 'family_history_bp': family_bp,
            }
            return render_template('pages/calculators.html',
                                   result=session['pre_checkup'], calculated=True)
        except Exception as e:
            flash(f'Calculation error: {str(e)}', 'danger')
    pre = session.get('pre_checkup', {})
    return render_template('pages/calculators.html', result=pre, calculated=bool(pre))

@app.route('/encyclopedia')
def encyclopedia():
    return render_template('pages/encyclopedia.html', diseases=HEALTH_KNOWLEDGE_BASE)

@app.route('/tracker', methods=['GET', 'POST'])
def tracker():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    disease = session.get('active_disease', 'Heart Disease')
    plan    = HEALTH_KNOWLEDGE_BASE.get(disease, HEALTH_KNOWLEDGE_BASE['Heart Disease']).get('daily_plan', {})
    conn    = get_db_connection()
    if request.method == 'POST':
        if conn:
            try:
                conn.cursor().execute(
                    """INSERT INTO recovery_logs
                    (user_id, disease_name, date, diet_quality, exercise_mins, symptom_severity, notes)
                    VALUES (%s,%s,CURRENT_DATE,%s,%s,%s,%s)""",
                    (session['user_id'], disease, request.form['diet'],
                     request.form['exercise'], request.form['severity'], request.form['notes'])
                )
                conn.commit()
                flash("Daily Log Saved!", "success")
            except Exception as e:
                conn.rollback(); flash("Error saving log.", "danger")
                print(f"Tracker save error: {e}")
            finally:
                conn.close()
        return redirect(url_for('tracker'))
    dates, severity = [], []
    if conn:
        try:
            c = conn.cursor()
            c.execute("SELECT date, symptom_severity FROM recovery_logs WHERE user_id=%s ORDER BY date ASC LIMIT 7",
                      (session['user_id'],))
            hist     = c.fetchall()
            dates    = [h[0].strftime('%a') for h in hist]
            severity = [h[1] for h in hist]
        except Exception as e:
            print(f"Tracker data error: {e}")
        finally:
            conn.close()
    return render_template('pages/tracker.html',
                           disease=disease, plan=plan, dates=dates, severity=severity,
                           date=date.today().strftime('%A, %B %d'))

@app.route('/symptom-checker', methods=['GET', 'POST'])
def symptom_checker():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    diagnosis    = None
    all_matches  = []
    error_msg    = None

    if request.method == 'POST':
        selected = request.form.getlist('symptoms')

        # ── Require at least 2 symptoms ──────────────────────────────────────
        if len(selected) < 2:
            error_msg = 'Please select at least 2 symptoms for an accurate analysis.'
        else:
            scores = []
            for disease_key, data in HEALTH_KNOWLEDGE_BASE.items():
                matched  = [s for s in data['symptoms'] if s in selected]
                count    = len(matched)
                if count > 0:
                    pct = round((count / len(data['symptoms'])) * 100)
                    scores.append((count, pct, disease_key, matched))

            # Sort by match count descending, take top 5
            scores.sort(reverse=True)
            top_matches = scores[:5]

            if not top_matches:
                error_msg = 'No known condition matched your symptoms. Try selecting more symptoms.'
            else:
                # Build water intake recommendation based on symptoms
                water_msg = 'Drink at least 8 glasses (2L) of water daily.'
                if any(s in selected for s in ['dizziness','dry mouth','fatigue','headache']):
                    water_msg = 'Drink 10–12 glasses of water daily — dehydration worsens your symptoms.'
                elif any(s in selected for s in ['high blood pressure','swelling','kidney pain']):
                    water_msg = 'Drink 2–2.5L water daily. Avoid excessive salt with fluids.'
                elif any(s in selected for s in ['frequent urination','excessive thirst']):
                    water_msg = 'Drink 8–10 glasses water but monitor glucose — excessive thirst may signal diabetes.'

                for (count, pct, disease_key, matched) in top_matches:
                    d = HEALTH_KNOWLEDGE_BASE[disease_key]
                    all_matches.append({
                        'name':      d['title'],
                        'key':       disease_key,
                        'match_pct': pct,
                        'matched_symptoms': matched,
                        'plan':      d.get('daily_plan', {}),
                        'recovery':  d.get('recovery', {}),
                        'water':     water_msg
                    })

                # Set primary match for tracker redirect
                if all_matches:
                    session['active_disease'] = top_matches[0][2]
                    diagnosis = all_matches[0]   # kept for backward compat

    all_symptoms = sorted(list(set([s for d in HEALTH_KNOWLEDGE_BASE.values() for s in d['symptoms']])))
    return render_template('pages/symptom_checker.html',
                           symptoms=all_symptoms,
                           diagnosis=diagnosis,
                           all_matches=all_matches,
                           error_msg=error_msg)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    user = None
    if conn:
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE id=%s", (session['user_id'],))
            user = c.fetchone()
        except Exception as e:
            print(f"Profile error: {e}")
        finally:
            conn.close()
    return render_template('profile/index.html', user=user, google_maps_key=GOOGLE_MAPS_API_KEY)

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    if conn:
        try:
            c = conn.cursor()
            c.execute("INSERT INTO feedback (user_id, rating, comment) VALUES (%s,%s,%s)",
                      (session['user_id'], request.form.get('rating'), request.form.get('comment')))
            conn.commit()
            flash("Thank you for your feedback!", "success")
        except Exception as e:
            conn.rollback(); flash("Error submitting feedback.", "danger")
            print(f"Feedback error: {e}")
        finally:
            conn.close()
    return redirect(url_for('dashboard'))


# =============================================================================
# API ENDPOINTS
# =============================================================================
@app.route('/api/nearby-places', methods=['POST'])
def api_nearby_places():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    if not GOOGLE_MAPS_API_KEY:
        return jsonify({'success': False, 'error': 'Google Maps API not configured'}), 500
    try:
        import googlemaps  # type: ignore
        data        = request.json or {}
        latitude    = float(data.get('latitude',  13.0827))
        longitude   = float(data.get('longitude', 80.2707))
        radius      = int(data.get('radius', 5000))
        search_type = data.get('type', 'both')
        gmaps       = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
        def fetch(place_type):
            result = gmaps.places_nearby(location=(latitude, longitude), radius=radius, type=place_type)
            places = []
            for place in result.get('results', [])[:15]:
                photo_ref = place['photos'][0].get('photo_reference') if place.get('photos') else None
                places.append({
                    'name': place.get('name'), 'address': place.get('vicinity'),
                    'rating': place.get('rating', 'N/A'),
                    'open_now': place.get('opening_hours', {}).get('open_now', None),
                    'lat': place['geometry']['location']['lat'],
                    'lng': place['geometry']['location']['lng'],
                    'place_id': place.get('place_id'),
                    'photo_ref': photo_ref, 'type': place_type
                })
            return places
        hospitals  = fetch('hospital') if search_type in ('hospital', 'both') else []
        pharmacies = fetch('pharmacy') if search_type in ('pharmacy', 'both') else []
        return jsonify({'success': True, 'hospitals': hospitals,
                        'pharmacies': pharmacies, 'total': len(hospitals) + len(pharmacies)})
    except ImportError:
        return jsonify({'success': False, 'error': 'googlemaps not installed'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/place-details', methods=['GET'])
def api_place_details():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    place_id = request.args.get('place_id')
    if not place_id:
        return jsonify({'success': False, 'error': 'place_id required'}), 400
    if not GOOGLE_MAPS_API_KEY:
        return jsonify({'success': False, 'error': 'API not configured'}), 500
    try:
        import googlemaps  # type: ignore
        gmaps   = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
        details = gmaps.place(place_id=place_id,
                              fields=['name','formatted_address','formatted_phone_number',
                                      'website','opening_hours','rating','user_ratings_total'])
        return jsonify({'success': True, 'details': details.get('result', {})})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/estimate-bp', methods=['POST'])
def api_estimate_bp():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    if not BP_ESTIMATOR_AVAILABLE:
        return jsonify({'success': False, 'error': 'BP estimator not available'}), 500
    try:
        data = request.json
        bp_input = {
            'age':                         int(data.get('age', 30)),
            'weight':                      float(data.get('weight', 70)),
            'height':                      float(data.get('height', 170)),
            'exercise_minutes':            int(data.get('exercise_minutes', 30)),
            'sleep_hours':                 float(data.get('sleep_hours', 7)),
            'stress_level':                int(data.get('stress_level', 5)),
            'smoking':                     data.get('smoking', False),
            'alcohol_frequency':           data.get('alcohol', 'never'),
            'salt_intake':                 data.get('salt_intake', 'medium'),
            'family_history_hypertension': data.get('family_history_bp', False),
            'sedentary_hours':             int(data.get('sedentary_hours', 8)),
            'water_intake':                int(data.get('water_intake', 8))
        }
        bp_result         = estimate_blood_pressure(bp_input)
        bp_interpretation = interpret_bp_result(bp_result)
        return jsonify({'success': True, 'bp_estimate': bp_result, 'interpretation': bp_interpretation})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/test')
def api_test():
    return jsonify({
        'success':  True,
        'message':  'Health Risk Prediction API is running!',
        'timestamp': datetime.now().isoformat(),
        'features': {
            'bp_estimator':     BP_ESTIMATOR_AVAILABLE,
            'ml_model':         ml_model is not None,
            'google_maps':      GOOGLE_MAPS_API_KEY is not None,
            'disease_analysis': get_top_diseases is not None
        }
    })

# =============================================================================
# MISCELLANEOUS
# =============================================================================
@app.route('/nearby', methods=['GET', 'POST'])
def nearby():
    hospitals  = []
    pharmacies = []
    error      = None
    api_key    = GOOGLE_MAPS_API_KEY
    lat        = '13.0827'   # default: Chennai, India
    lng        = '80.2707'
    radius     = '5000'

    if request.method == 'POST':
        lat         = request.form.get('latitude',  '13.0827')
        lng         = request.form.get('longitude', '80.2707')
        radius      = request.form.get('radius',    '5000')
        search_type = request.form.get('search_type', 'both')

        if not api_key:
            error = 'Google Maps API key is not configured. Add GOOGLE_MAPS_API_KEY to your .env file.'
        else:
            try:
                import googlemaps
                gmaps = googlemaps.Client(key=api_key)

                def fetch_places(place_type):
                    results = []
                    try:
                        resp = gmaps.places_nearby(
                            location=(float(lat), float(lng)),
                            radius=int(radius),
                            type=place_type
                        )
                        for p in resp.get('results', []):
                            loc = p.get('geometry', {}).get('location', {})
                            oh  = p.get('opening_hours', {})
                            results.append({
                                'name':    p.get('name', 'Unknown'),
                                'address': p.get('vicinity', 'Address unavailable'),
                                'lat':     loc.get('lat', lat),
                                'lng':     loc.get('lng', lng),
                                'rating':  p.get('rating', 'N/A'),
                                'open_now': oh.get('open_now', None)
                            })
                    except Exception as e:
                        print(f'Places API error ({place_type}): {e}')
                    return results

                if search_type in ('hospital', 'both'):
                    hospitals = fetch_places('hospital')
                if search_type in ('pharmacy', 'both'):
                    pharmacies = fetch_places('pharmacy')

                if not hospitals and not pharmacies:
                    error = 'No results found in this area. Try increasing the search radius.'

            except ImportError:
                error = 'googlemaps library not installed. Run: pip install googlemaps'
            except Exception as e:
                error = f'Maps API error: {str(e)}'
                print(f'Nearby route error: {e}')

    return render_template('pages/nearby.html',
                            hospitals=hospitals, pharmacies=pharmacies,
                            error=error, api_key=api_key,
                            lat=lat, lng=lng, radius=radius)

@app.route('/download_report')
def download_report():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    try:
        from fpdf import FPDF
        conn = get_db_connection()
        assessment = None
        user_name = session.get('user_name', 'User')
        if conn:
            try:
                c = conn.cursor()
                c.execute("SELECT * FROM assessments WHERE user_id=%s ORDER BY created_at DESC LIMIT 1",
                          (session['user_id'],))
                assessment = c.fetchone()
            except Exception as e:
                print(f"Report DB error: {e}")
            finally:
                conn.close()

        class HealthPDF(FPDF):
            def header(self):
                self.set_fill_color(13, 110, 110)
                self.rect(0, 0, 210, 38, 'F')
                self.set_font('Helvetica', 'B', 20)
                self.set_text_color(255, 255, 255)
                self.set_xy(10, 8)
                self.cell(0, 10, 'HealthPredict AI', ln=False)
                self.set_font('Helvetica', '', 10)
                self.set_xy(10, 22)
                self.cell(0, 6, 'Predictive Health Risk Report  |  Daily Routine Analysis by ML')
                self.set_text_color(0, 0, 0)
                self.ln(20)

            def footer(self):
                self.set_y(-15)
                self.set_font('Helvetica', 'I', 8)
                self.set_text_color(150, 150, 150)
                self.cell(0, 10, f'Page {self.page_no()} | DISCLAIMER: This report is for informational purposes only. Consult a licensed doctor.', align='C')

        pdf = HealthPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # ── Patient Info ─────────────────────────────────────────────────────
        pdf.set_font('Helvetica', 'B', 13)
        pdf.set_fill_color(240, 248, 248)
        pdf.set_draw_color(13, 110, 110)
        pdf.cell(0, 10, f'  Patient Report: {user_name}', border='LB', fill=True, ln=True)
        pdf.ln(3)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(90, 7, f'  Generated: {datetime.now().strftime("%B %d, %Y  %H:%M")}')
        pdf.cell(0, 7, f'  Patient ID: #{session["user_id"]:04d}', ln=True)
        pdf.ln(6)

        if assessment:
            (_, _, bp_sys, bp_dias, bp_estimated, bp_confidence,
             glucose, bmi, smoking, alcohol,
             sleep_hours, screen_time, activity_mins, stress_level,
             risk_heart, risk_diabetes, risk_hypertension,
             risk_sleep, risk_anxiety, risk_obesity,
             overall_score, overall_risk, created_at, *_rest) = (list(assessment) + [None]*10)[:24]

            created_str = created_at.strftime('%Y-%m-%d') if created_at else 'N/A'

            # ── Overall Risk Score ────────────────────────────────────────────
            pdf.set_font('Helvetica', 'B', 13)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 8, '  Overall Health Risk Score', ln=True)
            pdf.ln(2)

            score_val    = overall_score or 0
            score_color  = (220, 53, 69) if score_val > 70 else (255, 153, 0) if score_val > 40 else (40, 167, 69)
            bar_width    = int(score_val * 1.7)
            pdf.set_fill_color(230, 230, 230)
            pdf.rect(10, pdf.get_y(), 170, 10, 'F')
            pdf.set_fill_color(*score_color)
            pdf.rect(10, pdf.get_y(), bar_width, 10, 'F')
            pdf.set_font('Helvetica', 'B', 10)
            pdf.set_text_color(255, 255, 255)
            pdf.set_xy(10, pdf.get_y())
            pdf.cell(bar_width, 10, f'  {score_val}%  {overall_risk or "N/A"} RISK', align='L')
            pdf.ln(14)

            # ── Vital Stats ───────────────────────────────────────────────────
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('Helvetica', 'B', 13)
            pdf.cell(0, 8, '  Daily Routine Vitals (from your last assessment)', ln=True)
            pdf.ln(2)

            vitals = [
                ('Blood Pressure',   f'{bp_sys or "?"}/{bp_dias or "?"}  mmHg' + (' (Estimated)' if bp_estimated else '')),
                ('BMI',              f'{round(float(bmi), 1) if bmi else "N/A"}'),
                ('Sleep Hours',      f'{sleep_hours or "N/A"}  hrs/night'),
                ('Screen Time',      f'{screen_time or "N/A"}  hrs/day'),
                ('Activity',         f'{activity_mins or "N/A"}  mins/day'),
                ('Stress Level',     f'{stress_level or "N/A"}  / 10'),
                ('Assessment Date',  created_str),
            ]
            pdf.set_font('Helvetica', '', 10)
            pdf.set_fill_color(248, 249, 250)
            for i, (label, value) in enumerate(vitals):
                fill = i % 2 == 0
                pdf.set_fill_color(248, 249, 250) if fill else pdf.set_fill_color(255, 255, 255)
                pdf.cell(85, 8, f'  {label}', border='B', fill=fill)
                pdf.cell(0,  8, f'  {value}',  border='B', fill=fill, ln=True)
            pdf.ln(6)

            # ── Disease Risk Table ────────────────────────────────────────────
            pdf.set_font('Helvetica', 'B', 13)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 8, '  ML Disease Risk Predictions', ln=True)
            pdf.ln(2)

            diseases = [
                ('Heart Disease',    risk_heart or 'Low'),
                ('Diabetes Type 2',  risk_diabetes or 'Low'),
                ('Hypertension',     risk_hypertension or 'Low'),
                ('Sleep Disorder',   risk_sleep or 'Low'),
                ('Obesity',          risk_obesity or 'Low'),
            ]
            color_map = {'High': (220, 53, 69), 'Medium': (255, 153, 0), 'Low': (40, 167, 69)}
            pdf.set_font('Helvetica', 'B', 10)
            pdf.set_fill_color(13, 110, 110)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(120, 9, '  Disease', border=1, fill=True)
            pdf.cell(0,   9, '  Risk Level', border=1, fill=True, ln=True)
            pdf.set_font('Helvetica', '', 10)
            for dname, dlevel in diseases:
                rc = color_map.get(dlevel, (150, 150, 150))
                pdf.set_text_color(0, 0, 0)
                pdf.cell(120, 8, f'  {dname}', border='B')
                pdf.set_text_color(*rc)
                pdf.set_font('Helvetica', 'B', 10)
                pdf.cell(0, 8, f'  >> {dlevel}', border='B', ln=True)
                pdf.set_font('Helvetica', '', 10)
            pdf.ln(6)

            # ── Recommendations ───────────────────────────────────────────────
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('Helvetica', 'B', 13)
            pdf.cell(0, 8, '  Personalized Recommendations', ln=True)
            pdf.ln(2)
            pdf.set_font('Helvetica', '', 10)
            recs = []
            if float(bmi or 25) > 30:
                recs.append('Obesity risk detected. Aim for 10,000 steps/day and a calorie-deficit diet.')
            if int(bp_sys or 120) > 130:
                recs.append('Elevated blood pressure. Reduce salt intake and practice deep breathing.')
            if float(sleep_hours or 7) < 6:
                recs.append('Insufficient sleep. Target 7-8 hours; avoid screens 1 hr before bed.')
            if int(activity_mins or 30) < 30:
                recs.append('Low activity. WHO recommends 150 min/week of moderate exercise.')
            if int(stress_level or 5) > 7:
                recs.append('High stress. Try Yoga Nidra, journaling, or Pranayama breathing.')
            if not recs:
                recs.append('Great job! Maintain your current healthy lifestyle habits.')
            for r in recs:
                pdf.set_font('Helvetica', 'B', 10)
                pdf.write(8, '- ')
                pdf.set_font('Helvetica', '', 10)
                pdf.write(8, r + '\n')
        else:
            pdf.set_font('Helvetica', 'I', 12)
            pdf.set_text_color(150, 150, 150)
            pdf.cell(0, 20, 'No assessment data found. Please complete a health checkup first.', align='C', ln=True)

        buf = BytesIO()
        pdf_bytes = pdf.output()
        buf.write(pdf_bytes)
        buf.seek(0)
        response = make_response(buf.read())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename="HealthPredict_Report_{user_name.replace(" ", "_")}_{datetime.now().strftime("%Y%m%d")}.pdf"'
        return response

    except ImportError:
        flash("PDF library not installed. Run: pip install fpdf2", "danger")
        return redirect(url_for('dashboard'))
    except Exception as e:
        print(f"PDF generation error: {e}")
        import traceback; traceback.print_exc()
        flash(f"Report generation failed: {str(e)}", "danger")
        return redirect(url_for('dashboard'))

# =============================================================================
# OFFLINE PAGE — for PWA fallback
# =============================================================================
@app.route('/offline')
def offline():
    return render_template('offline.html')

# =============================================================================
# ERROR HANDLERS — inline HTML so they NEVER fail even if template is missing
# =============================================================================
@app.errorhandler(404)
def not_found(error):
    # Try template first, fallback to inline HTML
    try:
        return render_template('errors/404.html'), 404
    except Exception:
        return """
        <!DOCTYPE html><html><head><title>404</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head><body class="bg-light">
        <div class="container text-center mt-5">
            <h1 class="display-1 text-danger">404</h1>
            <h3>Page Not Found</h3>
            <p class="text-muted">The page you are looking for does not exist.</p>
            <a href="/dashboard" class="btn btn-primary rounded-pill px-4">Go to Dashboard</a>
            &nbsp;
            <a href="/" class="btn btn-outline-secondary rounded-pill px-4">Go Home</a>
        </div></body></html>""", 404

@app.errorhandler(500)
def internal_error(error):
    try:
        return render_template('errors/500.html'), 500
    except Exception:
        return """
        <!DOCTYPE html><html><head><title>500</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head><body class="bg-light">
        <div class="container text-center mt-5">
            <h1 class="display-1 text-warning">500</h1>
            <h3>Internal Server Error</h3>
            <p class="text-muted">Something went wrong. Check your terminal for details.</p>
            <a href="/dashboard" class="btn btn-primary rounded-pill px-4">Go to Dashboard</a>
        </div></body></html>""", 500

# =============================================================================
# RUN
# =============================================================================
if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🚀 HEALTH RISK PREDICTION SYSTEM - STARTING")
    print("=" * 70)

    init_db()

    # ── Confirm template files exist at startup ──────────────────────────────
    import os as _os
    templates_dir = _os.path.join(_os.path.dirname(__file__), 'templates')
    critical_templates = [
        'find_disease.html',
        'disease_result.html',
        'home.html',
        'dashboard/index.html',
        'prediction/form.html',
        'prediction/result.html',
    ]
    print("\n📁 TEMPLATE CHECK:")
    for tpl in critical_templates:
        full = _os.path.join(templates_dir, tpl)
        status = "✅" if _os.path.exists(full) else "❌ MISSING"
        print(f"   {status}  templates/{tpl}")

    print("\n📊 SYSTEM STATUS:")
    print(f"   {'✅' if ml_model              else '❌'} ML Model:         {'Loaded'             if ml_model              else 'Not Available'}")
    print(f"   {'✅' if BP_ESTIMATOR_AVAILABLE else '❌'} BP Estimator:     {'Ready'              if BP_ESTIMATOR_AVAILABLE else 'Not Available'}")
    print(f"   {'✅' if GOOGLE_MAPS_API_KEY   else '❌'} Google Maps:      {'Configured'         if GOOGLE_MAPS_API_KEY   else 'Not Configured'}")
    print(f"   {'✅' if get_top_diseases      else '❌'} Disease Analyser: {'500+ diseases loaded' if get_top_diseases      else 'NOT FOUND'}")

    print("\n📍 ACCESS AT:     http://localhost:5000")
    print("🔬 FIND DISEASE:  http://localhost:5000/find-disease")
    print("🔍 API TEST:      http://localhost:5000/api/test")
    print("=" * 70 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)