# colección de países
paises = [
    {
        "nombre": "colombia",
        "capital": "bogota",
        "moneda": "peso colombiano",
        "ciudades": [
            {
                "nombre": "bogota",
                "poblacion": 8.2,
                "fundacion": 1538,
            },
            {
                "nombre": "medellin",
                "poblacion": 2.6,
                "fundacion": 1616,
            },
            {
                "nombre": "cali",
                "poblacion": 2.2,
                "fundacion": 1536,
            }
        ]
    },
    {
        "nombre": "peru",
        "capital": "lima",
        "moneda": "sol",
        "ciudades": [
            {
                "nombre": "lima",
                "poblacion": 9.6,
                "fundacion": 1535,
            },
            {
                "nombre": "cozcu",
                "poblacion": 12.5,
                "fundacion": 1438,
            },
        ]
    },
    {
        "nombre": "inglaterra",
        "capital": "londres",
        "moneda": "libra",
        "ciudades": [
            {
                "nombre": "londres",
                "poblacion": 9.0,
                "fundacion": 47,
            },
            {
                "nombre": "manchester",
                "poblacion": 2.5,
                "fundacion": 1890,
            },
        ]
    },
    {
        "nombre": "españa",
        "capital": "madrid",
        "moneda": "euro",
        "ciudades": [
            {
                "nombre": "madrid",
                "poblacion": 3.2,
                "fundacion": 865,
            },
            {
                "nombre": "barcelona",
                "poblacion": 1.6,
                "fundacion": 1249,
            },
        ]
    },
]

# iterar cada país
print("-------------------")
print("recorrido de países")
print("-------------------")


for pais in paises: 
    print("Nombre:", pais["nombre"]) 
    print("Capital:", pais["capital"]) 
    print("Ciudades principales de", pais["nombre"]) 
    for ciudad in pais["ciudades"]: 
        print(f"- {ciudad['nombre']}: Población: {ciudad['poblacion']} millones, Fundación: {ciudad['fundacion']}")
    print("----------------------")