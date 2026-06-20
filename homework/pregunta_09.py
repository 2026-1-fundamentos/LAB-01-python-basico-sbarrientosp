"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_09():
    conteo = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            cols = linea.strip().split("\t")
            for par in cols[4].split(","):
                k = par.split(":")[0]
                conteo[k] = conteo.get(k, 0) + 1
    return dict(sorted(conteo.items()))