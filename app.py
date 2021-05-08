
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')



app.run(port = 8000, debug = True)




