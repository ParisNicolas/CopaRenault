from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def home():
    return render_template('main/home.html')

@main_bp.route('/informacion')
def info():
    return render_template('main/info.html')

@main_bp.route('/inscribirse', methods=('GET', 'POST'))
def inscribirse():
    if request.method == 'POST':
        pass
    return render_template('main/inscribirse.html')