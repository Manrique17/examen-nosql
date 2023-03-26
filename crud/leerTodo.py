from .connection import *

def leerTodo(filtro):
    print("\n")
    if filtro == 1: 
        docs = col.find().sort("fecha_emision")
        for doc in docs: 
            print(doc)
    elif filtro == 0:
        docs = col.find()
        for doc in docs: 
            print(doc)