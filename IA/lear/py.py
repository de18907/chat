"""
MATLAB

Las funciones scipy.io.loadmaty le scipy.io.savematpermiten leer y escribir archivos MATLAB. 

La función scipy.spatial.distance.pdistcalcula la distancia entre todos los pares de puntos en un conjunto dado:


Matplotlib

"""
import pymongo
import pymongo import MongoClient

cluster = MongoClient("mongodb+srv://sergioaugustominaya:SAnh350z@cluster0-j1pqn.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = { "_id": 0, "name": "tim", "score": 5 }

collection.insert_one(post)
