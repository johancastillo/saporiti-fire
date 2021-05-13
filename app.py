
from flask import Flask, render_template

app = Flask(__name__)

development = True

@app.route('/')
def Home():
    if development:
        return render_template('development.html')
    else:
        return render_template('index.html')



app.run(host = '0.0.0.0')




