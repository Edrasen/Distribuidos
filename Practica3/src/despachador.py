from pymongo import MongoClient
import json
import random

url_portadas = []
books = []
prestados = []
portada = ""

client = MongoClient('localhost')

db = client['prac3']

collection = db['books']

docs = collection.find({})

for doc in docs:
    url = doc['datos']['portada']
    name = doc['datos']['name']
    url_portadas.append(url)
    books.append(name)

#print(url_portadas)
print(books)

def set_status(idCliente,nameClient, horaIn):
    global portada
    if len(books) > 0:
        datos = ""
        pos = random.randint(0,len(books)-1)
        random_book = books[pos]
        random_b = collection.find_one({"datos.name": random_book})
        if random_b['status'] == "D":
            portada = url_portadas[pos]
            print(portada)
            collection.update({
                "datos.name": random_book}, 
                { "$set":{ "status": "N"}})
            datos = "Nombre: {} \nAutor: {} \nAño: {:n} \nEditorial: {}".format(random_b['datos']['name'],random_b['datos']['autor'],random_b['datos']['anio'],random_b['datos']['editorial'])
            collection.update({
                "datos.name": random_book},
                {"$push":{"prestamos": 
                    {"idCliente": idCliente, 
                    "idUsuario": nameClient, 
                    "horaInicio": horaIn, 
                    "horaFin": "11:11", 
                    "fecha": "06/05/2021"}
                    }
                    })
            books.remove(random_book)
            return datos
        else:
            set_status()
    else:
        print("NO hay más libros")
        return None
#set_status()

def reset_status():
    collection.update_many({}, { "$set":{ "status": "D"}})

#reset_status()