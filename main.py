from camper import mostraCampers, guardar as guardarCamper
from notas import notasPrueba as prueba
from conexiones import conexion as con, guardar

campers = con('campers')
trainer = {}
rutas = {}
salas = {}
pruebas = con('pruebas')
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

trainer[1] = {'nombreT': 'Miguel'}
rutas[1] = {'nombreRuta': 'Java'}
salas[1] = {'sala': 'Sputnik'}
# pruebas[2] = {'teorico': 0, 'practico': 0, 'promedio': 0}
rutaTrainer[1] = {'idRutaT': 1, 'horario': '6-9am'}
matriculas[1] = {'idTreinerM': 1, 'idRutaM': 1, 'idSalaM': 1, 'fechaInico': '11-27-2023', 'fechaFin': '06-27-2024'}

guardarCamper(campers)
mostraCampers(campers)

# prueba(campers, pruebas)

print(campers)
print(pruebas)