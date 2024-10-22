curso = {
   "nombre": "peluquería 1",
   "estudiantes": 15,
   "profesores": ["Teresita"]
}
#curso es un diccionario con 3 llaves 

print(curso["estudiantes"])
#accedemos a la notación de la llave con los corchetes

curso["estudiantes"]+=1

print(curso["estudiantes"])

curso["profesores"].append("Juan")

print(curso)
