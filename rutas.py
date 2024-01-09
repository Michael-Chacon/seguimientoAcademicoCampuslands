import os
from utils import seleccionarSgbd
from validaciones import romperCiclo
from conexiones import conexion, guardar

def retornarIdSala(idRuta):
    rutas = conexion('rutas')
    return rutas[idRuta]['idsalaR']


def guardarRuta():
    rutas = conexion('rutas')
    salas = conexion('salas')
    temarioRuta = conexion('temarioRuta')
    print
    bandera = True
    while bandera:
        os.system('clear')
        print("\n*** Alerta - los ids 1, 2, 3 estan asignados por defento, no los uses ***")
        idRuta = input("Ingresa el id de la nueva ruta: ")
        if idRuta in rutas:
            print(f"\n*** Error - el id {idRuta} ya esta asignado a la ruta {rutas[idRuta]['nombreR']} ***\n")
        else:
            nombre = input("Nombre de la ruta (ejm: Java): ")
            print("\n***** SGBD *****")
            db = []
            print("Selecciona 2 sistemas gestores de bases de datos (ejm: 12):\n\t1: Mysql\n\t2: MongoDb\n\t3: Postgresql\n")
            for i in range(0,2):
                #hay que validar el ingreso de letras en el las DB
                if i == 0:
                    principal = int(input("Seleccione el SGBD principal de la ruta: "))
                    db.append(seleccionarSgbd(principal) + " P")
                else:
                    alternativo = int(input("Seleccione el SGBD alternativo de la ruta: "))
                    # temarioRuta[idRuta]['bases de datos'].append(seleccionarSgbd(alternativo))
                    db.append(seleccionarSgbd(alternativo) + " S")

            banderaHija = True
            print("\n***** BACKEND *****")
            backend = []
            
            while banderaHija:
                back = input("Ingrese el framework que que se verá en la ruta: ")
                backend.append(back)
                banderaHija = romperCiclo('otro framework al temario backend')
            temarioRuta[idRuta] = {'fundamentos': ["Introducción a la algoritmia", "PSeInt", "Python", "Git y gitHub"], "programacion web": ["HTML", "CSS", "Tailwind"], "programacion formal": [nombre], "bases de datos": db, "backend": backend}
            guardar('temarioRuta', temarioRuta)

            print(f"\nSeleccione la sala que le va a asignar a la nueva ruta:")
            for llave, valor in salas.items():
                print(f"\t{llave}: {valor['nombreS']}")
            idSala = input(": ")
            if idSala not in salas:
                print(f"\n*** Error - el id {idSala} no existe ***\n")
            else:
                print('\n--- Ruta creada con éxito ---\n')
                rutas[idRuta] = {'nombreR': nombre, 'idsalaR': idSala}
                guardar('rutas', rutas)
        bandera = romperCiclo('un nuevo ruta')