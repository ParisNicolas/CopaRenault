from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

class SQLQueryForm(FlaskForm):
    query = TextAreaField('SQL Query', validators=[DataRequired()])
    submit = SubmitField('Execute')