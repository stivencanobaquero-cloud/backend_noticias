from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/noticias')
def obtener_noticias():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'Colombia OR Meta OR Villavicencio',
        'language': 'es',
        'sortBy': 'publishedAt',
        'apiKey': 'TU_API_KEY_REAL'
    }
    r = requests.get(url, params=params)
    return jsonify(r.json())
