from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_login import login_required, login_user, logout_user, current_user
from flaskr import bcrypt, db
from flaskr.models import Usuario

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
