from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sezam')
def sezam():
    return '<marquee>Odkryłeś tajne wejście, gratuluję!</marquee>'

app.run()
