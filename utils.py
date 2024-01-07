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


def seleccionarSgbd(opcion):
    if opcion == 1:
        return 'Mysql'
    elif opcion == 2:
        return 'MongoDb'
    elif opcion == 3:
        return 'Postgresql'