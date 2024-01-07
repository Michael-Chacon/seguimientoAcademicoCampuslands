import os
from conexiones import conexion, guardar
from validaciones import romperCiclo

def retornarIdSala(idRuta):
    rutas = conexion('rutas')
    return rutas[idRuta]['idSalaR']


def guardarRuta():
    rutas = conexion('rutas')
    salas = conexion('salas')
    temarioRuta = conexion('temarioRuta')
    bandera = True
    while bandera:
        os.system('clear')
        print("\n*** Alerta - los ids 1, 2, 3 estan asignados por defento, no los uses ***")
        idRuta = input("Ingresa el id de la nueva ruta: ")
        if idRuta in rutas:
            print(f"\n*** Error - el id {idRuta} ya esta asignado a la ruta {rutas[idRuta]['nombreR']} ***\n")
        else:
            nombre = input("Nombre de la ruta (ejm: Java): ")
            print("***** SGBD *****")
            print("Selecciona 2 sistemas gestores de bases de datos (ejm: 12):\n\t1: Mysql\n\t2: MongoDb\n\t3: Postgresql\n")
            for i in range(0,2):
                #hay que validar el ingreso de letras en el las DB
                if i == 0:
                    principal = int(input("Seleccione el SGBD principal de la ruta: "))
                else:
                    alternativo = int(input("Seleccione el SGBD alternativo de la ruta: "))
                    
            banderaNose = True
            while True:
                print("***** BACKEND *****")
                back = input("Ingrese el framework que que se verá en la ruta: ")
                banderaNose = romperCiclo('otro framework al temario backend')


            # print(f"\nSeleccione la sala que le va a asignar a la nueva ruta:")
            # for llave, valor in salas.items():
            #     print(f"\t{llave}: {valor['nombreS']}")
            # idSala = input(": ")
            # if idSala not in salas:
            #     print(f"\n*** Error - el id {idSala} no existe ***\n")
            # else:
            #     print('\n--- Ruta creada con éxito ---\n')
            #     rutas[idRuta] = {'nombreR': nombre, 'idsalaR': idSala}
            #     guardar('rutas', rutas)
        bandera = romperCiclo('un nuevo ruta')