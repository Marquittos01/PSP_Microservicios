from flask import Flask, jsonify
import requests
import json

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    try:
        data = {}

        if parametro1 == 'geo' or parametro2 == 'geo':
            geo_url = f'http://localhost:5000/{municipioid}/geo'
            geo_response = requests.get(geo_url)
            if geo_response.status_code == 200:
                data['geo'] = geo_response.json()
            else:
                data['geo'] = "No se encontró información geográfica"

        if parametro1 == 'meteo' or parametro2 == 'meteo':
            meteo_url = f'http://localhost:5001/{municipioid}/weather'
            meteo_response = requests.get(meteo_url)
            if meteo_response.status_code == 200:
                data['meteo'] = meteo_response.json()
            else:
                data['meteo'] = "No se encontró información meteorológica"

        if parametro1 == 'demo' or parametro2 == 'demo':
            demo_url = f'http://localhost:5002/{municipioid}/demo'
            demo_response = requests.get(demo_url)
            if demo_response.status_code == 200:
                data['demo'] = demo_response.json()
            else:
                data['demo'] = "No se encontró información demográfica"

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": "Hubo un error al procesar la solicitud"}), 500

if __name__ == '__main__':
    app4.run(port=5003)