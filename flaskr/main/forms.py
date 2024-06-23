# forms.py
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, RadioField, TelField, EmailField, FieldList, FormField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class TeamMemberForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    telefono = TelField('Tel', validators=[DataRequired()])
    email = EmailField('Mail', validators=[DataRequired(), Email()])
    dni = StringField('DNI', validators=[DataRequired()])
    celiaco = BooleanField('Celiaco')
    vegano = BooleanField('Vegano')

class RegistrationForm(FlaskForm):
    colegio = StringField('Colegio', validators=[DataRequired()])
    deporte = RadioField('Deporte', choices=[('basket', 'Basket'), ('voley', 'Voley'), ('futbol', 'Futbol')], validators=[DataRequired()])
    encargado = StringField('Nombre del Encargado', validators=[DataRequired()])
    telefono = TelField('Teléfono', validators=[DataRequired()])
    nombre_equipo = StringField('Nombre del equipo (Opcional)')
    integrantes = FieldList(FormField(TeamMemberForm), min_entries=8, max_entries=12)
    recaptcha = RecaptchaField()
