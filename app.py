import datetime

from flask import Flask, render_template

app = Flask(__name__)

#   ENDPOINT
@app.route("/dashboard")
#   FUNCIÓN DEL ENDPOINT
def tienda_online():

    #   INFORMACIÓN GENERAL
    info_general = {
        "admin": "moha",
        "tienda": "TecnoMarket",
        "fecha": datetime.date.today()
    }


    #   LISTA PRODUCTOS
    product = [
        {
            "nombre":"Gorra MilfShakes",
            "precio":23.99,
            "stock": 25,
            "categoria":"Ropa"
         },
        {
            "nombre": "Iphone 13",
            "precio": 780,
            "stock": 7,
            "categoria": "Electrónica"
        },
        {
            "nombre": "Sudadera WeekDay",
            "precio": 79.99,
            "stock": 0,
            "categoria": "Ropa"
        },
        {
            "nombre": "AirPods Pro 2",
            "precio": 120.99,
            "stock": 12,
            "categoria": "Electrónica"
        },
    ]

    #   NÚMERO TOTAL DE PRODUCTOS EN STOCK
    total_stock = 0
    for total in product:
        total_stock += total["stock"]


    #   LISTA CLIENTES
    client = [
        {
            "nombre":"Maria",
            "email":"maria@gmail.com",
            "activo":True,
            "pedidos": 3
        },
        {
            "nombre": "Alejandro",
            "email": "alejandro@gmail.com",
            "activo": False,
            "pedidos": 1
        },{
            "nombre":"Isa",
            "email":"isa@gmail.com",
            "activo":True,
            "pedidos": 5
        },
        {
            "nombre": "Elvis",
            "email": "elvis@gmail.com",
            "activo": True,
            "pedidos": 8
        }
    ]

    #   NÚMERO DE CLIENTES ACTIVOS
    clientes_activos = 0
    for cliente in client:
        if cliente["activo"] == True:
            clientes_activos += 1
    #   CLIENTE CON MAYOR NÚMERO DE PEDIDOS REALIZADOS
    nombre_cliente = ""
    max_pedidos = 0
    for cliente in client:
        if cliente["pedidos"] > max_pedidos:
            max_pedidos = cliente["pedidos"]
            nombre_cliente = cliente["nombre"]


    #   LISTAS PEDIDOS
    order = [
        {
            "cliente":"Isa",
            "total": 103.98,
            "fecha": "28/04/2025"
        },
        {
            "cliente": "Elvis",
            "total": 900.99,
            "fecha": "01/04/2025"
        },
        {
            "cliente": "Alejandro",
            "total": 23.99,
            "fecha": "15/04/2025"
        },
    ]
    #   INGRESO TOTAL
    total_ingreso = 0
    for pedido in order:
        total_ingreso += pedido["total"]


    return render_template("dashboard.html", **info_general, productos=product, total = total_stock , clientes=client, activos = clientes_activos, cliente_max_pedidos = nombre_cliente, pedidos=order, ingreso_total = total_ingreso)

if __name__ == "__main__":
    app.run(debug=True)