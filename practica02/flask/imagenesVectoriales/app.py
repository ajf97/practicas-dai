from flask import Flask
from pysvg.filter import *
from pysvg.gradient import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *
from pysvg.parser import parse
import random

app = Flask(__name__)


@app.route('/')
def imagenes_svg():
    shape = ShapeBuilder()
    picture = Svg("test")
    # path = 'static/images/vectorial_' + str(random.randint(1, 250)) + '.svg'
    path = 'static/images/vectorial.svg'

    colors = ['red', 'yellow', 'black', 'brown', 'blue', 'pink']

    picture.addElement(shape.createRect(0, 0, random.randint(1, 400),
                                        random.randint(1, 200),
                                        random.randint(1, 20),
                                        random.randint(1, 20), strokewidth=2,
                                        stroke=random.choice(colors)))
    picture.addElement(shape.createRect(random.randint(1, 100),
                                        random.randint(1, 50),
                                        random.randint(1, 200),
                                        random.randint(1, 100), strokewidth=2,
                                        stroke=random.choice(colors),
                                        fill=random.choice(colors)))
    picture.addElement(shape.createCircle(random.randint(1, 700),
                                          random.randint(1, 500),
                                          random.randint(1, 50), strokewidth=5,
                                          stroke=random.choice(colors)))
    picture.addElement(shape.createEllipse(random.randint(1, 600),
                                           random.randint(1, 50),
                                           random.randint(1, 50),
                                           random.randint(1, 30), strokewidth=5,
                                           stroke=random.choice(colors)))
    picture.addElement(shape.createEllipse(random.randint(1, 700),
                                           random.randint(1, 50),
                                           random.randint(1, 50),
                                           random.randint(1, 30), strokewidth=5,
                                           stroke=random.choice(colors),
                                           fill=random.choice(colors)))
    picture.addElement(shape.createLine(0, 0,
                                        random.randint(1, 300),
                                        random.randint(1, 300), strokewidth=2,
                                        stroke=random.choice(colors)))
    picture.save(path)
    return '<img src={} height="1000px" width="1000px"/>'.format(path)


# Limpiamos caché para evitar que el navegador utilice la misma imagen.
@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


@app.errorhandler(404)
def page_not_found(error):
    return '''
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <h2>Ups! no hemos encontrado la página</h2>
            <img src="/static/images/404.jpeg">
        '''
