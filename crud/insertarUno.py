import os
from .connection import * 

def insertarUno(): 
    clear()
    print("Insertando...\n")
    obj = {}

    flag = True
    while flag: 
        try: 
            id = input("_id: ")
            id = int(id)
            flag = False
        except: 
            print("Id entero, por favor.")
    
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    flag = True
    while flag: 
        fecha = input("Año de emisión: ")
        try: 
            fecha = int(fecha)
            flag = False
        except: 
            print("Valor entero, por favor")
    flag = True
    while flag: 
        duracion = input("Duracion: ")
        try: 
            duracion = int(duracion)
            flag = False
        except: 
            print("Valor entero, por favor")

    obj["_id"] = id
    obj["titulo"] = titulo
    obj["autor"] = autor
    obj["genero"] = genero
    obj["fecha_emision"] = fecha
    obj["duracion"] = duracion
    
    res = col.insert_one(obj)
    print(obj)
    print("\n¡Insertada correctamente!")
    
        
def clear(): 
    os.system("clear")