import os
from conexiones import guardar, conexion
from validaciones import existeElId as hayId

notasPruebas = conexion('pruebas') # Obtener el diccionario con todas las notas

def guardarNotasPrueba(campers):
    os.system('clear')
    idCamper = 0
    try:
        idCamper = input('Ingrese el id del camper: ')
        # hayId(idCamper, campers)
    except:
        print(f"El id {idCamper} no es valido")
    else:
        if(not hayId(idCamper, campers)):
            print(f"No existe un camper con el id {idCamper}")
        else:
            if hayId(idCamper, notasPruebas):
                print(f"{campers[idCamper]['nombreC']} ya realizo las pruebas")
            else:
                teorica = float(input('Nota de la prueba teorica: '))
                practica = float(input('Nota de la prueba practica: '))
                promedio = (teorica + practica) / 2

                if promedio >= 60:
                    campers[idCamper]['estado'] = 'aprobado'
                elif promedio < 60:
                    campers[idCamper]['estado'] = 'reprobado'

                notasPruebas[idCamper] = {'teorica': teorica, 'practica': practica, 'promedio': promedio}

                guardar('pruebas', notasPruebas)


def estudiantePruebaAdmision(idAspir):
    pass
