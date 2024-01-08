from conexiones import conexion
from notas import estudiantePruebaAdmision as promedio
from validaciones import romperCiclo
from utils import mostrarCampersConFiltro as busquedaConFiltro, mostrarInfoBasica, rutaTreinerHorario, listarRutas, obtenerNombreTrainer, camperPerteneceARuta
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


def rutaCamperTrainer():
    rutas = conexion('rutas')
    bandera = True
    while bandera:
        print("\n******************************************************")
        print("*   CAMPERS Y ENTRENADORES QUE PERTENECEN A UNA RUTA  *")
        print("******************************************************\n")
        listarRutas(rutas)
        
        idRuta = input("Seleccione la ruta por su respectivo id: ")
        if idRuta not in rutas:
            print(f"*** Error - el id {idRuta} no pertenece a ninguna ruta")
        else:
            print("\n\t***************************")
            print(f"\t\t{rutas[idRuta]['nombreR']}  ")
            print("\t***************************\n")

            print(f"Trainer: {obtenerNombreTrainer(idRuta)}")

            print(100 * "-")
            print("| ID \t| NOMBRE \t| APELLIDOS")
            print(100 * "-")
            for llave, valor in campers.items():
                if valor['estado'] == 'aprobado' and valor['haveRuta'] == 'si':
                    if camperPerteneceARuta(llave, idRuta):
                        print(f"| {llave} \t| {valor['nombreC']} \t| {valor['apellidos']} ")
                        print(80 * "-")
        bandera = romperCiclo(' el id de otra ruta para ver su trainer y campers')