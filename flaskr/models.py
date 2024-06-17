from . import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40))
    deporte = db.Column(db.Enum('futbol', 'basket', 'voley', name='deporte'), nullable=False)
    colegio = db.Column(db.String(50), nullable=False)
    nombre_encargado = db.Column(db.String(30), nullable=False)
    telefono_encargado = db.Column(db.String(15), nullable=False)
    pagado = db.Column(db.Boolean, default=False)

    integrantes = db.relationship('Integrante', backref='equipo', lazy='dynamic')
    partidos = db.relationship('Partido', backref='equipo', lazy=True)

    def __repr__(self):
        return f'<Equipo {self.title}>'

class Integrante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    telefono = db.Column(db.String(15), unique=True, nullable=False)
    DNI = db.Column(db.String(8), unique=True, nullable=False)
    celiaco = db.Column(db.Boolean, default=False)
    vegano = db.Column(db.Boolean, default=False)
    group_id = db.Column(db.Integer, db.ForeignKey('equipo.id'))

    def __repr__(self):
        return f'<Integrante {self.username}>'
    

class Partido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.Time, nullable=False)
    cancha = db.Column(db.Integer, nullable=False)

    equipo1_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    equipo2_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    
    equipo1 = db.relationship('Equipo', foreign_keys=[equipo1_id])
    equipo2 = db.relationship('Equipo', foreign_keys=[equipo2_id])

    resultado = db.Column(db.String(20))

    def __repr__(self):
        return f'<Partido {self.username}>'
    
