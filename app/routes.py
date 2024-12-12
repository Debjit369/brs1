from flask import Blueprint, render_template, url_for, redirect
from app.forms import LoginForm, RegisterForm
from app import db
from app.models import User
from flask_login import login_user

bp = Blueprint('main', __name__)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # Simple password validation
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)
