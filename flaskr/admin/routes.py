from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_login import login_required, login_user, logout_user, current_user
from flaskr import bcrypt, db
from flaskr.models import Usuario, Equipo

from .forms import LoginForm

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

@admin.route('/')
@login_required
def home():
    return render_template('admin/home.html')


@admin.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("admin.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("admin.home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("admin/login.html", form=form)
    return render_template("admin/login.html", form=form)


@admin.route('/logout')
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("admin.login"))


@admin.route('/inscripciones')
@login_required
def inscripciones():
    equipos = Equipo.query.filter(Equipo.pagado == False).all()
    return render_template('admin/inscripciones.html', equipos=equipos)

@admin.route('/inscripciones/<int:id>')
@login_required
def inscripcion_id(id):
    equipo = Equipo.query.get(id)
    integrantes = equipo.integrantes.all()
    return render_template('admin/inscripcion.html', equipo=equipo, integrantes=integrantes)

@admin.route('/inscripciones/confirmar/<int:id>')
@login_required
def confirmar_inscripcion(id):
    db.session.query(Equipo).filter_by(id=id).update({"pagado": True}, synchronize_session=False)
    db.session.commit()
    flash("Formulario aceptado", "success")
    return render_template('admin/inscripcion.html')

@admin.route('/inscripciones/eliminar/<int:id>')
@login_required
def eliminar_equipo(id):
    equipo = Equipo.query.get(id)
    if equipo:
        try:
            # Eliminar los integrantes asociados al equipo
            for integrante in equipo.integrantes:
                db.session.delete(integrante)
            # Eliminar el equipo
            db.session.delete(equipo)
            db.session.commit()
            flash("Equipo eliminado con éxito", "success")
            return redirect(url_for("admin.inscripciones"))  # Redirigir a la página de inicio
        except Exception as e:
            db.session.rollback()
            return f"Error al eliminar equipo: {e}"
    flash("Equipo no encontrado", "warning")
    return redirect(url_for("admin.inscripciones"))  # Redirigir a la página de inicio