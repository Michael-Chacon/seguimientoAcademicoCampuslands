import os
from validaciones import romperCiclo
from conexiones import guardar as guardarTrainer, conexion as con

#immportar los jsons
rutas = con('rutas')
horarios = con('horarios')
rutaTrainers = con('rutaTrainers')
trainers = con('trainers')

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
       
       
def mostrarInfoBasica():
    print(40 * "-")
    print("| ID \t| NOMBRE \t|")
    print(40 * "-")
    for llave, valor in trainers.items():
       
        print(f"| {llave} \t| {valor['nombreT']} \t|")
        print(40 * "-")


def guardarRutaTrainer():
    bandera = True
    while bandera:
        mostrarInfoBasica()
        idTrainer = input('Escriba el id del treiner al que le va a asignar la ruta: ')
        if idTrainer not in  trainers:
            print(f"\nError - el id {idTrainer} no esta asignado a ningun trainer\n")
        else:
            print(f"\nSeleccione la ruta que le va a asignar al trainer {trainers[idTrainer]['nombreT']}:")
            for llave, valor in rutas.items():
                print(f"\t{llave}: {valor['nombreR']}")
            idRuta = input(": ")
            if idRuta not in rutas:
                print(f"Error - el id {idRuta} no está asignado a ninguna ruta")
            else:
                print("\nSelecione el horario en que el trainer dictara la ruta:")
                for llave, valor in horarios.items():
                    print(f"\t{llave}: {valor['hora']}")
                hora = input(": ")
        bandera = romperCiclo('otra ruta a otro trainer')