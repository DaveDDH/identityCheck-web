from flask import Flask, request, render_template

import os
ON_HEROKU = os.environ.get('ON_HEROKU')
if ON_HEROKU:
    # get the heroku port 
    port = int(os.environ.get("PORT", 17995))  # as per OP comments default is 17995
else:
    port = 3000

app = Flask(__name__, static_url_path='')

@app.route('/')
def content():
  return render_template('index.html')

app.run(port=port)