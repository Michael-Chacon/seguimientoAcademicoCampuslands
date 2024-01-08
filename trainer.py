import os
from validaciones import romperCiclo
from conexiones import guardar as guardarEnJson, conexion as con

#immportar los jsons
rutas = con('rutas')
horarios = con('horarios')
rutaTrainers = con('rutaTrainers')
trainers = con('trainers')


def guardar():
    bandera = True
    while bandera:
        os.system('clear')
        id = input('Ingrese el id del trainer: ')
        if id in trainers:
            print(f"\n*** Error - el trainer {trainers[id]['nombreT']} ya tiene asigando el id {id} ***\n")
        else:
            nombre = input('Ingrese el nombre del trainer: ')
            apellidos = input('Ingrese el apellido del trainer: ')
            trainers[id] = {'nombreT': nombre, 'apellidos': apellidos}
            guardarEnJson('trainers', trainers)
            rutaTrainers[id] = {'idHorario': [], 'idRutaRT': []}
            guardarEnJson('rutaTrainers', rutaTrainers)
            print('\n--- Trainer registrado con éxito ---\n')
        bandera = romperCiclo('otro treiner')
       

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
            if len(rutaTrainers[idTrainer]['idHorario']) == 4:
                print(f"\n*** Alerta - el trainer {trainers[idTrainer]['nombreT']} no tiene horarios disponibles ***\n")
                bandera = False
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
                        if rutaTrainers[idTrainer]['idHorario'].count(llave) == 0:
                            print(f"\t{llave}: {valor['hora']}")
                    hora = input(": ")
                    if hora not in horarios:
                        print("\nError- el horario seleccionado no existe\n")
                    else:
                        rutaTrainers[idTrainer]['idHorario'].append(hora)
                        rutaTrainers[idTrainer]['idRutaRT'].append(idRuta)
                        guardarEnJson('rutaTrainers', rutaTrainers)
        bandera = romperCiclo('otra ruta a otro trainer')


def trainerRutasHorarios(id):
    listaRutas = []
    rutaTrainers = con('rutaTrainers')
    print("\tID") # onden en el que se muestran los datos: id - id de la ruta - id del horario
    for i in range(0,len(rutaTrainers[id]['idHorario'])):
        print(f"\t{i}: {buscarDatosRuta(rutaTrainers[id]['idRutaRT'][i])} | {buscarDatosHora(rutaTrainers[id]['idHorario'][i])}")
        arrayTemporal = [i+1, rutaTrainers[id]['idRutaRT'][i], rutaTrainers[id]['idHorario'][i]]
        listaRutas.append(arrayTemporal)
    return listaRutas


def buscarDatosRuta(idRuta):
    return rutas[idRuta]['nombreR']


def buscarDatosHora(idHorario):
    
    return horarios[idHorario]['hora']
