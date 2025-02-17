from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

#función
@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    # URL de la API
    url = f"https://www.el-tiempo.net/api/json/v2/provincias/18/municipios/{municipioid}"
    print(url)

    # Hacer la solicitud GET
    response = requests.get(url)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json
        meteo_data = {
            "temperatura_actual": data.get("temperatura_actual", "No disponible"),
            "temperaturas_max_min": {
                "max": data.get("temperaturas", {}).get("max", "No disponible"),
                "min": data.get("temperaturas", {}).get("min", "No disponible"),
            },
            "humedad": data.get("humedad", "No disponible"),
            "viento": data.get("viento", "No disponible"),
            "precipitacion": data.get("precipitacion", "No disponible"),
            "lluvia": data.get("lluvia", "No disponible"),
        }
        return jsonify(meteo_data)
    
    else:
        return jsonify({"error": "No se pudo obtener la información del clima"}), 500

if __name__ == '__main__':
    app2.run(port=5001)
