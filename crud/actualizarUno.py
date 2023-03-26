import os
from .connection import * 

def actualizarUno(): 
    clear()
    print("Actualizando...\n")
    actualizar()
        

def actualizar():
    flag = True
    while flag:
        id = input("\n_id a actualizar: ")
        try: 
            id = int(id)
            flag = False
            generarNuevo(id)
        except: 
            print("_id no válido, intente de nuevo.")
            flag = True



def generarNuevo(id): 
    docs = col.find({"_id": int(id)})
    newObj = {}
    newObj["_id"] = int(id)
    for doc in docs: 
        for x, y in doc.items(): 
            if x != "_id": 
                flag = True
                while flag: 

                    print("Antes, " +str(x) + ": " + str(y))
                    newY = input("Ahora, "+ str(x)+ ": ")

                    if x == "fecha_emision" or x == "duracion": 
                        try: 
                            newY = int(newY)
                            flag = False
                        except: 
                            print("Valor entero, por favor")
                    else: 
                        flag = False
                
                newObj[x] = newY
    if newObj["duracion"] > 0 and newObj["fecha_emision"] > 1800: 
        res = col.update_one({"_id": id}, {"$set": newObj})
        print(newObj)
        print("¡Actualizado!")
    else: 
        print("Algo salió mal, intente de nuevo.")

def clear(): 
    os.system("clear")