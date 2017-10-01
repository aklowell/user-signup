from flask import Flask, request, redirect, render_template
import cgi
import os


#boilerplate language to call templates

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ('/')
def display_signup():
    return render_template('signup.html')

@app.route ('/', methods = ['POST'])
def validate_entries():
    user_name = request.form['user-name']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error=''
    password_error=''
    verify_error = ''
    email_error = ''
        
    if len(user_name) < 3 or len(user_name) >20 or " " in user_name:
        username_error = 'That is not a valid username. Must be 3-20 characters and no spaces.'
        user_name = ''
    else:
        user_name = user_name

    if len(password) <3 or len(password) >20 or " " in password:
        password_error = 'That is not a valid password. Must be 3-20 characters and no spaces.'
        password = ''
    else:
        password = password

    if not verify == password:
        verify_error = "Passwords do not match, please try again."
        verify = ''
    else:
        verify = verify

    if len(email) > 0 and ((email.count("@")>1) or (email.count("@")==0)):
        email_error = "That is not a valid e-mail address. You may leave this blank."
        email = ''
    
    if len(email) > 0 and ((email.count(".")>1) or (email.count(".")==0)):
        email_error = "That is not a valid e-mail address. You may leave this blank."
        email = ''
    if len(email) > 0 and " " in email:
        email_error = "That is not a valid e-mail address. You may leave this blank."
        email = ''
    else:
        email = email 

    if not username_error and not password_error and not verify_error and not email_error:
        user_name = request.form['user-name']
        return render_template ('welcome.html', name= user_name)
    
    else:
        return render_template("signup.html", 
    username_error=username_error,
    password_error=password_error, 
    verify_error = verify_error,
    email_error=email_error,
    user_name=user_name,
    password=password,
    verify = verify,
    email = email)

app.run()
