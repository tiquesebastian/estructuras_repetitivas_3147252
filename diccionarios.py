#diccionarios:

##son colecciones de datos
#cada elemento en un diccionario
#se pueden dividir en dos partes 
# ## 1.clave: el nombre del elemento 








pais = {
    "nombre": "colombia",
    "capital": "bogota",
    "idioma": "español",
    "poblacion":51,
    "superficie": 1141748,
    "moneda": "peso colombiano", 
    "ciudades": [
        "bogota",
        "medellin",
        "cali",
        "barrabquilla",
        "cartagena"
        
    ]
}

#acceder a propiedades:
print("capital de colombia:" , pais["capital"])
print("y se habla" , pais ["idioma"])
print("habitantes:" ,pais ["poblacion"])
print("y sus ciudades son:")
for ciudad in pais ["ciudades"]:
    print (ciudad)