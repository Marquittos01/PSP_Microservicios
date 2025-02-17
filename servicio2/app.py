from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
# función
def get_meteo(municipioid):
    # URL de la API
    url = f"https://www.el-tiempo.net/api/json/v2/provincias/18/municipios/{municipioid}", 

    # Hacer la solicitud GET
    response = requests.get(url)
    print(response.status_code)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = jsonify(response)  # Convertir la respuesta a JSON

        # Guardar los datos en un archivo JSON
        with open("tiempo_municipio.json", "w", encoding="utf-8") as file:
            file.write(data)

        print("Datos guardados en 'tiempo_municipio.json'")
    else:
        print(f"Error al acceder a la API: {response.status_code}")


    if __name__ == '__main__':
        app2.run(port=5001)
