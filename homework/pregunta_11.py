"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_11():
    sumas = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            cols = linea.strip().split("\t")
            num = int(cols[1])
            for letra in cols[3].split(","):
                sumas[letra] = sumas.get(letra, 0) + num
    return dict(sorted(sumas.items()))