from flask import Flask
app = Flask(__name__)


@app.route('/user/<username>')
def router_pages(username):
    return '''
              <head>
                <link rel="stylesheet" href="/static/style.css">
              </head>
              <h1>La página de %s</h1>
              <img src="/static/images/gatito.jpeg">
              ''' % (username)


@app.errorhandler(404)
def page_not_found(error):
    return '''
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <h2>Ups! no hemos encontrado la página</h2>
            <img src="/static/images/404.jpeg">
            '''
