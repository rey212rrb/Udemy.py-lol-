mi_set = set([1, 2, 3, 4, 5])
#print(mi_set)

otro_set = {1, 1, 2, 3, 4, 5, "Hola", (1,2)}
print(type(otro_set))
print(otro_set)

print("Hola" in otro_set)

unico_set = mi_set.union(otro_set)
print(unico_set)

unico_set.add((1,2))
print(unico_set)

unico_set.remove(2)
print(unico_set)

#No se pueden eliminar elementos que no esten en el set