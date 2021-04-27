import os
import json
from flask import Flask, request, render_template

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import apiKey
import apiCount

cred = credentials.Certificate('identitychecker-ed56b-firebase-adminsdk-g29ea-e2c07edaa8.json')
firebaseApp = firebase_admin.initialize_app(cred, {'databaseURL': 'https://identitychecker-ed56b-default-rtdb.firebaseio.com/'})

app = Flask(__name__, static_url_path='')

@app.route('/')
def content():
  return render_template('index.html')

@app.route('/signin')
def contentSignIn():
  return render_template('signin.html')

@app.route('/signup')
def contentSignUp():
  return render_template('signup.html')

@app.route('/main')
def contentMain():
  return render_template('main.html')

@app.route('/api/key', methods=["GET","POST"])
def apiKeyController():
  if request.method == 'GET':
    return apiKey.getKey(request.args.get('id'), db)
  elif request.method == 'POST':
    return apiKey.setKey(request.data, db)

@app.route('/api/count', methods=["GET","POST"])
def apiCountController():
  if request.method == 'GET':
    return apiCount.getCount(request.args.get('id'), db)
  elif request.method == 'POST':
    return apiCount.setCount(request.args.get('id'), db)

port = int(os.environ.get("PORT", 33507))
app.run(host='127.0.0.1', port=port)