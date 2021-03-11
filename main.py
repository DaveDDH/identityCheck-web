from flask import Flask, request, render_template
import os

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

port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)