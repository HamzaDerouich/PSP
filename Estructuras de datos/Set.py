"""
    Un set es una colección desordenada de elementos únicos. No permite duplicados y no mantiene el orden de los elementos.
"""

array_set = {1,2,3,4,5}
print(array_set)

array_set.add(1) #Metodo que añade datos al set 
array_set.add(6)

print(array_set)

array_set_dos = {7,8,9,10,11}
union = array_set.union(array_set_dos)

print(union)
