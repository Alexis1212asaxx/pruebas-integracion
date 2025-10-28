from flask import Flask, render_template, redirect, url_for
import os

# Crear app y definir carpeta templates
app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))

# Lista de productos simulados
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 20, "imagen": "camiseta.jpg"},
    {"id": 2, "nombre": "Pantalón", "precio": 35, "imagen": "pantalon.jpg"},
    {"id": 3, "nombre": "Zapatos", "precio": 50, "imagen": "zapatos.jpg"}
]

carrito = []  # Carrito vacío

@app.route('/')
def index():
    return render_template('index.html', productos=productos)  # Mostrar productos

@app.route('/agregar/<int:producto_id>')
def agregar_carrito(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        carrito.append(producto)  # Agregar producto al carrito
    return redirect(url_for('index'))

@app.route('/carrito')
def ver_carrito():
    total = sum(item['precio'] for item in carrito)  # Calcular total
    return render_template('carrito.html', carrito=carrito, total=total)

if __name__ == "__main__":
    app.run(debug=True)  # Ejecutar app
