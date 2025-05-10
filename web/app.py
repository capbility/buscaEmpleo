from flask import Flask, render_template, request, jsonify, url_for, redirect
import asyncio
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.job_finder import run_job_finder  

import csv 
import glob

app = Flask(__name__)
entorno = os.name
@app.route('/')
def index():
    directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    archivos = glob.glob(os.path.join(directorio, 'jobs_*.csv'))  # Busca todos los archivos que coincidan
    print(archivos)
    if archivos:
        if len(archivos) == 1:
            ruta_csv= archivos[0]
            #print(ruta_csv)
        else:
            ruta_csv= max(archivos, key=lambda x: os.path.basename(x))
            #print(ruta_csv)
        if not os.path.exists(ruta_csv):
            return jsonify({'data': []})
        data = []
        if entorno == 'nt':
            with open(ruta_csv, 'r', encoding='latin1') as f:
                reader = csv.reader(f)
                for row in reader:
                    if not row:  # evita filas vacías
                        continue
                    data.append({
                        'title': row[0],
                        'company': row[1],
                        'link': row[2],
                        'salary': row[3],
                        'location': row[4]
                    })

            return render_template('index.html', resultados=data)
        else: 
            with open(ruta_csv, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if not row:  # evita filas vacías
                        continue
                    data.append({
                        'title': row[0],
                        'company': row[1],
                        'link': row[2],
                        'salary': row[3],
                        'location': row[4]
                    })

            return render_template('index.html', resultados=data)
    else:
        return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        palabra_clave = request.form['palabra_clave']
        discapacidad = request.form['discapacidad'] == 'si'
        cantidad = int(request.form['cantidad'])
        #print(f"Datos recibidos: palabra clave para el puesto: {palabra_clave}, discapacidad: {discapacidad}, cantidad de ofertas: {cantidad}")
        asyncio.run(run_job_finder(palabra_clave, discapacidad, cantidad))
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
