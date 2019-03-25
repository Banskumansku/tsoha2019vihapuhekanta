from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    print("asd1")
    if request.method == "GET":
        print("asd1.5")
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit
    print("asd2")
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        print("asd3")
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    print("asd4")
    login_user(user)
    return redirect(url_for("index"))


@app.route('/auth/register', methods=['GET', 'POST'])
def auth_register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('/auth/register.html', form=form)


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))