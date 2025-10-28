from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
#Es una aplicacion de tienda en linea muy basica
# Productos simulados
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 20, "imagen": "camiseta.jpg"},
    {"id": 2, "nombre": "Pantalón", "precio": 35, "imagen": "pantalon.jpg"},
    {"id": 3, "nombre": "Zapatos", "precio": 50, "imagen": "zapatos.jpg"}
]

carrito = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar/<int:producto_id>')
def agregar_carrito(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        carrito.append(producto)
    return redirect(url_for('index'))

@app.route('/carrito')
def ver_carrito():
    total = sum(item['precio'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

if __name__ == "__main__":
    app.run(debug=True)

#codigo de prueba en tests/test_app.py