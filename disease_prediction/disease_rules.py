"""Disease rules for 500+ conditions across 20+ categories."""

DISEASE_RULES = {
    'Coronary Artery Disease': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 63, 'weight': 0.4},
            {'field': 'stress', 'op': '<', 'value': 140, 'weight': 0.39},
            {'field': 'sleep_hours', 'op': 'between', 'value': [21, 33], 'weight': 0.27},
            {'field': 'bp_sys', 'op': '<', 'value': 7, 'weight': 0.3},
            {'field': 'alcohol', 'op': '<', 'value': 140, 'weight': 0.39},
        ]
    },
    'Atrial Fibrillation': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 2, 'weight': 0.34},
            {'field': 'salt_intake', 'op': '<', 'value': 88, 'weight': 0.38},
            {'field': 'screen_time', 'op': '<', 'value': 87, 'weight': 0.19},
            {'field': 'bmi', 'op': '>', 'value': 92, 'weight': 0.25},
        ]
    },
    'Heart Failure': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'weight', 'op': '>=', 'value': 118, 'weight': 0.42},
            {'field': 'water_intake', 'op': '>', 'value': 97, 'weight': 0.49},
            {'field': 'bmi', 'op': 'between', 'value': [60, 89], 'weight': 0.22},
            {'field': 'bp_sys', 'op': 'between', 'value': [24, 35], 'weight': 0.18},
        ]
    },
    'Peripheral Artery Disease': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'activity_mins', 'op': '>=', 'value': 60, 'weight': 0.49},
            {'field': 'bmi', 'op': '<=', 'value': 94, 'weight': 0.21},
            {'field': 'stress', 'op': '>=', 'value': 69, 'weight': 0.24},
            {'field': 'salt_intake', 'op': '>', 'value': 44, 'weight': 0.34},
            {'field': 'smoking', 'op': '<', 'value': 98, 'weight': 0.17},
        ]
    },
    'Deep Vein Thrombosis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [40, 51], 'weight': 0.19},
            {'field': 'activity_mins', 'op': '>', 'value': 103, 'weight': 0.42},
            {'field': 'screen_time', 'op': '>', 'value': 146, 'weight': 0.18},
            {'field': 'bp_dias', 'op': '<', 'value': 102, 'weight': 0.36},
        ]
    },
    'Pulmonary Embolism': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'bp_dias', 'op': '<', 'value': 64, 'weight': 0.21},
            {'field': 'alcohol', 'op': 'between', 'value': [57, 80], 'weight': 0.32},
            {'field': 'height', 'op': '<=', 'value': 36, 'weight': 0.24},
            {'field': 'weight', 'op': '<=', 'value': 13, 'weight': 0.14},
            {'field': 'bmi', 'op': '<', 'value': 109, 'weight': 0.35},
        ]
    },
    'Aortic Aneurysm': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 120, 'weight': 0.25},
            {'field': 'weight', 'op': '>=', 'value': 3, 'weight': 0.49},
            {'field': 'alcohol', 'op': '>', 'value': 138, 'weight': 0.37},
            {'field': 'screen_time', 'op': '>=', 'value': 112, 'weight': 0.14},
            {'field': 'activity_mins', 'op': '<=', 'value': 68, 'weight': 0.1},
        ]
    },
    'Endocarditis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 28, 'weight': 0.3},
            {'field': 'height', 'op': '>=', 'value': 130, 'weight': 0.44},
            {'field': 'weight', 'op': '<', 'value': 42, 'weight': 0.16},
            {'field': 'water_intake', 'op': 'between', 'value': [58, 78], 'weight': 0.47},
            {'field': 'bp_dias', 'op': '>', 'value': 93, 'weight': 0.14},
        ]
    },
    'Myocarditis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'activity_mins', 'op': '>', 'value': 146, 'weight': 0.2},
            {'field': 'bmi', 'op': '>', 'value': 18, 'weight': 0.39},
            {'field': 'height', 'op': '<', 'value': 122, 'weight': 0.15},
            {'field': 'smoking', 'op': '<', 'value': 109, 'weight': 0.21},
        ]
    },
    'Pericarditis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 103, 'weight': 0.39},
            {'field': 'smoking', 'op': '>=', 'value': 133, 'weight': 0.28},
            {'field': 'bp_dias', 'op': '>', 'value': 17, 'weight': 0.2},
        ]
    },
    'Cardiomyopathy': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [57, 74], 'weight': 0.32},
            {'field': 'bmi', 'op': '>', 'value': 16, 'weight': 0.38},
            {'field': 'screen_time', 'op': '>', 'value': 85, 'weight': 0.46},
            {'field': 'activity_mins', 'op': 'between', 'value': [51, 67], 'weight': 0.2},
        ]
    },
    'Mitral Valve Prolapse': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'sleep_hours', 'op': 'between', 'value': [35, 60], 'weight': 0.33},
            {'field': 'salt_intake', 'op': '<=', 'value': 25, 'weight': 0.18},
            {'field': 'smoking', 'op': '<=', 'value': 106, 'weight': 0.24},
            {'field': 'water_intake', 'op': '>', 'value': 26, 'weight': 0.37},
            {'field': 'age', 'op': '<=', 'value': 28, 'weight': 0.39},
        ]
    },
    'Aortic Stenosis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'activity_mins', 'op': '<', 'value': 36, 'weight': 0.31},
            {'field': 'bp_dias', 'op': '<', 'value': 64, 'weight': 0.21},
            {'field': 'bmi', 'op': '<=', 'value': 141, 'weight': 0.42},
        ]
    },
    'Angina Pectoris': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [25, 42], 'weight': 0.43},
            {'field': 'activity_mins', 'op': '<=', 'value': 55, 'weight': 0.29},
            {'field': 'water_intake', 'op': '>', 'value': 1, 'weight': 0.17},
        ]
    },
    'Cardiac Arrhythmia': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 143, 'weight': 0.21},
            {'field': 'smoking', 'op': '<=', 'value': 76, 'weight': 0.16},
            {'field': 'activity_mins', 'op': '>', 'value': 139, 'weight': 0.33},
            {'field': 'age', 'op': '>=', 'value': 150, 'weight': 0.12},
        ]
    },
    'Bradycardia': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [52, 64], 'weight': 0.16},
            {'field': 'sleep_hours', 'op': '>', 'value': 61, 'weight': 0.34},
            {'field': 'bp_dias', 'op': '>', 'value': 146, 'weight': 0.48},
            {'field': 'stress', 'op': 'between', 'value': [59, 71], 'weight': 0.34},
        ]
    },
    'Tachycardia': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [40, 58], 'weight': 0.33},
            {'field': 'activity_mins', 'op': '>=', 'value': 102, 'weight': 0.2},
            {'field': 'sleep_hours', 'op': '>=', 'value': 19, 'weight': 0.28},
            {'field': 'age', 'op': '<=', 'value': 145, 'weight': 0.35},
        ]
    },
    'Atherosclerosis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [36, 50], 'weight': 0.19},
            {'field': 'bp_sys', 'op': '>', 'value': 95, 'weight': 0.45},
            {'field': 'screen_time', 'op': '<', 'value': 140, 'weight': 0.28},
        ]
    },
    'Varicose Veins': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'stress', 'op': 'between', 'value': [53, 63], 'weight': 0.49},
            {'field': 'smoking', 'op': 'between', 'value': [26, 40], 'weight': 0.22},
            {'field': 'screen_time', 'op': '>', 'value': 142, 'weight': 0.46},
            {'field': 'sleep_hours', 'op': '>=', 'value': 54, 'weight': 0.21},
            {'field': 'water_intake', 'op': '<', 'value': 68, 'weight': 0.37},
        ]
    },
    'Raynauds Disease': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 14, 'weight': 0.46},
            {'field': 'bmi', 'op': '<=', 'value': 12, 'weight': 0.43},
            {'field': 'age', 'op': '>=', 'value': 68, 'weight': 0.41},
            {'field': 'stress', 'op': '<=', 'value': 110, 'weight': 0.32},
            {'field': 'alcohol', 'op': '>', 'value': 39, 'weight': 0.14},
        ]
    },
    'Hypotension': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 38, 'weight': 0.33},
            {'field': 'bp_dias', 'op': '<', 'value': 94, 'weight': 0.12},
            {'field': 'bmi', 'op': '>=', 'value': 64, 'weight': 0.18},
            {'field': 'salt_intake', 'op': '>', 'value': 144, 'weight': 0.24},
            {'field': 'weight', 'op': 'between', 'value': [35, 50], 'weight': 0.4},
        ]
    },
    'Hypertensive Crisis': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'bp_sys', 'op': '>', 'value': 86, 'weight': 0.17},
            {'field': 'salt_intake', 'op': '<=', 'value': 64, 'weight': 0.42},
            {'field': 'stress', 'op': '<', 'value': 28, 'weight': 0.41},
        ]
    },
    'Rheumatic Heart Disease': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'salt_intake', 'op': '>', 'value': 57, 'weight': 0.44},
            {'field': 'activity_mins', 'op': '<=', 'value': 59, 'weight': 0.24},
            {'field': 'stress', 'op': '>', 'value': 103, 'weight': 0.36},
            {'field': 'bp_dias', 'op': '>=', 'value': 72, 'weight': 0.45},
        ]
    },
    'Congenital Heart Defect': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [54, 74], 'weight': 0.26},
            {'field': 'age', 'op': '>', 'value': 67, 'weight': 0.45},
            {'field': 'activity_mins', 'op': 'between', 'value': [36, 47], 'weight': 0.49},
            {'field': 'sleep_hours', 'op': 'between', 'value': [40, 63], 'weight': 0.27},
        ]
    },
    'Wolff-Parkinson-White': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 148, 'weight': 0.25},
            {'field': 'activity_mins', 'op': '>=', 'value': 112, 'weight': 0.12},
            {'field': 'age', 'op': 'between', 'value': [54, 70], 'weight': 0.47},
            {'field': 'bp_dias', 'op': '<=', 'value': 85, 'weight': 0.13},
            {'field': 'salt_intake', 'op': '>=', 'value': 32, 'weight': 0.37},
        ]
    },
    'Long QT Syndrome': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'stress', 'op': 'between', 'value': [46, 66], 'weight': 0.22},
            {'field': 'bp_dias', 'op': '>=', 'value': 50, 'weight': 0.32},
            {'field': 'water_intake', 'op': '<=', 'value': 45, 'weight': 0.37},
            {'field': 'alcohol', 'op': 'between', 'value': [55, 65], 'weight': 0.22},
            {'field': 'screen_time', 'op': '>=', 'value': 149, 'weight': 0.18},
        ]
    },
    'Takotsubo Cardiomyopathy': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 114, 'weight': 0.29},
            {'field': 'smoking', 'op': '<', 'value': 44, 'weight': 0.3},
            {'field': 'alcohol', 'op': '>', 'value': 86, 'weight': 0.21},
            {'field': 'bmi', 'op': '<', 'value': 58, 'weight': 0.37},
            {'field': 'stress', 'op': '<', 'value': 63, 'weight': 0.11},
        ]
    },
    'Cardiac Tamponade': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 148, 'weight': 0.28},
            {'field': 'activity_mins', 'op': '<=', 'value': 63, 'weight': 0.3},
            {'field': 'sleep_hours', 'op': '>', 'value': 28, 'weight': 0.46},
            {'field': 'water_intake', 'op': '<', 'value': 133, 'weight': 0.17},
        ]
    },
    'Pulmonary Hypertension': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [27, 51], 'weight': 0.2},
            {'field': 'activity_mins', 'op': '<=', 'value': 144, 'weight': 0.37},
            {'field': 'smoking', 'op': '>=', 'value': 114, 'weight': 0.48},
            {'field': 'alcohol', 'op': 'between', 'value': [55, 79], 'weight': 0.27},
        ]
    },
    'Hypertension': {
        'category': 'Cardiovascular', 'icon': 'fa-heartbeat',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 64, 'weight': 0.28},
            {'field': 'height', 'op': '>=', 'value': 134, 'weight': 0.41},
            {'field': 'bp_dias', 'op': '<', 'value': 20, 'weight': 0.21},
        ]
    },
    'Type 1 Diabetes': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 82, 'weight': 0.21},
            {'field': 'weight', 'op': '>', 'value': 60, 'weight': 0.16},
            {'field': 'bp_dias', 'op': '<', 'value': 17, 'weight': 0.38},
            {'field': 'water_intake', 'op': '<=', 'value': 120, 'weight': 0.23},
            {'field': 'height', 'op': '>', 'value': 108, 'weight': 0.18},
        ]
    },
    'Type 2 Diabetes': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'alcohol', 'op': 'between', 'value': [21, 49], 'weight': 0.48},
            {'field': 'bp_sys', 'op': '<=', 'value': 91, 'weight': 0.1},
            {'field': 'stress', 'op': '<=', 'value': 108, 'weight': 0.44},
            {'field': 'height', 'op': 'between', 'value': [34, 59], 'weight': 0.42},
        ]
    },
    'Gestational Diabetes': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 100, 'weight': 0.29},
            {'field': 'bp_sys', 'op': '<=', 'value': 120, 'weight': 0.39},
            {'field': 'sleep_hours', 'op': 'between', 'value': [45, 73], 'weight': 0.31},
        ]
    },
    'Prediabetes': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 110, 'weight': 0.13},
            {'field': 'sleep_hours', 'op': '<=', 'value': 67, 'weight': 0.17},
            {'field': 'bp_dias', 'op': '>=', 'value': 84, 'weight': 0.18},
            {'field': 'bp_sys', 'op': '<=', 'value': 108, 'weight': 0.21},
            {'field': 'screen_time', 'op': '>', 'value': 139, 'weight': 0.29},
        ]
    },
    'Metabolic Syndrome': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 11, 'weight': 0.36},
            {'field': 'salt_intake', 'op': '>', 'value': 52, 'weight': 0.48},
            {'field': 'age', 'op': 'between', 'value': [28, 53], 'weight': 0.16},
        ]
    },
    'Hypoglycemia': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [49, 67], 'weight': 0.48},
            {'field': 'salt_intake', 'op': '>=', 'value': 30, 'weight': 0.17},
            {'field': 'activity_mins', 'op': '>=', 'value': 7, 'weight': 0.14},
            {'field': 'bp_sys', 'op': 'between', 'value': [44, 66], 'weight': 0.37},
            {'field': 'screen_time', 'op': '>', 'value': 63, 'weight': 0.34},
        ]
    },
    'Diabetic Ketoacidosis': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'smoking', 'op': '>=', 'value': 31, 'weight': 0.44},
            {'field': 'salt_intake', 'op': 'between', 'value': [42, 69], 'weight': 0.41},
            {'field': 'bp_sys', 'op': '>=', 'value': 88, 'weight': 0.13},
        ]
    },
    'Diabetic Neuropathy': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 28, 'weight': 0.43},
            {'field': 'bp_sys', 'op': '>=', 'value': 118, 'weight': 0.35},
            {'field': 'alcohol', 'op': '<', 'value': 134, 'weight': 0.27},
        ]
    },
    'Diabetic Retinopathy': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'stress', 'op': 'between', 'value': [54, 79], 'weight': 0.42},
            {'field': 'water_intake', 'op': '<=', 'value': 69, 'weight': 0.43},
            {'field': 'bp_sys', 'op': '<', 'value': 23, 'weight': 0.43},
            {'field': 'screen_time', 'op': '<=', 'value': 119, 'weight': 0.2},
            {'field': 'salt_intake', 'op': 'between', 'value': [41, 51], 'weight': 0.37},
        ]
    },
    'Hyperglycemia': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'salt_intake', 'op': '>=', 'value': 55, 'weight': 0.17},
            {'field': 'screen_time', 'op': '>=', 'value': 71, 'weight': 0.24},
            {'field': 'weight', 'op': '>', 'value': 49, 'weight': 0.31},
            {'field': 'bmi', 'op': '<', 'value': 126, 'weight': 0.39},
        ]
    },
    'Insulin Resistance': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 126, 'weight': 0.38},
            {'field': 'bp_dias', 'op': '>', 'value': 57, 'weight': 0.14},
            {'field': 'bp_sys', 'op': '<', 'value': 149, 'weight': 0.22},
            {'field': 'screen_time', 'op': '<=', 'value': 89, 'weight': 0.32},
            {'field': 'weight', 'op': 'between', 'value': [49, 67], 'weight': 0.23},
        ]
    },
    'Cushings Syndrome': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 50, 'weight': 0.15},
            {'field': 'bp_sys', 'op': '>', 'value': 48, 'weight': 0.4},
            {'field': 'activity_mins', 'op': '<', 'value': 71, 'weight': 0.4},
            {'field': 'alcohol', 'op': 'between', 'value': [26, 42], 'weight': 0.34},
        ]
    },
    'Addisons Disease': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'activity_mins', 'op': '>=', 'value': 4, 'weight': 0.17},
            {'field': 'alcohol', 'op': 'between', 'value': [22, 33], 'weight': 0.15},
            {'field': 'weight', 'op': '>=', 'value': 33, 'weight': 0.38},
            {'field': 'salt_intake', 'op': '<=', 'value': 4, 'weight': 0.14},
        ]
    },
    'Phenylketonuria': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 88, 'weight': 0.29},
            {'field': 'sleep_hours', 'op': '>', 'value': 123, 'weight': 0.2},
            {'field': 'bmi', 'op': '>', 'value': 19, 'weight': 0.26},
            {'field': 'alcohol', 'op': '>', 'value': 145, 'weight': 0.16},
            {'field': 'bp_dias', 'op': '>', 'value': 31, 'weight': 0.5},
        ]
    },
    'Galactosemia': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'alcohol', 'op': '<=', 'value': 58, 'weight': 0.34},
            {'field': 'salt_intake', 'op': 'between', 'value': [48, 67], 'weight': 0.25},
            {'field': 'weight', 'op': '<=', 'value': 16, 'weight': 0.22},
            {'field': 'height', 'op': '>', 'value': 54, 'weight': 0.48},
            {'field': 'activity_mins', 'op': '>=', 'value': 41, 'weight': 0.36},
        ]
    },
    'Wilsons Disease': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'sleep_hours', 'op': 'between', 'value': [20, 43], 'weight': 0.13},
            {'field': 'water_intake', 'op': 'between', 'value': [22, 39], 'weight': 0.29},
            {'field': 'screen_time', 'op': '>=', 'value': 117, 'weight': 0.38},
        ]
    },
    'Hemochromatosis': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 51, 'weight': 0.47},
            {'field': 'bp_sys', 'op': '>', 'value': 39, 'weight': 0.32},
            {'field': 'stress', 'op': '<', 'value': 43, 'weight': 0.13},
        ]
    },
    'Porphyria': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'weight', 'op': 'between', 'value': [48, 61], 'weight': 0.47},
            {'field': 'bp_dias', 'op': '>=', 'value': 70, 'weight': 0.38},
            {'field': 'height', 'op': 'between', 'value': [25, 54], 'weight': 0.3},
            {'field': 'age', 'op': '<=', 'value': 65, 'weight': 0.39},
        ]
    },
    'Gout': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 148, 'weight': 0.48},
            {'field': 'height', 'op': '>', 'value': 69, 'weight': 0.5},
            {'field': 'smoking', 'op': '>', 'value': 45, 'weight': 0.41},
        ]
    },
    'Hyperuricemia': {
        'category': 'Metabolic', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'water_intake', 'op': '<=', 'value': 47, 'weight': 0.47},
            {'field': 'height', 'op': '<=', 'value': 126, 'weight': 0.35},
            {'field': 'bmi', 'op': '<=', 'value': 86, 'weight': 0.24},
            {'field': 'bp_sys', 'op': '>', 'value': 85, 'weight': 0.44},
        ]
    },
    'Asthma': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 103, 'weight': 0.22},
            {'field': 'salt_intake', 'op': 'between', 'value': [25, 45], 'weight': 0.11},
            {'field': 'stress', 'op': '>=', 'value': 104, 'weight': 0.15},
            {'field': 'weight', 'op': '>', 'value': 139, 'weight': 0.36},
        ]
    },
    'COPD': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'bp_sys', 'op': '>', 'value': 93, 'weight': 0.18},
            {'field': 'height', 'op': '<=', 'value': 14, 'weight': 0.35},
            {'field': 'activity_mins', 'op': '>=', 'value': 74, 'weight': 0.32},
            {'field': 'weight', 'op': '<=', 'value': 62, 'weight': 0.15},
        ]
    },
    'Chronic Bronchitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>=', 'value': 142, 'weight': 0.32},
            {'field': 'bp_dias', 'op': '>', 'value': 30, 'weight': 0.19},
            {'field': 'weight', 'op': '>', 'value': 40, 'weight': 0.36},
            {'field': 'height', 'op': '>=', 'value': 70, 'weight': 0.3},
            {'field': 'water_intake', 'op': '<=', 'value': 63, 'weight': 0.49},
        ]
    },
    'Emphysema': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 131, 'weight': 0.25},
            {'field': 'alcohol', 'op': '<', 'value': 71, 'weight': 0.45},
            {'field': 'bp_sys', 'op': '>=', 'value': 130, 'weight': 0.47},
            {'field': 'stress', 'op': '>', 'value': 77, 'weight': 0.21},
        ]
    },
    'Pneumonia': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 115, 'weight': 0.45},
            {'field': 'water_intake', 'op': '<=', 'value': 142, 'weight': 0.24},
            {'field': 'height', 'op': '<=', 'value': 83, 'weight': 0.28},
            {'field': 'activity_mins', 'op': '<', 'value': 60, 'weight': 0.33},
            {'field': 'bp_dias', 'op': '>', 'value': 122, 'weight': 0.23},
        ]
    },
    'Tuberculosis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'alcohol', 'op': '<=', 'value': 39, 'weight': 0.25},
            {'field': 'bp_dias', 'op': '>', 'value': 85, 'weight': 0.15},
            {'field': 'bmi', 'op': '<=', 'value': 117, 'weight': 0.14},
            {'field': 'age', 'op': '<', 'value': 40, 'weight': 0.26},
            {'field': 'activity_mins', 'op': '<=', 'value': 68, 'weight': 0.41},
        ]
    },
    'Lung Cancer': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 85, 'weight': 0.36},
            {'field': 'smoking', 'op': 'between', 'value': [40, 70], 'weight': 0.25},
            {'field': 'salt_intake', 'op': '<=', 'value': 10, 'weight': 0.45},
            {'field': 'height', 'op': '>', 'value': 74, 'weight': 0.19},
        ]
    },
    'Pulmonary Fibrosis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'smoking', 'op': '>', 'value': 26, 'weight': 0.27},
            {'field': 'salt_intake', 'op': '>', 'value': 77, 'weight': 0.28},
            {'field': 'age', 'op': '>', 'value': 15, 'weight': 0.23},
        ]
    },
    'Pleural Effusion': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 63, 'weight': 0.27},
            {'field': 'weight', 'op': '<=', 'value': 47, 'weight': 0.33},
            {'field': 'sleep_hours', 'op': '<', 'value': 98, 'weight': 0.13},
            {'field': 'alcohol', 'op': '<', 'value': 150, 'weight': 0.3},
        ]
    },
    'Pneumothorax': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 118, 'weight': 0.36},
            {'field': 'screen_time', 'op': '>', 'value': 120, 'weight': 0.46},
            {'field': 'bp_sys', 'op': 'between', 'value': [48, 69], 'weight': 0.16},
        ]
    },
    'Bronchiectasis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 117, 'weight': 0.38},
            {'field': 'screen_time', 'op': '<', 'value': 124, 'weight': 0.5},
            {'field': 'bmi', 'op': '<', 'value': 92, 'weight': 0.25},
            {'field': 'alcohol', 'op': '>=', 'value': 76, 'weight': 0.5},
            {'field': 'age', 'op': '<=', 'value': 145, 'weight': 0.21},
        ]
    },
    'Acute Respiratory Distress': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 128, 'weight': 0.46},
            {'field': 'stress', 'op': '<', 'value': 91, 'weight': 0.34},
            {'field': 'activity_mins', 'op': '<', 'value': 36, 'weight': 0.35},
            {'field': 'salt_intake', 'op': '>', 'value': 11, 'weight': 0.46},
            {'field': 'bp_sys', 'op': '<=', 'value': 94, 'weight': 0.11},
        ]
    },
    'Cystic Fibrosis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 84, 'weight': 0.46},
            {'field': 'alcohol', 'op': '<=', 'value': 34, 'weight': 0.17},
            {'field': 'weight', 'op': '>=', 'value': 70, 'weight': 0.31},
            {'field': 'activity_mins', 'op': '>=', 'value': 124, 'weight': 0.47},
            {'field': 'bp_sys', 'op': '>=', 'value': 120, 'weight': 0.42},
        ]
    },
    'Sarcoidosis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<', 'value': 102, 'weight': 0.44},
            {'field': 'salt_intake', 'op': 'between', 'value': [45, 55], 'weight': 0.25},
            {'field': 'screen_time', 'op': 'between', 'value': [43, 61], 'weight': 0.15},
        ]
    },
    'Silicosis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 60, 'weight': 0.14},
            {'field': 'water_intake', 'op': '>', 'value': 144, 'weight': 0.35},
            {'field': 'screen_time', 'op': 'between', 'value': [24, 54], 'weight': 0.19},
            {'field': 'height', 'op': '>=', 'value': 30, 'weight': 0.36},
            {'field': 'sleep_hours', 'op': '>', 'value': 78, 'weight': 0.48},
        ]
    },
    'Asbestosis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 138, 'weight': 0.19},
            {'field': 'activity_mins', 'op': '<=', 'value': 139, 'weight': 0.28},
            {'field': 'water_intake', 'op': 'between', 'value': [29, 52], 'weight': 0.4},
            {'field': 'salt_intake', 'op': '>', 'value': 105, 'weight': 0.43},
        ]
    },
    'Interstitial Lung Disease': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 114, 'weight': 0.19},
            {'field': 'stress', 'op': '>=', 'value': 95, 'weight': 0.14},
            {'field': 'height', 'op': '>=', 'value': 71, 'weight': 0.12},
            {'field': 'screen_time', 'op': '>', 'value': 117, 'weight': 0.48},
        ]
    },
    'Pulmonary Edema': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 6, 'weight': 0.36},
            {'field': 'age', 'op': '>=', 'value': 33, 'weight': 0.2},
            {'field': 'smoking', 'op': '<', 'value': 142, 'weight': 0.13},
        ]
    },
    'RSV Infection': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 60, 'weight': 0.43},
            {'field': 'screen_time', 'op': '<', 'value': 1, 'weight': 0.42},
            {'field': 'stress', 'op': '<', 'value': 139, 'weight': 0.5},
        ]
    },
    'Influenza Pneumonia': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 7, 'weight': 0.14},
            {'field': 'sleep_hours', 'op': '>', 'value': 61, 'weight': 0.24},
            {'field': 'height', 'op': '>=', 'value': 68, 'weight': 0.11},
            {'field': 'age', 'op': '<', 'value': 135, 'weight': 0.4},
        ]
    },
    'Allergic Rhinitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'smoking', 'op': '>', 'value': 93, 'weight': 0.29},
            {'field': 'water_intake', 'op': 'between', 'value': [52, 69], 'weight': 0.14},
            {'field': 'height', 'op': '>', 'value': 134, 'weight': 0.39},
        ]
    },
    'Sinusitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 123, 'weight': 0.12},
            {'field': 'bp_sys', 'op': '<=', 'value': 126, 'weight': 0.37},
            {'field': 'salt_intake', 'op': '<=', 'value': 21, 'weight': 0.13},
            {'field': 'screen_time', 'op': 'between', 'value': [28, 46], 'weight': 0.16},
        ]
    },
    'Laryngitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [40, 62], 'weight': 0.32},
            {'field': 'weight', 'op': 'between', 'value': [52, 81], 'weight': 0.22},
            {'field': 'bp_sys', 'op': '>', 'value': 30, 'weight': 0.42},
            {'field': 'salt_intake', 'op': 'between', 'value': [33, 56], 'weight': 0.39},
            {'field': 'water_intake', 'op': '<', 'value': 117, 'weight': 0.27},
        ]
    },
    'Pharyngitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'bp_sys', 'op': '>', 'value': 81, 'weight': 0.23},
            {'field': 'smoking', 'op': '>=', 'value': 40, 'weight': 0.25},
            {'field': 'alcohol', 'op': '<=', 'value': 22, 'weight': 0.13},
            {'field': 'bmi', 'op': '<=', 'value': 96, 'weight': 0.14},
        ]
    },
    'Tonsillitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 144, 'weight': 0.33},
            {'field': 'weight', 'op': '>=', 'value': 106, 'weight': 0.37},
            {'field': 'screen_time', 'op': '<=', 'value': 14, 'weight': 0.45},
        ]
    },
    'Epiglottitis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'weight', 'op': '>=', 'value': 148, 'weight': 0.24},
            {'field': 'water_intake', 'op': '<', 'value': 124, 'weight': 0.16},
            {'field': 'activity_mins', 'op': '>', 'value': 143, 'weight': 0.24},
            {'field': 'bp_sys', 'op': '>', 'value': 147, 'weight': 0.41},
        ]
    },
    'Croup': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'alcohol', 'op': '<=', 'value': 143, 'weight': 0.44},
            {'field': 'age', 'op': 'between', 'value': [37, 47], 'weight': 0.47},
            {'field': 'activity_mins', 'op': '>=', 'value': 80, 'weight': 0.38},
        ]
    },
    'Pertussis': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 37, 'weight': 0.17},
            {'field': 'height', 'op': '<=', 'value': 8, 'weight': 0.13},
            {'field': 'bmi', 'op': 'between', 'value': [46, 70], 'weight': 0.19},
            {'field': 'bp_dias', 'op': '<', 'value': 84, 'weight': 0.25},
        ]
    },
    'Legionnaires Disease': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 40, 'weight': 0.45},
            {'field': 'sleep_hours', 'op': 'between', 'value': [25, 43], 'weight': 0.12},
            {'field': 'water_intake', 'op': '<=', 'value': 114, 'weight': 0.29},
            {'field': 'bp_dias', 'op': '>=', 'value': 132, 'weight': 0.19},
            {'field': 'bmi', 'op': '>=', 'value': 73, 'weight': 0.27},
        ]
    },
    'Pleurisy': {
        'category': 'Respiratory', 'icon': 'fa-lungs',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [39, 50], 'weight': 0.29},
            {'field': 'activity_mins', 'op': '<=', 'value': 15, 'weight': 0.49},
            {'field': 'age', 'op': '<', 'value': 55, 'weight': 0.22},
            {'field': 'stress', 'op': '>=', 'value': 31, 'weight': 0.22},
            {'field': 'bmi', 'op': '<=', 'value': 45, 'weight': 0.4},
        ]
    },
    'Alzheimers Disease': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_sys', 'op': 'between', 'value': [52, 79], 'weight': 0.38},
            {'field': 'smoking', 'op': '>=', 'value': 11, 'weight': 0.13},
            {'field': 'bp_dias', 'op': '>', 'value': 20, 'weight': 0.28},
        ]
    },
    'Parkinsons Disease': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 107, 'weight': 0.33},
            {'field': 'stress', 'op': '>', 'value': 84, 'weight': 0.26},
            {'field': 'sleep_hours', 'op': 'between', 'value': [43, 55], 'weight': 0.28},
            {'field': 'water_intake', 'op': '>', 'value': 103, 'weight': 0.2},
        ]
    },
    'Multiple Sclerosis': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 87, 'weight': 0.45},
            {'field': 'stress', 'op': '>=', 'value': 20, 'weight': 0.41},
            {'field': 'height', 'op': '>', 'value': 50, 'weight': 0.31},
            {'field': 'bp_dias', 'op': '>=', 'value': 38, 'weight': 0.39},
            {'field': 'screen_time', 'op': '>', 'value': 51, 'weight': 0.16},
        ]
    },
    'Epilepsy': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 20, 'weight': 0.4},
            {'field': 'sleep_hours', 'op': '<=', 'value': 145, 'weight': 0.29},
            {'field': 'smoking', 'op': '<=', 'value': 145, 'weight': 0.37},
        ]
    },
    'Migraine': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [60, 80], 'weight': 0.23},
            {'field': 'sleep_hours', 'op': '<=', 'value': 114, 'weight': 0.13},
            {'field': 'alcohol', 'op': '>=', 'value': 15, 'weight': 0.42},
            {'field': 'bp_sys', 'op': 'between', 'value': [49, 73], 'weight': 0.13},
            {'field': 'age', 'op': '>', 'value': 74, 'weight': 0.25},
        ]
    },
    'Tension Headache': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 130, 'weight': 0.35},
            {'field': 'bp_sys', 'op': '<=', 'value': 11, 'weight': 0.33},
            {'field': 'water_intake', 'op': 'between', 'value': [40, 69], 'weight': 0.36},
        ]
    },
    'Cluster Headache': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 116, 'weight': 0.48},
            {'field': 'bmi', 'op': '>=', 'value': 22, 'weight': 0.49},
            {'field': 'height', 'op': '<', 'value': 113, 'weight': 0.12},
            {'field': 'weight', 'op': 'between', 'value': [30, 51], 'weight': 0.31},
        ]
    },
    'Ischemic Stroke': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 87, 'weight': 0.26},
            {'field': 'smoking', 'op': 'between', 'value': [60, 90], 'weight': 0.12},
            {'field': 'bp_sys', 'op': '>', 'value': 143, 'weight': 0.23},
            {'field': 'salt_intake', 'op': '<=', 'value': 39, 'weight': 0.21},
        ]
    },
    'Hemorrhagic Stroke': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [42, 61], 'weight': 0.37},
            {'field': 'smoking', 'op': '<=', 'value': 22, 'weight': 0.15},
            {'field': 'screen_time', 'op': 'between', 'value': [41, 55], 'weight': 0.25},
            {'field': 'salt_intake', 'op': 'between', 'value': [47, 73], 'weight': 0.14},
        ]
    },
    'Transient Ischemic Attack': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 55, 'weight': 0.22},
            {'field': 'bp_sys', 'op': '<=', 'value': 36, 'weight': 0.18},
            {'field': 'activity_mins', 'op': '>', 'value': 26, 'weight': 0.22},
            {'field': 'smoking', 'op': 'between', 'value': [53, 64], 'weight': 0.43},
        ]
    },
    'Bells Palsy': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'screen_time', 'op': 'between', 'value': [44, 58], 'weight': 0.15},
            {'field': 'sleep_hours', 'op': '<', 'value': 43, 'weight': 0.43},
            {'field': 'salt_intake', 'op': '<=', 'value': 94, 'weight': 0.12},
            {'field': 'alcohol', 'op': '<', 'value': 73, 'weight': 0.49},
            {'field': 'weight', 'op': '<', 'value': 80, 'weight': 0.31},
        ]
    },
    'Trigeminal Neuralgia': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 147, 'weight': 0.25},
            {'field': 'bp_dias', 'op': '<=', 'value': 98, 'weight': 0.41},
            {'field': 'weight', 'op': 'between', 'value': [30, 46], 'weight': 0.27},
            {'field': 'smoking', 'op': '<', 'value': 14, 'weight': 0.45},
        ]
    },
    'Meningitis': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 27, 'weight': 0.32},
            {'field': 'alcohol', 'op': 'between', 'value': [38, 50], 'weight': 0.44},
            {'field': 'sleep_hours', 'op': '>=', 'value': 132, 'weight': 0.28},
            {'field': 'activity_mins', 'op': '<=', 'value': 57, 'weight': 0.14},
            {'field': 'height', 'op': '>=', 'value': 107, 'weight': 0.47},
        ]
    },
    'Encephalitis': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_sys', 'op': 'between', 'value': [44, 56], 'weight': 0.25},
            {'field': 'screen_time', 'op': '<', 'value': 26, 'weight': 0.11},
            {'field': 'salt_intake', 'op': '>=', 'value': 36, 'weight': 0.42},
        ]
    },
    'Brain Tumor': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 36, 'weight': 0.38},
            {'field': 'salt_intake', 'op': '<=', 'value': 2, 'weight': 0.28},
            {'field': 'bmi', 'op': '>', 'value': 39, 'weight': 0.2},
        ]
    },
    'Myasthenia Gravis': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'smoking', 'op': 'between', 'value': [27, 46], 'weight': 0.31},
            {'field': 'activity_mins', 'op': '>=', 'value': 62, 'weight': 0.15},
            {'field': 'bp_dias', 'op': 'between', 'value': [27, 52], 'weight': 0.28},
            {'field': 'alcohol', 'op': 'between', 'value': [52, 80], 'weight': 0.11},
            {'field': 'stress', 'op': '<', 'value': 1, 'weight': 0.22},
        ]
    },
    'Guillain-Barre Syndrome': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 48, 'weight': 0.33},
            {'field': 'smoking', 'op': '>', 'value': 93, 'weight': 0.31},
            {'field': 'bmi', 'op': 'between', 'value': [52, 79], 'weight': 0.32},
            {'field': 'age', 'op': '<=', 'value': 12, 'weight': 0.45},
            {'field': 'weight', 'op': '>=', 'value': 5, 'weight': 0.2},
        ]
    },
    'ALS': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 27, 'weight': 0.24},
            {'field': 'salt_intake', 'op': 'between', 'value': [41, 55], 'weight': 0.39},
            {'field': 'age', 'op': '>=', 'value': 45, 'weight': 0.32},
            {'field': 'smoking', 'op': '<=', 'value': 123, 'weight': 0.49},
        ]
    },
    'Huntingtons Disease': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<', 'value': 118, 'weight': 0.13},
            {'field': 'age', 'op': '>=', 'value': 52, 'weight': 0.18},
            {'field': 'bmi', 'op': '>=', 'value': 132, 'weight': 0.47},
            {'field': 'weight', 'op': 'between', 'value': [22, 52], 'weight': 0.29},
            {'field': 'bp_sys', 'op': '>=', 'value': 13, 'weight': 0.24},
        ]
    },
    'Essential Tremor': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 95, 'weight': 0.15},
            {'field': 'bp_dias', 'op': '<=', 'value': 99, 'weight': 0.4},
            {'field': 'bp_sys', 'op': '<', 'value': 128, 'weight': 0.3},
            {'field': 'water_intake', 'op': 'between', 'value': [25, 48], 'weight': 0.21},
            {'field': 'bmi', 'op': '<=', 'value': 47, 'weight': 0.34},
        ]
    },
    'Cerebral Palsy': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '>=', 'value': 84, 'weight': 0.14},
            {'field': 'smoking', 'op': '>=', 'value': 110, 'weight': 0.22},
            {'field': 'sleep_hours', 'op': '<=', 'value': 11, 'weight': 0.24},
            {'field': 'bp_dias', 'op': 'between', 'value': [37, 67], 'weight': 0.5},
            {'field': 'age', 'op': '>', 'value': 104, 'weight': 0.37},
        ]
    },
    'Hydrocephalus': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 37, 'weight': 0.48},
            {'field': 'height', 'op': '<=', 'value': 18, 'weight': 0.11},
            {'field': 'activity_mins', 'op': '>=', 'value': 146, 'weight': 0.24},
            {'field': 'age', 'op': 'between', 'value': [48, 69], 'weight': 0.16},
        ]
    },
    'Peripheral Neuropathy': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 136, 'weight': 0.33},
            {'field': 'screen_time', 'op': '<=', 'value': 72, 'weight': 0.23},
            {'field': 'activity_mins', 'op': '>', 'value': 48, 'weight': 0.11},
            {'field': 'height', 'op': 'between', 'value': [55, 68], 'weight': 0.25},
        ]
    },
    'Sciatica': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 55, 'weight': 0.38},
            {'field': 'weight', 'op': '>=', 'value': 126, 'weight': 0.38},
            {'field': 'activity_mins', 'op': '>', 'value': 19, 'weight': 0.15},
            {'field': 'water_intake', 'op': '<', 'value': 114, 'weight': 0.46},
        ]
    },
    'Carpal Tunnel Syndrome': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 17, 'weight': 0.37},
            {'field': 'water_intake', 'op': 'between', 'value': [39, 54], 'weight': 0.22},
            {'field': 'salt_intake', 'op': '<', 'value': 131, 'weight': 0.42},
        ]
    },
    'Narcolepsy': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 61, 'weight': 0.42},
            {'field': 'salt_intake', 'op': '<=', 'value': 142, 'weight': 0.11},
            {'field': 'height', 'op': '>=', 'value': 142, 'weight': 0.29},
        ]
    },
    'Restless Legs Syndrome': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 102, 'weight': 0.13},
            {'field': 'alcohol', 'op': '<=', 'value': 105, 'weight': 0.31},
            {'field': 'height', 'op': '>', 'value': 82, 'weight': 0.15},
        ]
    },
    'Vertigo BPPV': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 133, 'weight': 0.29},
            {'field': 'bp_sys', 'op': '<', 'value': 142, 'weight': 0.45},
            {'field': 'alcohol', 'op': 'between', 'value': [28, 51], 'weight': 0.17},
            {'field': 'height', 'op': '>', 'value': 133, 'weight': 0.43},
            {'field': 'activity_mins', 'op': '>=', 'value': 83, 'weight': 0.17},
        ]
    },
    'Menieres Disease': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'activity_mins', 'op': '>=', 'value': 133, 'weight': 0.48},
            {'field': 'screen_time', 'op': '>', 'value': 142, 'weight': 0.2},
            {'field': 'bp_sys', 'op': '<', 'value': 137, 'weight': 0.35},
            {'field': 'bmi', 'op': 'between', 'value': [57, 85], 'weight': 0.36},
            {'field': 'stress', 'op': '<', 'value': 87, 'weight': 0.36},
        ]
    },
    'Concussion': {
        'category': 'Neurological', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 148, 'weight': 0.13},
            {'field': 'screen_time', 'op': '<', 'value': 107, 'weight': 0.41},
            {'field': 'smoking', 'op': '>', 'value': 140, 'weight': 0.3},
            {'field': 'bp_sys', 'op': '>=', 'value': 104, 'weight': 0.29},
            {'field': 'bp_dias', 'op': '<=', 'value': 16, 'weight': 0.13},
        ]
    },
    'Major Depression': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 53, 'weight': 0.29},
            {'field': 'screen_time', 'op': 'between', 'value': [40, 61], 'weight': 0.16},
            {'field': 'water_intake', 'op': '<', 'value': 132, 'weight': 0.4},
        ]
    },
    'Bipolar Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 32, 'weight': 0.2},
            {'field': 'screen_time', 'op': '<=', 'value': 25, 'weight': 0.2},
            {'field': 'age', 'op': '>=', 'value': 108, 'weight': 0.48},
            {'field': 'bp_sys', 'op': '<', 'value': 148, 'weight': 0.43},
            {'field': 'weight', 'op': '<', 'value': 128, 'weight': 0.41},
        ]
    },
    'Generalized Anxiety': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 128, 'weight': 0.45},
            {'field': 'age', 'op': '>', 'value': 130, 'weight': 0.48},
            {'field': 'weight', 'op': '<', 'value': 91, 'weight': 0.19},
            {'field': 'bmi', 'op': '>', 'value': 121, 'weight': 0.21},
            {'field': 'bp_sys', 'op': 'between', 'value': [26, 49], 'weight': 0.1},
        ]
    },
    'Panic Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '>=', 'value': 94, 'weight': 0.41},
            {'field': 'age', 'op': '<=', 'value': 144, 'weight': 0.12},
            {'field': 'screen_time', 'op': '>=', 'value': 19, 'weight': 0.32},
        ]
    },
    'Social Anxiety': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'water_intake', 'op': '<=', 'value': 72, 'weight': 0.41},
            {'field': 'height', 'op': 'between', 'value': [26, 48], 'weight': 0.15},
            {'field': 'screen_time', 'op': '>=', 'value': 94, 'weight': 0.32},
            {'field': 'sleep_hours', 'op': '<', 'value': 103, 'weight': 0.34},
        ]
    },
    'OCD': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 86, 'weight': 0.12},
            {'field': 'salt_intake', 'op': '<=', 'value': 39, 'weight': 0.31},
            {'field': 'height', 'op': 'between', 'value': [59, 79], 'weight': 0.16},
            {'field': 'activity_mins', 'op': '<=', 'value': 77, 'weight': 0.5},
            {'field': 'alcohol', 'op': '>=', 'value': 131, 'weight': 0.3},
        ]
    },
    'PTSD': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_dias', 'op': 'between', 'value': [21, 42], 'weight': 0.22},
            {'field': 'screen_time', 'op': '>', 'value': 150, 'weight': 0.49},
            {'field': 'stress', 'op': '>', 'value': 68, 'weight': 0.34},
            {'field': 'salt_intake', 'op': 'between', 'value': [23, 51], 'weight': 0.33},
            {'field': 'height', 'op': '<', 'value': 98, 'weight': 0.31},
        ]
    },
    'Schizophrenia': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 29, 'weight': 0.11},
            {'field': 'activity_mins', 'op': '>', 'value': 108, 'weight': 0.28},
            {'field': 'sleep_hours', 'op': '<=', 'value': 106, 'weight': 0.38},
        ]
    },
    'ADHD': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'alcohol', 'op': 'between', 'value': [23, 37], 'weight': 0.47},
            {'field': 'water_intake', 'op': '<', 'value': 123, 'weight': 0.32},
            {'field': 'weight', 'op': '<=', 'value': 45, 'weight': 0.23},
            {'field': 'bp_dias', 'op': 'between', 'value': [42, 72], 'weight': 0.24},
            {'field': 'stress', 'op': 'between', 'value': [35, 53], 'weight': 0.29},
        ]
    },
    'Autism Spectrum': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 77, 'weight': 0.48},
            {'field': 'salt_intake', 'op': '>=', 'value': 126, 'weight': 0.38},
            {'field': 'bp_sys', 'op': '<=', 'value': 71, 'weight': 0.24},
            {'field': 'screen_time', 'op': '>', 'value': 140, 'weight': 0.33},
            {'field': 'weight', 'op': '<=', 'value': 38, 'weight': 0.43},
        ]
    },
    'Borderline Personality': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 21, 'weight': 0.48},
            {'field': 'bp_sys', 'op': '<=', 'value': 123, 'weight': 0.36},
            {'field': 'stress', 'op': '<', 'value': 70, 'weight': 0.43},
            {'field': 'smoking', 'op': '>=', 'value': 62, 'weight': 0.15},
        ]
    },
    'Anorexia Nervosa': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [34, 45], 'weight': 0.19},
            {'field': 'sleep_hours', 'op': '<=', 'value': 121, 'weight': 0.23},
            {'field': 'activity_mins', 'op': '<', 'value': 141, 'weight': 0.1},
        ]
    },
    'Bulimia Nervosa': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 52, 'weight': 0.29},
            {'field': 'salt_intake', 'op': '>=', 'value': 16, 'weight': 0.23},
            {'field': 'bmi', 'op': 'between', 'value': [22, 37], 'weight': 0.19},
        ]
    },
    'Insomnia Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 10, 'weight': 0.47},
            {'field': 'bp_sys', 'op': '<=', 'value': 75, 'weight': 0.17},
            {'field': 'age', 'op': '>', 'value': 28, 'weight': 0.22},
            {'field': 'bp_dias', 'op': '>=', 'value': 140, 'weight': 0.28},
        ]
    },
    'Seasonal Affective Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bp_dias', 'op': '<', 'value': 120, 'weight': 0.44},
            {'field': 'stress', 'op': '<', 'value': 85, 'weight': 0.42},
            {'field': 'sleep_hours', 'op': '<=', 'value': 48, 'weight': 0.36},
            {'field': 'age', 'op': '>=', 'value': 146, 'weight': 0.42},
            {'field': 'bp_sys', 'op': '<', 'value': 104, 'weight': 0.34},
        ]
    },
    'Substance Use Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'water_intake', 'op': '>=', 'value': 25, 'weight': 0.13},
            {'field': 'sleep_hours', 'op': '<', 'value': 64, 'weight': 0.29},
            {'field': 'age', 'op': '>=', 'value': 115, 'weight': 0.25},
            {'field': 'bp_sys', 'op': '>=', 'value': 147, 'weight': 0.22},
        ]
    },
    'Agoraphobia': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '>=', 'value': 16, 'weight': 0.38},
            {'field': 'smoking', 'op': '>', 'value': 41, 'weight': 0.29},
            {'field': 'bp_dias', 'op': 'between', 'value': [39, 52], 'weight': 0.47},
        ]
    },
    'Dissociative Identity': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'stress', 'op': '>=', 'value': 57, 'weight': 0.35},
            {'field': 'sleep_hours', 'op': '<=', 'value': 96, 'weight': 0.16},
            {'field': 'water_intake', 'op': 'between', 'value': [54, 70], 'weight': 0.47},
            {'field': 'screen_time', 'op': 'between', 'value': [25, 51], 'weight': 0.45},
            {'field': 'smoking', 'op': 'between', 'value': [24, 52], 'weight': 0.38},
        ]
    },
    'Adjustment Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [32, 60], 'weight': 0.46},
            {'field': 'weight', 'op': '<', 'value': 134, 'weight': 0.17},
            {'field': 'water_intake', 'op': '>', 'value': 150, 'weight': 0.37},
        ]
    },
    'Somatoform Disorder': {
        'category': 'Mental Health', 'icon': 'fa-brain',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [23, 47], 'weight': 0.28},
            {'field': 'activity_mins', 'op': 'between', 'value': [56, 67], 'weight': 0.27},
            {'field': 'height', 'op': '<=', 'value': 79, 'weight': 0.37},
            {'field': 'age', 'op': '<=', 'value': 1, 'weight': 0.2},
        ]
    },
    'Osteoarthritis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'activity_mins', 'op': 'between', 'value': [47, 68], 'weight': 0.13},
            {'field': 'alcohol', 'op': '>', 'value': 16, 'weight': 0.32},
            {'field': 'bmi', 'op': '<=', 'value': 105, 'weight': 0.11},
            {'field': 'stress', 'op': '<', 'value': 108, 'weight': 0.41},
            {'field': 'water_intake', 'op': '<=', 'value': 97, 'weight': 0.28},
        ]
    },
    'Rheumatoid Arthritis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [42, 55], 'weight': 0.15},
            {'field': 'activity_mins', 'op': 'between', 'value': [28, 45], 'weight': 0.26},
            {'field': 'age', 'op': '>', 'value': 119, 'weight': 0.49},
            {'field': 'salt_intake', 'op': 'between', 'value': [44, 61], 'weight': 0.27},
        ]
    },
    'Osteoporosis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 49, 'weight': 0.16},
            {'field': 'alcohol', 'op': '>', 'value': 108, 'weight': 0.11},
            {'field': 'height', 'op': '>', 'value': 18, 'weight': 0.2},
        ]
    },
    'Fibromyalgia': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 13, 'weight': 0.28},
            {'field': 'activity_mins', 'op': '>', 'value': 60, 'weight': 0.26},
            {'field': 'height', 'op': '<', 'value': 15, 'weight': 0.4},
        ]
    },
    'Lupus SLE': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'water_intake', 'op': '>=', 'value': 148, 'weight': 0.19},
            {'field': 'screen_time', 'op': 'between', 'value': [40, 57], 'weight': 0.34},
            {'field': 'stress', 'op': '<', 'value': 134, 'weight': 0.49},
        ]
    },
    'Ankylosing Spondylitis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 143, 'weight': 0.21},
            {'field': 'height', 'op': '<', 'value': 110, 'weight': 0.35},
            {'field': 'weight', 'op': '<=', 'value': 89, 'weight': 0.12},
        ]
    },
    'Gout Arthritis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 82, 'weight': 0.41},
            {'field': 'alcohol', 'op': '<=', 'value': 77, 'weight': 0.26},
            {'field': 'bp_sys', 'op': '<', 'value': 122, 'weight': 0.4},
            {'field': 'activity_mins', 'op': '<', 'value': 37, 'weight': 0.22},
            {'field': 'weight', 'op': '>', 'value': 107, 'weight': 0.32},
        ]
    },
    'Tendinitis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 66, 'weight': 0.26},
            {'field': 'activity_mins', 'op': '>=', 'value': 116, 'weight': 0.36},
            {'field': 'bp_sys', 'op': '>', 'value': 49, 'weight': 0.31},
            {'field': 'age', 'op': '>=', 'value': 11, 'weight': 0.25},
            {'field': 'sleep_hours', 'op': '<', 'value': 144, 'weight': 0.42},
        ]
    },
    'Bursitis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'bp_dias', 'op': '<', 'value': 86, 'weight': 0.45},
            {'field': 'stress', 'op': '>', 'value': 49, 'weight': 0.18},
            {'field': 'salt_intake', 'op': '>', 'value': 123, 'weight': 0.4},
        ]
    },
    'Carpal Tunnel': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'smoking', 'op': 'between', 'value': [45, 62], 'weight': 0.38},
            {'field': 'water_intake', 'op': '>=', 'value': 98, 'weight': 0.41},
            {'field': 'bp_dias', 'op': 'between', 'value': [39, 57], 'weight': 0.36},
        ]
    },
    'Plantar Fasciitis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'water_intake', 'op': '<=', 'value': 121, 'weight': 0.29},
            {'field': 'salt_intake', 'op': '>=', 'value': 95, 'weight': 0.47},
            {'field': 'screen_time', 'op': '<=', 'value': 57, 'weight': 0.12},
            {'field': 'sleep_hours', 'op': '>', 'value': 150, 'weight': 0.2},
        ]
    },
    'Rotator Cuff Injury': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 51, 'weight': 0.22},
            {'field': 'screen_time', 'op': '<', 'value': 63, 'weight': 0.25},
            {'field': 'water_intake', 'op': 'between', 'value': [41, 59], 'weight': 0.36},
            {'field': 'weight', 'op': '<=', 'value': 91, 'weight': 0.28},
            {'field': 'sleep_hours', 'op': '<', 'value': 126, 'weight': 0.39},
        ]
    },
    'Herniated Disc': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 20, 'weight': 0.31},
            {'field': 'smoking', 'op': '>', 'value': 106, 'weight': 0.41},
            {'field': 'sleep_hours', 'op': '<', 'value': 39, 'weight': 0.13},
        ]
    },
    'Spinal Stenosis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'activity_mins', 'op': 'between', 'value': [23, 52], 'weight': 0.28},
            {'field': 'smoking', 'op': 'between', 'value': [51, 61], 'weight': 0.47},
            {'field': 'age', 'op': 'between', 'value': [20, 30], 'weight': 0.32},
        ]
    },
    'Scoliosis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'smoking', 'op': '>=', 'value': 74, 'weight': 0.31},
            {'field': 'age', 'op': 'between', 'value': [47, 62], 'weight': 0.43},
            {'field': 'sleep_hours', 'op': '>', 'value': 62, 'weight': 0.31},
            {'field': 'screen_time', 'op': 'between', 'value': [42, 60], 'weight': 0.31},
            {'field': 'weight', 'op': '>', 'value': 104, 'weight': 0.25},
        ]
    },
    'Osteomyelitis': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 58, 'weight': 0.5},
            {'field': 'stress', 'op': '>', 'value': 9, 'weight': 0.36},
            {'field': 'bmi', 'op': '<=', 'value': 142, 'weight': 0.25},
            {'field': 'height', 'op': '>', 'value': 44, 'weight': 0.35},
        ]
    },
    'Pagets Disease': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 85, 'weight': 0.36},
            {'field': 'height', 'op': '>', 'value': 11, 'weight': 0.46},
            {'field': 'activity_mins', 'op': '<', 'value': 146, 'weight': 0.46},
        ]
    },
    'Rickets': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'stress', 'op': '>', 'value': 72, 'weight': 0.47},
            {'field': 'weight', 'op': 'between', 'value': [31, 51], 'weight': 0.36},
            {'field': 'age', 'op': '<', 'value': 102, 'weight': 0.33},
            {'field': 'sleep_hours', 'op': '>=', 'value': 62, 'weight': 0.16},
        ]
    },
    'Polymyalgia Rheumatica': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 139, 'weight': 0.37},
            {'field': 'screen_time', 'op': '<=', 'value': 36, 'weight': 0.4},
            {'field': 'alcohol', 'op': '>', 'value': 89, 'weight': 0.3},
            {'field': 'age', 'op': '>', 'value': 20, 'weight': 0.27},
            {'field': 'bp_dias', 'op': 'between', 'value': [58, 80], 'weight': 0.41},
        ]
    },
    'Myofascial Pain': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 116, 'weight': 0.41},
            {'field': 'water_intake', 'op': '<', 'value': 97, 'weight': 0.24},
            {'field': 'bp_dias', 'op': '<', 'value': 98, 'weight': 0.37},
            {'field': 'sleep_hours', 'op': 'between', 'value': [35, 47], 'weight': 0.22},
        ]
    },
    'Frozen Shoulder': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 40, 'weight': 0.25},
            {'field': 'alcohol', 'op': '<=', 'value': 28, 'weight': 0.23},
            {'field': 'bmi', 'op': '>', 'value': 114, 'weight': 0.48},
        ]
    },
    'Tennis Elbow': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 23, 'weight': 0.14},
            {'field': 'sleep_hours', 'op': '<=', 'value': 143, 'weight': 0.28},
            {'field': 'weight', 'op': '<=', 'value': 23, 'weight': 0.14},
            {'field': 'bp_sys', 'op': 'between', 'value': [58, 78], 'weight': 0.14},
        ]
    },
    'Golfers Elbow': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 22, 'weight': 0.27},
            {'field': 'alcohol', 'op': 'between', 'value': [35, 63], 'weight': 0.46},
            {'field': 'weight', 'op': '<', 'value': 44, 'weight': 0.37},
            {'field': 'activity_mins', 'op': '>=', 'value': 127, 'weight': 0.22},
        ]
    },
    'Shin Splints': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 108, 'weight': 0.27},
            {'field': 'screen_time', 'op': '<=', 'value': 93, 'weight': 0.41},
            {'field': 'bp_sys', 'op': '<', 'value': 127, 'weight': 0.39},
        ]
    },
    'Stress Fracture': {
        'category': 'Musculoskeletal', 'icon': 'fa-bone',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 35, 'weight': 0.28},
            {'field': 'stress', 'op': '>', 'value': 86, 'weight': 0.48},
            {'field': 'smoking', 'op': '<=', 'value': 85, 'weight': 0.42},
            {'field': 'water_intake', 'op': '>=', 'value': 35, 'weight': 0.27},
            {'field': 'screen_time', 'op': '>=', 'value': 52, 'weight': 0.34},
        ]
    },
    'GERD': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 82, 'weight': 0.49},
            {'field': 'stress', 'op': '<=', 'value': 63, 'weight': 0.49},
            {'field': 'bp_dias', 'op': '<=', 'value': 101, 'weight': 0.21},
            {'field': 'water_intake', 'op': '>', 'value': 52, 'weight': 0.47},
        ]
    },
    'Peptic Ulcer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 141, 'weight': 0.37},
            {'field': 'age', 'op': '<=', 'value': 54, 'weight': 0.48},
            {'field': 'weight', 'op': '>=', 'value': 18, 'weight': 0.43},
            {'field': 'bp_dias', 'op': '<=', 'value': 78, 'weight': 0.16},
            {'field': 'stress', 'op': '>=', 'value': 109, 'weight': 0.36},
        ]
    },
    'Gastritis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 123, 'weight': 0.5},
            {'field': 'height', 'op': '<=', 'value': 108, 'weight': 0.31},
            {'field': 'weight', 'op': '>', 'value': 93, 'weight': 0.42},
            {'field': 'smoking', 'op': 'between', 'value': [25, 38], 'weight': 0.36},
        ]
    },
    'Irritable Bowel Syndrome': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 12, 'weight': 0.17},
            {'field': 'weight', 'op': '<=', 'value': 85, 'weight': 0.49},
            {'field': 'bp_sys', 'op': '>', 'value': 67, 'weight': 0.1},
        ]
    },
    'Crohns Disease': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [56, 73], 'weight': 0.32},
            {'field': 'bp_dias', 'op': '>=', 'value': 129, 'weight': 0.26},
            {'field': 'sleep_hours', 'op': '>=', 'value': 124, 'weight': 0.5},
        ]
    },
    'Ulcerative Colitis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 22, 'weight': 0.47},
            {'field': 'bmi', 'op': '<', 'value': 88, 'weight': 0.24},
            {'field': 'weight', 'op': '<', 'value': 90, 'weight': 0.31},
        ]
    },
    'Celiac Disease': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 116, 'weight': 0.39},
            {'field': 'bp_sys', 'op': '>', 'value': 30, 'weight': 0.22},
            {'field': 'age', 'op': '>=', 'value': 43, 'weight': 0.36},
            {'field': 'screen_time', 'op': 'between', 'value': [30, 50], 'weight': 0.17},
        ]
    },
    'Diverticulitis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 104, 'weight': 0.19},
            {'field': 'smoking', 'op': '<', 'value': 111, 'weight': 0.17},
            {'field': 'bp_dias', 'op': '>', 'value': 51, 'weight': 0.39},
            {'field': 'weight', 'op': 'between', 'value': [20, 36], 'weight': 0.27},
            {'field': 'activity_mins', 'op': '>=', 'value': 17, 'weight': 0.4},
        ]
    },
    'Appendicitis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [40, 56], 'weight': 0.17},
            {'field': 'water_intake', 'op': '>', 'value': 126, 'weight': 0.2},
            {'field': 'height', 'op': '>=', 'value': 101, 'weight': 0.34},
            {'field': 'alcohol', 'op': '>', 'value': 118, 'weight': 0.24},
            {'field': 'salt_intake', 'op': '<', 'value': 77, 'weight': 0.43},
        ]
    },
    'Gallstones': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 81, 'weight': 0.37},
            {'field': 'bmi', 'op': '<', 'value': 47, 'weight': 0.22},
            {'field': 'bp_sys', 'op': '<', 'value': 108, 'weight': 0.3},
            {'field': 'alcohol', 'op': '<', 'value': 109, 'weight': 0.33},
            {'field': 'activity_mins', 'op': '<=', 'value': 45, 'weight': 0.35},
        ]
    },
    'Pancreatitis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<=', 'value': 48, 'weight': 0.22},
            {'field': 'bp_sys', 'op': '<=', 'value': 92, 'weight': 0.35},
            {'field': 'age', 'op': '<=', 'value': 99, 'weight': 0.15},
            {'field': 'smoking', 'op': 'between', 'value': [46, 71], 'weight': 0.36},
            {'field': 'weight', 'op': '<=', 'value': 22, 'weight': 0.3},
        ]
    },
    'Hepatitis A': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 71, 'weight': 0.22},
            {'field': 'stress', 'op': 'between', 'value': [49, 77], 'weight': 0.22},
            {'field': 'salt_intake', 'op': '<=', 'value': 29, 'weight': 0.32},
            {'field': 'smoking', 'op': '>', 'value': 140, 'weight': 0.21},
            {'field': 'bp_dias', 'op': 'between', 'value': [22, 46], 'weight': 0.43},
        ]
    },
    'Hepatitis B': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 64, 'weight': 0.14},
            {'field': 'screen_time', 'op': '>', 'value': 90, 'weight': 0.28},
            {'field': 'bmi', 'op': '<=', 'value': 31, 'weight': 0.45},
            {'field': 'bp_sys', 'op': '<', 'value': 90, 'weight': 0.42},
            {'field': 'salt_intake', 'op': '<=', 'value': 36, 'weight': 0.17},
        ]
    },
    'Hepatitis C': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 146, 'weight': 0.42},
            {'field': 'screen_time', 'op': 'between', 'value': [54, 69], 'weight': 0.21},
            {'field': 'bp_sys', 'op': '>=', 'value': 69, 'weight': 0.22},
        ]
    },
    'Cirrhosis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 106, 'weight': 0.15},
            {'field': 'age', 'op': '>=', 'value': 33, 'weight': 0.45},
            {'field': 'salt_intake', 'op': '<', 'value': 83, 'weight': 0.2},
            {'field': 'stress', 'op': '<=', 'value': 148, 'weight': 0.3},
            {'field': 'bp_sys', 'op': '<=', 'value': 20, 'weight': 0.25},
        ]
    },
    'Fatty Liver Disease': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 72, 'weight': 0.26},
            {'field': 'smoking', 'op': '>=', 'value': 125, 'weight': 0.28},
            {'field': 'screen_time', 'op': 'between', 'value': [25, 49], 'weight': 0.1},
            {'field': 'salt_intake', 'op': '>=', 'value': 137, 'weight': 0.44},
            {'field': 'bp_dias', 'op': '<', 'value': 55, 'weight': 0.49},
        ]
    },
    'Gastroparesis': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'stress', 'op': '>=', 'value': 87, 'weight': 0.43},
            {'field': 'weight', 'op': 'between', 'value': [51, 71], 'weight': 0.15},
            {'field': 'alcohol', 'op': '>', 'value': 118, 'weight': 0.12},
            {'field': 'age', 'op': '>', 'value': 41, 'weight': 0.47},
        ]
    },
    'Lactose Intolerance': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 110, 'weight': 0.5},
            {'field': 'activity_mins', 'op': '<', 'value': 78, 'weight': 0.45},
            {'field': 'sleep_hours', 'op': '>=', 'value': 93, 'weight': 0.14},
            {'field': 'bp_sys', 'op': '>', 'value': 43, 'weight': 0.25},
        ]
    },
    'Food Poisoning': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 60, 'weight': 0.39},
            {'field': 'bp_dias', 'op': '>', 'value': 1, 'weight': 0.38},
            {'field': 'activity_mins', 'op': '<=', 'value': 58, 'weight': 0.13},
        ]
    },
    'C Difficile Infection': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 88, 'weight': 0.1},
            {'field': 'bmi', 'op': '<=', 'value': 123, 'weight': 0.38},
            {'field': 'sleep_hours', 'op': '<', 'value': 27, 'weight': 0.25},
            {'field': 'activity_mins', 'op': '>=', 'value': 77, 'weight': 0.25},
            {'field': 'screen_time', 'op': '<=', 'value': 35, 'weight': 0.41},
        ]
    },
    'Hemorrhoids': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 145, 'weight': 0.13},
            {'field': 'age', 'op': 'between', 'value': [48, 69], 'weight': 0.36},
            {'field': 'salt_intake', 'op': '<', 'value': 39, 'weight': 0.35},
            {'field': 'bp_dias', 'op': 'between', 'value': [33, 45], 'weight': 0.37},
            {'field': 'sleep_hours', 'op': '<', 'value': 99, 'weight': 0.4},
        ]
    },
    'Anal Fissure': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 64, 'weight': 0.42},
            {'field': 'stress', 'op': '>', 'value': 73, 'weight': 0.2},
            {'field': 'salt_intake', 'op': '>', 'value': 78, 'weight': 0.44},
            {'field': 'activity_mins', 'op': 'between', 'value': [32, 54], 'weight': 0.34},
        ]
    },
    'Colorectal Cancer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 62, 'weight': 0.41},
            {'field': 'bp_dias', 'op': '<=', 'value': 128, 'weight': 0.15},
            {'field': 'alcohol', 'op': 'between', 'value': [20, 41], 'weight': 0.13},
            {'field': 'screen_time', 'op': '<', 'value': 146, 'weight': 0.25},
        ]
    },
    'Esophageal Cancer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'screen_time', 'op': 'between', 'value': [50, 62], 'weight': 0.37},
            {'field': 'age', 'op': 'between', 'value': [36, 52], 'weight': 0.13},
            {'field': 'bmi', 'op': '>', 'value': 102, 'weight': 0.48},
            {'field': 'smoking', 'op': '>=', 'value': 129, 'weight': 0.35},
        ]
    },
    'Stomach Cancer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 138, 'weight': 0.13},
            {'field': 'weight', 'op': 'between', 'value': [25, 44], 'weight': 0.16},
            {'field': 'bmi', 'op': 'between', 'value': [29, 56], 'weight': 0.47},
            {'field': 'bp_dias', 'op': '<=', 'value': 17, 'weight': 0.33},
        ]
    },
    'Pancreatic Cancer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 62, 'weight': 0.39},
            {'field': 'age', 'op': '<', 'value': 112, 'weight': 0.13},
            {'field': 'sleep_hours', 'op': '<=', 'value': 15, 'weight': 0.34},
            {'field': 'bp_sys', 'op': '<', 'value': 36, 'weight': 0.15},
        ]
    },
    'Liver Cancer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 89, 'weight': 0.3},
            {'field': 'weight', 'op': 'between', 'value': [36, 51], 'weight': 0.41},
            {'field': 'bp_sys', 'op': '<', 'value': 69, 'weight': 0.4},
            {'field': 'sleep_hours', 'op': '>', 'value': 110, 'weight': 0.23},
            {'field': 'bp_dias', 'op': 'between', 'value': [56, 86], 'weight': 0.13},
        ]
    },
    'Bile Duct Cancer': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 15, 'weight': 0.3},
            {'field': 'water_intake', 'op': 'between', 'value': [30, 48], 'weight': 0.17},
            {'field': 'bmi', 'op': 'between', 'value': [27, 44], 'weight': 0.37},
        ]
    },
    'Small Bowel Obstruction': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 4, 'weight': 0.12},
            {'field': 'activity_mins', 'op': '>', 'value': 99, 'weight': 0.29},
            {'field': 'sleep_hours', 'op': '<', 'value': 10, 'weight': 0.47},
            {'field': 'smoking', 'op': '<=', 'value': 64, 'weight': 0.19},
            {'field': 'weight', 'op': '>=', 'value': 20, 'weight': 0.21},
        ]
    },
    'Hiatal Hernia': {
        'category': 'Digestive', 'icon': 'fa-stomach',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 14, 'weight': 0.3},
            {'field': 'sleep_hours', 'op': '<', 'value': 12, 'weight': 0.42},
            {'field': 'water_intake', 'op': '>', 'value': 73, 'weight': 0.45},
            {'field': 'bp_sys', 'op': '>=', 'value': 117, 'weight': 0.13},
            {'field': 'age', 'op': '>=', 'value': 145, 'weight': 0.18},
        ]
    },
    'Hypothyroidism': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'smoking', 'op': 'between', 'value': [43, 71], 'weight': 0.2},
            {'field': 'bp_dias', 'op': '<', 'value': 140, 'weight': 0.39},
            {'field': 'activity_mins', 'op': '<', 'value': 105, 'weight': 0.1},
            {'field': 'age', 'op': '<', 'value': 3, 'weight': 0.32},
        ]
    },
    'Hyperthyroidism': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'age', 'op': '<=', 'value': 79, 'weight': 0.44},
            {'field': 'sleep_hours', 'op': '<', 'value': 61, 'weight': 0.31},
            {'field': 'water_intake', 'op': '<=', 'value': 37, 'weight': 0.48},
            {'field': 'bp_sys', 'op': '>', 'value': 60, 'weight': 0.12},
        ]
    },
    'Graves Disease': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 22, 'weight': 0.28},
            {'field': 'height', 'op': '>', 'value': 101, 'weight': 0.3},
            {'field': 'bmi', 'op': 'between', 'value': [47, 61], 'weight': 0.33},
            {'field': 'stress', 'op': '>=', 'value': 81, 'weight': 0.2},
            {'field': 'weight', 'op': '>=', 'value': 70, 'weight': 0.23},
        ]
    },
    'Hashimotos Thyroiditis': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 150, 'weight': 0.15},
            {'field': 'sleep_hours', 'op': '<', 'value': 116, 'weight': 0.14},
            {'field': 'weight', 'op': '>=', 'value': 138, 'weight': 0.26},
        ]
    },
    'Thyroid Nodules': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 119, 'weight': 0.28},
            {'field': 'stress', 'op': '>', 'value': 78, 'weight': 0.14},
            {'field': 'salt_intake', 'op': 'between', 'value': [40, 54], 'weight': 0.12},
            {'field': 'bmi', 'op': '<', 'value': 102, 'weight': 0.49},
        ]
    },
    'Thyroid Cancer': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 45, 'weight': 0.2},
            {'field': 'bmi', 'op': '<=', 'value': 143, 'weight': 0.44},
            {'field': 'salt_intake', 'op': 'between', 'value': [49, 62], 'weight': 0.2},
            {'field': 'stress', 'op': '>', 'value': 57, 'weight': 0.1},
            {'field': 'screen_time', 'op': '<', 'value': 96, 'weight': 0.43},
        ]
    },
    'Adrenal Insufficiency': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 67, 'weight': 0.33},
            {'field': 'bmi', 'op': '>', 'value': 51, 'weight': 0.5},
            {'field': 'alcohol', 'op': '<=', 'value': 24, 'weight': 0.42},
            {'field': 'bp_sys', 'op': '>', 'value': 119, 'weight': 0.12},
            {'field': 'age', 'op': '<', 'value': 111, 'weight': 0.47},
        ]
    },
    'Pheochromocytoma': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 110, 'weight': 0.11},
            {'field': 'sleep_hours', 'op': '>=', 'value': 48, 'weight': 0.19},
            {'field': 'screen_time', 'op': '>=', 'value': 39, 'weight': 0.28},
            {'field': 'age', 'op': 'between', 'value': [35, 65], 'weight': 0.35},
            {'field': 'water_intake', 'op': '<=', 'value': 141, 'weight': 0.26},
        ]
    },
    'Hyperparathyroidism': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 36, 'weight': 0.21},
            {'field': 'bp_dias', 'op': '<', 'value': 135, 'weight': 0.36},
            {'field': 'stress', 'op': 'between', 'value': [44, 65], 'weight': 0.42},
            {'field': 'height', 'op': 'between', 'value': [42, 70], 'weight': 0.41},
        ]
    },
    'Hypoparathyroidism': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'screen_time', 'op': '<=', 'value': 7, 'weight': 0.21},
            {'field': 'bp_sys', 'op': 'between', 'value': [37, 48], 'weight': 0.19},
            {'field': 'weight', 'op': 'between', 'value': [57, 74], 'weight': 0.24},
            {'field': 'sleep_hours', 'op': '>', 'value': 62, 'weight': 0.2},
            {'field': 'bp_dias', 'op': 'between', 'value': [23, 40], 'weight': 0.43},
        ]
    },
    'Acromegaly': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 45, 'weight': 0.24},
            {'field': 'sleep_hours', 'op': '<', 'value': 92, 'weight': 0.34},
            {'field': 'height', 'op': '>', 'value': 91, 'weight': 0.38},
            {'field': 'smoking', 'op': 'between', 'value': [32, 57], 'weight': 0.16},
            {'field': 'weight', 'op': '>=', 'value': 10, 'weight': 0.17},
        ]
    },
    'Growth Hormone Deficiency': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 6, 'weight': 0.34},
            {'field': 'weight', 'op': '<=', 'value': 52, 'weight': 0.1},
            {'field': 'activity_mins', 'op': '>=', 'value': 83, 'weight': 0.39},
        ]
    },
    'Prolactinoma': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 37, 'weight': 0.33},
            {'field': 'salt_intake', 'op': '>', 'value': 94, 'weight': 0.44},
            {'field': 'sleep_hours', 'op': '>=', 'value': 102, 'weight': 0.38},
        ]
    },
    'Diabetes Insipidus': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 35, 'weight': 0.22},
            {'field': 'activity_mins', 'op': '<=', 'value': 125, 'weight': 0.42},
            {'field': 'alcohol', 'op': '>=', 'value': 144, 'weight': 0.17},
            {'field': 'smoking', 'op': '>=', 'value': 45, 'weight': 0.19},
            {'field': 'water_intake', 'op': '>=', 'value': 76, 'weight': 0.39},
        ]
    },
    'SIADH': {
        'category': 'Endocrine', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 147, 'weight': 0.48},
            {'field': 'bp_dias', 'op': 'between', 'value': [58, 78], 'weight': 0.11},
            {'field': 'smoking', 'op': '<', 'value': 27, 'weight': 0.36},
        ]
    },
    'Chronic Kidney Disease': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>=', 'value': 61, 'weight': 0.4},
            {'field': 'bp_sys', 'op': '>=', 'value': 23, 'weight': 0.17},
            {'field': 'salt_intake', 'op': '>=', 'value': 68, 'weight': 0.28},
            {'field': 'stress', 'op': '<', 'value': 90, 'weight': 0.38},
        ]
    },
    'Acute Kidney Injury': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 13, 'weight': 0.39},
            {'field': 'bp_sys', 'op': '<=', 'value': 43, 'weight': 0.39},
            {'field': 'bp_dias', 'op': '<=', 'value': 90, 'weight': 0.45},
            {'field': 'height', 'op': '<=', 'value': 123, 'weight': 0.14},
        ]
    },
    'Kidney Stones': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 19, 'weight': 0.17},
            {'field': 'salt_intake', 'op': '>', 'value': 82, 'weight': 0.22},
            {'field': 'stress', 'op': '>', 'value': 44, 'weight': 0.13},
            {'field': 'bp_dias', 'op': '<', 'value': 141, 'weight': 0.39},
            {'field': 'bmi', 'op': '>=', 'value': 124, 'weight': 0.34},
        ]
    },
    'Urinary Tract Infection': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'age', 'op': '<=', 'value': 43, 'weight': 0.48},
            {'field': 'height', 'op': '<=', 'value': 26, 'weight': 0.16},
            {'field': 'bp_sys', 'op': '<', 'value': 105, 'weight': 0.49},
            {'field': 'smoking', 'op': 'between', 'value': [38, 57], 'weight': 0.21},
            {'field': 'stress', 'op': '>', 'value': 147, 'weight': 0.12},
        ]
    },
    'Pyelonephritis': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 93, 'weight': 0.16},
            {'field': 'age', 'op': '<=', 'value': 123, 'weight': 0.14},
            {'field': 'stress', 'op': '>', 'value': 44, 'weight': 0.11},
            {'field': 'alcohol', 'op': '>=', 'value': 122, 'weight': 0.49},
            {'field': 'sleep_hours', 'op': '>=', 'value': 121, 'weight': 0.41},
        ]
    },
    'Glomerulonephritis': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 140, 'weight': 0.14},
            {'field': 'bp_sys', 'op': '<', 'value': 98, 'weight': 0.25},
            {'field': 'screen_time', 'op': '<', 'value': 68, 'weight': 0.28},
            {'field': 'weight', 'op': '<=', 'value': 69, 'weight': 0.21},
        ]
    },
    'Nephrotic Syndrome': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 25, 'weight': 0.4},
            {'field': 'sleep_hours', 'op': '>=', 'value': 106, 'weight': 0.42},
            {'field': 'smoking', 'op': '<', 'value': 100, 'weight': 0.32},
            {'field': 'height', 'op': '<=', 'value': 122, 'weight': 0.49},
            {'field': 'salt_intake', 'op': '<', 'value': 21, 'weight': 0.29},
        ]
    },
    'Polycystic Kidney': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'salt_intake', 'op': '>', 'value': 133, 'weight': 0.3},
            {'field': 'alcohol', 'op': 'between', 'value': [59, 73], 'weight': 0.37},
            {'field': 'bmi', 'op': '<=', 'value': 43, 'weight': 0.17},
            {'field': 'stress', 'op': '<', 'value': 109, 'weight': 0.15},
        ]
    },
    'Bladder Cancer': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 38, 'weight': 0.18},
            {'field': 'weight', 'op': '>=', 'value': 18, 'weight': 0.23},
            {'field': 'bmi', 'op': '<=', 'value': 142, 'weight': 0.32},
        ]
    },
    'Kidney Cancer': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'salt_intake', 'op': '>=', 'value': 4, 'weight': 0.31},
            {'field': 'alcohol', 'op': 'between', 'value': [46, 59], 'weight': 0.34},
            {'field': 'bp_sys', 'op': '<', 'value': 150, 'weight': 0.16},
            {'field': 'bmi', 'op': '>', 'value': 26, 'weight': 0.33},
        ]
    },
    'Benign Prostatic Hyperplasia': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'salt_intake', 'op': 'between', 'value': [46, 64], 'weight': 0.45},
            {'field': 'bp_sys', 'op': '<=', 'value': 122, 'weight': 0.33},
            {'field': 'age', 'op': '<', 'value': 37, 'weight': 0.21},
            {'field': 'smoking', 'op': 'between', 'value': [45, 56], 'weight': 0.37},
        ]
    },
    'Prostate Cancer': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 122, 'weight': 0.12},
            {'field': 'stress', 'op': '>=', 'value': 78, 'weight': 0.11},
            {'field': 'bp_sys', 'op': '>=', 'value': 26, 'weight': 0.44},
            {'field': 'activity_mins', 'op': '<', 'value': 114, 'weight': 0.22},
        ]
    },
    'Urinary Incontinence': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 23, 'weight': 0.34},
            {'field': 'activity_mins', 'op': '<=', 'value': 105, 'weight': 0.18},
            {'field': 'salt_intake', 'op': '<=', 'value': 96, 'weight': 0.4},
            {'field': 'age', 'op': 'between', 'value': [24, 43], 'weight': 0.42},
        ]
    },
    'Interstitial Cystitis': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'water_intake', 'op': '<=', 'value': 135, 'weight': 0.15},
            {'field': 'height', 'op': '>', 'value': 52, 'weight': 0.17},
            {'field': 'age', 'op': '<', 'value': 13, 'weight': 0.11},
            {'field': 'bp_sys', 'op': '<', 'value': 119, 'weight': 0.21},
            {'field': 'alcohol', 'op': '<=', 'value': 32, 'weight': 0.35},
        ]
    },
    'Hydronephrosis': {
        'category': 'Kidney Urological', 'icon': 'fa-kidneys',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 115, 'weight': 0.25},
            {'field': 'activity_mins', 'op': '<=', 'value': 90, 'weight': 0.33},
            {'field': 'bp_dias', 'op': '<', 'value': 67, 'weight': 0.44},
            {'field': 'sleep_hours', 'op': '>=', 'value': 13, 'weight': 0.11},
            {'field': 'screen_time', 'op': 'between', 'value': [33, 50], 'weight': 0.41},
        ]
    },
    'Eczema': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'activity_mins', 'op': '<', 'value': 105, 'weight': 0.21},
            {'field': 'weight', 'op': '>', 'value': 3, 'weight': 0.45},
            {'field': 'water_intake', 'op': '<', 'value': 3, 'weight': 0.36},
            {'field': 'stress', 'op': '>=', 'value': 79, 'weight': 0.34},
            {'field': 'bp_sys', 'op': '<=', 'value': 90, 'weight': 0.46},
        ]
    },
    'Psoriasis': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 134, 'weight': 0.29},
            {'field': 'height', 'op': '<=', 'value': 2, 'weight': 0.33},
            {'field': 'weight', 'op': '>=', 'value': 73, 'weight': 0.32},
            {'field': 'screen_time', 'op': '>', 'value': 87, 'weight': 0.29},
        ]
    },
    'Acne Vulgaris': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 67, 'weight': 0.44},
            {'field': 'smoking', 'op': '>=', 'value': 133, 'weight': 0.18},
            {'field': 'activity_mins', 'op': '>', 'value': 104, 'weight': 0.42},
            {'field': 'salt_intake', 'op': '>=', 'value': 7, 'weight': 0.37},
        ]
    },
    'Rosacea': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 108, 'weight': 0.2},
            {'field': 'bp_sys', 'op': '<=', 'value': 150, 'weight': 0.39},
            {'field': 'salt_intake', 'op': 'between', 'value': [41, 58], 'weight': 0.43},
            {'field': 'alcohol', 'op': 'between', 'value': [50, 71], 'weight': 0.36},
            {'field': 'height', 'op': '>=', 'value': 143, 'weight': 0.44},
        ]
    },
    'Contact Dermatitis': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'stress', 'op': '>', 'value': 67, 'weight': 0.29},
            {'field': 'alcohol', 'op': 'between', 'value': [31, 51], 'weight': 0.41},
            {'field': 'smoking', 'op': '>', 'value': 58, 'weight': 0.19},
        ]
    },
    'Urticaria Hives': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'salt_intake', 'op': '>=', 'value': 85, 'weight': 0.27},
            {'field': 'screen_time', 'op': '>=', 'value': 119, 'weight': 0.33},
            {'field': 'bmi', 'op': '<=', 'value': 150, 'weight': 0.12},
            {'field': 'smoking', 'op': 'between', 'value': [32, 58], 'weight': 0.13},
            {'field': 'sleep_hours', 'op': '<=', 'value': 106, 'weight': 0.31},
        ]
    },
    'Vitiligo': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 52, 'weight': 0.15},
            {'field': 'screen_time', 'op': '<=', 'value': 118, 'weight': 0.49},
            {'field': 'sleep_hours', 'op': '>=', 'value': 47, 'weight': 0.44},
        ]
    },
    'Melanoma': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 46, 'weight': 0.35},
            {'field': 'screen_time', 'op': '>', 'value': 71, 'weight': 0.1},
            {'field': 'activity_mins', 'op': '<', 'value': 41, 'weight': 0.33},
        ]
    },
    'Basal Cell Carcinoma': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 112, 'weight': 0.15},
            {'field': 'height', 'op': '<=', 'value': 123, 'weight': 0.26},
            {'field': 'bp_sys', 'op': '>', 'value': 52, 'weight': 0.12},
            {'field': 'screen_time', 'op': '>', 'value': 136, 'weight': 0.46},
        ]
    },
    'Squamous Cell Carcinoma': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 64, 'weight': 0.35},
            {'field': 'stress', 'op': '>=', 'value': 27, 'weight': 0.22},
            {'field': 'water_intake', 'op': 'between', 'value': [30, 42], 'weight': 0.34},
        ]
    },
    'Fungal Skin Infection': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'stress', 'op': '>=', 'value': 134, 'weight': 0.28},
            {'field': 'height', 'op': 'between', 'value': [28, 48], 'weight': 0.24},
            {'field': 'water_intake', 'op': '>=', 'value': 43, 'weight': 0.4},
        ]
    },
    'Cellulitis': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 34, 'weight': 0.19},
            {'field': 'stress', 'op': '>', 'value': 44, 'weight': 0.34},
            {'field': 'sleep_hours', 'op': '>=', 'value': 10, 'weight': 0.38},
            {'field': 'weight', 'op': '>=', 'value': 13, 'weight': 0.41},
        ]
    },
    'Impetigo': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 6, 'weight': 0.36},
            {'field': 'bmi', 'op': '>', 'value': 98, 'weight': 0.27},
            {'field': 'activity_mins', 'op': 'between', 'value': [29, 45], 'weight': 0.2},
            {'field': 'salt_intake', 'op': '>', 'value': 26, 'weight': 0.22},
            {'field': 'smoking', 'op': '>=', 'value': 36, 'weight': 0.35},
        ]
    },
    'Shingles Herpes Zoster': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'salt_intake', 'op': '>', 'value': 31, 'weight': 0.3},
            {'field': 'stress', 'op': '>', 'value': 128, 'weight': 0.41},
            {'field': 'activity_mins', 'op': 'between', 'value': [36, 62], 'weight': 0.18},
            {'field': 'screen_time', 'op': '>=', 'value': 76, 'weight': 0.38},
        ]
    },
    'Scabies': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [33, 58], 'weight': 0.3},
            {'field': 'bp_sys', 'op': '<', 'value': 23, 'weight': 0.1},
            {'field': 'sleep_hours', 'op': 'between', 'value': [29, 41], 'weight': 0.37},
        ]
    },
    'Alopecia Areata': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 60, 'weight': 0.46},
            {'field': 'water_intake', 'op': '>=', 'value': 13, 'weight': 0.21},
            {'field': 'sleep_hours', 'op': '<', 'value': 75, 'weight': 0.45},
            {'field': 'bp_dias', 'op': '>=', 'value': 30, 'weight': 0.27},
            {'field': 'activity_mins', 'op': '>', 'value': 36, 'weight': 0.1},
        ]
    },
    'Seborrheic Dermatitis': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 113, 'weight': 0.23},
            {'field': 'weight', 'op': '>=', 'value': 24, 'weight': 0.45},
            {'field': 'screen_time', 'op': '>=', 'value': 103, 'weight': 0.17},
            {'field': 'bp_dias', 'op': '<=', 'value': 99, 'weight': 0.21},
            {'field': 'smoking', 'op': '<=', 'value': 43, 'weight': 0.36},
        ]
    },
    'Lichen Planus': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 41, 'weight': 0.49},
            {'field': 'bmi', 'op': '<=', 'value': 124, 'weight': 0.46},
            {'field': 'smoking', 'op': '<=', 'value': 98, 'weight': 0.17},
        ]
    },
    'Pemphigus': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 34, 'weight': 0.45},
            {'field': 'bp_dias', 'op': '<=', 'value': 106, 'weight': 0.15},
            {'field': 'water_intake', 'op': '>', 'value': 81, 'weight': 0.13},
            {'field': 'age', 'op': 'between', 'value': [56, 84], 'weight': 0.41},
        ]
    },
    'Folliculitis': {
        'category': 'Dermatological', 'icon': 'fa-allergies',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 25, 'weight': 0.31},
            {'field': 'bp_sys', 'op': '<', 'value': 99, 'weight': 0.29},
            {'field': 'sleep_hours', 'op': 'between', 'value': [59, 70], 'weight': 0.46},
        ]
    },
    'Influenza': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 121, 'weight': 0.3},
            {'field': 'bp_dias', 'op': '<', 'value': 126, 'weight': 0.13},
            {'field': 'screen_time', 'op': '<', 'value': 72, 'weight': 0.23},
        ]
    },
    'COVID-19': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 97, 'weight': 0.32},
            {'field': 'bp_sys', 'op': '<', 'value': 114, 'weight': 0.13},
            {'field': 'smoking', 'op': '<=', 'value': 128, 'weight': 0.14},
        ]
    },
    'Common Cold': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 5, 'weight': 0.49},
            {'field': 'bmi', 'op': '<=', 'value': 143, 'weight': 0.26},
            {'field': 'height', 'op': '>', 'value': 78, 'weight': 0.43},
            {'field': 'smoking', 'op': 'between', 'value': [49, 69], 'weight': 0.18},
        ]
    },
    'Dengue Fever': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'salt_intake', 'op': '>', 'value': 117, 'weight': 0.43},
            {'field': 'screen_time', 'op': 'between', 'value': [58, 83], 'weight': 0.41},
            {'field': 'alcohol', 'op': '>=', 'value': 30, 'weight': 0.39},
            {'field': 'bmi', 'op': '<', 'value': 91, 'weight': 0.1},
        ]
    },
    'Malaria': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 96, 'weight': 0.32},
            {'field': 'smoking', 'op': '>', 'value': 43, 'weight': 0.12},
            {'field': 'bp_dias', 'op': '<', 'value': 105, 'weight': 0.43},
            {'field': 'bmi', 'op': '>=', 'value': 49, 'weight': 0.34},
            {'field': 'sleep_hours', 'op': '<=', 'value': 49, 'weight': 0.19},
        ]
    },
    'Typhoid': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 12, 'weight': 0.4},
            {'field': 'smoking', 'op': 'between', 'value': [48, 72], 'weight': 0.15},
            {'field': 'alcohol', 'op': 'between', 'value': [28, 53], 'weight': 0.48},
            {'field': 'age', 'op': 'between', 'value': [55, 78], 'weight': 0.39},
            {'field': 'salt_intake', 'op': '<=', 'value': 46, 'weight': 0.47},
        ]
    },
    'Cholera': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 33, 'weight': 0.39},
            {'field': 'bmi', 'op': '<=', 'value': 83, 'weight': 0.36},
            {'field': 'height', 'op': '<=', 'value': 64, 'weight': 0.27},
            {'field': 'screen_time', 'op': '<=', 'value': 76, 'weight': 0.49},
            {'field': 'smoking', 'op': '<', 'value': 132, 'weight': 0.16},
        ]
    },
    'HIV AIDS': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'salt_intake', 'op': 'between', 'value': [55, 85], 'weight': 0.44},
            {'field': 'activity_mins', 'op': '<', 'value': 75, 'weight': 0.18},
            {'field': 'smoking', 'op': '>=', 'value': 34, 'weight': 0.47},
            {'field': 'alcohol', 'op': '<', 'value': 83, 'weight': 0.3},
        ]
    },
    'Hepatitis E': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 150, 'weight': 0.32},
            {'field': 'height', 'op': '<=', 'value': 137, 'weight': 0.37},
            {'field': 'screen_time', 'op': '<=', 'value': 134, 'weight': 0.42},
            {'field': 'sleep_hours', 'op': '>', 'value': 14, 'weight': 0.25},
            {'field': 'age', 'op': '<', 'value': 42, 'weight': 0.21},
        ]
    },
    'Rabies': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 16, 'weight': 0.16},
            {'field': 'alcohol', 'op': '>=', 'value': 139, 'weight': 0.18},
            {'field': 'age', 'op': '>=', 'value': 27, 'weight': 0.43},
            {'field': 'smoking', 'op': 'between', 'value': [55, 77], 'weight': 0.45},
        ]
    },
    'Measles': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'water_intake', 'op': '>=', 'value': 13, 'weight': 0.38},
            {'field': 'bp_sys', 'op': '<=', 'value': 81, 'weight': 0.27},
            {'field': 'height', 'op': '>', 'value': 65, 'weight': 0.11},
        ]
    },
    'Mumps': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 95, 'weight': 0.43},
            {'field': 'salt_intake', 'op': 'between', 'value': [58, 74], 'weight': 0.32},
            {'field': 'alcohol', 'op': '<', 'value': 46, 'weight': 0.22},
        ]
    },
    'Rubella': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 132, 'weight': 0.48},
            {'field': 'sleep_hours', 'op': '<=', 'value': 72, 'weight': 0.12},
            {'field': 'height', 'op': '>=', 'value': 150, 'weight': 0.15},
            {'field': 'bp_sys', 'op': '>', 'value': 40, 'weight': 0.23},
            {'field': 'age', 'op': '<', 'value': 14, 'weight': 0.47},
        ]
    },
    'Chickenpox': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'weight', 'op': '>=', 'value': 147, 'weight': 0.3},
            {'field': 'water_intake', 'op': '>=', 'value': 82, 'weight': 0.13},
            {'field': 'height', 'op': '<', 'value': 134, 'weight': 0.48},
            {'field': 'bmi', 'op': 'between', 'value': [54, 81], 'weight': 0.16},
            {'field': 'bp_dias', 'op': '>', 'value': 55, 'weight': 0.24},
        ]
    },
    'Mononucleosis': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 56, 'weight': 0.24},
            {'field': 'salt_intake', 'op': 'between', 'value': [55, 85], 'weight': 0.31},
            {'field': 'age', 'op': '>', 'value': 115, 'weight': 0.37},
            {'field': 'stress', 'op': 'between', 'value': [35, 46], 'weight': 0.47},
            {'field': 'water_intake', 'op': '<=', 'value': 30, 'weight': 0.47},
        ]
    },
    'Zika Virus': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'stress', 'op': 'between', 'value': [21, 47], 'weight': 0.39},
            {'field': 'salt_intake', 'op': '>=', 'value': 131, 'weight': 0.31},
            {'field': 'water_intake', 'op': '<=', 'value': 50, 'weight': 0.12},
            {'field': 'bp_sys', 'op': 'between', 'value': [26, 41], 'weight': 0.13},
        ]
    },
    'Chikungunya': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 54, 'weight': 0.35},
            {'field': 'smoking', 'op': '<', 'value': 109, 'weight': 0.45},
            {'field': 'bmi', 'op': '<', 'value': 112, 'weight': 0.32},
            {'field': 'salt_intake', 'op': '>', 'value': 40, 'weight': 0.4},
            {'field': 'age', 'op': '<=', 'value': 10, 'weight': 0.39},
        ]
    },
    'Yellow Fever': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 65, 'weight': 0.17},
            {'field': 'weight', 'op': '>', 'value': 59, 'weight': 0.33},
            {'field': 'screen_time', 'op': '<=', 'value': 104, 'weight': 0.26},
        ]
    },
    'Lyme Disease': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 31, 'weight': 0.26},
            {'field': 'weight', 'op': '>', 'value': 17, 'weight': 0.36},
            {'field': 'salt_intake', 'op': 'between', 'value': [24, 45], 'weight': 0.12},
            {'field': 'height', 'op': '>', 'value': 78, 'weight': 0.22},
        ]
    },
    'Sepsis': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 113, 'weight': 0.41},
            {'field': 'bp_dias', 'op': '<=', 'value': 8, 'weight': 0.43},
            {'field': 'weight', 'op': '<', 'value': 35, 'weight': 0.31},
            {'field': 'water_intake', 'op': 'between', 'value': [60, 74], 'weight': 0.22},
            {'field': 'screen_time', 'op': '>=', 'value': 3, 'weight': 0.48},
        ]
    },
    'Tetanus': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'salt_intake', 'op': 'between', 'value': [22, 32], 'weight': 0.16},
            {'field': 'weight', 'op': 'between', 'value': [55, 67], 'weight': 0.26},
            {'field': 'stress', 'op': '<', 'value': 89, 'weight': 0.4},
            {'field': 'activity_mins', 'op': '<=', 'value': 132, 'weight': 0.46},
            {'field': 'sleep_hours', 'op': '<', 'value': 65, 'weight': 0.17},
        ]
    },
    'Diphtheria': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 146, 'weight': 0.37},
            {'field': 'age', 'op': 'between', 'value': [55, 67], 'weight': 0.28},
            {'field': 'bp_sys', 'op': '>', 'value': 51, 'weight': 0.2},
        ]
    },
    'Ebola': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 92, 'weight': 0.48},
            {'field': 'sleep_hours', 'op': '<', 'value': 18, 'weight': 0.14},
            {'field': 'stress', 'op': '>=', 'value': 85, 'weight': 0.29},
            {'field': 'alcohol', 'op': '>=', 'value': 40, 'weight': 0.38},
            {'field': 'salt_intake', 'op': 'between', 'value': [40, 63], 'weight': 0.25},
        ]
    },
    'West Nile Virus': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 57, 'weight': 0.2},
            {'field': 'alcohol', 'op': '<=', 'value': 93, 'weight': 0.21},
            {'field': 'activity_mins', 'op': '>=', 'value': 119, 'weight': 0.45},
        ]
    },
    'Hand Foot Mouth Disease': {
        'category': 'Infectious', 'icon': 'fa-virus',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 28, 'weight': 0.29},
            {'field': 'sleep_hours', 'op': 'between', 'value': [37, 51], 'weight': 0.13},
            {'field': 'height', 'op': '<', 'value': 20, 'weight': 0.21},
            {'field': 'bmi', 'op': '>', 'value': 8, 'weight': 0.44},
        ]
    },
    'PCOS': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 55, 'weight': 0.41},
            {'field': 'age', 'op': 'between', 'value': [54, 79], 'weight': 0.2},
            {'field': 'alcohol', 'op': '<', 'value': 58, 'weight': 0.25},
            {'field': 'smoking', 'op': '>=', 'value': 129, 'weight': 0.15},
            {'field': 'height', 'op': '>', 'value': 129, 'weight': 0.26},
        ]
    },
    'Endometriosis': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 43, 'weight': 0.44},
            {'field': 'salt_intake', 'op': 'between', 'value': [30, 45], 'weight': 0.16},
            {'field': 'weight', 'op': 'between', 'value': [29, 54], 'weight': 0.36},
        ]
    },
    'Uterine Fibroids': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 60, 'weight': 0.4},
            {'field': 'sleep_hours', 'op': '>=', 'value': 11, 'weight': 0.25},
            {'field': 'alcohol', 'op': '<', 'value': 93, 'weight': 0.31},
            {'field': 'water_intake', 'op': '<=', 'value': 12, 'weight': 0.47},
        ]
    },
    'Cervical Cancer': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 134, 'weight': 0.14},
            {'field': 'smoking', 'op': '>=', 'value': 68, 'weight': 0.43},
            {'field': 'weight', 'op': 'between', 'value': [44, 74], 'weight': 0.33},
        ]
    },
    'Ovarian Cancer': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'screen_time', 'op': 'between', 'value': [24, 50], 'weight': 0.36},
            {'field': 'stress', 'op': '<=', 'value': 58, 'weight': 0.49},
            {'field': 'height', 'op': '<=', 'value': 89, 'weight': 0.24},
            {'field': 'weight', 'op': '<=', 'value': 2, 'weight': 0.45},
        ]
    },
    'Uterine Cancer': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<=', 'value': 20, 'weight': 0.17},
            {'field': 'weight', 'op': '>=', 'value': 48, 'weight': 0.18},
            {'field': 'activity_mins', 'op': '>=', 'value': 31, 'weight': 0.34},
            {'field': 'salt_intake', 'op': '<', 'value': 85, 'weight': 0.27},
            {'field': 'bmi', 'op': '<=', 'value': 123, 'weight': 0.37},
        ]
    },
    'Breast Cancer': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 106, 'weight': 0.36},
            {'field': 'age', 'op': '<', 'value': 147, 'weight': 0.12},
            {'field': 'smoking', 'op': '<', 'value': 132, 'weight': 0.15},
        ]
    },
    'Vaginitis': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 67, 'weight': 0.12},
            {'field': 'sleep_hours', 'op': 'between', 'value': [58, 86], 'weight': 0.48},
            {'field': 'alcohol', 'op': '>', 'value': 73, 'weight': 0.45},
        ]
    },
    'Pelvic Inflammatory Disease': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 121, 'weight': 0.34},
            {'field': 'water_intake', 'op': '<', 'value': 106, 'weight': 0.19},
            {'field': 'smoking', 'op': '<', 'value': 47, 'weight': 0.42},
        ]
    },
    'Preeclampsia': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [41, 65], 'weight': 0.21},
            {'field': 'weight', 'op': 'between', 'value': [44, 66], 'weight': 0.13},
            {'field': 'sleep_hours', 'op': '>', 'value': 134, 'weight': 0.11},
            {'field': 'smoking', 'op': '<=', 'value': 25, 'weight': 0.43},
            {'field': 'activity_mins', 'op': '<=', 'value': 10, 'weight': 0.46},
        ]
    },
    'Ectopic Pregnancy': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 34, 'weight': 0.14},
            {'field': 'height', 'op': 'between', 'value': [47, 73], 'weight': 0.43},
            {'field': 'bp_sys', 'op': '>=', 'value': 136, 'weight': 0.45},
            {'field': 'bp_dias', 'op': '<', 'value': 124, 'weight': 0.48},
            {'field': 'weight', 'op': '>=', 'value': 148, 'weight': 0.34},
        ]
    },
    'Ovarian Cyst': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'bp_sys', 'op': '<', 'value': 60, 'weight': 0.2},
            {'field': 'bmi', 'op': '>=', 'value': 140, 'weight': 0.34},
            {'field': 'water_intake', 'op': '>=', 'value': 2, 'weight': 0.18},
        ]
    },
    'Menorrhagia': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 97, 'weight': 0.31},
            {'field': 'smoking', 'op': '<', 'value': 81, 'weight': 0.38},
            {'field': 'bp_sys', 'op': '>=', 'value': 110, 'weight': 0.14},
            {'field': 'salt_intake', 'op': 'between', 'value': [54, 77], 'weight': 0.2},
            {'field': 'alcohol', 'op': '>=', 'value': 102, 'weight': 0.34},
        ]
    },
    'Amenorrhea': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'bp_sys', 'op': 'between', 'value': [50, 65], 'weight': 0.41},
            {'field': 'screen_time', 'op': 'between', 'value': [36, 55], 'weight': 0.32},
            {'field': 'smoking', 'op': '>=', 'value': 102, 'weight': 0.41},
        ]
    },
    'Premenstrual Syndrome': {
        'category': 'Gynecological', 'icon': 'fa-female',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 115, 'weight': 0.4},
            {'field': 'salt_intake', 'op': '<', 'value': 131, 'weight': 0.14},
            {'field': 'bp_dias', 'op': '>=', 'value': 14, 'weight': 0.42},
            {'field': 'activity_mins', 'op': '<=', 'value': 2, 'weight': 0.49},
            {'field': 'bmi', 'op': '<', 'value': 112, 'weight': 0.29},
        ]
    },
    'Glaucoma': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 21, 'weight': 0.19},
            {'field': 'height', 'op': '>', 'value': 103, 'weight': 0.39},
            {'field': 'smoking', 'op': 'between', 'value': [58, 69], 'weight': 0.21},
        ]
    },
    'Cataracts': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 52, 'weight': 0.28},
            {'field': 'smoking', 'op': 'between', 'value': [22, 51], 'weight': 0.21},
            {'field': 'water_intake', 'op': 'between', 'value': [59, 74], 'weight': 0.38},
        ]
    },
    'Macular Degeneration': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 1, 'weight': 0.2},
            {'field': 'activity_mins', 'op': '>', 'value': 103, 'weight': 0.5},
            {'field': 'bp_dias', 'op': '<=', 'value': 52, 'weight': 0.26},
            {'field': 'smoking', 'op': '>', 'value': 18, 'weight': 0.39},
            {'field': 'sleep_hours', 'op': 'between', 'value': [55, 83], 'weight': 0.21},
        ]
    },
    'Diabetic Retinopathy': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 50, 'weight': 0.19},
            {'field': 'water_intake', 'op': '<=', 'value': 67, 'weight': 0.33},
            {'field': 'sleep_hours', 'op': '<=', 'value': 144, 'weight': 0.3},
            {'field': 'bmi', 'op': 'between', 'value': [27, 53], 'weight': 0.22},
        ]
    },
    'Conjunctivitis': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [48, 70], 'weight': 0.2},
            {'field': 'height', 'op': '<=', 'value': 87, 'weight': 0.41},
            {'field': 'bp_dias', 'op': '<=', 'value': 8, 'weight': 0.46},
            {'field': 'weight', 'op': '>', 'value': 98, 'weight': 0.2},
        ]
    },
    'Dry Eye Syndrome': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 59, 'weight': 0.37},
            {'field': 'salt_intake', 'op': '>=', 'value': 91, 'weight': 0.26},
            {'field': 'water_intake', 'op': 'between', 'value': [36, 53], 'weight': 0.1},
            {'field': 'stress', 'op': '>', 'value': 88, 'weight': 0.26},
            {'field': 'bmi', 'op': 'between', 'value': [50, 70], 'weight': 0.47},
        ]
    },
    'Retinal Detachment': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'activity_mins', 'op': 'between', 'value': [32, 57], 'weight': 0.21},
            {'field': 'alcohol', 'op': '<', 'value': 62, 'weight': 0.19},
            {'field': 'screen_time', 'op': '<', 'value': 64, 'weight': 0.19},
            {'field': 'smoking', 'op': '>=', 'value': 28, 'weight': 0.16},
        ]
    },
    'Strabismus': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 139, 'weight': 0.35},
            {'field': 'age', 'op': '<=', 'value': 81, 'weight': 0.25},
            {'field': 'weight', 'op': 'between', 'value': [51, 66], 'weight': 0.45},
        ]
    },
    'Otitis Media': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 148, 'weight': 0.19},
            {'field': 'sleep_hours', 'op': '>', 'value': 109, 'weight': 0.31},
            {'field': 'weight', 'op': 'between', 'value': [42, 64], 'weight': 0.11},
            {'field': 'salt_intake', 'op': '<', 'value': 31, 'weight': 0.28},
            {'field': 'smoking', 'op': '<=', 'value': 3, 'weight': 0.23},
        ]
    },
    'Otitis Externa': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 26, 'weight': 0.25},
            {'field': 'screen_time', 'op': '>=', 'value': 67, 'weight': 0.35},
            {'field': 'sleep_hours', 'op': 'between', 'value': [37, 62], 'weight': 0.21},
        ]
    },
    'Tinnitus': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 109, 'weight': 0.17},
            {'field': 'activity_mins', 'op': '<=', 'value': 96, 'weight': 0.38},
            {'field': 'bp_dias', 'op': '<=', 'value': 47, 'weight': 0.21},
            {'field': 'alcohol', 'op': '<', 'value': 59, 'weight': 0.49},
            {'field': 'bmi', 'op': '>=', 'value': 143, 'weight': 0.42},
        ]
    },
    'Hearing Loss': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 39, 'weight': 0.18},
            {'field': 'bp_dias', 'op': '>', 'value': 128, 'weight': 0.17},
            {'field': 'sleep_hours', 'op': 'between', 'value': [40, 65], 'weight': 0.31},
            {'field': 'screen_time', 'op': '>=', 'value': 146, 'weight': 0.32},
        ]
    },
    'Deviated Septum': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'bp_sys', 'op': '>', 'value': 16, 'weight': 0.38},
            {'field': 'activity_mins', 'op': '>=', 'value': 25, 'weight': 0.29},
            {'field': 'weight', 'op': '>=', 'value': 93, 'weight': 0.2},
        ]
    },
    'Nasal Polyps': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'water_intake', 'op': '>=', 'value': 106, 'weight': 0.24},
            {'field': 'bmi', 'op': '>=', 'value': 51, 'weight': 0.45},
            {'field': 'smoking', 'op': 'between', 'value': [54, 69], 'weight': 0.36},
            {'field': 'screen_time', 'op': '>=', 'value': 131, 'weight': 0.23},
            {'field': 'height', 'op': '<=', 'value': 98, 'weight': 0.46},
        ]
    },
    'Oral Cancer': {
        'category': 'Eye ENT', 'icon': 'fa-eye',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 38, 'weight': 0.35},
            {'field': 'sleep_hours', 'op': '>=', 'value': 147, 'weight': 0.27},
            {'field': 'water_intake', 'op': '>', 'value': 88, 'weight': 0.13},
            {'field': 'screen_time', 'op': '>=', 'value': 75, 'weight': 0.23},
            {'field': 'bp_dias', 'op': 'between', 'value': [37, 61], 'weight': 0.36},
        ]
    },
    'Lupus SLE Auto': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'smoking', 'op': 'between', 'value': [48, 71], 'weight': 0.31},
            {'field': 'sleep_hours', 'op': '<', 'value': 33, 'weight': 0.44},
            {'field': 'salt_intake', 'op': '<', 'value': 21, 'weight': 0.36},
            {'field': 'stress', 'op': '<', 'value': 25, 'weight': 0.26},
        ]
    },
    'Rheumatoid Arthritis Auto': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'bp_dias', 'op': 'between', 'value': [45, 71], 'weight': 0.12},
            {'field': 'salt_intake', 'op': '>', 'value': 40, 'weight': 0.14},
            {'field': 'bmi', 'op': '<=', 'value': 64, 'weight': 0.22},
        ]
    },
    'Type 1 Diabetes Auto': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 34, 'weight': 0.35},
            {'field': 'weight', 'op': '<', 'value': 92, 'weight': 0.11},
            {'field': 'bp_sys', 'op': '<=', 'value': 139, 'weight': 0.29},
            {'field': 'screen_time', 'op': 'between', 'value': [54, 69], 'weight': 0.28},
            {'field': 'salt_intake', 'op': 'between', 'value': [60, 88], 'weight': 0.28},
        ]
    },
    'Multiple Sclerosis Auto': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [42, 67], 'weight': 0.22},
            {'field': 'weight', 'op': '<', 'value': 114, 'weight': 0.42},
            {'field': 'stress', 'op': '>=', 'value': 40, 'weight': 0.26},
            {'field': 'screen_time', 'op': '>', 'value': 35, 'weight': 0.1},
        ]
    },
    'Celiac Disease Auto': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 126, 'weight': 0.31},
            {'field': 'salt_intake', 'op': '<=', 'value': 111, 'weight': 0.22},
            {'field': 'screen_time', 'op': 'between', 'value': [20, 47], 'weight': 0.19},
            {'field': 'bp_dias', 'op': '<', 'value': 144, 'weight': 0.26},
        ]
    },
    'Psoriasis Auto': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'bp_sys', 'op': '<', 'value': 100, 'weight': 0.17},
            {'field': 'bp_dias', 'op': '<', 'value': 109, 'weight': 0.21},
            {'field': 'alcohol', 'op': '<', 'value': 70, 'weight': 0.31},
            {'field': 'stress', 'op': 'between', 'value': [46, 62], 'weight': 0.42},
        ]
    },
    'Sjogrens Syndrome': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<', 'value': 117, 'weight': 0.22},
            {'field': 'height', 'op': '<=', 'value': 126, 'weight': 0.21},
            {'field': 'stress', 'op': '>=', 'value': 13, 'weight': 0.11},
        ]
    },
    'Vasculitis': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 73, 'weight': 0.49},
            {'field': 'screen_time', 'op': '<', 'value': 3, 'weight': 0.39},
            {'field': 'stress', 'op': '>', 'value': 127, 'weight': 0.16},
            {'field': 'bp_sys', 'op': '>=', 'value': 128, 'weight': 0.27},
            {'field': 'weight', 'op': '<=', 'value': 9, 'weight': 0.38},
        ]
    },
    'Scleroderma': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 101, 'weight': 0.12},
            {'field': 'sleep_hours', 'op': 'between', 'value': [32, 50], 'weight': 0.29},
            {'field': 'water_intake', 'op': '>', 'value': 64, 'weight': 0.15},
            {'field': 'weight', 'op': '<=', 'value': 9, 'weight': 0.2},
        ]
    },
    'Polymyositis': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 54, 'weight': 0.31},
            {'field': 'water_intake', 'op': '<=', 'value': 80, 'weight': 0.37},
            {'field': 'screen_time', 'op': '<', 'value': 11, 'weight': 0.35},
        ]
    },
    'Dermatomyositis': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [50, 80], 'weight': 0.15},
            {'field': 'stress', 'op': '<', 'value': 14, 'weight': 0.24},
            {'field': 'alcohol', 'op': '<', 'value': 61, 'weight': 0.49},
            {'field': 'salt_intake', 'op': '<=', 'value': 43, 'weight': 0.23},
            {'field': 'screen_time', 'op': 'between', 'value': [35, 45], 'weight': 0.15},
        ]
    },
    'Antiphospholipid Syndrome': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 40, 'weight': 0.38},
            {'field': 'screen_time', 'op': '>', 'value': 128, 'weight': 0.2},
            {'field': 'bmi', 'op': 'between', 'value': [60, 71], 'weight': 0.24},
        ]
    },
    'Mixed Connective Tissue': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 28, 'weight': 0.38},
            {'field': 'sleep_hours', 'op': '<=', 'value': 143, 'weight': 0.19},
            {'field': 'alcohol', 'op': '>=', 'value': 113, 'weight': 0.42},
        ]
    },
    'Goodpastures Syndrome': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'activity_mins', 'op': '>', 'value': 92, 'weight': 0.38},
            {'field': 'alcohol', 'op': '<', 'value': 11, 'weight': 0.2},
            {'field': 'water_intake', 'op': '<=', 'value': 139, 'weight': 0.32},
            {'field': 'weight', 'op': '<', 'value': 140, 'weight': 0.33},
            {'field': 'bp_sys', 'op': '>=', 'value': 71, 'weight': 0.39},
        ]
    },
    'Behcets Disease': {
        'category': 'Autoimmune', 'icon': 'fa-shield-virus',
        'conditions': [
            {'field': 'salt_intake', 'op': 'between', 'value': [53, 67], 'weight': 0.16},
            {'field': 'bp_dias', 'op': '>=', 'value': 139, 'weight': 0.43},
            {'field': 'screen_time', 'op': '<=', 'value': 130, 'weight': 0.1},
            {'field': 'water_intake', 'op': '<', 'value': 94, 'weight': 0.45},
            {'field': 'alcohol', 'op': '<', 'value': 17, 'weight': 0.23},
        ]
    },
    'Iron Deficiency Anemia': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'water_intake', 'op': '<=', 'value': 128, 'weight': 0.18},
            {'field': 'salt_intake', 'op': 'between', 'value': [38, 58], 'weight': 0.16},
            {'field': 'bp_sys', 'op': '>=', 'value': 134, 'weight': 0.14},
            {'field': 'alcohol', 'op': '>', 'value': 34, 'weight': 0.12},
            {'field': 'sleep_hours', 'op': '>', 'value': 125, 'weight': 0.18},
        ]
    },
    'Sickle Cell Disease': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 100, 'weight': 0.33},
            {'field': 'smoking', 'op': '<=', 'value': 66, 'weight': 0.31},
            {'field': 'age', 'op': '>=', 'value': 19, 'weight': 0.19},
        ]
    },
    'Thalassemia': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 21, 'weight': 0.47},
            {'field': 'water_intake', 'op': '>', 'value': 107, 'weight': 0.24},
            {'field': 'bp_sys', 'op': '>', 'value': 69, 'weight': 0.43},
        ]
    },
    'Hemophilia': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 20, 'weight': 0.43},
            {'field': 'stress', 'op': 'between', 'value': [34, 61], 'weight': 0.14},
            {'field': 'water_intake', 'op': '<', 'value': 64, 'weight': 0.18},
            {'field': 'alcohol', 'op': '<', 'value': 143, 'weight': 0.32},
            {'field': 'weight', 'op': '>', 'value': 148, 'weight': 0.41},
        ]
    },
    'Thrombocytopenia': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 110, 'weight': 0.38},
            {'field': 'bmi', 'op': '<', 'value': 141, 'weight': 0.42},
            {'field': 'bp_dias', 'op': 'between', 'value': [30, 57], 'weight': 0.24},
            {'field': 'alcohol', 'op': '<=', 'value': 81, 'weight': 0.47},
        ]
    },
    'Leukemia ALL': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 111, 'weight': 0.26},
            {'field': 'alcohol', 'op': '>=', 'value': 145, 'weight': 0.34},
            {'field': 'weight', 'op': '<', 'value': 141, 'weight': 0.25},
            {'field': 'stress', 'op': '>=', 'value': 115, 'weight': 0.48},
            {'field': 'water_intake', 'op': '>', 'value': 73, 'weight': 0.39},
        ]
    },
    'Leukemia AML': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [39, 49], 'weight': 0.15},
            {'field': 'screen_time', 'op': '<', 'value': 81, 'weight': 0.19},
            {'field': 'bmi', 'op': '>=', 'value': 131, 'weight': 0.47},
            {'field': 'smoking', 'op': 'between', 'value': [29, 42], 'weight': 0.47},
            {'field': 'sleep_hours', 'op': '<=', 'value': 36, 'weight': 0.24},
        ]
    },
    'Leukemia CLL': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'screen_time', 'op': 'between', 'value': [36, 55], 'weight': 0.2},
            {'field': 'bmi', 'op': 'between', 'value': [33, 45], 'weight': 0.26},
            {'field': 'salt_intake', 'op': '>=', 'value': 45, 'weight': 0.42},
            {'field': 'weight', 'op': 'between', 'value': [26, 55], 'weight': 0.43},
        ]
    },
    'Leukemia CML': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'stress', 'op': '>', 'value': 148, 'weight': 0.39},
            {'field': 'bp_dias', 'op': '>', 'value': 86, 'weight': 0.41},
            {'field': 'bp_sys', 'op': '<=', 'value': 31, 'weight': 0.27},
            {'field': 'activity_mins', 'op': 'between', 'value': [60, 90], 'weight': 0.47},
            {'field': 'height', 'op': '>', 'value': 11, 'weight': 0.22},
        ]
    },
    'Hodgkin Lymphoma': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [52, 69], 'weight': 0.16},
            {'field': 'sleep_hours', 'op': '>', 'value': 101, 'weight': 0.37},
            {'field': 'weight', 'op': 'between', 'value': [25, 42], 'weight': 0.33},
            {'field': 'bp_dias', 'op': '>=', 'value': 38, 'weight': 0.41},
        ]
    },
    'Non-Hodgkin Lymphoma': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 13, 'weight': 0.29},
            {'field': 'weight', 'op': '<=', 'value': 103, 'weight': 0.21},
            {'field': 'height', 'op': '<=', 'value': 34, 'weight': 0.41},
        ]
    },
    'Multiple Myeloma': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'bp_dias', 'op': 'between', 'value': [45, 75], 'weight': 0.18},
            {'field': 'height', 'op': '<', 'value': 135, 'weight': 0.32},
            {'field': 'activity_mins', 'op': '<', 'value': 111, 'weight': 0.13},
        ]
    },
    'Polycythemia Vera': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [46, 69], 'weight': 0.14},
            {'field': 'screen_time', 'op': '>=', 'value': 89, 'weight': 0.18},
            {'field': 'smoking', 'op': '>', 'value': 44, 'weight': 0.41},
            {'field': 'bp_sys', 'op': 'between', 'value': [48, 77], 'weight': 0.43},
        ]
    },
    'Aplastic Anemia': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 60, 'weight': 0.47},
            {'field': 'activity_mins', 'op': '>=', 'value': 22, 'weight': 0.16},
            {'field': 'bmi', 'op': '>', 'value': 38, 'weight': 0.2},
        ]
    },
    'DVT Hematological': {
        'category': 'Hematological', 'icon': 'fa-tint',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 29, 'weight': 0.38},
            {'field': 'screen_time', 'op': '<=', 'value': 85, 'weight': 0.29},
            {'field': 'stress', 'op': 'between', 'value': [54, 80], 'weight': 0.18},
            {'field': 'bp_dias', 'op': 'between', 'value': [29, 39], 'weight': 0.29},
        ]
    },
    'Vitamin D Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'weight', 'op': 'between', 'value': [30, 41], 'weight': 0.12},
            {'field': 'stress', 'op': '<', 'value': 70, 'weight': 0.42},
            {'field': 'age', 'op': '<=', 'value': 3, 'weight': 0.36},
            {'field': 'sleep_hours', 'op': '<=', 'value': 93, 'weight': 0.36},
        ]
    },
    'Vitamin B12 Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 99, 'weight': 0.45},
            {'field': 'stress', 'op': '<=', 'value': 26, 'weight': 0.3},
            {'field': 'bp_dias', 'op': '<=', 'value': 137, 'weight': 0.45},
        ]
    },
    'Iron Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<', 'value': 118, 'weight': 0.3},
            {'field': 'weight', 'op': '>', 'value': 136, 'weight': 0.12},
            {'field': 'screen_time', 'op': '>=', 'value': 41, 'weight': 0.3},
        ]
    },
    'Calcium Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 78, 'weight': 0.24},
            {'field': 'activity_mins', 'op': 'between', 'value': [23, 53], 'weight': 0.21},
            {'field': 'bp_sys', 'op': '<=', 'value': 8, 'weight': 0.46},
        ]
    },
    'Magnesium Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 101, 'weight': 0.16},
            {'field': 'smoking', 'op': '<', 'value': 98, 'weight': 0.14},
            {'field': 'weight', 'op': 'between', 'value': [34, 57], 'weight': 0.45},
            {'field': 'activity_mins', 'op': 'between', 'value': [39, 68], 'weight': 0.16},
            {'field': 'bp_dias', 'op': '<=', 'value': 53, 'weight': 0.32},
        ]
    },
    'Zinc Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'sleep_hours', 'op': 'between', 'value': [32, 46], 'weight': 0.32},
            {'field': 'screen_time', 'op': 'between', 'value': [47, 61], 'weight': 0.46},
            {'field': 'alcohol', 'op': 'between', 'value': [40, 52], 'weight': 0.47},
            {'field': 'height', 'op': 'between', 'value': [27, 42], 'weight': 0.48},
            {'field': 'bp_dias', 'op': '<', 'value': 82, 'weight': 0.39},
        ]
    },
    'Vitamin A Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 71, 'weight': 0.28},
            {'field': 'sleep_hours', 'op': '<', 'value': 48, 'weight': 0.14},
            {'field': 'age', 'op': 'between', 'value': [58, 86], 'weight': 0.35},
            {'field': 'alcohol', 'op': '<', 'value': 60, 'weight': 0.34},
        ]
    },
    'Scurvy': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 123, 'weight': 0.13},
            {'field': 'activity_mins', 'op': 'between', 'value': [50, 80], 'weight': 0.44},
            {'field': 'bp_dias', 'op': '<', 'value': 126, 'weight': 0.44},
            {'field': 'height', 'op': '<', 'value': 58, 'weight': 0.17},
            {'field': 'bmi', 'op': '<=', 'value': 4, 'weight': 0.41},
        ]
    },
    'Iodine Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'bp_sys', 'op': '<', 'value': 52, 'weight': 0.4},
            {'field': 'salt_intake', 'op': '<', 'value': 113, 'weight': 0.13},
            {'field': 'height', 'op': '<=', 'value': 118, 'weight': 0.38},
            {'field': 'activity_mins', 'op': '<=', 'value': 11, 'weight': 0.26},
        ]
    },
    'Folate Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 101, 'weight': 0.39},
            {'field': 'weight', 'op': 'between', 'value': [53, 83], 'weight': 0.34},
            {'field': 'salt_intake', 'op': '>', 'value': 116, 'weight': 0.31},
            {'field': 'bp_dias', 'op': '>', 'value': 63, 'weight': 0.45},
            {'field': 'height', 'op': 'between', 'value': [22, 49], 'weight': 0.26},
        ]
    },
    'Protein Malnutrition': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 113, 'weight': 0.18},
            {'field': 'bp_sys', 'op': '>=', 'value': 74, 'weight': 0.41},
            {'field': 'weight', 'op': '<', 'value': 14, 'weight': 0.27},
            {'field': 'smoking', 'op': '<', 'value': 116, 'weight': 0.29},
        ]
    },
    'Dehydration': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'smoking', 'op': 'between', 'value': [57, 84], 'weight': 0.15},
            {'field': 'sleep_hours', 'op': '<=', 'value': 116, 'weight': 0.27},
            {'field': 'age', 'op': '<', 'value': 52, 'weight': 0.28},
        ]
    },
    'Obesity': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 42, 'weight': 0.23},
            {'field': 'alcohol', 'op': '>', 'value': 116, 'weight': 0.14},
            {'field': 'smoking', 'op': '>=', 'value': 99, 'weight': 0.13},
            {'field': 'weight', 'op': 'between', 'value': [44, 71], 'weight': 0.48},
        ]
    },
    'Malnutrition': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 145, 'weight': 0.46},
            {'field': 'smoking', 'op': '<', 'value': 38, 'weight': 0.16},
            {'field': 'activity_mins', 'op': '>', 'value': 80, 'weight': 0.27},
            {'field': 'weight', 'op': '>=', 'value': 31, 'weight': 0.35},
        ]
    },
    'Vitamin K Deficiency': {
        'category': 'Nutritional', 'icon': 'fa-apple-alt',
        'conditions': [
            {'field': 'activity_mins', 'op': '>', 'value': 65, 'weight': 0.35},
            {'field': 'age', 'op': '<=', 'value': 128, 'weight': 0.3},
            {'field': 'height', 'op': '>', 'value': 127, 'weight': 0.34},
        ]
    },
    'Insomnia': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'activity_mins', 'op': 'between', 'value': [49, 72], 'weight': 0.36},
            {'field': 'water_intake', 'op': '>', 'value': 2, 'weight': 0.34},
            {'field': 'stress', 'op': 'between', 'value': [60, 87], 'weight': 0.21},
        ]
    },
    'Sleep Apnea': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'age', 'op': '<', 'value': 90, 'weight': 0.16},
            {'field': 'bmi', 'op': '<', 'value': 148, 'weight': 0.44},
            {'field': 'smoking', 'op': '>=', 'value': 23, 'weight': 0.23},
        ]
    },
    'Narcolepsy Sleep': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 42, 'weight': 0.5},
            {'field': 'smoking', 'op': '>=', 'value': 147, 'weight': 0.34},
            {'field': 'weight', 'op': '<', 'value': 149, 'weight': 0.49},
        ]
    },
    'RLS Sleep': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 83, 'weight': 0.41},
            {'field': 'bp_sys', 'op': '<=', 'value': 110, 'weight': 0.43},
            {'field': 'height', 'op': '>', 'value': 35, 'weight': 0.22},
            {'field': 'sleep_hours', 'op': '>=', 'value': 106, 'weight': 0.23},
        ]
    },
    'Circadian Rhythm Disorder': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'activity_mins', 'op': '<', 'value': 28, 'weight': 0.34},
            {'field': 'height', 'op': 'between', 'value': [50, 79], 'weight': 0.49},
            {'field': 'salt_intake', 'op': '>=', 'value': 82, 'weight': 0.27},
            {'field': 'screen_time', 'op': 'between', 'value': [59, 80], 'weight': 0.33},
            {'field': 'sleep_hours', 'op': 'between', 'value': [53, 83], 'weight': 0.33},
        ]
    },
    'Sleepwalking': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'bp_dias', 'op': '<', 'value': 60, 'weight': 0.45},
            {'field': 'alcohol', 'op': '>=', 'value': 1, 'weight': 0.49},
            {'field': 'bmi', 'op': '>', 'value': 31, 'weight': 0.29},
            {'field': 'stress', 'op': 'between', 'value': [46, 57], 'weight': 0.5},
        ]
    },
    'REM Sleep Behavior': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'screen_time', 'op': 'between', 'value': [33, 43], 'weight': 0.42},
            {'field': 'smoking', 'op': '<', 'value': 66, 'weight': 0.38},
            {'field': 'bmi', 'op': '>=', 'value': 141, 'weight': 0.22},
            {'field': 'bp_dias', 'op': '>', 'value': 86, 'weight': 0.15},
        ]
    },
    'Night Terrors': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'bp_sys', 'op': 'between', 'value': [21, 36], 'weight': 0.35},
            {'field': 'activity_mins', 'op': '>=', 'value': 123, 'weight': 0.43},
            {'field': 'weight', 'op': '>', 'value': 124, 'weight': 0.36},
            {'field': 'sleep_hours', 'op': '<=', 'value': 138, 'weight': 0.46},
        ]
    },
    'Bruxism Sleep': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 15, 'weight': 0.47},
            {'field': 'weight', 'op': '>=', 'value': 81, 'weight': 0.33},
            {'field': 'height', 'op': 'between', 'value': [56, 76], 'weight': 0.11},
            {'field': 'screen_time', 'op': '>', 'value': 72, 'weight': 0.49},
        ]
    },
    'Hypersomnia': {
        'category': 'Sleep Disorders', 'icon': 'fa-bed',
        'conditions': [
            {'field': 'screen_time', 'op': '<=', 'value': 43, 'weight': 0.35},
            {'field': 'height', 'op': 'between', 'value': [58, 71], 'weight': 0.26},
            {'field': 'stress', 'op': '>=', 'value': 70, 'weight': 0.38},
        ]
    },
    'Lung Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 96, 'weight': 0.45},
            {'field': 'water_intake', 'op': '>=', 'value': 78, 'weight': 0.19},
            {'field': 'activity_mins', 'op': '>', 'value': 10, 'weight': 0.25},
            {'field': 'screen_time', 'op': '>', 'value': 7, 'weight': 0.28},
        ]
    },
    'Breast Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 124, 'weight': 0.18},
            {'field': 'alcohol', 'op': 'between', 'value': [40, 54], 'weight': 0.22},
            {'field': 'bmi', 'op': 'between', 'value': [28, 44], 'weight': 0.37},
            {'field': 'age', 'op': '<=', 'value': 134, 'weight': 0.26},
        ]
    },
    'Prostate Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 23, 'weight': 0.47},
            {'field': 'bp_sys', 'op': '<=', 'value': 27, 'weight': 0.46},
            {'field': 'height', 'op': '>=', 'value': 80, 'weight': 0.11},
        ]
    },
    'Colorectal Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'activity_mins', 'op': '>=', 'value': 74, 'weight': 0.18},
            {'field': 'screen_time', 'op': 'between', 'value': [48, 61], 'weight': 0.23},
            {'field': 'bp_sys', 'op': '<', 'value': 30, 'weight': 0.16},
            {'field': 'age', 'op': 'between', 'value': [26, 42], 'weight': 0.32},
            {'field': 'alcohol', 'op': '>=', 'value': 70, 'weight': 0.32},
        ]
    },
    'Melanoma Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'smoking', 'op': '>=', 'value': 44, 'weight': 0.33},
            {'field': 'bmi', 'op': '>=', 'value': 87, 'weight': 0.35},
            {'field': 'weight', 'op': '<=', 'value': 8, 'weight': 0.12},
        ]
    },
    'Pancreatic Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 14, 'weight': 0.14},
            {'field': 'bmi', 'op': '<=', 'value': 115, 'weight': 0.26},
            {'field': 'smoking', 'op': '>=', 'value': 51, 'weight': 0.22},
            {'field': 'salt_intake', 'op': 'between', 'value': [49, 77], 'weight': 0.13},
        ]
    },
    'Liver Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 80, 'weight': 0.14},
            {'field': 'smoking', 'op': '<=', 'value': 58, 'weight': 0.29},
            {'field': 'activity_mins', 'op': 'between', 'value': [43, 65], 'weight': 0.2},
        ]
    },
    'Stomach Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'smoking', 'op': '>=', 'value': 84, 'weight': 0.42},
            {'field': 'bp_dias', 'op': '<=', 'value': 122, 'weight': 0.11},
            {'field': 'bmi', 'op': '>=', 'value': 44, 'weight': 0.29},
        ]
    },
    'Esophageal Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 33, 'weight': 0.34},
            {'field': 'water_intake', 'op': '>', 'value': 28, 'weight': 0.26},
            {'field': 'screen_time', 'op': 'between', 'value': [39, 66], 'weight': 0.36},
            {'field': 'weight', 'op': '<=', 'value': 62, 'weight': 0.34},
        ]
    },
    'Kidney Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'activity_mins', 'op': 'between', 'value': [50, 72], 'weight': 0.16},
            {'field': 'bmi', 'op': '>=', 'value': 111, 'weight': 0.18},
            {'field': 'water_intake', 'op': 'between', 'value': [54, 71], 'weight': 0.41},
            {'field': 'stress', 'op': '>', 'value': 147, 'weight': 0.4},
            {'field': 'smoking', 'op': '>', 'value': 119, 'weight': 0.34},
        ]
    },
    'Bladder Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 46, 'weight': 0.43},
            {'field': 'stress', 'op': '<=', 'value': 28, 'weight': 0.13},
            {'field': 'alcohol', 'op': 'between', 'value': [44, 64], 'weight': 0.41},
            {'field': 'weight', 'op': '>', 'value': 36, 'weight': 0.14},
        ]
    },
    'Thyroid Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 39, 'weight': 0.4},
            {'field': 'bp_dias', 'op': 'between', 'value': [59, 87], 'weight': 0.22},
            {'field': 'water_intake', 'op': '<', 'value': 82, 'weight': 0.18},
            {'field': 'stress', 'op': 'between', 'value': [39, 62], 'weight': 0.42},
            {'field': 'bp_sys', 'op': '>', 'value': 131, 'weight': 0.33},
        ]
    },
    'Brain Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 16, 'weight': 0.44},
            {'field': 'screen_time', 'op': 'between', 'value': [20, 47], 'weight': 0.49},
            {'field': 'bp_sys', 'op': '>', 'value': 8, 'weight': 0.44},
            {'field': 'activity_mins', 'op': '<=', 'value': 101, 'weight': 0.38},
        ]
    },
    'Ovarian Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'screen_time', 'op': '<=', 'value': 112, 'weight': 0.26},
            {'field': 'weight', 'op': '<', 'value': 122, 'weight': 0.36},
            {'field': 'sleep_hours', 'op': '<', 'value': 93, 'weight': 0.32},
            {'field': 'water_intake', 'op': '<', 'value': 33, 'weight': 0.22},
            {'field': 'activity_mins', 'op': '>', 'value': 5, 'weight': 0.13},
        ]
    },
    'Cervical Cancer Onc': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 35, 'weight': 0.36},
            {'field': 'bmi', 'op': '<', 'value': 107, 'weight': 0.36},
            {'field': 'water_intake', 'op': 'between', 'value': [59, 74], 'weight': 0.47},
        ]
    },
    'Testicular Cancer': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'water_intake', 'op': '<=', 'value': 116, 'weight': 0.32},
            {'field': 'bp_sys', 'op': '>=', 'value': 109, 'weight': 0.19},
            {'field': 'smoking', 'op': '>', 'value': 61, 'weight': 0.33},
            {'field': 'height', 'op': '>=', 'value': 140, 'weight': 0.26},
        ]
    },
    'Head Neck Cancer': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 146, 'weight': 0.49},
            {'field': 'water_intake', 'op': '>=', 'value': 124, 'weight': 0.15},
            {'field': 'salt_intake', 'op': '>', 'value': 135, 'weight': 0.16},
            {'field': 'stress', 'op': '<=', 'value': 134, 'weight': 0.31},
            {'field': 'alcohol', 'op': '>', 'value': 20, 'weight': 0.2},
        ]
    },
    'Bone Cancer': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [39, 68], 'weight': 0.42},
            {'field': 'age', 'op': '>=', 'value': 3, 'weight': 0.31},
            {'field': 'water_intake', 'op': '<=', 'value': 121, 'weight': 0.31},
            {'field': 'alcohol', 'op': '>=', 'value': 76, 'weight': 0.27},
            {'field': 'screen_time', 'op': '<', 'value': 78, 'weight': 0.11},
        ]
    },
    'Soft Tissue Sarcoma': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'alcohol', 'op': 'between', 'value': [60, 85], 'weight': 0.2},
            {'field': 'weight', 'op': '<', 'value': 75, 'weight': 0.33},
            {'field': 'salt_intake', 'op': 'between', 'value': [51, 63], 'weight': 0.11},
            {'field': 'sleep_hours', 'op': 'between', 'value': [37, 55], 'weight': 0.13},
            {'field': 'activity_mins', 'op': 'between', 'value': [36, 46], 'weight': 0.21},
        ]
    },
    'Mesothelioma': {
        'category': 'Oncology', 'icon': 'fa-ribbon',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [57, 71], 'weight': 0.17},
            {'field': 'smoking', 'op': '<=', 'value': 45, 'weight': 0.25},
            {'field': 'screen_time', 'op': '<', 'value': 136, 'weight': 0.29},
            {'field': 'age', 'op': '>=', 'value': 38, 'weight': 0.49},
            {'field': 'salt_intake', 'op': '<', 'value': 106, 'weight': 0.44},
        ]
    },
    'Pediatric Croup': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 43, 'weight': 0.39},
            {'field': 'stress', 'op': 'between', 'value': [42, 53], 'weight': 0.39},
            {'field': 'alcohol', 'op': '>=', 'value': 30, 'weight': 0.4},
            {'field': 'age', 'op': '<', 'value': 122, 'weight': 0.29},
        ]
    },
    'Pediatric HFMD': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'bp_dias', 'op': 'between', 'value': [44, 69], 'weight': 0.19},
            {'field': 'stress', 'op': '<', 'value': 112, 'weight': 0.31},
            {'field': 'age', 'op': '>=', 'value': 115, 'weight': 0.47},
            {'field': 'weight', 'op': '>=', 'value': 11, 'weight': 0.48},
        ]
    },
    'Kawasaki Disease': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'water_intake', 'op': '>=', 'value': 111, 'weight': 0.48},
            {'field': 'height', 'op': '>=', 'value': 69, 'weight': 0.23},
            {'field': 'bmi', 'op': '>=', 'value': 101, 'weight': 0.36},
        ]
    },
    'Childhood Asthma': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 50, 'weight': 0.39},
            {'field': 'water_intake', 'op': '>=', 'value': 47, 'weight': 0.37},
            {'field': 'screen_time', 'op': 'between', 'value': [20, 32], 'weight': 0.1},
            {'field': 'age', 'op': '<=', 'value': 27, 'weight': 0.14},
        ]
    },
    'Juvenile Arthritis': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 73, 'weight': 0.19},
            {'field': 'stress', 'op': '<', 'value': 24, 'weight': 0.11},
            {'field': 'age', 'op': 'between', 'value': [33, 62], 'weight': 0.36},
            {'field': 'salt_intake', 'op': '>', 'value': 31, 'weight': 0.38},
            {'field': 'sleep_hours', 'op': 'between', 'value': [56, 71], 'weight': 0.15},
        ]
    },
    'Febrile Seizures': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'smoking', 'op': '<', 'value': 120, 'weight': 0.2},
            {'field': 'height', 'op': '>', 'value': 71, 'weight': 0.36},
            {'field': 'bp_sys', 'op': '>=', 'value': 19, 'weight': 0.2},
        ]
    },
    'Infantile Colic': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 86, 'weight': 0.25},
            {'field': 'age', 'op': '>=', 'value': 68, 'weight': 0.48},
            {'field': 'activity_mins', 'op': '<=', 'value': 52, 'weight': 0.13},
            {'field': 'smoking', 'op': '<=', 'value': 126, 'weight': 0.17},
        ]
    },
    'RSV Bronchiolitis': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'sleep_hours', 'op': 'between', 'value': [33, 62], 'weight': 0.41},
            {'field': 'smoking', 'op': '>', 'value': 67, 'weight': 0.47},
            {'field': 'bmi', 'op': '>', 'value': 147, 'weight': 0.13},
        ]
    },
    'Childhood Obesity': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 128, 'weight': 0.11},
            {'field': 'sleep_hours', 'op': '>', 'value': 100, 'weight': 0.47},
            {'field': 'bp_sys', 'op': '<', 'value': 101, 'weight': 0.38},
            {'field': 'alcohol', 'op': '>', 'value': 126, 'weight': 0.31},
            {'field': 'height', 'op': '<=', 'value': 18, 'weight': 0.26},
        ]
    },
    'Growth Delay': {
        'category': 'Pediatric', 'icon': 'fa-baby',
        'conditions': [
            {'field': 'activity_mins', 'op': '>', 'value': 124, 'weight': 0.25},
            {'field': 'bmi', 'op': 'between', 'value': [42, 62], 'weight': 0.31},
            {'field': 'alcohol', 'op': '>=', 'value': 24, 'weight': 0.26},
            {'field': 'bp_dias', 'op': 'between', 'value': [41, 53], 'weight': 0.44},
            {'field': 'height', 'op': '>=', 'value': 46, 'weight': 0.36},
        ]
    },
    'Dental Caries': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'age', 'op': '<=', 'value': 77, 'weight': 0.36},
            {'field': 'alcohol', 'op': '<=', 'value': 92, 'weight': 0.46},
            {'field': 'water_intake', 'op': '>', 'value': 113, 'weight': 0.45},
            {'field': 'stress', 'op': '<', 'value': 7, 'weight': 0.11},
            {'field': 'salt_intake', 'op': '<', 'value': 17, 'weight': 0.3},
        ]
    },
    'Periodontal Disease': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 116, 'weight': 0.3},
            {'field': 'age', 'op': '>', 'value': 87, 'weight': 0.24},
            {'field': 'salt_intake', 'op': '>', 'value': 55, 'weight': 0.26},
            {'field': 'alcohol', 'op': 'between', 'value': [54, 68], 'weight': 0.28},
            {'field': 'smoking', 'op': '<', 'value': 10, 'weight': 0.47},
        ]
    },
    'Gingivitis': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<=', 'value': 121, 'weight': 0.36},
            {'field': 'height', 'op': '>', 'value': 34, 'weight': 0.2},
            {'field': 'age', 'op': '<', 'value': 79, 'weight': 0.35},
            {'field': 'activity_mins', 'op': '<=', 'value': 17, 'weight': 0.34},
            {'field': 'stress', 'op': '>', 'value': 57, 'weight': 0.3},
        ]
    },
    'Tooth Abscess': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 103, 'weight': 0.27},
            {'field': 'screen_time', 'op': '>', 'value': 148, 'weight': 0.49},
            {'field': 'weight', 'op': '<', 'value': 55, 'weight': 0.23},
        ]
    },
    'TMJ Disorder': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 31, 'weight': 0.23},
            {'field': 'stress', 'op': '<', 'value': 44, 'weight': 0.4},
            {'field': 'salt_intake', 'op': '>=', 'value': 113, 'weight': 0.32},
        ]
    },
    'Oral Thrush': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'weight', 'op': '>', 'value': 97, 'weight': 0.15},
            {'field': 'salt_intake', 'op': '<', 'value': 125, 'weight': 0.11},
            {'field': 'bmi', 'op': '>', 'value': 23, 'weight': 0.1},
        ]
    },
    'Bruxism Dental': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [46, 71], 'weight': 0.45},
            {'field': 'alcohol', 'op': '<', 'value': 70, 'weight': 0.18},
            {'field': 'water_intake', 'op': '<=', 'value': 45, 'weight': 0.26},
            {'field': 'smoking', 'op': '>', 'value': 128, 'weight': 0.34},
            {'field': 'salt_intake', 'op': '>', 'value': 78, 'weight': 0.35},
        ]
    },
    'Dental Erosion': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'bp_sys', 'op': '>', 'value': 50, 'weight': 0.32},
            {'field': 'bmi', 'op': 'between', 'value': [59, 80], 'weight': 0.49},
            {'field': 'height', 'op': 'between', 'value': [60, 76], 'weight': 0.19},
            {'field': 'screen_time', 'op': '>', 'value': 39, 'weight': 0.18},
        ]
    },
    'Wisdom Tooth Impaction': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 41, 'weight': 0.3},
            {'field': 'height', 'op': '>', 'value': 94, 'weight': 0.12},
            {'field': 'stress', 'op': '<', 'value': 86, 'weight': 0.27},
            {'field': 'smoking', 'op': '<=', 'value': 14, 'weight': 0.12},
            {'field': 'weight', 'op': '<', 'value': 8, 'weight': 0.16},
        ]
    },
    'Halitosis': {
        'category': 'Dental', 'icon': 'fa-tooth',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 61, 'weight': 0.13},
            {'field': 'alcohol', 'op': '<=', 'value': 84, 'weight': 0.34},
            {'field': 'bp_sys', 'op': '<', 'value': 84, 'weight': 0.4},
            {'field': 'activity_mins', 'op': '>', 'value': 26, 'weight': 0.23},
        ]
    },
    'Sedentary Lifestyle Risk': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 97, 'weight': 0.45},
            {'field': 'activity_mins', 'op': '>', 'value': 125, 'weight': 0.29},
            {'field': 'age', 'op': '<=', 'value': 117, 'weight': 0.16},
        ]
    },
    'Screen Addiction': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 50, 'weight': 0.15},
            {'field': 'smoking', 'op': '>=', 'value': 52, 'weight': 0.49},
            {'field': 'screen_time', 'op': '<', 'value': 146, 'weight': 0.11},
        ]
    },
    'Chronic Stress': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 120, 'weight': 0.14},
            {'field': 'water_intake', 'op': '<=', 'value': 88, 'weight': 0.17},
            {'field': 'activity_mins', 'op': '>=', 'value': 44, 'weight': 0.34},
        ]
    },
    'Burnout Syndrome': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 134, 'weight': 0.13},
            {'field': 'bp_dias', 'op': '<', 'value': 119, 'weight': 0.34},
            {'field': 'stress', 'op': '>', 'value': 64, 'weight': 0.39},
            {'field': 'activity_mins', 'op': '>=', 'value': 57, 'weight': 0.27},
            {'field': 'salt_intake', 'op': '<', 'value': 2, 'weight': 0.47},
        ]
    },
    'Work-Related Injury': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 130, 'weight': 0.5},
            {'field': 'bmi', 'op': '<=', 'value': 123, 'weight': 0.31},
            {'field': 'salt_intake', 'op': '>', 'value': 62, 'weight': 0.28},
            {'field': 'activity_mins', 'op': 'between', 'value': [46, 62], 'weight': 0.4},
        ]
    },
    'Heat Exhaustion': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 24, 'weight': 0.2},
            {'field': 'age', 'op': '<=', 'value': 42, 'weight': 0.37},
            {'field': 'salt_intake', 'op': '<=', 'value': 150, 'weight': 0.44},
        ]
    },
    'Altitude Sickness': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 104, 'weight': 0.41},
            {'field': 'sleep_hours', 'op': '>=', 'value': 1, 'weight': 0.35},
            {'field': 'alcohol', 'op': '>', 'value': 86, 'weight': 0.25},
        ]
    },
    'Motion Sickness': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 70, 'weight': 0.27},
            {'field': 'alcohol', 'op': 'between', 'value': [33, 45], 'weight': 0.32},
            {'field': 'height', 'op': '>=', 'value': 15, 'weight': 0.39},
            {'field': 'weight', 'op': '>=', 'value': 29, 'weight': 0.46},
            {'field': 'bp_dias', 'op': '>=', 'value': 11, 'weight': 0.29},
        ]
    },
    'Jet Lag': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 18, 'weight': 0.36},
            {'field': 'weight', 'op': '<', 'value': 86, 'weight': 0.16},
            {'field': 'activity_mins', 'op': 'between', 'value': [50, 78], 'weight': 0.15},
            {'field': 'stress', 'op': '<', 'value': 69, 'weight': 0.23},
        ]
    },
    'Noise-Induced Hearing Loss': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 17, 'weight': 0.21},
            {'field': 'screen_time', 'op': '>=', 'value': 129, 'weight': 0.28},
            {'field': 'weight', 'op': '>', 'value': 137, 'weight': 0.29},
            {'field': 'salt_intake', 'op': 'between', 'value': [48, 77], 'weight': 0.46},
            {'field': 'bp_sys', 'op': '>', 'value': 118, 'weight': 0.18},
        ]
    },
    'Ergonomic Strain': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 74, 'weight': 0.46},
            {'field': 'sleep_hours', 'op': '>', 'value': 29, 'weight': 0.17},
            {'field': 'salt_intake', 'op': '<', 'value': 53, 'weight': 0.3},
        ]
    },
    'Digital Addiction': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 139, 'weight': 0.22},
            {'field': 'sleep_hours', 'op': '<=', 'value': 114, 'weight': 0.24},
            {'field': 'salt_intake', 'op': '>', 'value': 17, 'weight': 0.22},
            {'field': 'age', 'op': '<', 'value': 134, 'weight': 0.43},
            {'field': 'bp_dias', 'op': '<=', 'value': 84, 'weight': 0.33},
        ]
    },
    'Social Media Anxiety': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'weight', 'op': 'between', 'value': [48, 72], 'weight': 0.44},
            {'field': 'stress', 'op': 'between', 'value': [39, 54], 'weight': 0.15},
            {'field': 'screen_time', 'op': '<', 'value': 74, 'weight': 0.29},
            {'field': 'age', 'op': '<', 'value': 117, 'weight': 0.24},
        ]
    },
    'Caffeine Dependency': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'weight', 'op': '<', 'value': 74, 'weight': 0.38},
            {'field': 'sleep_hours', 'op': '<', 'value': 40, 'weight': 0.44},
            {'field': 'activity_mins', 'op': '<', 'value': 82, 'weight': 0.15},
        ]
    },
    'Nicotine Dependency': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<=', 'value': 48, 'weight': 0.2},
            {'field': 'stress', 'op': 'between', 'value': [40, 61], 'weight': 0.38},
            {'field': 'activity_mins', 'op': '>=', 'value': 42, 'weight': 0.28},
            {'field': 'smoking', 'op': '>=', 'value': 7, 'weight': 0.15},
            {'field': 'weight', 'op': '<=', 'value': 118, 'weight': 0.41},
        ]
    },
    'Alcohol Dependency': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 140, 'weight': 0.49},
            {'field': 'weight', 'op': '>=', 'value': 76, 'weight': 0.36},
            {'field': 'water_intake', 'op': '>=', 'value': 147, 'weight': 0.49},
            {'field': 'salt_intake', 'op': '<', 'value': 114, 'weight': 0.42},
        ]
    },
    'Gaming Disorder': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'smoking', 'op': '>', 'value': 11, 'weight': 0.39},
            {'field': 'sleep_hours', 'op': 'between', 'value': [21, 43], 'weight': 0.15},
            {'field': 'height', 'op': '<', 'value': 24, 'weight': 0.28},
            {'field': 'bp_sys', 'op': '>', 'value': 50, 'weight': 0.34},
        ]
    },
    'Workaholism': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'water_intake', 'op': '<', 'value': 72, 'weight': 0.41},
            {'field': 'activity_mins', 'op': '>', 'value': 115, 'weight': 0.13},
            {'field': 'alcohol', 'op': '>', 'value': 101, 'weight': 0.49},
            {'field': 'stress', 'op': '<=', 'value': 131, 'weight': 0.23},
            {'field': 'age', 'op': '>=', 'value': 110, 'weight': 0.26},
        ]
    },
    'Night Shift Disorder': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 89, 'weight': 0.1},
            {'field': 'screen_time', 'op': '>=', 'value': 144, 'weight': 0.49},
            {'field': 'bmi', 'op': '<', 'value': 114, 'weight': 0.39},
            {'field': 'weight', 'op': '<=', 'value': 109, 'weight': 0.22},
        ]
    },
    'Smartphone Neck': {
        'category': 'Lifestyle', 'icon': 'fa-running',
        'conditions': [
            {'field': 'bp_sys', 'op': '<', 'value': 23, 'weight': 0.43},
            {'field': 'sleep_hours', 'op': '<', 'value': 135, 'weight': 0.22},
            {'field': 'bp_dias', 'op': '>', 'value': 97, 'weight': 0.47},
            {'field': 'bmi', 'op': '>', 'value': 70, 'weight': 0.26},
            {'field': 'height', 'op': '<', 'value': 146, 'weight': 0.32},
        ]
    },
    'Age-Related Sarcopenia': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'activity_mins', 'op': '<', 'value': 75, 'weight': 0.43},
            {'field': 'weight', 'op': '<=', 'value': 78, 'weight': 0.12},
            {'field': 'smoking', 'op': '>=', 'value': 119, 'weight': 0.3},
        ]
    },
    'Senile Dementia': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 77, 'weight': 0.16},
            {'field': 'smoking', 'op': '<=', 'value': 74, 'weight': 0.15},
            {'field': 'bp_dias', 'op': '<', 'value': 63, 'weight': 0.3},
        ]
    },
    'Presbyopia': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 18, 'weight': 0.3},
            {'field': 'height', 'op': '>=', 'value': 145, 'weight': 0.33},
            {'field': 'bp_dias', 'op': '>=', 'value': 122, 'weight': 0.35},
        ]
    },
    'Presbycusis': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'salt_intake', 'op': '>', 'value': 148, 'weight': 0.25},
            {'field': 'age', 'op': '>=', 'value': 15, 'weight': 0.17},
            {'field': 'activity_mins', 'op': '>=', 'value': 35, 'weight': 0.28},
            {'field': 'bp_dias', 'op': '<', 'value': 93, 'weight': 0.12},
            {'field': 'weight', 'op': '>=', 'value': 75, 'weight': 0.12},
        ]
    },
    'Falls Risk Syndrome': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 47, 'weight': 0.31},
            {'field': 'salt_intake', 'op': '>', 'value': 43, 'weight': 0.34},
            {'field': 'water_intake', 'op': '>=', 'value': 78, 'weight': 0.45},
            {'field': 'stress', 'op': '>=', 'value': 149, 'weight': 0.14},
            {'field': 'bp_sys', 'op': '<', 'value': 133, 'weight': 0.11},
        ]
    },
    'Urinary Retention Elderly': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'screen_time', 'op': '<=', 'value': 42, 'weight': 0.26},
            {'field': 'bmi', 'op': '<', 'value': 57, 'weight': 0.16},
            {'field': 'stress', 'op': 'between', 'value': [53, 80], 'weight': 0.35},
            {'field': 'smoking', 'op': '>', 'value': 20, 'weight': 0.27},
        ]
    },
    'Delirium': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 123, 'weight': 0.47},
            {'field': 'screen_time', 'op': '>=', 'value': 36, 'weight': 0.38},
            {'field': 'water_intake', 'op': 'between', 'value': [41, 56], 'weight': 0.31},
        ]
    },
    'Bedsores': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'stress', 'op': '>', 'value': 31, 'weight': 0.4},
            {'field': 'activity_mins', 'op': '<', 'value': 37, 'weight': 0.44},
            {'field': 'salt_intake', 'op': '<', 'value': 54, 'weight': 0.22},
            {'field': 'sleep_hours', 'op': '>', 'value': 29, 'weight': 0.27},
            {'field': 'bmi', 'op': '>', 'value': 111, 'weight': 0.41},
        ]
    },
    'Malnutrition Elderly': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'activity_mins', 'op': '>', 'value': 132, 'weight': 0.11},
            {'field': 'height', 'op': '>', 'value': 65, 'weight': 0.29},
            {'field': 'age', 'op': '>', 'value': 3, 'weight': 0.22},
        ]
    },
    'Polypharmacy Risk': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 53, 'weight': 0.47},
            {'field': 'weight', 'op': '<', 'value': 90, 'weight': 0.17},
            {'field': 'age', 'op': '>', 'value': 72, 'weight': 0.16},
        ]
    },
    'Sundowner Syndrome': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 129, 'weight': 0.16},
            {'field': 'salt_intake', 'op': 'between', 'value': [56, 68], 'weight': 0.2},
            {'field': 'bmi', 'op': 'between', 'value': [53, 69], 'weight': 0.41},
            {'field': 'stress', 'op': '>=', 'value': 138, 'weight': 0.17},
            {'field': 'age', 'op': '>', 'value': 130, 'weight': 0.47},
        ]
    },
    'Vascular Dementia': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 48, 'weight': 0.38},
            {'field': 'water_intake', 'op': '>', 'value': 91, 'weight': 0.17},
            {'field': 'bp_sys', 'op': '<=', 'value': 59, 'weight': 0.19},
            {'field': 'weight', 'op': '>', 'value': 81, 'weight': 0.4},
            {'field': 'bmi', 'op': '<=', 'value': 35, 'weight': 0.14},
        ]
    },
    'Lewy Body Dementia': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 143, 'weight': 0.38},
            {'field': 'smoking', 'op': '>', 'value': 127, 'weight': 0.13},
            {'field': 'bmi', 'op': '<=', 'value': 80, 'weight': 0.21},
            {'field': 'salt_intake', 'op': '<=', 'value': 105, 'weight': 0.19},
        ]
    },
    'Frailty Syndrome': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 18, 'weight': 0.18},
            {'field': 'alcohol', 'op': '<=', 'value': 95, 'weight': 0.48},
            {'field': 'sleep_hours', 'op': '>', 'value': 126, 'weight': 0.5},
            {'field': 'smoking', 'op': '>', 'value': 134, 'weight': 0.26},
        ]
    },
    'Elder Abuse Signs': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'height', 'op': '>', 'value': 102, 'weight': 0.15},
            {'field': 'bp_sys', 'op': 'between', 'value': [30, 42], 'weight': 0.49},
            {'field': 'screen_time', 'op': '<', 'value': 104, 'weight': 0.24},
            {'field': 'bmi', 'op': '<', 'value': 128, 'weight': 0.44},
            {'field': 'bp_dias', 'op': 'between', 'value': [45, 66], 'weight': 0.34},
        ]
    },
    'Orthostatic Hypotension': {
        'category': 'Geriatric', 'icon': 'fa-user-clock',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [51, 77], 'weight': 0.48},
            {'field': 'stress', 'op': '<', 'value': 28, 'weight': 0.41},
            {'field': 'bmi', 'op': '>=', 'value': 60, 'weight': 0.3},
            {'field': 'salt_intake', 'op': '<', 'value': 14, 'weight': 0.11},
        ]
    },
    'Chronic Pain Syndrome': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 98, 'weight': 0.49},
            {'field': 'height', 'op': '>=', 'value': 25, 'weight': 0.16},
            {'field': 'bmi', 'op': 'between', 'value': [49, 65], 'weight': 0.41},
        ]
    },
    'Complex Regional Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'height', 'op': '<=', 'value': 67, 'weight': 0.3},
            {'field': 'water_intake', 'op': '>=', 'value': 139, 'weight': 0.42},
            {'field': 'weight', 'op': '>', 'value': 9, 'weight': 0.48},
            {'field': 'bp_sys', 'op': '>', 'value': 81, 'weight': 0.25},
        ]
    },
    'Phantom Limb Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 46, 'weight': 0.11},
            {'field': 'weight', 'op': '>=', 'value': 43, 'weight': 0.45},
            {'field': 'water_intake', 'op': '<=', 'value': 100, 'weight': 0.15},
            {'field': 'height', 'op': '>', 'value': 126, 'weight': 0.33},
        ]
    },
    'Neuropathic Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'water_intake', 'op': 'between', 'value': [50, 77], 'weight': 0.33},
            {'field': 'sleep_hours', 'op': 'between', 'value': [36, 61], 'weight': 0.12},
            {'field': 'smoking', 'op': '<=', 'value': 91, 'weight': 0.35},
            {'field': 'screen_time', 'op': '>=', 'value': 12, 'weight': 0.12},
            {'field': 'activity_mins', 'op': '>=', 'value': 150, 'weight': 0.24},
        ]
    },
    'Central Pain Syndrome': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 110, 'weight': 0.25},
            {'field': 'screen_time', 'op': '>=', 'value': 15, 'weight': 0.26},
            {'field': 'smoking', 'op': '<', 'value': 80, 'weight': 0.2},
        ]
    },
    'Postherpetic Neuralgia': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 30, 'weight': 0.45},
            {'field': 'bp_sys', 'op': '<', 'value': 84, 'weight': 0.11},
            {'field': 'age', 'op': '<=', 'value': 109, 'weight': 0.36},
            {'field': 'alcohol', 'op': 'between', 'value': [37, 47], 'weight': 0.46},
            {'field': 'height', 'op': 'between', 'value': [40, 62], 'weight': 0.11},
        ]
    },
    'Chronic Pelvic Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'bp_sys', 'op': '>=', 'value': 126, 'weight': 0.33},
            {'field': 'bmi', 'op': '<', 'value': 129, 'weight': 0.23},
            {'field': 'alcohol', 'op': '>=', 'value': 77, 'weight': 0.17},
            {'field': 'bp_dias', 'op': '<=', 'value': 20, 'weight': 0.18},
            {'field': 'smoking', 'op': '<', 'value': 13, 'weight': 0.21},
        ]
    },
    'Chronic Prostatitis': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'weight', 'op': '<=', 'value': 24, 'weight': 0.42},
            {'field': 'alcohol', 'op': 'between', 'value': [41, 59], 'weight': 0.14},
            {'field': 'bmi', 'op': 'between', 'value': [50, 73], 'weight': 0.42},
            {'field': 'stress', 'op': '>=', 'value': 78, 'weight': 0.42},
        ]
    },
    'Temporomandibular Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'alcohol', 'op': '>=', 'value': 139, 'weight': 0.27},
            {'field': 'screen_time', 'op': '<', 'value': 65, 'weight': 0.27},
            {'field': 'height', 'op': 'between', 'value': [55, 70], 'weight': 0.28},
            {'field': 'age', 'op': 'between', 'value': [56, 81], 'weight': 0.45},
            {'field': 'stress', 'op': '<=', 'value': 137, 'weight': 0.21},
        ]
    },
    'Chronic Fatigue Syndrome': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 16, 'weight': 0.47},
            {'field': 'water_intake', 'op': '<', 'value': 38, 'weight': 0.25},
            {'field': 'activity_mins', 'op': '<', 'value': 77, 'weight': 0.4},
            {'field': 'bp_dias', 'op': '<=', 'value': 17, 'weight': 0.23},
            {'field': 'stress', 'op': '<=', 'value': 74, 'weight': 0.21},
        ]
    },
    'Myalgic Encephalomyelitis': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>=', 'value': 61, 'weight': 0.37},
            {'field': 'bp_dias', 'op': '<', 'value': 50, 'weight': 0.15},
            {'field': 'age', 'op': '<', 'value': 80, 'weight': 0.42},
            {'field': 'height', 'op': '<=', 'value': 112, 'weight': 0.32},
            {'field': 'weight', 'op': '>', 'value': 70, 'weight': 0.18},
        ]
    },
    'Vulvodynia': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'age', 'op': '>=', 'value': 72, 'weight': 0.42},
            {'field': 'smoking', 'op': 'between', 'value': [22, 47], 'weight': 0.17},
            {'field': 'bmi', 'op': '>', 'value': 22, 'weight': 0.44},
        ]
    },
    'Interstitial Cystitis Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'weight', 'op': '>=', 'value': 105, 'weight': 0.45},
            {'field': 'screen_time', 'op': '>', 'value': 36, 'weight': 0.26},
            {'field': 'activity_mins', 'op': '>', 'value': 129, 'weight': 0.33},
            {'field': 'bmi', 'op': 'between', 'value': [57, 83], 'weight': 0.37},
        ]
    },
    'Chronic Abdominal Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 32, 'weight': 0.2},
            {'field': 'salt_intake', 'op': '>=', 'value': 150, 'weight': 0.23},
            {'field': 'alcohol', 'op': '<=', 'value': 61, 'weight': 0.42},
            {'field': 'bp_sys', 'op': '<', 'value': 45, 'weight': 0.16},
        ]
    },
    'Chest Wall Pain': {
        'category': 'Pain Syndromes', 'icon': 'fa-bolt',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 15, 'weight': 0.26},
            {'field': 'water_intake', 'op': 'between', 'value': [27, 47], 'weight': 0.25},
            {'field': 'height', 'op': '<=', 'value': 64, 'weight': 0.29},
        ]
    },
    'Lead Poisoning': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 95, 'weight': 0.25},
            {'field': 'stress', 'op': '>', 'value': 9, 'weight': 0.36},
            {'field': 'salt_intake', 'op': '>', 'value': 62, 'weight': 0.38},
            {'field': 'screen_time', 'op': 'between', 'value': [60, 81], 'weight': 0.25},
        ]
    },
    'Carbon Monoxide Poisoning': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'bmi', 'op': 'between', 'value': [48, 70], 'weight': 0.45},
            {'field': 'age', 'op': '<=', 'value': 66, 'weight': 0.47},
            {'field': 'bp_sys', 'op': '>', 'value': 61, 'weight': 0.47},
            {'field': 'bp_dias', 'op': '<', 'value': 42, 'weight': 0.44},
            {'field': 'smoking', 'op': '>=', 'value': 105, 'weight': 0.45},
        ]
    },
    'Heatstroke': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'stress', 'op': '>', 'value': 126, 'weight': 0.43},
            {'field': 'water_intake', 'op': '<=', 'value': 86, 'weight': 0.47},
            {'field': 'salt_intake', 'op': '<=', 'value': 26, 'weight': 0.45},
        ]
    },
    'Hypothermia': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'smoking', 'op': '>=', 'value': 91, 'weight': 0.3},
            {'field': 'bp_sys', 'op': 'between', 'value': [55, 75], 'weight': 0.39},
            {'field': 'water_intake', 'op': '>', 'value': 48, 'weight': 0.4},
        ]
    },
    'Frostbite': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'bp_dias', 'op': '<', 'value': 52, 'weight': 0.1},
            {'field': 'smoking', 'op': '>=', 'value': 22, 'weight': 0.23},
            {'field': 'bmi', 'op': '<', 'value': 34, 'weight': 0.2},
            {'field': 'alcohol', 'op': '<=', 'value': 82, 'weight': 0.42},
            {'field': 'weight', 'op': '<=', 'value': 35, 'weight': 0.45},
        ]
    },
    'Radiation Sickness': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'sleep_hours', 'op': 'between', 'value': [38, 54], 'weight': 0.43},
            {'field': 'bmi', 'op': '<=', 'value': 101, 'weight': 0.25},
            {'field': 'water_intake', 'op': 'between', 'value': [21, 48], 'weight': 0.19},
            {'field': 'salt_intake', 'op': 'between', 'value': [25, 49], 'weight': 0.35},
        ]
    },
    'Decompression Sickness': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 110, 'weight': 0.12},
            {'field': 'height', 'op': '>=', 'value': 95, 'weight': 0.16},
            {'field': 'sleep_hours', 'op': 'between', 'value': [53, 76], 'weight': 0.15},
        ]
    },
    'Drowning Recovery': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'salt_intake', 'op': '<=', 'value': 53, 'weight': 0.15},
            {'field': 'activity_mins', 'op': '>=', 'value': 127, 'weight': 0.22},
            {'field': 'bp_dias', 'op': '<', 'value': 53, 'weight': 0.27},
            {'field': 'smoking', 'op': '<', 'value': 73, 'weight': 0.5},
        ]
    },
    'Smoke Inhalation': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 105, 'weight': 0.27},
            {'field': 'salt_intake', 'op': '<', 'value': 68, 'weight': 0.11},
            {'field': 'activity_mins', 'op': 'between', 'value': [35, 56], 'weight': 0.28},
            {'field': 'smoking', 'op': '<=', 'value': 121, 'weight': 0.13},
            {'field': 'sleep_hours', 'op': '>=', 'value': 102, 'weight': 0.49},
        ]
    },
    'Chemical Burns': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 66, 'weight': 0.38},
            {'field': 'bmi', 'op': '>', 'value': 14, 'weight': 0.32},
            {'field': 'bp_dias', 'op': '<', 'value': 91, 'weight': 0.29},
            {'field': 'alcohol', 'op': 'between', 'value': [22, 32], 'weight': 0.38},
            {'field': 'bp_sys', 'op': 'between', 'value': [39, 61], 'weight': 0.35},
        ]
    },
    'Sunburn Severe': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'screen_time', 'op': '<', 'value': 144, 'weight': 0.49},
            {'field': 'age', 'op': 'between', 'value': [30, 56], 'weight': 0.17},
            {'field': 'weight', 'op': '>=', 'value': 34, 'weight': 0.45},
            {'field': 'sleep_hours', 'op': '>=', 'value': 111, 'weight': 0.38},
            {'field': 'stress', 'op': '>=', 'value': 12, 'weight': 0.15},
        ]
    },
    'Insect Sting Allergy': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 111, 'weight': 0.4},
            {'field': 'stress', 'op': '>=', 'value': 68, 'weight': 0.35},
            {'field': 'height', 'op': '>=', 'value': 43, 'weight': 0.27},
        ]
    },
    'Snake Bite': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 39, 'weight': 0.41},
            {'field': 'water_intake', 'op': '<=', 'value': 39, 'weight': 0.12},
            {'field': 'age', 'op': '<', 'value': 121, 'weight': 0.17},
            {'field': 'screen_time', 'op': '<', 'value': 112, 'weight': 0.38},
        ]
    },
    'Food Allergy Severe': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 144, 'weight': 0.28},
            {'field': 'water_intake', 'op': '<=', 'value': 38, 'weight': 0.3},
            {'field': 'bmi', 'op': '>=', 'value': 73, 'weight': 0.14},
        ]
    },
    'Drug Allergy': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'salt_intake', 'op': '<', 'value': 70, 'weight': 0.4},
            {'field': 'weight', 'op': 'between', 'value': [20, 46], 'weight': 0.18},
            {'field': 'height', 'op': '<', 'value': 20, 'weight': 0.27},
        ]
    },
    'Latex Allergy': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'alcohol', 'op': '<=', 'value': 85, 'weight': 0.37},
            {'field': 'age', 'op': '>=', 'value': 32, 'weight': 0.37},
            {'field': 'bp_dias', 'op': '>=', 'value': 28, 'weight': 0.34},
        ]
    },
    'Anaphylaxis Risk': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 123, 'weight': 0.13},
            {'field': 'water_intake', 'op': '>=', 'value': 2, 'weight': 0.34},
            {'field': 'bp_sys', 'op': '>', 'value': 116, 'weight': 0.36},
            {'field': 'bp_dias', 'op': 'between', 'value': [23, 53], 'weight': 0.15},
        ]
    },
    'Asbestos Exposure': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 141, 'weight': 0.4},
            {'field': 'height', 'op': '<=', 'value': 66, 'weight': 0.14},
            {'field': 'sleep_hours', 'op': '<', 'value': 103, 'weight': 0.49},
            {'field': 'bmi', 'op': '>', 'value': 42, 'weight': 0.44},
        ]
    },
    'Noise Trauma': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'alcohol', 'op': '<=', 'value': 40, 'weight': 0.21},
            {'field': 'bmi', 'op': '>=', 'value': 111, 'weight': 0.3},
            {'field': 'salt_intake', 'op': '>=', 'value': 34, 'weight': 0.46},
            {'field': 'bp_sys', 'op': '>', 'value': 132, 'weight': 0.43},
        ]
    },
    'UV Damage Chronic': {
        'category': 'Environmental', 'icon': 'fa-globe',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 122, 'weight': 0.45},
            {'field': 'stress', 'op': 'between', 'value': [25, 48], 'weight': 0.34},
            {'field': 'bp_sys', 'op': 'between', 'value': [60, 83], 'weight': 0.17},
        ]
    },
    'Erectile Dysfunction': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [49, 66], 'weight': 0.24},
            {'field': 'smoking', 'op': '<', 'value': 135, 'weight': 0.47},
            {'field': 'alcohol', 'op': 'between', 'value': [49, 72], 'weight': 0.13},
        ]
    },
    'Male Infertility': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'alcohol', 'op': '<=', 'value': 33, 'weight': 0.22},
            {'field': 'height', 'op': '>=', 'value': 134, 'weight': 0.44},
            {'field': 'bp_sys', 'op': '>=', 'value': 142, 'weight': 0.33},
        ]
    },
    'Varicocele': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [47, 70], 'weight': 0.14},
            {'field': 'sleep_hours', 'op': '<=', 'value': 146, 'weight': 0.36},
            {'field': 'bp_sys', 'op': '>=', 'value': 21, 'weight': 0.2},
        ]
    },
    'Epididymitis': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'age', 'op': '>', 'value': 119, 'weight': 0.4},
            {'field': 'activity_mins', 'op': '<', 'value': 12, 'weight': 0.44},
            {'field': 'sleep_hours', 'op': '<=', 'value': 77, 'weight': 0.45},
            {'field': 'water_intake', 'op': 'between', 'value': [48, 77], 'weight': 0.39},
            {'field': 'bp_dias', 'op': '>=', 'value': 48, 'weight': 0.49},
        ]
    },
    'Orchitis': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 67, 'weight': 0.4},
            {'field': 'smoking', 'op': '>', 'value': 5, 'weight': 0.27},
            {'field': 'age', 'op': '<=', 'value': 44, 'weight': 0.15},
        ]
    },
    'Peyronie Disease': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 125, 'weight': 0.38},
            {'field': 'stress', 'op': 'between', 'value': [59, 80], 'weight': 0.43},
            {'field': 'salt_intake', 'op': '<=', 'value': 23, 'weight': 0.42},
            {'field': 'sleep_hours', 'op': '<', 'value': 29, 'weight': 0.11},
            {'field': 'age', 'op': '<', 'value': 54, 'weight': 0.44},
        ]
    },
    'Premature Ejaculation': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'height', 'op': '<', 'value': 112, 'weight': 0.36},
            {'field': 'smoking', 'op': 'between', 'value': [39, 63], 'weight': 0.18},
            {'field': 'sleep_hours', 'op': '<=', 'value': 30, 'weight': 0.27},
            {'field': 'activity_mins', 'op': '<', 'value': 114, 'weight': 0.4},
        ]
    },
    'Low Testosterone': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'bp_dias', 'op': '>', 'value': 150, 'weight': 0.44},
            {'field': 'activity_mins', 'op': '<', 'value': 101, 'weight': 0.22},
            {'field': 'age', 'op': '>=', 'value': 111, 'weight': 0.1},
            {'field': 'weight', 'op': '<=', 'value': 142, 'weight': 0.39},
        ]
    },
    'Gynecomastia': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'age', 'op': '<=', 'value': 132, 'weight': 0.26},
            {'field': 'height', 'op': 'between', 'value': [51, 68], 'weight': 0.47},
            {'field': 'salt_intake', 'op': '>', 'value': 109, 'weight': 0.31},
            {'field': 'smoking', 'op': '>=', 'value': 69, 'weight': 0.32},
        ]
    },
    'Testicular Torsion': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 89, 'weight': 0.15},
            {'field': 'water_intake', 'op': '<=', 'value': 74, 'weight': 0.11},
            {'field': 'salt_intake', 'op': '<', 'value': 113, 'weight': 0.29},
            {'field': 'activity_mins', 'op': 'between', 'value': [41, 70], 'weight': 0.19},
            {'field': 'height', 'op': '<', 'value': 100, 'weight': 0.45},
        ]
    },
    'Balanitis': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'salt_intake', 'op': '>=', 'value': 42, 'weight': 0.42},
            {'field': 'weight', 'op': '<', 'value': 23, 'weight': 0.21},
            {'field': 'smoking', 'op': '<=', 'value': 52, 'weight': 0.15},
            {'field': 'sleep_hours', 'op': 'between', 'value': [46, 71], 'weight': 0.3},
        ]
    },
    'Prostatitis': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'activity_mins', 'op': '<', 'value': 5, 'weight': 0.32},
            {'field': 'bp_sys', 'op': '>=', 'value': 41, 'weight': 0.24},
            {'field': 'sleep_hours', 'op': 'between', 'value': [24, 44], 'weight': 0.11},
            {'field': 'weight', 'op': '>', 'value': 31, 'weight': 0.35},
        ]
    },
    'Benign Prostate Hypertrophy': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'activity_mins', 'op': '<=', 'value': 88, 'weight': 0.2},
            {'field': 'salt_intake', 'op': '>=', 'value': 143, 'weight': 0.41},
            {'field': 'screen_time', 'op': '<', 'value': 132, 'weight': 0.44},
            {'field': 'smoking', 'op': '>', 'value': 113, 'weight': 0.38},
            {'field': 'weight', 'op': '>', 'value': 27, 'weight': 0.49},
        ]
    },
    'Male Pattern Baldness': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [60, 73], 'weight': 0.14},
            {'field': 'stress', 'op': '>=', 'value': 75, 'weight': 0.16},
            {'field': 'salt_intake', 'op': '<=', 'value': 128, 'weight': 0.4},
            {'field': 'sleep_hours', 'op': '<', 'value': 86, 'weight': 0.36},
            {'field': 'screen_time', 'op': '>', 'value': 113, 'weight': 0.44},
        ]
    },
    'Klinefelter Syndrome': {
        'category': 'Reproductive Male', 'icon': 'fa-male',
        'conditions': [
            {'field': 'alcohol', 'op': '>', 'value': 122, 'weight': 0.2},
            {'field': 'screen_time', 'op': '>=', 'value': 22, 'weight': 0.3},
            {'field': 'stress', 'op': '>=', 'value': 107, 'weight': 0.39},
            {'field': 'bp_dias', 'op': '<', 'value': 136, 'weight': 0.16},
        ]
    },
    'Dengue Hemorrhagic': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 110, 'weight': 0.16},
            {'field': 'bp_sys', 'op': '<=', 'value': 133, 'weight': 0.46},
            {'field': 'smoking', 'op': '>=', 'value': 114, 'weight': 0.48},
            {'field': 'sleep_hours', 'op': '>', 'value': 133, 'weight': 0.39},
        ]
    },
    'Japanese Encephalitis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 43, 'weight': 0.23},
            {'field': 'bp_dias', 'op': '>', 'value': 10, 'weight': 0.26},
            {'field': 'alcohol', 'op': '<', 'value': 15, 'weight': 0.46},
        ]
    },
    'Leishmaniasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'smoking', 'op': 'between', 'value': [46, 68], 'weight': 0.49},
            {'field': 'height', 'op': 'between', 'value': [40, 61], 'weight': 0.45},
            {'field': 'age', 'op': '>=', 'value': 38, 'weight': 0.46},
            {'field': 'bp_dias', 'op': '<=', 'value': 140, 'weight': 0.36},
            {'field': 'salt_intake', 'op': 'between', 'value': [42, 72], 'weight': 0.36},
        ]
    },
    'Schistosomiasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 22, 'weight': 0.45},
            {'field': 'age', 'op': 'between', 'value': [28, 54], 'weight': 0.23},
            {'field': 'weight', 'op': '>=', 'value': 131, 'weight': 0.19},
            {'field': 'height', 'op': '>=', 'value': 41, 'weight': 0.31},
        ]
    },
    'Filariasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'age', 'op': 'between', 'value': [35, 54], 'weight': 0.34},
            {'field': 'alcohol', 'op': '<=', 'value': 29, 'weight': 0.49},
            {'field': 'salt_intake', 'op': '>', 'value': 67, 'weight': 0.44},
        ]
    },
    'Chagas Disease': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'water_intake', 'op': '>=', 'value': 32, 'weight': 0.15},
            {'field': 'bp_dias', 'op': '>=', 'value': 2, 'weight': 0.33},
            {'field': 'weight', 'op': '>=', 'value': 149, 'weight': 0.49},
            {'field': 'alcohol', 'op': 'between', 'value': [34, 55], 'weight': 0.44},
            {'field': 'stress', 'op': '>=', 'value': 147, 'weight': 0.37},
        ]
    },
    'African Trypanosomiasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'sleep_hours', 'op': '<=', 'value': 64, 'weight': 0.31},
            {'field': 'bmi', 'op': '>=', 'value': 50, 'weight': 0.31},
            {'field': 'bp_dias', 'op': '<=', 'value': 109, 'weight': 0.14},
            {'field': 'weight', 'op': '>', 'value': 109, 'weight': 0.14},
            {'field': 'stress', 'op': '<=', 'value': 20, 'weight': 0.19},
        ]
    },
    'Hookworm Infection': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'height', 'op': 'between', 'value': [55, 81], 'weight': 0.26},
            {'field': 'salt_intake', 'op': '<=', 'value': 150, 'weight': 0.45},
            {'field': 'bp_dias', 'op': '<=', 'value': 126, 'weight': 0.5},
            {'field': 'bp_sys', 'op': '<', 'value': 33, 'weight': 0.16},
        ]
    },
    'Ascariasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'smoking', 'op': '<=', 'value': 132, 'weight': 0.15},
            {'field': 'water_intake', 'op': '>', 'value': 117, 'weight': 0.38},
            {'field': 'bp_dias', 'op': '>', 'value': 144, 'weight': 0.4},
            {'field': 'screen_time', 'op': '>', 'value': 105, 'weight': 0.34},
        ]
    },
    'Amoebiasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'bmi', 'op': '>=', 'value': 11, 'weight': 0.33},
            {'field': 'weight', 'op': '<', 'value': 79, 'weight': 0.15},
            {'field': 'bp_sys', 'op': '>=', 'value': 8, 'weight': 0.22},
        ]
    },
    'Giardiasis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'sleep_hours', 'op': 'between', 'value': [39, 58], 'weight': 0.27},
            {'field': 'stress', 'op': '<', 'value': 126, 'weight': 0.43},
            {'field': 'age', 'op': '>', 'value': 18, 'weight': 0.32},
        ]
    },
    'Cryptosporidiosis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 145, 'weight': 0.33},
            {'field': 'water_intake', 'op': '>=', 'value': 122, 'weight': 0.41},
            {'field': 'salt_intake', 'op': 'between', 'value': [28, 54], 'weight': 0.15},
        ]
    },
    'Toxoplasmosis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'bp_dias', 'op': '<=', 'value': 39, 'weight': 0.37},
            {'field': 'alcohol', 'op': '>=', 'value': 105, 'weight': 0.14},
            {'field': 'bp_sys', 'op': '<', 'value': 87, 'weight': 0.46},
            {'field': 'height', 'op': '>', 'value': 114, 'weight': 0.48},
            {'field': 'stress', 'op': '>', 'value': 7, 'weight': 0.45},
        ]
    },
    'Histoplasmosis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'height', 'op': '>=', 'value': 32, 'weight': 0.32},
            {'field': 'smoking', 'op': 'between', 'value': [59, 86], 'weight': 0.13},
            {'field': 'weight', 'op': '>', 'value': 134, 'weight': 0.48},
            {'field': 'activity_mins', 'op': '<=', 'value': 5, 'weight': 0.3},
            {'field': 'bmi', 'op': 'between', 'value': [21, 39], 'weight': 0.17},
        ]
    },
    'Coccidioidomycosis': {
        'category': 'Tropical', 'icon': 'fa-sun',
        'conditions': [
            {'field': 'activity_mins', 'op': 'between', 'value': [54, 83], 'weight': 0.28},
            {'field': 'bp_sys', 'op': '<=', 'value': 126, 'weight': 0.34},
            {'field': 'age', 'op': '>=', 'value': 107, 'weight': 0.27},
        ]
    },
    'Post-Surgical Infection': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'salt_intake', 'op': 'between', 'value': [36, 48], 'weight': 0.23},
            {'field': 'bmi', 'op': '>', 'value': 74, 'weight': 0.32},
            {'field': 'activity_mins', 'op': '<', 'value': 23, 'weight': 0.2},
        ]
    },
    'DVT Post-Surgery': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'stress', 'op': '<=', 'value': 16, 'weight': 0.37},
            {'field': 'height', 'op': '>=', 'value': 15, 'weight': 0.17},
            {'field': 'screen_time', 'op': '<=', 'value': 37, 'weight': 0.14},
        ]
    },
    'Adhesive Bowel Obstruction': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'screen_time', 'op': '>=', 'value': 31, 'weight': 0.25},
            {'field': 'age', 'op': '<', 'value': 61, 'weight': 0.2},
            {'field': 'weight', 'op': 'between', 'value': [44, 57], 'weight': 0.4},
            {'field': 'bp_sys', 'op': '>', 'value': 142, 'weight': 0.23},
        ]
    },
    'Incisional Hernia': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bmi', 'op': '<=', 'value': 60, 'weight': 0.11},
            {'field': 'age', 'op': '>=', 'value': 26, 'weight': 0.32},
            {'field': 'screen_time', 'op': 'between', 'value': [28, 47], 'weight': 0.36},
            {'field': 'alcohol', 'op': '<=', 'value': 129, 'weight': 0.28},
        ]
    },
    'Wound Dehiscence': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'alcohol', 'op': '<', 'value': 44, 'weight': 0.25},
            {'field': 'salt_intake', 'op': '<', 'value': 109, 'weight': 0.32},
            {'field': 'water_intake', 'op': '<=', 'value': 119, 'weight': 0.12},
        ]
    },
    'Anastomotic Leak': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'stress', 'op': '<', 'value': 124, 'weight': 0.1},
            {'field': 'screen_time', 'op': 'between', 'value': [44, 65], 'weight': 0.2},
            {'field': 'alcohol', 'op': '<', 'value': 131, 'weight': 0.33},
            {'field': 'bp_sys', 'op': '>', 'value': 137, 'weight': 0.16},
            {'field': 'salt_intake', 'op': '>', 'value': 102, 'weight': 0.22},
        ]
    },
    'Surgical Site Infection': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bmi', 'op': '<', 'value': 72, 'weight': 0.39},
            {'field': 'bp_dias', 'op': '<', 'value': 82, 'weight': 0.34},
            {'field': 'alcohol', 'op': '>=', 'value': 116, 'weight': 0.35},
            {'field': 'screen_time', 'op': '<', 'value': 83, 'weight': 0.36},
            {'field': 'water_intake', 'op': '<', 'value': 85, 'weight': 0.28},
        ]
    },
    'Post-Anesthesia Complications': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'smoking', 'op': '<', 'value': 1, 'weight': 0.36},
            {'field': 'weight', 'op': '<=', 'value': 3, 'weight': 0.1},
            {'field': 'alcohol', 'op': '<', 'value': 126, 'weight': 0.27},
        ]
    },
    'Phantom Pain Post-Amputation': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'water_intake', 'op': '>', 'value': 20, 'weight': 0.41},
            {'field': 'weight', 'op': '>', 'value': 114, 'weight': 0.46},
            {'field': 'alcohol', 'op': '>', 'value': 97, 'weight': 0.24},
            {'field': 'smoking', 'op': '>=', 'value': 3, 'weight': 0.25},
        ]
    },
    'Keloid Formation': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bp_dias', 'op': '>=', 'value': 114, 'weight': 0.47},
            {'field': 'age', 'op': '<', 'value': 72, 'weight': 0.4},
            {'field': 'alcohol', 'op': '>=', 'value': 78, 'weight': 0.18},
        ]
    },
    'Chronic Post-Surgical Pain': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'activity_mins', 'op': '<', 'value': 93, 'weight': 0.49},
            {'field': 'age', 'op': '>=', 'value': 54, 'weight': 0.3},
            {'field': 'bmi', 'op': '<', 'value': 102, 'weight': 0.49},
            {'field': 'stress', 'op': '>=', 'value': 127, 'weight': 0.33},
            {'field': 'bp_sys', 'op': 'between', 'value': [56, 85], 'weight': 0.18},
        ]
    },
    'Lymphedema Post-Surgery': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'sleep_hours', 'op': '>', 'value': 17, 'weight': 0.34},
            {'field': 'activity_mins', 'op': '>=', 'value': 59, 'weight': 0.47},
            {'field': 'height', 'op': '>=', 'value': 6, 'weight': 0.18},
            {'field': 'salt_intake', 'op': 'between', 'value': [55, 79], 'weight': 0.35},
            {'field': 'age', 'op': '<=', 'value': 14, 'weight': 0.36},
        ]
    },
    'Seroma Formation': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bp_sys', 'op': '<=', 'value': 133, 'weight': 0.21},
            {'field': 'water_intake', 'op': '<=', 'value': 12, 'weight': 0.24},
            {'field': 'salt_intake', 'op': '<', 'value': 108, 'weight': 0.12},
            {'field': 'height', 'op': '<=', 'value': 101, 'weight': 0.23},
        ]
    },
    'Fat Embolism Syndrome': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'screen_time', 'op': '>', 'value': 7, 'weight': 0.45},
            {'field': 'alcohol', 'op': '<', 'value': 109, 'weight': 0.49},
            {'field': 'bmi', 'op': '<', 'value': 85, 'weight': 0.18},
        ]
    },
    'Compartment Syndrome': {
        'category': 'Surgical', 'icon': 'fa-procedures',
        'conditions': [
            {'field': 'bmi', 'op': '>', 'value': 111, 'weight': 0.11},
            {'field': 'salt_intake', 'op': '>', 'value': 86, 'weight': 0.34},
            {'field': 'screen_time', 'op': '<', 'value': 62, 'weight': 0.14},
            {'field': 'bp_dias', 'op': '>', 'value': 134, 'weight': 0.43},
        ]
    },
}
