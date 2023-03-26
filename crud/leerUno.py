import os
from .connection import *


def leerUno(): 
    clear()
    flag = True
    docs = None
    while flag: 
        mensaje = """
Ver una pelicula... 

    Buscar por: 
        1. _id
        2. Titulo 
"""
        print(mensaje)
        opcion = input("Elija una opcion: ")
        if opcion == "1":    
            id = input("_id: ")
            try:
                docs = col.find({"_id": int(id)})
                flag = False
            except: 
                error()

        elif opcion == "2": 
            titulo = input("Titulo: ")
            docs = col.find({"titulo": titulo})
            flag = False
        else: 
            error()

       
    for doc in docs: 
        print(doc)



def error(): 
    clear()
    print("Opcion no valida, intente de nuevo.\n")

def clear(): 
    os.system("clear")