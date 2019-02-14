from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def full_validation():
    user_error = ''
    pass_error = ''
    ver_error = ''
    email_error = ''
    username = request.form['username']
    if(not username):
        user_error='You need a username'
    password = request.form['password']
    if(not password):
        pass_error='You need a password'
    verify = request.form['verify']
    if(not verify):
       ver_error='You need to verify your password'
    email = request.form['email']
    if(not validate(username)):
        user_error='Username should be between 3 and 20 characters with no spaces'
    if(not validate(password)):
        pass_error='Password should be between 3 and 20 characters with no spaces'
    if(not validate(verify)):
        ver_error='Verification password should be between 3 and 20 characters with no spaces'
    if(not validate_email(email)):
        email_error='submit a valid email or nothing'
    if(not is_match(password, verify)):
        pass_error='Please have your password and verification match'
        ver_error='Please have your password and verification match'
    if(not user_error and not pass_error and not ver_error and not email_error):
        return render_template('welcome.html', user = username)
    else:
        return render_template('index.html', user_error = user_error, pass_error = pass_error, ver_error = ver_error, email_error = email_error, username = username, email = email)

def validate(credential):
    if ' ' not in credential and 20>=len(credential) and 3<=len(credential):
        return True
    else:
        return False
def is_not_empty(thing):
    if thing == '':
        return False
    else:
        return True
def is_match(first, second):
    if first == second:
        return True
    else:
        return False
def validate_email(ema):
    if len(ema)!=0:
        if ema.count('@')==1 and ema.count('.')==1 and validate(ema):
            return True
        else:
            return False
    else:
        return True



@app.route("/")
def index():
    return render_template('index.html')


app.run()