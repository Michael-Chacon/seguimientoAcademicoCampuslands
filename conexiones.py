import json

def conexion(archivo):
    data = None
    with open(f"dataBase/{archivo}.json", "r") as f:
        data =  json.loads(f.read())
    return data


def guardar(archivo, diccionario):
    with open(f"dataBase/{archivo}.json", "w+") as f:
        f.write(json.dumps(diccionario, indent=3))