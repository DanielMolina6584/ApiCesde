from flask import Flask, request, jsonify
from domain.Crud import CRUD
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

crud = CRUD()

@app.route(f'{BASE_URL}/crear', methods=['POST'])
def crear_persona():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        cel = request.form['cel']
        crud.crearInfoPersona(nombre, apellido, email, cel)
        return 'Persona creada correctamente'

@app.route(f'{BASE_URL}/actualizar/<int:id_persona>', methods=['POST'])
def actualizar_persona(id_persona):
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nuevo_apellido = request.form['apellido']
        nuevo_email = request.form['email']
        nuevo_cel = request.form['cel']
        crud.actualizarInfoPersona(id_persona, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_cel)
        return 'Información de persona actualizada correctamente'

@app.route(f'{BASE_URL}/eliminar/<int:id_persona>', methods=['GET'])
def eliminar_persona(id_persona):
    if request.method == 'GET':
        crud.eliminarInfoPersona(id_persona)
        return 'Persona eliminada correctamente'

@app.route(f'{BASE_URL}/obtener', methods=['GET'])
def obtener_personas():
    if request.method == 'GET':
        personas = crud.getInfoPersona()
        return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)