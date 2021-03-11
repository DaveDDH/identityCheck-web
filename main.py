from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def content():
  return render_template('index.html')

app.run()