import os
from rutas import guardarRuta
from conexiones import conexion as con, guardar
from utils import mostrarInfoBasica as listarInfo
from notas import guardarNotasPrueba as prueba, matricularCamper, filtro
from camper import guardar as guardarCamper #, mostrarNotasAspirante as relacion
from trainer import guardar as guardarTrainer, guardarRutaTrainer as rutaTreiner
from informes import *

campers = con('campers')
trainers = con('trainers')
rutas = con('rutas')
salas = con('salas')

print("Hola, bienvenidos al programa que permite llevar el seguimiento académico de todos los campers")

mainFlag = True
while mainFlag:
    os.system('clear')
    print("\n\t********************")
    print("\t*  MENÚ PRINCIPAL  *")
    print("\t********************\n")

    print("""
        1. Todo sobre campers\n
        2. Todo sobre trainers\n
        3. Todo sobre rutas\n
        4. Informes\n
        0. Cerrar sesión\n
        """)
    
    opcion = input("\nIngrese el número de la opción correspondiente: ")
    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '0':
        break
    else:
        print("*** Error - Opción incorrecta ***")

    

# guardarCamper()
# prueba(campers)
# guardarTrainer()
# listarInfo(trainers, 'nombreT')
# relacion(campers)
# rutaTreiner()
# listarInfo(trainers, 'nombreT')
# guardarRuta()
# matricularCamper()
# filtro()
# print(trainers)
# print(pruebas)

#INFORMES
# campersInscritos()
# campersReprovados()
# trainesCampus()
# mostrarNotasAspirante()
# rutaCamperTrainer()
# filtrosXRuta() 