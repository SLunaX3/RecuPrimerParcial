
def ordenarCaracteres(cadena):
    caracteres_ordenados = sorted(cadena)
    cadena_ordenada = ''.join(caracteres_ordenados)
    return cadena_ordenada

# main
cadena_original = "cadena"
cadena_ordenada = ordenarCaracteres(cadena_original)
print(cadena_ordenada)

