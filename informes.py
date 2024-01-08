import os
from conexiones import conexion
from notas import estudiantePruebaAdmision as promedio, obtenerModulosDeRutasNoTabla
from validaciones import romperCiclo
from utils import mostrarCampersConFiltro as busquedaConFiltro, mostrarInfoBasica, rutaTreinerHorario, listarRutas, obtenerNombreTrainer, camperPerteneceARuta
campers = conexion('campers')
rutas = conexion('rutas')


def campersInscritos():
    os.system('clear')
    print("\n\t***********************")
    print("\t*  CAMPERS INSCRITOS  *")
    print("\t***********************\n")
    busquedaConFiltro('inscrito', 'no')
    salir = input("Enter para salir")


def mostrarNotasAspirante():
    os.system('clear')
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
    salir = input("Enter para salir")

def trainesCampus():
    os.system('clear')
    print("\n\t***********************************************")
    print("\t*   ENTRENADORES QUE TRABAJAN EN CAMPUSLANDS  *")
    print("\t***********************************************\n")

    trainers = conexion('trainers')
    mostrarInfoBasica(trainers, 'nombreT')
    salir = input("Enter para salir")


def campersReprovados():
    os.system('clear')
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
    salir = input("Enter para salir")


def rutaCamperTrainer():
    os.system('clear')
    bandera = True
    while bandera:
        os.system('clear')
        print("\n******************************************************")
        print("*   CAMPERS Y ENTRENADORES QUE PERTENECEN A UNA RUTA  *")
        print("******************************************************\n")
        listarRutas(rutas)
        
        idRuta = input("Seleccione la ruta por su respectivo id: ")
        if idRuta not in rutas:
            print(f"*** Error - el id {idRuta} no pertenece a ninguna ruta")
        else:
            os.system('clear')
            print("\n\t***************************")
            print(f"\t\t{rutas[idRuta]['nombreR']}  ")
            print("\t***************************\n")

            print(f"Trainer: {obtenerNombreTrainer(idRuta)}\n")
            print("Listado de Campers: ")
            print(80 * "-")
            print("| ID \t| NOMBRE \t| APELLIDOS")
            print(80 * "-")
            for llave, valor in campers.items():
                if valor['estado'] == 'aprobado' and valor['haveRuta'] == 'si':
                    if camperPerteneceARuta(llave, idRuta):
                        print(f"| {llave} \t| {valor['nombreC']} \t| {valor['apellidos']} ")
                        print(80 * "-")
        bandera = romperCiclo(' el id de otra ruta para ver su trainer y campers')


def filtrosXRuta():
    os.system('clear')
    print("\n******************************************************")
    print("*   CAMPERS Y ENTRENADORES QUE PERTENECEN A UNA RUTA  *")
    print("******************************************************\n")
    listarRutas(rutas)
    
    idRuta = input("Seleccione la ruta por su respectivo id: ")
    if idRuta not in rutas:
        print(f"*** Error - el id {idRuta} no pertenece a ninguna ruta")
    else:
        os.system('clear')
        print("\n\t***************************")
        print(f"\t\t{rutas[idRuta]['nombreR']}  ")
        print("\t***************************\n")

        print(f"Trainer: {obtenerNombreTrainer(idRuta)}\n")

        obtenerModulosDeRutasNoTabla(idRuta, 'fundamentos')
        obtenerModulosDeRutasNoTabla(idRuta, 'programacion web')
        obtenerModulosDeRutasNoTabla(idRuta, 'programacion formal')
        obtenerModulosDeRutasNoTabla(idRuta, 'bases de datos')
        obtenerModulosDeRutasNoTabla(idRuta, 'backend')
        salir = input("Enter para salir")