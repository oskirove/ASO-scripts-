#Bloque en el cual generamos la palabra aleatoria
import requests
import time
url = "https://random-word-api.herokuapp.com/word?lang=es"
respuesta = requests.get(url)
palabra = respuesta.json()[0]
print(palabra)

#Texto introductorio.
print("Bienvenido al ahorcado\nTendrás 8 intentos para averiguar la palabra misteriosa")

cont = 0
lista_caracteres = []
#Creamos un bucle que se repita 8 veces y cuando este llegue a 8 se
#rompa y muestre que el jugador ha perdido
while cont < 8:
    caracter_usuario = input("Introduce un caracter ")
    lista_caracteres.append(caracter_usuario)
    print(lista_caracteres)

    #Mostramos por pantalla el número de intentos que lleva el usuario
    #y lo adaptamos para que use de manera correcta la gramática
    if cont == 0:
        print("Llevas",cont+1,"intento")
    elif cont >= 1:
        print("Llevas",cont+1,"intentos")

    #Si el usuario introduce más de un caracter el programa avisara
    #al usuario de que solo debe introducir un caracter
    if len(caracter_usuario) != 1:
        print("Por favor, introduce un único caracter.")

    print("Palabra: ", end="")
    #Este bucle recorre cada caracter de la palabra aleatoria
    #y comprueba si coincide con el caracter del usuario.
    for char in palabra:
        if char == caracter_usuario:
            #Utilizamos el end dentro del print para que el siguiente print
            #que aparece en el apartado else se continuen en la misma linea
            print(caracter_usuario,end="")
        #Si el texto contiene un espacio en blanco este se mostrará como tal
        #y no como un guión.
        elif char == " ":
            print(" ",end="")
        else:
            print("_", end="")
    cont+=1
    #Añadimos un salto de linea para mejorar la legibilidad y para que
    #no aparezca todo el texto en una misma linea
    print()

#Si el usuario llega al limite de sus intentos tras 1 segundo aparecera el siguiente print.
time.sleep(1)
if cont == 8:
    print("Lo sentimos, no has acertado.\nLa palabra misteriosa era",palabra,)