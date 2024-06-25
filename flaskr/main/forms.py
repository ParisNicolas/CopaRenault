# forms.py
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, RadioField, TelField, EmailField, FieldList, FormField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp, Optional

class TeamMemberForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")])
    telefono = TelField('Teléfono', validators=[DataRequired(), Regexp(r'^\+?[\d\s\-.()]{7,}$', message="Formato de teléfono inválido")])
    email = EmailField('Correo Electrónico', validators=[DataRequired(), Email(message="Correo electrónico inválido")])
    dni = StringField('DNI', validators=[DataRequired(), Length(min=7, max=8, message="El DNI debe tener entre 7 y 8 dígitos"), Regexp(r'^\d+$', message="El DNI debe contener solo números")])
    celiaco = BooleanField('Celiaco')
    vegano = BooleanField('Vegano')

class RegistrationForm(FlaskForm):
    colegio = StringField('Colegio', validators=[DataRequired(), Length(min=2, max=100, message="El nombre del colegio debe tener entre 2 y 100 caracteres")])
    deporte = RadioField('Deporte', choices=[('futbol', 'Fútbol'), ('basket', 'Basket'), ('voley', 'Vóley')], validators=[DataRequired()])
    encargado = StringField('Nombre del Encargado', validators=[DataRequired(), Length(min=2, max=50, message="El nombre del encargado debe tener entre 2 y 50 caracteres")])
    telefono = TelField('Teléfono', validators=[DataRequired(), Regexp(r'^\+?[\d\s\-.()]{7,}$', message="Formato de teléfono inválido")])
    nombre_equipo = StringField('Nombre del equipo (Opcional)', validators=[Optional(), Length(max=50, message="El nombre del equipo debe tener un máximo de 50 caracteres")])
    integrantes = FieldList(FormField(TeamMemberForm), min_entries=8, max_entries=12)
    recaptcha = RecaptchaField()

