import os
from .connection import *

def eliminarUno(): 
    clear()
    flag = True
    while flag: 
        print("Eliminando...\n")

        print("s para salir")
        id = input("_id a eliminar: ")
        try: 
            if id == "s": 
                flag = False
            else:
                id = int(id)
                res = col.delete_one({"_id": id})
                if res.deleted_count > 0: 
                    print("¡Eliminado!")
                    flag = False
                else: 
                    print("Algo salió mal, intente de nuevo.\n\n")
        except: 
            print("Algo salió mal, intente de nuevo.\n\n")

def clear(): 
    os.system("clear")