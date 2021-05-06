from pymongo import MongoClient
import json
import random

url_portadas = []
books = []
prestados = []

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

def set_status():
    datos = ""
    pos = random.randint(0,len(books)-1)
    random_book = books[pos]
    random_b = collection.find_one({"datos.name": random_book})
    if random_b['status'] == "D":
        collection.update({
            "datos.name": random_book}, 
            { "$set":{ "status": "N"}})
        datos = "Nombre: {} \nAutor: {} \nAño: {:n} \nEditorial: {}".format(random_b['datos']['name'],random_b['datos']['autor'],random_b['datos']['anio'],random_b['datos']['editorial'])
        books.remove(random_book)
        return datos
    else:
        set_status()

#set_status()

def reset_status():
    collection.update_many({}, { "$set":{ "status": "D"}})

#reset_status()