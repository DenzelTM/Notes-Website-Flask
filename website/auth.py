from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash #this enables us to store our password in a more secure format.

auth = Blueprint('auth', __name__)
#routes
@auth.route('/login', methods=['GET' , 'POST']) #get and post are used to exept the methods/routes using HTTP requests
def login():
    return render_template("login.html" , boolean=True)

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/sign-up' , methods=['GET' , 'POST'])
def sign_up():
    if request.method == 'POST' :
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be grester than 4 characters', catergory = 'error')
        elif len(firstName) < 2:
            flash('First Name must be grester than 2 characters', catergory = 'error')
        elif password1 != password2:
            flash('Passwords dont match', catergory = 'error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 character', catergory = 'error')
        else:
            new_user = User(email=email, firstName=firstName, password = generate_password_hash(password1, method= 'sha256')) # Sha256 is a hashing algorithm 
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!' , category='Success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")