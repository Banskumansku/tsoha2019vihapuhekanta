from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route('/auth/register', methods=['GET', 'POST'])
def auth_register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.username.data == "admin":
            urole = "ADMIN"
        else:
            urole = "ANY"

        if not form.username.data.islower():
            error = "Usernames should be in lowercase"
            return render_template('auth/register.html', form=form, error=error)
        if '@' in form.username.data or '-' in form.username.data or '|' in form.username.data:
            error = "Usernames should not have special characters."
            return render_template('auth/register.html', form=form, error=error)

        user = User(form.username.data, form.password.data, urole)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        login_user(user)
        modification = 'account_created'
        from application.logs.views import add_log
        add_log(modification, None, user.id)
        return redirect(url_for('index'))
    return render_template('auth/register.html', form=form)


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


