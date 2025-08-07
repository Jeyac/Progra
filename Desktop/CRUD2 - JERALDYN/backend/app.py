from flask import Flask, request, jsonify
from flask_cors import CORS  # Permite que la API se use desde otros dominios
from database import init_app, db
from models import Alumno

app = Flask(__name__)
CORS(app)  # Habilitar CORS en toda la app

init_app(app)  # Inicializar la base de datos

@app.route('/')
def home():
    # Mensaje de bienvenida
    return jsonify({"mensaje": "API de Alumnos"}), 200

# Crear alumno
@app.route('/alumnos', methods=['POST'])
def crear_alumno():
    # Recibir datos en formato JSON
    data = request.get_json()
    # Crear nuevo alumno
    alumno = Alumno(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'])
    db.session.add(alumno)  # Agregar a la base
    db.session.commit()  # Guardar cambios
    return jsonify(alumno.to_dict()), 201  # Responder con el alumno creado

# Listar todos los alumnos
@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    # Consultar todos los alumnos
    alumnos = Alumno.query.all()
    # Convertir a formato JSON
    return jsonify([a.to_dict() for a in alumnos])

# Obtener un alumno por ID
@app.route('/alumnos/<int:id>', methods=['GET'])
def obtener_alumno(id):
    # Buscar alumno por ID o devolver error 404
    alumno = Alumno.query.get_or_404(id)
    return jsonify(alumno.to_dict())

# Modificar alumno
@app.route('/alumnos/<int:id>', methods=['PUT'])
def actualizar_alumno(id):
    # Recibir datos nuevos
    data = request.get_json()
    # Buscar alumno
    alumno = Alumno.query.get_or_404(id)
    # Actualizar campos si se enviaron nuevos valores
    alumno.nombre = data.get('nombre', alumno.nombre)
    alumno.apellido = data.get('apellido', alumno.apellido)
    alumno.edad = data.get('edad', alumno.edad)
    db.session.commit()  # Guardar cambios
    return jsonify(alumno.to_dict())

# Eliminar alumno
@app.route('/alumnos/<int:id>', methods=['DELETE'])
def eliminar_alumno(id):
    # Buscar alumno
    alumno = Alumno.query.get_or_404(id)
    # Eliminar de la base
    db.session.delete(alumno)
    db.session.commit()
    return jsonify({"mensaje": f"Alumno con ID {id} eliminado correctamente"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)  # Ejecutar la app en modo desarrollo

