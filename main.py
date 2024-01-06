from camper import guardar as guardarCamper, mostrarNotasAspirante as relacion
from trainer import guardar as guardarTrainer
from notas import guardarNotasPrueba as prueba
from conexiones import conexion as con, guardar
from utils import mostrarInfoBasica as listarInfo


campers = con('campers')
trainers = con('trainers')
rutas = con('rutas')
salas = con('salas')
# pruebas = con('pruebas')
rutaTrainer = {}
matriculas = {}


# campers[1] = {'nombreC': 'Alexis',
#                 'apellidos': 'Chacón',
#                 'acudiente': 'Maria Chacón',
#                 'direccion': 'Floridablanca',
#                 'telefono': {'celular': [], 'fijo': []},
#                 'estado': 'inscrito'
#             }
# guardar('campers', campers)

# trainer[1] = {'nombreT': 'Miguel'}
rutas[1] = {'nombreRuta': 'Java'}
salas[1] = {'sala': 'Sputnik'}
# pruebas[2] = {'teorico': 0, 'practico': 0, 'promedio': 0}
rutaTrainer[1] = {'idRutaT': 1, 'horario': '6-9am'}
matriculas[1] = {'idTreinerM': 1, 'idRutaM': 1, 'idSalaM': 1, 'fechaInico': '11-27-2023', 'fechaFin': '06-27-2024'}

# guardarCamper(campers)
listarInfo(campers, 'nombreC')
# relacion(campers)

# # guardarTrainer(trainers)
# listarInfo(trainers, 'nombreT')

# prueba(campers)

# print(trainers)
# print(pruebas)