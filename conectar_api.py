import requests
from PIL import Image
from io import BytesIO

print("Bienvenidos a la Pokedex")
print()

# Bucle principal
while True:
    print("Seleccione una opción:" )
    print("1. Buscar Pokémon")
    print("2. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        # Pasamos la API a una variable llamada URL
        base_url = 'https://pokeapi.co/api/v2/'

        # Definimos un endpoint
        endpoint = 'pokemon'

        # Ingresamos el nombre de nuestro Pokémon
        resource_name = input("Ingresa el nombre de tu Pokémon favorito: ").strip().lower()

        # Construimos la URL completa
        url = f'{base_url}{endpoint}/{resource_name}/'

        # Realizamos el llamado a la API
        response = requests.get(url)

        # Verificamos si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()

            # Nombre del Pokémon
            print(f"\nNombre: {data['name'].capitalize()}")

            # Tipos del Pokémon
            print("Tipos:")
            for poke_type in data['types']:
                print(f"- {poke_type['type']['name']}")

            # Peso y altura
            print(f"Peso: {data['weight']} (decidecalogramos)")
            print(f"Altura: {data['height']} (decímetros)")

            # Estadísticas base
            print("\nEstadísticas base:")
            for stat in data['stats']:
                print(f"- {stat['stat']['name']}: {stat['base_stat']}")

            # Movimientos que puede aprender (mostramos solo los primeros 5)
            print("\nMovimientos (los primeros 5):")
            for move in data['moves'][:5]:
                print(f"- {move['move']['name']}")

            # Obtenemos la URL del sprite frontal
            sprite_url = data['sprites']['front_default']

            # Descargamos el sprite
            sprite_response = requests.get(sprite_url)

            # Abrimos la imagen usando PIL (Pillow)
            img = Image.open(BytesIO(sprite_response.content))

            # Mostramos la imagen
            img.show()
        else:
            print(f"Error: {response.status_code}")

    elif opcion == "2":
        print("Saliendo de la Pokedex...")
        break  # Salimos del bucle y terminamos el programa

    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        



