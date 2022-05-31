# Declarar una variable
calificacion = input("Intrduce tu calificación de la AZ-900: ")
calificacion = int(calificacion)

# Preguntar si la calificación es menor a 700
if calificacion < 700 :
    print("Vess, por no estudiar") # Si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("MIENTESSSSS!!! No puedes sacar más de mil")
else :
    print("Felicidades, pasa por tu certificado") # Si no, imprime esto


# Verificador de la mayoría de edad
edad = int(input("Introduce tu edad "))

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abulitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del timepo")
else :
    print("No puedes llevarte esos cigarros")
