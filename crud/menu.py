import os
import time
from .opciones import *
from .leerTodo import *
from .leerUno import *
from .insertarUno import *
from .actualizarUno import *
from .eliminarUno import *


def menu(): 
    clear()
    flag = True
    print("""
            ¡Bienvenido!
        """)
    while flag: 
        opcion = opciones()
        if opcion == "1": 
            clear()
            print("Todos las peliculas...\n")
            print("¿Desea filtrar por fecha? (s/n)")
            filtro = input()
            if filtro == "s": 
                leerTodo(1)
            else: 
                leerTodo(0)
            
        elif opcion == "2": 
            leerUno()
        elif opcion == "3": 
            insertarUno()
        elif opcion == "4": 
            actualizarUno()
        elif opcion == "5": 
            eliminarUno()
        elif opcion == "6": 
            clear()
            print("\n ¡Buen día!")
            time.sleep(2)
            flag = False
        else: 
            print("Opción no válida. Intenta de nuevo.")


def clear(): 
    os.system("clear")