from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():

    #dowolny kod Python
    #u nas wystawione na localhost
    return "Hello World!"

app.run()