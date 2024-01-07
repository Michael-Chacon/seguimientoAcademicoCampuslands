import os
from rutas import retornarIdSala
from camper import registrarAsigancionRuta
from conexiones import guardar, conexion
from trainer import trainerRutasHorarios
from validaciones import existeElId as hayId,  cuposEnHorario, romperCiclo
from utils import mostrarCampersConFiltro as mostrarCampers, mostrarInfoBasica, restarCupoAHorario

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
    banderaMain = True
    while banderaMain:
        print("\nListado de campers con estado aprobado y sin ruta asignada:")
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
                print("Seleccione el ID de la ruta que le va a asigar al camper: ")
                # onden en el que se muestran los datos: id (0) - id de la ruta(1) - id del horario(2)
                rutasHorarios = trainerRutasHorarios(idTrainer)
                print(rutasHorarios)
                bandera = True
                while bandera:
                    try:
                        rutaSeleccionada = int(input(": "))
                    # validar por si ingresa una letra y pedir de nuevo que ingrese la opcion
                        if rutaSeleccionada > len(rutasHorarios)-1:
                            print(f"El id {rutaSeleccionada} no pertenece a ninguna ruta")
                        else:
                            bandera = False
                    except Exception:
                        print('Error - el dato ingresado no es correcto, ingrese el dato nuevamente')

                # validar que el horario tenga cupos disponibles
                if cuposEnHorario(rutasHorarios[rutaSeleccionada][2]):
                    fechaInicio = input('Ingrese la fecha de inicio con el formato d-m-a: ')
                    fechaInicio = input('Ingrese la fecha de finalización con el formato d-m-a: ')
                    # obtener el id de la sala pero del json de rutas.
                    idSale = retornarIdSala(rutasHorarios[rutaSeleccionada][1])
                    matriculas[idCamper] = {'idTrainerM': idTrainer, "idRutaM": rutasHorarios[rutaSeleccionada][1], "fechaInicio": fechaInicio, "fechaFin": fechaInicio, "idSalaM": idSale}
                    guardar('matriculas', matriculas)
                    registrarAsigancionRuta(idCamper)
                    restarCupoAHorario(rutasHorarios[rutaSeleccionada][2])
                    print("--- Camper matriculado con éxito ---")
                else:
                    print("*** Alerta - el horario seleccionado no tiene cupos disponibles, el camper no puede ser matriculdo en este horario ***")
            banderaMain = romperCiclo('matricular otro camper')
            os.system('clear')


def filtro():
    campers = conexion('campers')

    print(f"\nListado de campers con estado aprobado:")
    mostrarCampers('aprobado', 'si')
    camper = input("Seleccine el id del camper al que le va a asiganar la nota del filtro: ")
    if camper not in campers:
        print(f"Error - el id {camper} no esta asignado a ningun camper")
