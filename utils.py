import os
from validaciones import romperCiclo
from conexiones import conexion as con, guardar as guardarEnJson


def mostrarInfoBasica(diccionario, name):
        print(40 * "-")
        print("| ID \t| NOMBRE ")
        print(40 * "-")
        for llave, valor in diccionario.items():
            print(f"| {llave} \t| {valor[name]} ")
            print(40 * "-")


def mostrarCampersConFiltro(estado, ruta):
    campers = con('campers')
    print("\nListado de campers con estado aprobado y sin ruta asignada:")
    print(40 * "-")
    print("| ID \t| NOMBRE ")
    print(40 * "-")
    for llave, valor in campers.items():
        if valor['estado'] == estado and valor['haveRuta'] == ruta:
            print(f"| {llave} \t| {valor['nombreC']} ")
            print(40 * "-")


def restarCupoAHorario(idHorario):
    horarios = con('horarios')
    horarios[idHorario]['disponible'] -= 1
    guardarEnJson('horarios', horarios)


def guardarRuta():
    rutas = con('rutas')
    salas = con('salas')
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
                guardarEnJson('rutas', rutas)
        bandera = romperCiclo('un nuevo ruta')