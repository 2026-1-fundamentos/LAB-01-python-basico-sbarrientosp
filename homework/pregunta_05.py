"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_05():
    vals = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            cols = linea.strip().split("\t")
            letra, num = cols[0], int(cols[1])
            if letra not in vals:
                vals[letra] = []
            vals[letra].append(num)
    return [(k, max(v), min(v)) for k, v in sorted(vals.items())]