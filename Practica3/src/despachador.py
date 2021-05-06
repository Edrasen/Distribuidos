from pymongo import MongoClient
import json
import random

url_portadas = []
books = []

client = MongoClient('localhost')

db = client['prac3']

collection = db['books']

docs = collection.find({})

for doc in docs:
    url = doc['datos']['portada']
    name = doc['datos']['name']
    url_portadas.append(url)
    books.append(name)

num_books = len(books) - 1

#print(url_portadas)
print(books)

def set_status():
    datos = ""
    random_book = books[random.randint(0,num_books)]
    random_b = collection.find_one({"datos.name": random_book})
    try: 
        if random_b['status'] == "D":
            collection.update({
                "datos.name": random_book}, 
                { "$set":{ "status": "N"}})
            datos = "Nombre: {} \nAutor: {} \nAño: {:n} \nEditorial: {}".format(random_b['datos']['name'],random_b['datos']['autor'],random_b['datos']['anio'],random_b['datos']['editorial'])
            return datos
            #print(datos)
        else:
            set_status()
    except:
        print("NO hay más libros")
        return "NO hay más libros"
#set_status()

def reset_status():
    collection.update_many({}, { "$set":{ "status": "D"}})

#reset_status()