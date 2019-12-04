############################
# Hola mundo en Flask
############################

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/hello')
def hello_page():
    return '''
            <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="static/style.css">
                </head>
                <body>
                    <h1>Hola!</h1>
                    <img src="static/images/gato.jpeg">
                </body>
            </html>
           '''
