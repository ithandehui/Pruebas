if(True):
    print("This line will be printed.")
euros=14

print("la variable euros es de tipo " + str (type(euros)))

euros2=14.25

print("la variable euros2 es de tipo " + str (type(euros2)))

euros3= "Tengo 6 euros"

print("la variable euros3 es de tipo " + str (type(euros3)))

print(euros3)

euros4= float(14)

print("la variable euros4 es de tipo " + str (type(euros4)))

titulo="hola'hola'"
titulo2='hola'
print(titulo)
print(titulo2)
print(titulo+titulo2)

variaslineas="""linea 1
linea 2
linea 3"""

print(variaslineas)

print(variaslineas+" " +titulo)

test=True

print(test)

print("------------------------------------------------------------------------------------------")

array=[1,2,3,4,5]

print (array)

array2=["uno","dos","tres"]

print(array2)

print(variaslineas + " " + str(array))

print("------------------------------------------------------------------------------------------")

algo = input ("Escribe algo")

print (algo)

print(str.upper(algo))
str.lower(algo)

print("------------------------------------------------------------------------------------------")
texto = input ("texto en mayusculas")

if (texto.isupper()):
    print(texto)

print("me gusta lilis")