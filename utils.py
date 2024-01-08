import os
from validaciones import romperCiclo
from conexiones import conexion as con, guardar as guardarEnJson


def mostrarInfoBasica(diccionario, name):
        print(60 * "-")
        print("| ID \t| NOMBRE \t| APELLIDOS")
        print(60 * "-")
        for llave, valor in diccionario.items():
            print(f"| {llave} \t| {valor[name]} \t| {valor['apellidos']}")
            print(60 * "-")


def mostrarCampersConFiltro(estado, ruta):
    campers = con('campers')
    print(80 * "-")
    print("| ID \t| NOMBRE \t| APELLIDOS ")
    print(80 * "-")
    for llave, valor in campers.items():
        if valor['estado'] == estado and valor['haveRuta'] == ruta:
            print(f"| {llave} \t| {valor['nombreC']} \t| {valor['apellidos']} ")
            print(80 * "-")


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
    
def seleccionarModulo(opcion):
    if opcion == '1':
        return 'fundamentos'
    elif opcion == '2':
        return 'programacion web'
    elif opcion == '3':
        return 'programacion formal'
    elif opcion == '4':
        return 'bases de datos'
    elif opcion == '5':
        return 'backend'
    

def rutaTreinerHorario(idCamper):
    matriculas = con('matriculas')
    idTrainer = matriculas[idCamper]['idTrainerM']
    idRuta = matriculas[idCamper]['idRutaM']
    trainer = retornarNombreTrainer(idTrainer)
    ruta = retornarNombreRuta(idRuta)
    return [trainer, ruta]


def retornarNombreTrainer(idTrainer):
    trainers = con('trainers')
    return trainers[idTrainer]['nombreT']


def retornarNombreRuta(idRuta):
    rutas = con('rutas')
    return rutas[idRuta]['nombreR']


def listarRutas(rutas):
        print(60 * "-")
        print("| ID \t| NOMBRE ")
        print(60 * "-")
        for llave, valor in rutas.items():
            print(f"| {llave} \t| {valor['nombreR']} ")
            print(60 * "-")


def obtenerNombreTrainer(idRuta):
    trainers = con('trainers')
    for llave, valor in trainers.items():
        if buscarRuta(llave, idRuta):
            return valor['nombreT']
            break


def buscarRuta(idTrainer, idRuta):
    rutaTrainer = con('rutaTrainers')
    if idRuta in rutaTrainer[idTrainer]['idRutaRT']:
        return True
    else: 
        return False


def camperPerteneceARuta(idCamper, idRuta):
    matriculas = con('matriculas')
    if matriculas[idCamper]['idRutaM'] == idRuta:
        return True
    else: 
        return False