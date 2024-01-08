from conexiones import conexion
from notas import estudiantePruebaAdmision as promedio
from utils import mostrarCampersConFiltro as busquedaConFiltro, mostrarInfoBasica, rutaTreinerHorario
campers = conexion('campers')

def campersInscritos():
    print("\n\t***********************")
    print("\t*  CAMPERS INSCRITOS  *")
    print("\t***********************\n")
    busquedaConFiltro('inscrito', 'no')


def mostrarNotasAspirante():
    print("\n\t*********************************************")
    print("\t*  CAMPERS QUE APROBARON EL EXAMEN INICIAL  *")
    print("\t*********************************************\n")

    print(80 * "-")
    print("| ID \t| NOMBRE \t| APELLIDOS \t| PROMEDIO")
    print(80 * "-")
    for llave, valor in campers.items():
        if valor['estado'] == 'aprobado':
            notas = promedio(llave)
            print(f"| {llave} \t| {valor['nombreC']} \t| {valor['apellidos']} \t| {notas[2]}")
            print(80 * "-")


def trainesCampus():
    print("\n\t***********************************************")
    print("\t*   ENTRENADORES QUE TRABAJAN EN CAMPUSLANDS  *")
    print("\t***********************************************\n")

    trainers = conexion('trainers')
    mostrarInfoBasica(trainers, 'nombreT')


def campersReprovados():
    print("\n\t***********************************")
    print("\t*   CAMPERS CON BAJO RENDIMIENTO  *")
    print("\t***********************************\n")

    print(100 * "-")
    print("| ID \t| NOMBRE \t| APELLIDOS \t| TRAINER \t| RUTA")
    print(100 * "-")
    for llave, valor in campers.items():
        if valor['estado'] == 'reprobado' and valor['haveRuta'] == 'si':
            data = rutaTreinerHorario(llave)
            print(f"| {llave} \t| {valor['nombreC']} \t| {valor['apellidos']} \t| {data[0]} \t| {data[1]} ")
            print(80 * "-")