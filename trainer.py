import os
from validaciones import romperCiclo
from conexiones import guardar as guardarTrainer


def guardar(trainers):
    bandera = True
    while bandera:
        os.system('clear')
        id = input('Ingrese el id del trainer: ')
        if id in trainers:
            print(f"\n*** Error - el trainer {trainers[id]['nombreT']} ya tiene asigando el id {id} ***\n")
        else:
            nombre = input('Ingrese el nombre del trainer: ')
            trainers[id] = {'nombreT': nombre}
            guardarTrainer('trainers', trainers)
            print('\n--- Trainer registrado con éxito ---\n')
        bandera = romperCiclo('un nuevo trainer')
