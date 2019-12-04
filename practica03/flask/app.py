from flask import Flask, render_template, session, request, redirect, url_for
from pickleshare import *
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = PickleShareDB('./db')


def historial(page):
    if 'username' in session:
        if 'historial' in session:
            if page not in session['historial']:
                session['historial'] = [page] + session['historial']
            if len(session['historial']) > 3:
                session['historial'].pop()
        else:
            session['historial'] = [page]


@app.route('/')
def index():
    historial((url_for('index'), 'Inicio'))
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in db and password == db[username]['password']:
            session['username'] = request.form['username']
            session['name'] = db[username]['name']
            session['email'] = db[username]['email']
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos'
            return render_template('index.html', error=error)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('historial', None)
    return redirect(url_for('index'))


@app.route('/about.html')
def about():
    historial((url_for('about'), 'Acerca de'))
    return render_template('about.html')


@app.route('/curiosity.html')
def curiosity():
    historial((url_for('curiosity'), 'Curiosidades'))
    return render_template('curiosity.html')


@app.route('/ephemeris.html')
def ephemeris():
    historial((url_for('ephemeris'), 'Efemérides'))
    return render_template('ephemeris.html')


@app.route('/profile.html')
def profile():
    if 'username' in session:
        historial((url_for('profile'), 'Mi perfil'))
        return render_template('profile.html')
    else:
        return redirect(url_for('index'))


@app.route('/update_profile.html', methods=['GET', 'POST'])
def edit():
    if 'username' not in session:
        return redirect(url_for('index'))
    elif request.method == 'GET' and session['username']:
        return render_template('update_profile.html')
    elif request.method == 'POST' and session['username']:
        username = session['username']

        db[username]['email'] = request.form['email']
        db[username]['password'] = request.form['password']
        db[username]['name'] = request.form['name']
        db[username] = db[username]  # Para forzar que se guarde en db

        session['name'] = db[username]['name']
        session['email'] = db[username]['email']

        return redirect(url_for('index'))


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'GET' and 'username' not in session:
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form['username']

        if username not in db:
            db[username] = dict()
            db[username]['email'] = request.form['email']
            db[username]['password'] = request.form['password']
            db[username]['name'] = request.form['name']
            db[username] = db[username]  # Para forzar que se guarde en db
            return redirect(url_for('index'))
        else:
            error = 'El usuario ya existe'
            return render_template('signup.html', error=error)

    elif session['username']:
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html')
