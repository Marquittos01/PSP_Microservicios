from flask import Flask, jsonify
import json

app3 = Flask(__name__)

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    with open("municipio.json") as file:
        data = json.load(file)

    if data["MUNICIPIOID"] == municipioid:
        return jsonify(data)
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404

if __name__ == '__main__':
    app3.run(port=5002)
