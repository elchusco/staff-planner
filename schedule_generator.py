def generate_schedule(off_days, min_staff_count, full_time_staff):
    # Logique pour générer la répartition du personnel selon les contraintes
    # Ex: Pour chaque demi-journée, on doit respecter min_staff_count, les contraintes des 45h, etc.

    # Exemple simplifié : planning sur 5 jours (10 demi-journées)
    schedule = {
        "Lundi Matin": [min_staff_count],
        "Lundi Après-midi": [min_staff_count],
        "Mardi Matin": [min_staff_count],
        "Mardi Après-midi": [min_staff_count],
        "Mercredi Matin": [min_staff_count],
        "Mercredi Après-midi": [min_staff_count],
        "Jeudi Matin": [min_staff_count],
        "Jeudi Après-midi": [min_staff_count],
        "Vendredi Matin": [min_staff_count],
        "Vendredi Après-midi": [min_staff_count]
    }

    # Générer les données pour le graphique Chart.js
    chart_data = [min_staff_count for _ in range(10)]  # 10 demi-journées

    return schedule, chart_data
