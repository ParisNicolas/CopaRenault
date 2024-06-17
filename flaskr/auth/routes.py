from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@auth.route('/')
def home():
    return render_template('auth/base.html')