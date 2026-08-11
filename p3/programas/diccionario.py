#Clave unica

persona = {"nombre":"Rey",
           1:"rrb",
           "edad":25,
           "valores": {"v1":"pp",1:"lalo" },
           "clave2":["a","b","c","d"]}

resultado = persona["clave2"][3].upper()

persona["status"] = "resultado"

#print(persona)

#print(persona.keys())

#print(persona.values())

#print(persona.items())

#print(persona.get("nombre"))

for clave, valor in persona.items():
    print(f"{clave}: {valor}")