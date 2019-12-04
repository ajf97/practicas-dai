import mandelbrot as mb
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def mandelbrot_page():
    x1 = request.args.get('x1') or -1
    x2 = request.args.get('x2') or 0.5
    y1 = request.args.get('y1') or -1
    y2 = request.args.get('y2') or 1
    width = request.args.get('width') or 255

    path = "static/images/mandelbrot.png"
    mb.pintaMandelbrot(x1, y1, x2, y2,
                       width, 255, path)

    return '''
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <h1>Fractal de Mandelbrot</h1>
            <img src={}>
            <h2>Argumentos</h2>
            <p>x1: {}</p>
            <p>x2: {}</p>
            <p>y1: {}</p>
            <p>y2: {}</p>
            <p>width: {}</p>
            '''.format(path, x1, x2, y1, y2, width)


@app.errorhandler(404)
def page_not_found(error):
    return '''
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <h2>Ups! no hemos encontrado la página</h2>
            <img src="/static/images/404.jpeg">
        '''


# Limpiamos caché para evitar que el navegador utilice la misma imagen.
@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response
