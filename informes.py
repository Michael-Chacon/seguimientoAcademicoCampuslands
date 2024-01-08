from utils import mostrarCampersConFiltro as busquedaConFiltro
from notas import estudiantePruebaAdmision as promedio
from conexiones import conexion


def campersInscritos():
    print("\n\t*************************")
    print("\t*  CAMPERS INSCRITOS  *")
    print("\t*************************\n")
    busquedaConFiltro('inscrito', 'no')


def mostrarNotasAspirante():
    campers = conexion('campers')
    print("\n\t*******************************************")
    print("\t*  CAMPERS QUE APROBARON EL EXAMEN INICIAL  *")
    print("\t*******************************************\n")

    print(80 * "-")
    print("| ID \t| NOMBRE \t| APELLIDOS \t| PROMEDIO")
    print(80 * "-")
    for llave, valor in campers.items():
        if campers[llave]['estado'] == 'aprobado':
            notas = promedio(llave)
            print(f"| {llave} \t| {valor['nombreC']} \t| {valor['apellidos']} \t| {notas[2]}")
            print(80 * "-")