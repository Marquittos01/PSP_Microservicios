from flask import Flask, jsonify
import requests
import json

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<param1>/<param2>', methods=['GET'])
def get_combined(municipioid, param1, param2):
    # Definir las URLs de los microservicios
    services = {
        "geo": f"http://127.0.0.1:5000/{municipioid}/geo",
        "meteo": f"http://127.0.0.1:5001/{municipioid}/meteo",
        "demo": f"http://127.0.0.1:5002/{municipioid}/demo"
    }

    # Verificar qué parámetros hay en la URL
    urls = []
    if param1 in services:
        urls.append((param1, services[param1]))
    if param2 in services:
        urls.append((param2, services[param2]))

    # Consultar los microservicios y almacenar las respuestas
    response_data = {}
    for key, url in urls: 
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_data[key] = response.json()
            else:
                response_data[key] = {"error": f"Servicio {key} no disponible",
                                      "codigo": response.status_code}
        except requests.exceptions.RequestException:
            response_data[key] = {"error": f"Error al conectar con el servicio {key}"}

    return jsonify(response_data)
    
if __name__ == '__main__':
    app4.run(port=5003)

