from rutas import guardarRuta
from conexiones import conexion as con, guardar
from utils import mostrarInfoBasica as listarInfo
from notas import guardarNotasPrueba as prueba, matricularCamper, filtro
from camper import guardar as guardarCamper #, mostrarNotasAspirante as relacion
from trainer import guardar as guardarTrainer, guardarRutaTrainer as rutaTreiner


campers = con('campers')
trainers = con('trainers')
rutas = con('rutas')
salas = con('salas')


# guardarCamper()
# guardarTrainer()
# listarInfo(trainers, 'nombreT')
# relacion(campers)
# rutaTreiner()
# listarInfo(trainers, 'nombreT')
# guardarRuta()
# prueba(campers)
# matricularCamper()
filtro()
# print(trainers)
# print(pruebas)