from flask import Flask, render_template, request, jsonify
import pandas as pd
from schedule_generator import generate_schedule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Récupération des données du formulaire
    off_days = int(request.form['off_days'])
    min_staff_count = int(request.form['min_staff_count'])
    full_time_staff = int(request.form['full_time_staff'])

    # Génération du planning
    schedule, chart_data = generate_schedule(off_days, min_staff_count, full_time_staff)

    # Génération du fichier CSV
    df = pd.DataFrame(schedule)
    csv_file = 'personnel_schedule.csv'
    df.to_csv(csv_file, index=False)

    # Retour des données pour mise à jour du graphique
    return jsonify(chart_data=chart_data, csv_file=csv_file)

if __name__ == '__main__':
    app.run(debug=True)
