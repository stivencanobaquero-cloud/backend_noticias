from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/noticias')
def obtener_noticias():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'Colombia',
        'language': 'es',
        'sortBy': 'publishedAt',
        'apiKey': 'ddd3a8123a8648a9a6a1bb13009c68ee'  # tu clave real aquí
    }
    r = requests.get(url, params=params)
    return jsonify(r.json())
