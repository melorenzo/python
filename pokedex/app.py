from flask import Flask, render_template, request, jsonify
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_pokemon', methods=['POST'])
def buscar_pokemon():
    resource_name = request.form['pokemon_name'].strip().lower()
    
    base_url = 'https://pokeapi.co/api/v2/'
    endpoint = 'pokemon'
    url = f'{base_url}{endpoint}/{resource_name}/'

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extraemos los datos del Pokémon
        pokemon_info = {
            "name": data['name'].capitalize(),
            "types": [poke_type['type']['name'] for poke_type in data['types']],
            "weight": data['weight'],
            "height": data['height'],
            "stats": {stat['stat']['name']: stat['base_stat'] for stat in data['stats']},
            "moves": [move['move']['name'] for move in data['moves'][:5]],
            "sprite_url": data['sprites']['front_default']
        }
        return jsonify(pokemon_info)
    else:
        return jsonify({"error": f"Error: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
