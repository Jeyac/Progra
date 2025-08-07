from database import db

# Modelo que representa la tabla "alumno" en la base de datos
class Alumno(db.Model):
    __tablename__ = 'alumno'  # Nombre de la tabla

    # Columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)  # ID único
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del alumno
    apellido = db.Column(db.String(100), nullable=False)  # Apellido del alumno
    edad = db.Column(db.Integer, nullable=False)  # Edad del alumno

    # Método para convertir el objeto en un diccionario (fácil de pasar a JSON)
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad
        }
