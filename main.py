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

# mainFlag = True
# while mainFlag:
#     os.system('clear')
#     print("\n\t********************")
#     print("\t*  MENÚ PRINCIPAL  *")
#     print("\t********************\n")

#     print("""
#         1. Todo sobre campers\n
#         2. Todo sobre trainers\n
#         3. Todo sobre rutas\n
#         0. Cerrar sesión\n
#         """)
#     break

# guardarCamper()
# guardarTrainer()
# listarInfo(trainers, 'nombreT')
# relacion(campers)
# rutaTreiner()
# listarInfo(trainers, 'nombreT')
# guardarRuta()
# prueba(campers)
# matricularCamper()
# filtro()
# print(trainers)
# print(pruebas)
campersInscritos()