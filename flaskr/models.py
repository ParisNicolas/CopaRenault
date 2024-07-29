from datetime import datetime
from . import db, bcrypt

from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<Usuario {self.email}>"

# Tabla intermedia para la relación muchos a muchos entre partidos y equipos
partidos_equipos = db.Table('partidos_equipos',
    db.Column('partido_id', db.Integer, db.ForeignKey('partido.id'), primary_key=True),
    db.Column('equipo_id', db.Integer, db.ForeignKey('equipo.id'), primary_key=True)
)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    deporte = db.Column(db.Enum('futbol', 'basket', 'voley', name='deporte'), nullable=False)
    colegio = db.Column(db.String(100), nullable=False)
    nombre_encargado = db.Column(db.String(50), nullable=False)
    telefono_encargado = db.Column(db.String(20), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now, nullable=False)
    pagado = db.Column(db.Boolean, default=False)
    
    integrantes = db.relationship('Integrante', backref='equipo', lazy='dynamic')
    partidos = db.relationship('Partido', secondary=partidos_equipos, back_populates='equipos')

    def __repr__(self):
        return f'<Equipo {self.colegio}>'

class Integrante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    DNI = db.Column(db.String(8), nullable=False)
    celiaco = db.Column(db.Boolean, default=False)
    vegano = db.Column(db.Boolean, default=False)
    group_id = db.Column(db.Integer, db.ForeignKey('equipo.id'))

    def __repr__(self):
        return f'<Integrante {self.nombre}>'
    

class Partido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.Time, nullable=False)
    cancha = db.Column(db.Integer, nullable=False)

    #equipo1_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    #equipo2_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    

    equipos = db.relationship('Equipo', secondary=partidos_equipos, back_populates='partidos')
    #equipo1 = db.relationship('Equipo', foreign_keys=[equipo1_id], backref='equipo1_partidos')
    #equipo2 = db.relationship('Equipo', foreign_keys=[equipo2_id], backref='equipo2_partidos')

    resultado = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Partido {self.equipo1}/{self.equipo2}>'
    
