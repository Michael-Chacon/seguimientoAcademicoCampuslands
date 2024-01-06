import os
from conexiones import guardar, conexion
from validaciones import existeElId as hayId

notasPruebas = conexion('pruebas') # Obtener el diccionario con todas las notas

def guardarNotasPrueba(campers):
    os.system('clear')
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


# def estudiantePruebaAdmision(idAspirante):
#     if idAspirante in notasPruebas:
#         teorico = notasPruebas[idAspirante]['teorica']
#         practica = notasPruebas[idAspirante]['practica']
#         promedio = notasPruebas[idAspirante]['promedio']
#         return [teorico, practica, promedio]
#     else:
#         return ['sin nota', 'sin nota', 'sin nota']
