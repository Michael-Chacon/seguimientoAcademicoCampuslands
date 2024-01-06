import os
from conexiones import guardar, conexion
from trainer import trainerRutasHorarios
from validaciones import existeElId as hayId
from utils import mostrarCampersConFiltro as mostrarCampers, mostrarInfoBasica

notasPruebas = conexion('pruebas') # Obtener el diccionario con todas las notas

def guardarNotasPrueba(campers):
    os.system('clear')
    mostrarCampers('inscrito', 'no')
    idAspirante = 0
    try:
        idAspirante = input('Ingrese el id del camper: ')
        # hayId(idAspirante, campers)
    except:
        print(f"El id {idAspirante} no es valido")
    else:
        if(not hayId(idAspirante, campers)):
            print(f"No existe un camper con el id {idAspirante}")
        else:
            if hayId(idAspirante, notasPruebas):
                print(f"{campers[idAspirante]['nombreC']} ya realizo las pruebas")
            else:
                teorica = float(input('Nota de la prueba teorica: '))
                practica = float(input('Nota de la prueba practica: '))
                promedio = (teorica + practica) / 2

                if promedio >= 60:
                    campers[idAspirante]['estado'] = 'aprobado'
                elif promedio < 60:
                    campers[idAspirante]['estado'] = 'reprobado'

                notasPruebas[idAspirante] = {'teorica': teorica, 'practica': practica, 'promedio': promedio}

                guardar('pruebas', notasPruebas)
                guardar('campers', campers)


# Ver las notas de los aspirantes
def estudiantePruebaAdmision(idAspirante):
    if idAspirante in notasPruebas:
        teorico = notasPruebas[idAspirante]['teorica']
        practica = notasPruebas[idAspirante]['practica']
        promedio = notasPruebas[idAspirante]['promedio']
        return [teorico, practica, promedio]
    else:
        return ['sin nota', 'sin nota', 'sin nota']


def matricularCamper():
    matriculas = conexion('matriculas')
    trainers = conexion('trainers')
    mostrarCampers('aprobado', 'no')
    idCamper = input("Ingrese el id del camper que va a matricular: ")
    if idCamper in matriculas:
        print(f"Error - ya existe un camper con el id {idCamper}")
    else:
        os.system('clear')
        
        mostrarInfoBasica(trainers, 'nombreT')
        idTrainer = input("seleccione el trainer por su respectivo id: ")
        if idTrainer not in trainers:
            print(f"Error - no existe ningun trainer con el id {id}")
        else:
            trainerRutasHorarios(idTrainer)