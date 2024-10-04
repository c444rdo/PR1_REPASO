print("Martínez Estrada Ricardo")
print(" ")

# Almacenar los precios en una lista
precios = [43, 57, 92, 20, 37, 5, 9]

# Ordenar la lista de precios en orden ascendente
precios.sort()

# Mostrar la lista ordenada
print ("Lista de precios en orden ascendente:", precios)
print ("")

print ("----------------------- DIFERENTE CÓDIGO -----------------------")
print (" ")

# Almacenar materias de un curso y desplegarlas en pantalla
materias = ["Pensamiento Matemático", "Español", "Inglés", "Química", "Civismo", "Francés"]
print("Materias del curso:", materias)

# Mostrar un mensaje por cada materia
for materia in materias:
    print("Estoy cursando", materia)

# Pedir la calificación de cada materia
calificaciones = []
for materia in materias:
    # Usar f-string para concatenar el mensaje
    calificacion = float(input(f"Ingrese la calificación para {materia}: "))
    calificaciones.append(calificacion)

# Mostrar las calificaciones
print("\nCalificaciones:")
for i, materia in enumerate(materias):
    print(f"En {materia} has obtenido {calificaciones[i]}")
print (" ")

print ("----------------------- DIFERENTE CÓDIGO -----------------------")
print (" ")

# Iniciar la lista para almacenar los números ganadores
numeros_ganadores = []

# Preguntar cuántos números quiere ingresar
cantidad = int(input("¿Cuántos números ganadores desea ingresar? "))

# Recoger los números ganadores
for i in range(cantidad):
    numero = int(input("Ingrese un número ganador: "))
    numeros_ganadores.append(numero)

# Ordenar la lista de números ganadores
numeros_ganadores.sort()

# Mostrar la lista ordenada
print("Números ganadores en orden ascendente:", numeros_ganadores)
