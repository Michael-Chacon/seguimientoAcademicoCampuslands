import os
from rutas import retornarIdSala
from camper import registrarAsigancionRuta
from conexiones import guardar, conexion
from trainer import trainerRutasHorarios
from validaciones import existeElId as hayId,  cuposEnHorario, romperCiclo
from utils import mostrarCampersConFiltro as mostrarCampers, mostrarInfoBasica, restarCupoAHorario, seleccionarModulo

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
                # onden en el que se muestran los datos: id (0) - id de la ruta(1) - id del horario(2) array de str
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
                    idSala = retornarIdSala(rutasHorarios[rutaSeleccionada][1])
                    matriculas[idCamper] = {'idTrainerM': idTrainer, "idRutaM": rutasHorarios[rutaSeleccionada][1], "fechaInicio": fechaInicio, "fechaFin": fechaInicio, "idSalaM": idSala}
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
    rutas = conexion('rutas')

    print(f"\nListado de campers con estado aprobado:")
    mostrarCampers('aprobado', 'si')
    camper = input("Seleccine el id del camper al que le va a asiganar la nota del filtro: ")
    if camper not in campers:
        print(f"Error - el id {camper} no esta asignado a ningun camper")
    else:
        os.system('clear')
        matriculas = conexion('matriculas')
        idRuta = matriculas[camper]['idRutaM']
        print(f"\n--- El camper {campers[camper]['nombreC']} está matriculado en la ruta {rutas[idRuta]['nombreR']} ---\n")
        print(f"Veamos los módulos de la ruta {rutas[idRuta]['nombreR']} en los que el camper tiene que presentar el filtro")
        
        print("\n\t", 40 * '*')
        print("\t * (1)\t FUNDAMENTOS DE PROGRAMACIÓN")
        obtenerModulosDeRutas(idRuta, 'fundamentos')

        print("\n\t", 40 * '*')
        print("\t * (2)\t PROGRAMACIÓN WEB")
        obtenerModulosDeRutas(idRuta, 'programacion web')

        print("\n\t", 40 * '*')
        print("\t * (3)\t PROGRAMACIÓN FORMAL")
        obtenerModulosDeRutas(idRuta, 'programacion formal')

        print("\n\t", 40 * '*')
        print("\t * (4)\t BASES DE DATOS")
        obtenerModulosDeRutas(idRuta, 'bases de datos')

        print("\n\t", 40 * '*')
        print("\t * (5)\t BACKEND")
        obtenerModulosDeRutas(idRuta, 'backend')

        idModulo = input("\nSeleccione el id modulo que va a evaluar, [el id esta entre corchete en el titulo de cada modulo]: ")
        moduloSelec = seleccionarModulo(idModulo)

        print(f"\n---------- Vas a calificar el módulo {moduloSelec.upper()} a {campers[camper]['nombreC']} ----------\n")
        print("Recordemos las pruebas y sus valores")
        print("--------------------")
        print("|VALOR | PRUEBA    |")
        print("--------------------")
        print("| 60%  | Practica  |")
        print("--------------------")
        print("| 30%  | Téorica   |")
        print("--------------------")
        print("| 10%  | Trabajos  |")
        print("--------------------")

        
        while True:
            try:
                practica = float(input("Ingresa la nota obtenida en la prueba practica: "))
            except Exception:
                print("El dato ingresado no es valido, ingrese la nota correctamente")
            else:
                break
            
        while True:
            try:
                teorica = float(input("Ingresa la nota obtenida en la prueba téorica: "))
            except Exception:
                print("El dato ingresado no es valido, ingrese la nota correctamente")
            else:
                break
        
        banderaQ = True
        trabajos = []
        while banderaQ:
            try:
                nota = float(input("Ingrese la nota del trabajo o quiz: "))
            except Exception:
                print("El dato ingresado no es valido, ingrese la nota correctamente")
            trabajos.append(nota)
            banderaQ = romperCiclo("otro nota")

        
        totalTrabajos = sum(trabajos) / len(trabajos)

        definitiva =  (totalTrabajos * 0.1) + (teorica * 0.3) + (practica * 0.6)



def obtenerModulosDeRutas(idRuta, modulo):
    temarioRuta = conexion('temarioRuta')
    modulos = temarioRuta[idRuta][modulo]
    contador = 0
    print("\t", 40 * '*')
    print("\t|# \t| \tTEMAS")
    print("\t", 40 * '-')
    for i in modulos:
        contador += 1
        print(f"\t|{contador} \t|{i}")
        print("\t", 40 * '-')
        
