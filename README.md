# API CRUD de Pokémon (Flask)

Mini proyecto de la Unidad Curricular **DevOps** — UTEC.

API REST que gestiona información de Pokémon (crear, leer, actualizar y eliminar). Toda la información se guarda **en memoria**: no se usa base de datos, por lo que los datos se reinician cada vez que se reinicia el servidor.

## Estructura del proyecto
.
├── app.py                                          # Servidor Flask con las rutas CRUD
├── README.md
└── postman/
    └── Pokemon_API.postman_collection.json         # Colección de pruebas Postman


## Requisitos previos

- Python 3.8 o superior instalado
- pip (viene incluido con Python)

## Instalación

1. Cloná este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. (Opcional pero recomendado) Creá un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```

3. Instalá Flask:
   ```bash
   pip install flask
   ```

## Cómo correr la API

```bash
python app.py
```

La API va a quedar disponible en:

```
http://127.0.0.1:5000
```

## Rutas disponibles

| Método | Ruta             | Descripción                           |
| ------ | ---------------- | ------------------------------------- |
| GET    | /pokemons        | Lista todos los Pokémon               |
| GET    | /pokemons/`<id>` | Obtiene un Pokémon específico por ID  |
| POST   | /pokemons        | Crea un nuevo Pokémon                 |
| PUT    | /pokemons/`<id>` | Actualiza un Pokémon existente por ID |
| DELETE | /pokemons/`<id>` | Elimina un Pokémon por ID             |

## Estructura de un Pokémon (JSON)

```json
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
```

> El campo `id` se genera automáticamente, no hace falta enviarlo al crear un Pokémon.

## Ejemplos de uso (con curl)

### 1. Listar todos los Pokémon

```bash
curl http://127.0.0.1:5000/pokemons
```

### 2. Obtener un Pokémon por ID

```bash
curl http://127.0.0.1:5000/pokemons/1
```

### 3. Crear un nuevo Pokémon

```bash
curl -X POST http://127.0.0.1:5000/pokemons \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Charmander",
    "imagen": "https://link.jpg",
    "caracteristicas": {"peso": 8.5, "altura": 0.6, "fuerza": 40, "edad": 2},
    "habilidades": ["Ascuas"],
    "tipo": "Fuego",
    "habitat": "Montañas"
  }'
```

### 4. Actualizar un Pokémon existente

```bash
curl -X PUT http://127.0.0.1:5000/pokemons/1 \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Raichu"}'
```

> Se pueden enviar solo los campos que se quieren modificar; el resto se mantiene igual.

### 5. Eliminar un Pokémon

```bash
curl -X DELETE http://127.0.0.1:5000/pokemons/1
```

## Notas

- Los datos se almacenan en una lista en memoria (`pokemons` en `app.py`), por lo que se pierden al reiniciar el servidor.
- Las respuestas de error (por ejemplo, Pokémon no encontrado) devuelven código HTTP `404`.
- Las creaciones exitosas devuelven código HTTP `201`, el resto de operaciones exitosas devuelven `200`.

## Pruebas con Postman

Se incluye una colección de Postman (Pokemon_API.postman_collection.json) con pruebas automatizadas para todos los endpoints (listar, crear, obtener por ID, actualizar, eliminar, y casos de error 404).

### Cómo usarla

1. Abrí Postman.
2. Hacé clic en *Import* y seleccioná el archivo Pokemon_API.postman_collection.json.
3. Asegurate de tener el servidor corriendo (python app.py) antes de ejecutar los requests.
4. Ejecutá los requests en orden (del 1 al 9), o corré toda la colección de una vez con *Run collection*.

> La colección usa una variable baseUrl (por defecto http://127.0.0.1:5000) y guarda automáticamente el id del Pokémon creado para reutilizarlo en los siguientes pasos.

## Autoras

- Veronica Couto y Daiana Silvera — UTEC, Unidad Curricular DevOps
