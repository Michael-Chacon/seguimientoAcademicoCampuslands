import os
from conexiones import conexion, guardar
from validaciones import romperCiclo

def retornarIdSala(idRuta):
    rutas = conexion('rutas')
    return rutas[idRuta]['idSalaR']


def guardarRuta():
    rutas = conexion('rutas')
    salas = conexion('salas')
    bandera = True
    while bandera:
        os.system('clear')
        print("\n*** Alerta - los ids 1, 2, 3 estan asignados por defento, no los uses ***")
        idRuta = input("Ingresa el id de la nueva ruta: ")
        if idRuta in rutas:
            print(f"\n*** Error - el id {idRuta} ya esta asignado a la ruta {rutas[idRuta]['nombreR']} ***\n")
        else:
            nombre = input("Nombre de la ruta: ")
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