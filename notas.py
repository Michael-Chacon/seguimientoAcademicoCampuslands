import os
from conexiones import guardar
from validaciones import existeElId as hayId


def notasPrueba(campers, pruebas):
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
            if hayId(idCamper, pruebas):
                print(f"{campers[idCamper]['nombreC']} ya realizo las pruebas")
            else:
                teorica = float(input('Nota de la prueba teorica: '))
                practica = float(input('Nota de la prueba practica: '))
                promedio = (teorica + practica) / 2

                if promedio >= 60:
                    campers[idCamper]['estado'] = 'aprobado'
                elif promedio < 60:
                    campers[idCamper]['estado'] = 'reprobado'

                pruebas[idCamper] = {'teorica': teorica, 'practica': practica, 'promedio': promedio}

                guardar('pruebas', pruebas)

