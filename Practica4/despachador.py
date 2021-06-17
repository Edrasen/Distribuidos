from pymongo import MongoClient, collection
import json
import random

url_portadas = []
books = []
prestados = []
portada = ""


client = MongoClient("mongodb://localhost:2717,localhost:2727,localhost:2737/?replicaSet=myReplicaSetD")

db = client['prac3']

collection = db['books']

docs = collection.find({})

for doc in docs:
    url = doc['datos']['portada']
    name = doc['datos']['name']
    url_portadas.append(url)
    books.append(name)

def set_status(idCliente,ipClient, horaIn):
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
                    "ipUsuario": ipClient, 
                    "horaInicio": horaIn, 
                    "fecha": "06/05/2021"}
                    }
                    })
            books.remove(random_book)
            url_portadas.pop(pos)
            return datos
        else:    
            set_status(idCliente,ipClient, horaIn)
    else:
        print("NO hay más libros")
        return None
#set_status()

def reset_status():
    global collection,client
    collection.update_many({}, { "$set":{ "status": "D"}})

reset_status()