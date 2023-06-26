
def reemplazarCaracteres(cadena, caracter_a_reemplazar, nuevo_caracter):
    cantidad_reemplazos = cadena.count(caracter_a_reemplazar)
    cadena_modificada = cadena.replace(caracter_a_reemplazar, nuevo_caracter)
    return cantidad_reemplazos, cadena_modificada

# main
cadena_original = "Cadena"
caracter_a_reemplazar = "a"
nuevo_caracter = "e"

cantidad_reemplazos, cadena_modificada = reemplazarCaracteres(cadena_original, caracter_a_reemplazar, nuevo_caracter)
print("Cantidad de reemplazos:", cantidad_reemplazos)
print("Cadena modificada:", cadena_modificada)



