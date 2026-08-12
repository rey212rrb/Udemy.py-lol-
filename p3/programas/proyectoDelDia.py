#1. Ingresar texto y pasarlo a minusculas
texto_ingresado = input("Ingrese un texto: ").lower()

#print(texto_ingresado)

#2. Declarar una lista en la cual almacenaremos las letras ingresadas por el usuario y las convertimos en minusculas
letras = []
letra1 = input("Ingrese la letra 1: ")
letras.append(letra1.lower())
letra2 = input("Ingrese la letra 2: ")
letras.append(letra2.lower())
letra3 = input("Ingrese la letra 3: ")
letras.append(letra3.lower())

#print(letras)

#3. Verificamos cuantas veces aparece cada letra en el texto ingresado
print(f"La letra {letra1} aparece: {texto_ingresado.count(letras[0])} veces.")
print(f"La letra {letra2} aparece: {texto_ingresado.count(letras[1])} veces.")
print(f"La letra {letra3} aparece: {texto_ingresado.count(letras[2])} veces.")

#4. Convertimos el texto en lista y contamos los elementos o palabras
palabras = len(texto_ingresado.split())
print(f"En el texto hay {palabras} palabras.")

#5. Mostramos primer letra y ultima del texto
print(f"La primer letra es {texto_ingresado[0]}")
print(f"La ultima letra es {texto_ingresado[-1]}")


#6. Mostramos el texto al reves
texto_inverso = texto_ingresado[::-1]
print(texto_inverso)

#7. Verificamos si extiste la palabra python en el texto ingresado
print("python" in texto_ingresado)

veredicto = {
    False : "No se encontro",
    True : "Se encontro"
}