from flask import Flask, jsonify
import json

app1 = Flask(__name__)


@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    with open("./municipio.json") as file:
        data = json.load(file)
        
    if (data["MUNICIPIOID"] == municipioid):
        return jsonify(data)
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404


if __name__ == '__main__':
    app1.run(port=5000)