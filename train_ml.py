"""
=============================================================================
PREDICTIVE HEALTH RISK — ML MODEL TRAINER
=============================================================================
This script trains a RandomForest classifier on your daily-routine CSVs.

HOW IT FITS INTO THE PROJECT:
  1. User fills the health assessment form (/assess)
  2. app.py sends their vitals → health_model.pkl (this model)
  3. Model predicts disease class → risk score computed → PDF report generated

DATASETS USED:
  • diabetes_data.csv      — Pima Indians Diabetes Dataset (768 records)
  • heart_data.csv         — Cardiovascular Disease Dataset (70 000 records)
  • sleep_data.csv         — Sleep Health & Lifestyle Dataset (374 records)
  • comprehensive_health_data.csv — Multi-disease routine data (if present)

HOW TO GET MORE DATA:
  • Kaggle: https://www.kaggle.com/datasets — search "health risk lifestyle"
  • UCI ML: https://archive.ics.uci.edu
  • NHANES: https://www.cdc.gov/nchs/nhanes
  Add new CSVs below following the existing pattern.

TO RETRAIN:
  python train_ml.py
=============================================================================
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import pickle
import os

print("\n" + "="*60)
print("ML  HEALTH RISK PREDICTION MODEL TRAINER")
print("="*60)

FEATURES = ['age', 'bmi', 'sleep_hours', 'activity_mins',
            'stress_level', 'bp_sys', 'bp_dias', 'screen_time']
TARGET   = 'Diagnosis'

master = pd.DataFrame(columns=FEATURES + [TARGET])

# -----------------------------------------------------------------
# 1. DIABETES DATASET
# -----------------------------------------------------------------
if os.path.exists('diabetes_data.csv'):
    print("\n>> Loading diabetes_data.csv ...")
    try:
        df = pd.read_csv('diabetes_data.csv')
        df.columns = df.columns.str.strip()
        tmp = pd.DataFrame()
        tmp['age']          = df.get('Age',           df.get('age',          30))
        tmp['bmi']          = df.get('BMI',           df.get('bmi',          25))
        tmp['bp_dias']      = df.get('BloodPressure', df.get('blood_pressure',80))
        tmp['bp_sys']       = tmp['bp_dias'] + 40
        tmp['sleep_hours']  = 7.0
        tmp['activity_mins']= 30
        tmp['stress_level'] = 5
        tmp['screen_time']  = 6.0
        if 'Outcome' in df.columns:
            tmp[TARGET] = df['Outcome'].map({1: 'Diabetes Type 2', 0: 'Healthy'})
        else:
            tmp[TARGET] = 'Healthy'
        master = pd.concat([master, tmp[FEATURES + [TARGET]]], ignore_index=True)
        print(f"   [OK]  {len(tmp):,} records added")
    except Exception as e:
        print(f"   WARNING️  Error: {e}")

# -----------------------------------------------------------------
# 2. HEART / CARDIOVASCULAR DATASET
# -----------------------------------------------------------------
if os.path.exists('heart_data.csv'):
    print("\n>> Loading heart_data.csv ...")
    try:
        df = pd.read_csv('heart_data.csv')
        if 'age' not in df.columns and 'Age' not in df.columns:
            df = pd.read_csv('heart_data.csv', sep=';')
        df.columns = df.columns.str.strip()
        tmp = pd.DataFrame()

        age_col = df.get('age', df.get('Age', None))
        if age_col is not None:
            tmp['age'] = age_col // 365 if age_col.mean() > 150 else age_col
        else:
            tmp['age'] = 45

        if 'weight' in df.columns and 'height' in df.columns:
            tmp['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
        else:
            tmp['bmi'] = 28.0

        tmp['bp_sys']        = df.get('ap_hi',    120)
        tmp['bp_dias']       = df.get('ap_lo',     80)
        tmp['activity_mins'] = df.get('active', 1).map({1: 45, 0: 10}) if 'active' in df.columns else 30
        tmp['sleep_hours']   = 6.5
        tmp['stress_level']  = 7
        tmp['screen_time']   = 5.0

        if 'cardio' in df.columns:
            tmp[TARGET] = df['cardio'].map({1: 'Heart Disease', 0: 'Healthy'})
        elif 'target' in df.columns:
            tmp[TARGET] = df['target'].map({1: 'Heart Disease', 0: 'Healthy'})
        else:
            tmp[TARGET] = 'Healthy'

        # Filter obviously bad BP readings from raw data
        tmp = tmp[(tmp['bp_sys'].between(60, 250)) & (tmp['bp_dias'].between(40, 160))]

        master = pd.concat([master, tmp[FEATURES + [TARGET]]], ignore_index=True)
        print(f"   [OK]  {len(tmp):,} records added")
    except Exception as e:
        print(f"   WARNING️  Error: {e}")

# -----------------------------------------------------------------
# 3. SLEEP & LIFESTYLE DATASET
# -----------------------------------------------------------------
if os.path.exists('sleep_data.csv'):
    print("\n>> Loading sleep_data.csv ...")
    try:
        df = pd.read_csv('sleep_data.csv')
        tmp = pd.DataFrame()
        tmp['age']          = df.get('Age', 35)
        tmp['sleep_hours']  = df.get('Sleep Duration', 7)
        tmp['activity_mins']= df.get('Physical Activity Level', 30)
        tmp['stress_level'] = df.get('Stress Level', 5)

        if 'Blood Pressure' in df.columns:
            try:
                bp = df['Blood Pressure'].str.split('/', expand=True).astype(float)
                tmp['bp_sys']  = bp[0]
                tmp['bp_dias'] = bp[1]
            except:
                tmp['bp_sys'] = 120; tmp['bp_dias'] = 80
        else:
            tmp['bp_sys'] = 120; tmp['bp_dias'] = 80

        bmi_map = {'Normal': 22, 'Normal Weight': 22, 'Overweight': 28, 'Obese': 33}
        tmp['bmi']         = df['BMI Category'].map(bmi_map).fillna(25) if 'BMI Category' in df.columns else 25
        tmp['screen_time'] = 8.0

        if 'Sleep Disorder' in df.columns:
            tmp[TARGET] = df['Sleep Disorder'].apply(
                lambda x: 'Sleep Insomnia' if str(x).strip() not in ('nan', 'None', '') else 'Healthy'
            )
        else:
            tmp[TARGET] = 'Healthy'

        master = pd.concat([master, tmp[FEATURES + [TARGET]]], ignore_index=True)
        print(f"   [OK]  {len(tmp):,} records added")
    except Exception as e:
        print(f"   WARNING️  Error: {e}")

# -----------------------------------------------------------------
# 4. COMPREHENSIVE HEALTH DATA (if available)
# -----------------------------------------------------------------
if os.path.exists('comprehensive_health_data.csv'):
    print("\n>> Loading comprehensive_health_data.csv ...")
    try:
        df = pd.read_csv('comprehensive_health_data.csv')
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        tmp = pd.DataFrame()
        for col in FEATURES:
            if col in df.columns:
                tmp[col] = df[col]
            else:
                tmp[col] = np.nan
        if TARGET.lower() in df.columns:
            tmp[TARGET] = df[TARGET.lower()]
        elif 'diagnosis' in df.columns:
            tmp[TARGET] = df['diagnosis']
        else:
            tmp[TARGET] = 'Healthy'
        master = pd.concat([master, tmp[FEATURES + [TARGET]]], ignore_index=True)
        print(f"   [OK]  {len(tmp):,} records added")
    except Exception as e:
        print(f"   WARNING️  Error: {e}")

# -----------------------------------------------------------------
# 5. SYNTHETIC FALLBACK — 5 disease classes, realistic distributions
# -----------------------------------------------------------------
if len(master) < 200:
    print("\nWARNING️  Not enough real data. Generating 3,000 synthetic records...")
    n = 3000
    rng = np.random.default_rng(42)

    syn = pd.DataFrame({
        'age':           rng.integers(18, 80, n),
        'bmi':           rng.uniform(16.0, 42.0, n),
        'sleep_hours':   rng.uniform(3.5, 10.5, n),
        'activity_mins': rng.integers(0, 180, n),
        'stress_level':  rng.integers(1, 10, n),
        'bp_sys':        rng.integers(88, 195, n),
        'bp_dias':       rng.integers(55, 120, n),
        'screen_time':   rng.uniform(0.5, 14.0, n),
    })

    def label_row(r):
        # Hypertension — high BP
        if r.bp_sys > 145:
            return 'Hypertension'
        # Obesity
        if r.bmi > 32 and r.activity_mins < 25:
            return 'Obesity'
        # Heart Disease — high BP + age + low activity
        if r.bp_sys > 135 and r.age > 45 and r.activity_mins < 30:
            return 'Heart Disease'
        # Diabetes — high BMI + low activity + older
        if r.bmi > 29 and r.activity_mins < 40 and r.age > 35:
            return 'Diabetes Type 2'
        # Insomnia — low sleep + high stress + high screen
        if r.sleep_hours < 5.5 and r.stress_level > 6 and r.screen_time > 8:
            return 'Sleep Insomnia'
        return 'Healthy'

    syn[TARGET] = syn.apply(label_row, axis=1)
    master = pd.concat([master, syn], ignore_index=True)
    print(f"   [OK]  Synthetic records generated.")

# -----------------------------------------------------------------
# CLEAN & PREP
# -----------------------------------------------------------------
master = master[FEATURES + [TARGET]].dropna()
master[FEATURES] = master[FEATURES].apply(pd.to_numeric, errors='coerce')
master = master.dropna()

print(f"\n[DATA] Final Dataset: {len(master):,} records")
print(master[TARGET].value_counts().to_string())

# -----------------------------------------------------------------
# TRAIN
# -----------------------------------------------------------------
print("\n>>> Training RandomForestClassifier ...")
X = master[FEATURES]
le = LabelEncoder()
y = le.fit_transform(master[TARGET])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=12,
    min_samples_leaf=2,
    class_weight='balanced',   # handles imbalanced classes
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# -----------------------------------------------------------------
# EVALUATE
# -----------------------------------------------------------------
acc = model.score(X_test, y_test)
print(f"\n[TARGET] Test Accuracy:  {acc*100:.2f}%")

cv_scores = cross_val_score(model, X, y, cv=5)
print(f"[CHART] 5-Fold CV Avg: {cv_scores.mean()*100:.2f}%  (±{cv_scores.std()*100:.2f}%)")

print("\n[REPORT] Classification Report:")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=le.classes_, zero_division=0))

print("\n🔑 Feature Importance (what daily habits matter most for your project):")
fi = sorted(zip(FEATURES, model.feature_importances_), key=lambda x: -x[1])
for feat, imp in fi:
    bar = '█' * int(imp * 50)
    print(f"   {feat:20s} {bar}  {imp:.3f}")

# -----------------------------------------------------------------
# SAVE
# -----------------------------------------------------------------
with open('health_model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'encoder': le}, f)

print("\n[OK]  health_model.pkl saved successfully!")
print("   → app.py will auto-load this on next restart.")
print("="*60 + "\n")