from wtforms import PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo

from application.auth.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username",[validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=2)])

    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
