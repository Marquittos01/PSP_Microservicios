from flask import Flask, jsonify
import requests
import json

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    print("f")
    
if __name__ == '__main__':
    app4.run(port=5003)

