import os
from rutas import guardarRuta
from conexiones import conexion as con
from notas import guardarNotasPrueba as prueba, matricularCamper, filtro
from camper import guardar as guardarCamper #, mostrarNotasAspirante as relacion
from trainer import guardar as guardarTrainer, guardarRutaTrainer as rutaTreiner
from informes import *

campers = con('campers')
trainers = con('trainers')
rutas = con('rutas')
salas = con('salas')

print("Hola, bienvenidos al programa que permite llevar el seguimiento académico de todos los campers")


while True:
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
        os.system('clear')
        while True:
            os.system('clear')
            print("\n\t******************")
            print("\t*  MENÚ CAMPERS  *")
            print("\t******************\n")
            opcion = input("\nOpciones sobre los campers:\n\t1: Registrar Camper\n\t2: Registro de prueba\n\t3: Matricular camper en una ruta\n\t4: Registrar nota de filtro a un camper\n\t0: Salir\n: ")
            if opcion == '1':
                guardarCamper()
            elif opcion == '2':
                prueba()
            elif opcion == '3':
                matricularCamper()
            elif opcion == '4':
                filtro()
            elif opcion == '0':
                break
            else:
                print("*** Error - Opción incorrecta ***")
                input("Enter para seleccionar opcion")


    elif opcion == '2':
        os.system('clear')
        while True:
            os.system('clear')
            print("\n\t*******************")
            print("\t*  MENÚ TRAINERS  *")
            print("\t*******************\n")
            opcion = input("\nOpciones sobre los trainers:\n\t1: Registrar trainer\n\t2: Asignar ruta a trainer\n\t0: Salir\n: ")
            if opcion == '1':
                guardarTrainer()
            elif opcion == '2':
                rutaTreiner()
            elif opcion == '0':
                break
            else:
                print("*** Error - Opción incorrecta ***")
                input("Enter para seleccionar opcion")
    elif opcion == '3':
        guardarRuta()
        
    elif opcion == '4':
        os.system('clear')
        while True:
            os.system('clear')
            print("\n\t******************")
            print("\t*  MENÚ INFORMES  *")
            print("\t******************\n")
            opcion = input("\nlistado de informes:\n\t1: Listado de campers que se encuentran en estado inscritos\n\t2: Listar los campers que aprobaron el examen inicial\n\t3: Listar los entrenadores que se encuentran trabajando con campuslands\n\t4: Listar los estudiantes que cuentan con bajo rendimiento\n\t5: Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento\n\t6: Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos de la ruta\n\t0: Salir\n: ")
            if opcion == '1':
                campersInscritos()
            elif opcion == '2':
                mostrarNotasAspirante()
            elif opcion == '3':
                trainesCampus()
            elif opcion == '4':
                campersReprovados()
            elif opcion == '5':
                rutaCamperTrainer()
            elif opcion == '6':
                filtrosXRuta()
            elif opcion == '0':
                break
            else:
                print("*** Error - Opción incorrecta ***")
                input("Enter para seleccionar opcion")
    elif opcion == '0':
        break
    else:
        print("*** Error - Opción incorrecta ***")
        salir = input("Enter para seleccionar opcion")
    