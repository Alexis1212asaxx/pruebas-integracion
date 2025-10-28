from app import app, productos, carrito
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Prueba que la página principal carga correctamente"""
    rv = client.get('/')
    assert rv.status_code == 200
    for producto in productos:
        assert bytes(producto['nombre'], 'utf-8') in rv.data

def test_agregar_carrito(client):
    """Prueba agregar un producto al carrito"""
    carrito.clear()  # Limpiar carrito antes de la prueba
    rv = client.get('/agregar/1', follow_redirects=True)
    assert rv.status_code == 200
    assert len(carrito) == 1
    assert carrito[0]['id'] == 1

def test_ver_carrito(client):
    """Prueba que el carrito se muestra correctamente"""
    carrito.clear()
    carrito.append(productos[0])
    rv = client.get('/carrito')
    assert rv.status_code == 200
    assert bytes(productos[0]['nombre'], 'utf-8') in rv.data
