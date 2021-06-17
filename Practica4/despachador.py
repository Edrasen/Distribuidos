from pymongo import MongoClient, collection
import json
import random
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")

#url_portadas = []
books = {}
prestados = []
portada = ""


client = MongoClient("mongodb://localhost:2717,localhost:2727,localhost:2737/?replicaSet=myReplicaSetD")

db = client['prac3']

collection = db['books']

docs = collection.find({})

for doc in docs:
    url = doc['datos']['portada']
    name = doc['datos']['name']
    books[name] = url
#print(books)
#print(len(books))
#print(url_portadas)

def getList(dict):
    return dict.keys()
      


def set_status(idCliente,ipClient, horaIn):
    global portada, books
    #print(len(books))
    if len(books) > 0:
        datos = ""
        random_book, portada = random.choice(list(books.items()))
        random_b = collection.find_one({"datos.name": random_book})
        if random_b['status'] == "D":
            print(random_book,portada)
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
                    "fecha": d1}
                    }
                    })
            books.pop(random_book)
            return datos
        else:    
            set_status(idCliente,ipClient, horaIn)
    else:
        print("NO hay más libros")
        return None
#set_status()

def reset_status():
    global books, url_portadas
    docs = collection.find({})
    collection.update_many({}, { "$set":{ "status": "D"}})
    books.clear()
    #docs = collection.find({})
    for doc in docs:
        url = doc['datos']['portada']
        name = doc['datos']['name']
        books[name] = url
    print(books)
    print(len(books))
#reset_status()