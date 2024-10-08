from flask import Blueprint, render_template, url_for, redirect, flash, request, abort, jsonify
from datetime import datetime

from .forms import RegistrationForm
from flaskr.models import Equipo, Integrante
from flaskr import db

main_bp = Blueprint('main', __name__, template_folder='templates')

sponsors = [
    {
        'image_link': 'static/img/perro_callejero.jpg',
        'title': 'Eventos Argentina',
        'description': 'Empresa líder en organización de eventos en Argentina.',
        'website_link': 'https://www.eventosargentina.com'
    },
    {
        'image_link': 'https://ams3.digitaloceanspaces.com/graffica/2023/02/cocacola-logo-1024x696.jpeg',
        'title': 'Coca-Cola Argentina',
        'description': 'Coca-Cola, la bebida refrescante más famosa del mundo.',
        'website_link': 'https://www.coca-cola.com/ar/es'
    },
    {
        'image_link': 'https://ecoobjetivo.com.ar/static/custom/logo-grande.png?t=2024-07-20+03%3A01%3A05.868706',
        'title': 'Cuidado Ambiental S.A.',
        'description': 'Comprometidos con la preservación del medio ambiente en Argentina.',
        'website_link': 'https://www.cuidadoambiental.com.ar'
    },
    {
        'image_link': 'https://cdn1.businessintriper.com/wp-content/uploads/2020/02/13200617/Patagonia-argentina.png',
        'title': 'Turismo Patagónico',
        'description': 'Descubre la belleza natural de la Patagonia Argentina con nosotros.',
        'website_link': 'https://www.turismopatagonico.com.ar'
    }
]


@main_bp.route('/')
def home():
    event_date = datetime(2025, 3, 20, 8, 0, 0)
    time_remaining = event_date - datetime.now()
    return render_template('main/home.html', days_remaining=time_remaining.days, sponsors=sponsors)

@main_bp.route('/informacion')
def info():
    return render_template('main/info.html')


#SOLO PARA EXPERIMENTAR CON FORMULARIO JSON

@main_bp.route('/inscribirse/', defaults={'deporte': 'futbol'}, methods=['GET', 'POST'])
@main_bp.route('/inscribirse/<deporte>', methods=['GET', 'POST'])
def inscribirse(deporte):
    if(not (deporte == 'futbol' or deporte == 'basket' or deporte == 'voley')):
        abort(404)

    if request.method == 'POST':
        data = request.get_json()
        form = RegistrationForm.from_json(data)

        if form.validate_on_submit():
            
            equipo = Equipo(
                nombre = data.nombre,
                deporte = data.deporte,
                colegio = data.colegio,
                nombre_encargado = data.encargado,
                telefono_encargado = data.telefono,
            )
            # Añadir el equipo a la sesión
            #db.session.add(equipo)
            #db.session.commit()
            print(equipo)

            # Crear objetos Integrante para cada miembro del equipo
            for integrante in data.integrantes:
                integrante_new = Integrante(
                    nombre = integrante.nombre,
                    telefono = integrante.telefono,
                    DNI = integrante.dni,
                    celiaco = integrante.celiaco,
                    vegano = integrante.vegano,
                    group_id = equipo.id
                )
                #db.session.add(integrante_new)
            # Confirmar todos los cambios en la base de datos
            #db.session.commit()
            print(data.integrantes.length)

            flash('El equipo ha sido registrado exitosamente.', 'success')
            return redirect(url_for('main.success'))
        else:
            # Debugging: Print form errors
            print("Form errors:", form.errors)
            return jsonify({"success": False, "errors": form.errors})
            #print("Form errors:", form.integrantes.errors)
            #print(form.integrantes.data)
    else:
        form = RegistrationForm()
    form.deporte.data = deporte
    return render_template('main/inscribirse-json.html', form=form, deporte=deporte)

# @main_bp.route('/inscribirse/', defaults={'deporte': None}, methods=['GET', 'POST'])
# @main_bp.route('/inscribirse/<deporte>', methods=['GET', 'POST'])
# def inscribirse(deporte):
#     form = RegistrationForm()
#     if form.validate_on_submit():

#         equipo = Equipo(
#             nombre=form.nombre_equipo.data,
#             deporte=form.deporte.data,
#             colegio=form.colegio.data,
#             nombre_encargado=form.encargado.data,
#             telefono_encargado=form.telefono.data,
#         )
#         # Añadir el equipo a la sesión
#         db.session.add(equipo)
#         db.session.commit()

#         # Crear objetos Integrante para cada miembro del equipo
#         for integrante in form.integrantes:
#             integrante_new = Integrante(
#                 nombre=integrante.nombre.data,
#                 telefono=integrante.telefono.data,
#                 DNI=integrante.dni.data,
#                 celiaco=integrante.celiaco.data,
#                 vegano=integrante.vegano.data,
#                 group_id=equipo.id
#             )
#             db.session.add(integrante_new)
#         # Confirmar todos los cambios en la base de datos
#         db.session.commit()

#         flash('El equipo ha sido registrado exitosamente.', 'success')
#         return redirect(url_for('main.success'))
#     else:
#         # Debugging: Print form errors
#         print("Form errors:", form.errors)
#         print("Form errors:", form.integrantes.errors)
#         #print(form.integrantes.data)

#     form.deporte.data = deporte
#     return render_template('main/inscribirse-wtf.html', form=form, deporte=deporte)
#     #return render_template('main/inscribirse.html')

@main_bp.route('/inscribirse/success')
def success():
    return "<h1>Formulario enviado con éxito</h1>"