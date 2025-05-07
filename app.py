#   LIBRERÍAS
import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


#   DATOS
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
        "categoria":"Ropa",
        "img":"https://milfshakes.es/cdn/shop/files/680e407e46b184b1ba1bc47c_Frontal-gorra.webp?v=1745764983"
        },
    {
        "nombre": "Iphone 13",
        "precio": 780,
        "stock": 7,
        "categoria": "Electrónica",
        "img":"https://res-1.cloudinary.com/grover/image/upload/v1632242422/e4vsrkuyzzlspnwtxbvj.png"
    },
    {
        "nombre": "Sudadera Stussy",
        "precio": 79.99,
        "stock": 0,
        "categoria": "Ropa",
        "img":"https://images.cults3d.com/mkigXOcrjp2dXsiwzP3kGcmLdHA=/516x516/filters:no_upscale()/https://fbi.cults3d.com/uploaders/28951487/illustration-file/84b8c090-3dc2-4175-9a09-95ac4a893e49/Capture-d'%C3%A9cran-2023-10-27-170127.png"
    },
    {
        "nombre": "AirPods Pro 2",
        "precio": 120.99,
        "stock": 12,
        "categoria": "Electrónica",
        "img":"https://m.media-amazon.com/images/I/51R8U4qEfAL.jpg"
    },
    {
        "nombre": "Caja Segarros",
        "precio": 5.66,
        "stock": 12,
        "categoria": "Consumo",
        "img":"https://imgs.search.brave.com/RgOQzlfsrj2wfE1CER70qXDBuw6UPG81uv0TaF1G6B0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9maW5v/ZmlsaXBpbm8ub3Jn/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDI1/LzA0L0FVbjFIMFku/anBlZw"
    },
]

#   LISTA CLIENTES
client = [
    {
        "nombre": "Alejandro",
        "email": "alejandro@gmail.com",
        "activo": False,
        "pedidos": 1,
        "img":"https://imgs.search.brave.com/GTEVtYeMLk6OhXBkFgtAEpRsvGpWEjg-Y1AUF7gWdBI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1Qk56WmhNRFZt/TWpJdFpHSXdZaTAw/TnpkaUxXSmtaamN0/TnpRNU16QTROamc0/TURCaFhrRXlYa0Zx/Y0djQC5qcGc"
    },
    {
        "nombre":"Maria",
        "email":"maria@gmail.com",
        "activo":True,
        "pedidos": 3,
        "img":"https://i.pinimg.com/474x/e5/c8/46/e5c84688a1629fa1007bf561e0a609b3.jpg"
    },
    {
        "nombre":"Juanjo",
        "email":"juanjo@gmail.com",
        "activo":True,
        "pedidos": 5,
        "img":"https://imgs.search.brave.com/fJ8FyVPAV1_1ONn-4TMLP0ZaI-rQDNuG_HbW4etA9r4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi8zLzNiL09i/aXNrXyVDNSVBMXBh/bnNrZWdhX3ByZWRz/ZWRuaWthX3ZsYWRl/X3ZfU2xvdmVuaWpp/XyUyODUzNjU4NjA1/OTMwJTI5XyUyOGNy/b3BwZWQlMjkuanBn/LzUxMnB4LU9iaXNr/XyVDNSVBMXBhbnNr/ZWdhX3ByZWRzZWRu/aWthX3ZsYWRlX3Zf/U2xvdmVuaWppXyUy/ODUzNjU4NjA1OTMw/JTI5XyUyOGNyb3Bw/ZWQlMjkuanBn"
    },
    {
        "nombre": "Elvis",
        "email": "elvis@gmail.com",
        "activo": True,
        "pedidos": 8,
        "img":"https://imgs.search.brave.com/wLPhT0jhWeoOi1C-DHNoGnWesiPwOy9JDDnaMWSbESg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1Qk1qVTRNemMw/WW1RdFl6bGtOeTAw/WmpKa0xXRTJORGt0/Wm1NMU9XWm1PVEF5/T1RCbFhrRXlYa0Zx/Y0djQC5qcGc"
    }
]

#   LISTAS PEDIDOS
order = [
    {
        "cliente":client[0]["nombre"],
        "total": 103.98,
        "fecha": "28/04/2025"
    },
    {
        "cliente":client[3]["nombre"],
        "total": 900.99,
        "fecha": "01/04/2025"
    },
    {
        "cliente":client[1]["nombre"],
        "total": 23.99,
        "fecha": "15/04/2025"
    },
]

#   ENDPOINT
@app.route("/")
def home():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
#   FUNCIÓN DEL ENDPOINT
def dashboard():

    #   NÚMERO TOTAL DE PRODUCTOS EN STOCK
    total_stock = 0
    for total in product:
        total_stock += total["stock"]

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

    #   INGRESO TOTAL
    total_ingreso = 0
    for pedido in order:
        total_ingreso += pedido["total"]

    return render_template("dashboard.html", **info_general, productos=product, total = total_stock , clientes=client, activos = clientes_activos, cliente_max_pedidos = nombre_cliente, pedidos=order, ingreso_total = total_ingreso)

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        
        nombre = request.form["nombre"]
        precio = f'{float(request.form["precio"]):.2f}'
        stock = int(request.form["stock"])
        categoria = request.form["categoria"]
        imagen = request.form["imagen"]

        diccionario = {
            "nombre":nombre,
            "precio":precio,
            "stock":stock,
            "categoria":categoria,
            "img":imagen
            }
        
        product.append(diccionario)

        return redirect(url_for("dashboard"))

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)