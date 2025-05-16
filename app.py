from flask import Flask, render_template, request, redirect, abort, url_for
import json

app = Flask(__name__)

def cargar_peliculas():
    with open('disney.json', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/peliculas')
def peliculas():
    return render_template('peliculas.html')

@app.route('/listapeliculas', methods=['POST'])
def listado_peliculas():
    peliculas = cargar_peliculas()
    cadena = request.form.get('busqueda', '').lower()
    if cadena:
        resultado = [p for p in peliculas if p['Titulo'].lower().startswith(cadena)]
    else:
        resultado = peliculas
    return render_template('lista.html', peliculas=resultado)

@app.route('/pelicula/<id>')
def detalle_pelicula(id):
    peliculas = cargar_peliculas()
    for p in peliculas:
        if p['ID'] == id:
            return render_template('detalle.html', peli=p)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)

