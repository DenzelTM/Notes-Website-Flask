from flask import Blueprint, render_template, request, flash

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
        #add user to database
    return render_template("sign_up.html")