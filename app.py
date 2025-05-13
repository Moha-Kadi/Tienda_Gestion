#   LIBRERÍAS
import datetime
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from decouple import config
URL_MONGO = config("ENLACE_DB", cast=str)

app = Flask(__name__)
mongo = MongoClient(URL_MONGO)
app.db = mongo.PythonMongoDB  

Productos = [producto for producto in app.db.Productos.find({})]


#   DATOS
#   INFORMACIÓN GENERAL
info_general = {
    "admin": "moha",
    "tienda": "TecnoMarket",
    "fecha": datetime.date.today()
}

# #   LISTA PRODUCTOS
# product = [
#     {
#         "nombre":"Gorra MilfShakes",
#         "precio":23.99,
#         "stock": 25,
#         "categoria":"Ropa",
#         "img":"https://milfshakes.es/cdn/shop/files/680e407e46b184b1ba1bc47c_Frontal-gorra.webp?v=1745764983"
#         },
#     {
#         "nombre": "Iphone 13",
#         "precio": 780,
#         "stock": 7,
#         "categoria": "Electrónica",
#         "img":"https://res-1.cloudinary.com/grover/image/upload/v1632242422/e4vsrkuyzzlspnwtxbvj.png"
#     },
#     {
#         "nombre": "Sudadera Stussy",
#         "precio": 79.99,
#         "stock": 0,
#         "categoria": "Ropa",
#         "img":"https://images.cults3d.com/mkigXOcrjp2dXsiwzP3kGcmLdHA=/516x516/filters:no_upscale()/https://fbi.cults3d.com/uploaders/28951487/illustration-file/84b8c090-3dc2-4175-9a09-95ac4a893e49/Capture-d'%C3%A9cran-2023-10-27-170127.png"
#     },
#     {
#         "nombre": "AirPods Pro 2",
#         "precio": 120.99,
#         "stock": 12,
#         "categoria": "Electrónica",
#         "img":"https://m.media-amazon.com/images/I/51R8U4qEfAL.jpg"
#     },
#     {
#         "nombre": "Caja Segarros",
#         "precio": 5.66,
#         "stock": 12,
#         "categoria": "Consumo",
#         "img":"https://imgs.search.brave.com/RgOQzlfsrj2wfE1CER70qXDBuw6UPG81uv0TaF1G6B0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9maW5v/ZmlsaXBpbm8ub3Jn/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDI1/LzA0L0FVbjFIMFku/anBlZw"
#     }, 
#     {
#         "nombre": "Caja Gipsy",
#         "precio": 129.99,
#         "stock": 6,
#         "categoria": "Gipsy Music",
#         "img":"https://www.laguitarreria.es/6860-large_default/cajon-flamenco-soy-gitana.jpg"
#     },
# ]

#   LISTA CLIENTES
client = [
    {
        "nombre": "Alejandro",
        "email": "alejandro@gmail.com",
        "activo": False,
        "pedidos": 1,
        "img":"https://labsaenzrenauld.com/wp-content/uploads/2020/10/Perfil-hombre-ba%CC%81sico_738242395.jpg"
    },
    {
        "nombre":"Maria",
        "email":"maria@gmail.com",
        "activo":True,
        "pedidos": 3,
        "img":"https://b2472105.smushcdn.com/2472105/wp-content/uploads/2023/09/Poses-Perfil-Profesional-Mujeres-ago.-10-2023-1-819x1024.jpg?lossy=1&strip=1&webp=1"
    },
    {
        "nombre":"Juanjo",
        "email":"juanjo@gmail.com",
        "activo":True,
        "pedidos": 5,
        "img":"https://upload.wikimedia.org/wikipedia/commons/2/24/Pedro_S%C3%A1nchez_in_2018d.jpg"
    },
    {
        "nombre": "Elvis",
        "email": "elvis@gmail.com",
        "activo": True,
        "pedidos": 8,
        "img":"https://c.pxhere.com/images/c6/91/441b53afa0a69dc4acfbb01dd205-1447095.jpg!d"
    },
    {
        "nombre": "Churumbel",
        "email": "churumbel@gmail.com",
        "activo": False,
        "pedidos": 1,
        "img":"https://yt3.googleusercontent.com/0yWvElIEwMpCzjPpkras00OuHs3bU_iWhb9a8CpbSxhQIx16XG8UN2qIz9qJl3XThg3KqLUfcw=s160-c-k-c0x00ffffff-no-rj"
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
        "fecha": "01/05/2025"
    },
    {
        "cliente":client[2]["nombre"],
        "total": 159.64,
        "fecha": "22/04/2025"
    },
    {
        "cliente":client[4]["nombre"],
        "total": 129.99,
        "fecha": "08/05/2025"
    }
]

#   ENDPOINT
@app.route("/")
def home():
    return redirect("/dashboard")

#   ENDPOINT
@app.route("/dashboard")
#   FUNCIÓN DEL ENDPOINT
def dashboard():

    #   NÚMERO TOTAL DE PRODUCTOS EN STOCK
    total_stock = 0
    for total in Productos:
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

    return render_template("dashboard.html", **info_general, products=Productos, total = total_stock , clientes=client, activos = clientes_activos, cliente_max_pedidos = nombre_cliente, pedidos=order, ingreso_total = total_ingreso)

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        
        nombre = request.form["nombre"]
        precio = f'{float(request.form["precio"]):.2f}'
        stock = int(request.form["stock"])
        categoria = request.form["categoria"]
        imagen = request.form["imagen"]

        parametros = {
            "nombre":nombre,
            "precio":precio,
            "stock":stock,
            "categoria":categoria,
            "img":imagen
            }
        
        Productos.append(parametros)
        app.db.Productos.insert_one(parametros)
        print(Productos)
        

        return redirect("/dashboard")

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)