"""
API CRUD de Pokémon con Flask
------------------------------
Proyecto Mini Proyecto en Python - Unidad Curricular DevOps - UTEC

La información se guarda "en memoria", es decir, en una lista de Python
que vive mientras el programa está corriendo. Si reiniciás el servidor,
los datos vuelven a su estado inicial.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# -----------------------------------------------------------------------
# "Base de datos" en memoria: una simple lista de diccionarios.
# Cada Pokémon tiene un id único que se genera automáticamente.
# -----------------------------------------------------------------------
pokemons = [
    {
        "id": 1,
        "nombre": "Pikachu",
        "imagen": "https://link_a_imagen_de_pikachu.jpg",
        "caracteristicas": {
            "peso": 6.0,
            "altura": 0.4,
            "fuerza": 55,
            "edad": 5
        },
        "habilidades": ["Impactrueno", "Cola férrea"],
        "tipo": "Eléctrico",
        "habitat": "Bosques"
    }
]

# Contador para asignar el próximo id disponible
siguiente_id = 2


def buscar_pokemon(pokemon_id):
    """Devuelve el pokémon con ese id, o None si no existe."""
    for p in pokemons:
        if p["id"] == pokemon_id:
            return p
    return None


# -----------------------------------------------------------------------
# GET /pokemons -> Lista todos los Pokémon
# -----------------------------------------------------------------------
@app.route("/pokemons", methods=["GET"])
def listar_pokemons():
    return jsonify(pokemons), 200


# -----------------------------------------------------------------------
# GET /pokemons/<id> -> Obtiene un Pokémon específico por ID
# -----------------------------------------------------------------------
@app.route("/pokemons/<int:pokemon_id>", methods=["GET"])
def obtener_pokemon(pokemon_id):
    pokemon = buscar_pokemon(pokemon_id)
    if pokemon is None:
        return jsonify({"error": "Pokémon no encontrado"}), 404
    return jsonify(pokemon), 200


# -----------------------------------------------------------------------
# POST /pokemons -> Crea un nuevo Pokémon
# -----------------------------------------------------------------------
@app.route("/pokemons", methods=["POST"])
def crear_pokemon():
    global siguiente_id

    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debes enviar un cuerpo JSON"}), 400

    # Validamos que estén los campos obligatorios básicos
    campos_requeridos = ["nombre", "imagen", "caracteristicas", "habilidades", "tipo", "habitat"]
    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({"error": f"Falta el campo obligatorio: {campo}"}), 400

    nuevo_pokemon = {
        "id": siguiente_id,
        "nombre": datos["nombre"],
        "imagen": datos["imagen"],
        "caracteristicas": datos["caracteristicas"],
        "habilidades": datos["habilidades"],
        "tipo": datos["tipo"],
        "habitat": datos["habitat"]
    }

    pokemons.append(nuevo_pokemon)
    siguiente_id += 1

    return jsonify(nuevo_pokemon), 201


# -----------------------------------------------------------------------
# PUT /pokemons/<id> -> Actualiza la información de un Pokémon por ID
# -----------------------------------------------------------------------
@app.route("/pokemons/<int:pokemon_id>", methods=["PUT"])
def actualizar_pokemon(pokemon_id):
    pokemon = buscar_pokemon(pokemon_id)
    if pokemon is None:
        return jsonify({"error": "Pokémon no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Debes enviar un cuerpo JSON"}), 400

    # Actualizamos solo los campos que vengan en el request
    for campo in ["nombre", "imagen", "caracteristicas", "habilidades", "tipo", "habitat"]:
        if campo in datos:
            pokemon[campo] = datos[campo]

    return jsonify(pokemon), 200


# -----------------------------------------------------------------------
# DELETE /pokemons/<id> -> Elimina un Pokémon por ID
# -----------------------------------------------------------------------
@app.route("/pokemons/<int:pokemon_id>", methods=["DELETE"])
def eliminar_pokemon(pokemon_id):
    pokemon = buscar_pokemon(pokemon_id)
    if pokemon is None:
        return jsonify({"error": "Pokémon no encontrado"}), 404

    pokemons.remove(pokemon)
    return jsonify({"mensaje": f"Pokémon con id {pokemon_id} eliminado"}), 200


# -----------------------------------------------------------------------
# Punto de entrada: corre el servidor de desarrollo de Flask
# -----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
