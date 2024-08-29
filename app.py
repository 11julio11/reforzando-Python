from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

#lista de productos en memoria
productos = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    productos.append({'nombre': nombre, 'precio': precio})
    return redirect(url_for('index'))

@app.route('/buscar', methods=['POST'])
def buscar():
    nombre = request.form['nombre']
    producto = next((p for p in productos if p['nombre'].lower() == nombre.lower()), None)
    resultado = f"producto encontrado: {producto['nombre']}, precio: ${producto['precio']}" if producto else "producto no encontrado"
    return render_template('index.html', productos=productos, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)