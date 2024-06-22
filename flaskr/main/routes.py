from flask import Blueprint, render_template, request
from datetime import datetime

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def home():
    event_date = datetime(2025, 3, 20, 8, 0, 0)
    time_remaining = event_date - datetime.now()
    return render_template('main/home.html', days_remaining=time_remaining.days)

@main_bp.route('/informacion')
def info():
    return render_template('main/info.html')

@main_bp.route('/inscribirse', methods=('GET', 'POST'))
def inscribirse():
    if request.method == 'POST':
        pass
    return render_template('main/inscribirse.html')