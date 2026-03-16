# disease_predictor.py
# Imports 501 disease rules from disease_rules.py

from disease_prediction.disease_rules import DISEASE_RULES


def calculate_disease_probabilities(user_data):
    results = []

    for disease_name, disease_info in DISEASE_RULES.items():
        total_weight   = 0
        matched_weight = 0
        matched_factors = []

        for condition in disease_info['conditions']:
            field    = condition['field']
            op       = condition.get('op', condition.get('operator', ''))
            value    = condition['value']
            weight   = condition['weight']

            total_weight += weight

            user_value = user_data.get(field)
            if user_value is None:
                continue

            matched = False
            try:
                if op == ">"       and float(user_value) > float(value):   matched = True
                elif op == "<"     and float(user_value) < float(value):   matched = True
                elif op == ">="    and float(user_value) >= float(value):  matched = True
                elif op == "<="    and float(user_value) <= float(value):  matched = True
                elif op == "=="    and str(user_value) == str(value):      matched = True
                elif op == "between" and isinstance(value, list) and len(value) == 2:
                    matched = float(value[0]) <= float(user_value) <= float(value[1])
            except (ValueError, TypeError):
                continue

            if matched:
                matched_weight += weight
                matched_factors.append(field.replace('_', ' ').title())

        if total_weight > 0:
            probability = round((matched_weight / total_weight) * 100)
        else:
            probability = 0

        if probability > 0:
            results.append({
                "name":        disease_name,
                "category":    disease_info['category'],
                "icon":        disease_info['icon'],
                "probability": probability,
                "factors":     matched_factors,
                "risk_level":  get_risk_level(probability)
            })

    results.sort(key=lambda x: x['probability'], reverse=True)
    return results


def get_risk_level(probability):
    if probability >= 70:
        return {"label": "High Risk",   "color": "danger",  "badge": "🔴"}
    elif probability >= 40:
        return {"label": "Medium Risk", "color": "warning", "badge": "🟡"}
    else:
        return {"label": "Low Risk",    "color": "success", "badge": "🟢"}


def get_top_diseases(user_data, top_n=10):
    return calculate_disease_probabilities(user_data)[:top_n]


def get_by_category(user_data):
    all_results = calculate_disease_probabilities(user_data)
    grouped = {}
    for disease in all_results:
        cat = disease['category']
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(disease)
    return grouped