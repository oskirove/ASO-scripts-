import time
import random
# Bloque en el cual creamos la lista de palabras aleatorias.
# Como el código que se recomienda en la práctica para generar
# la palabra aleatoria funciona algo mal utilizamos lo siguiente
palabras = [
    "manzana", "naranja", "pera", "platano", "uva",
    "fresa", "kiwi", "pina", "sandia", "melon",
    "limon", "lima", "mango", "cereza", "frambuesa",
    "arandano", "papaya", "granada", "coco", "ciruela",
    "albaricoque", "higo", "melocoton", "ciruela", "fruta",
    "vegetal", "zanahoria", "brocoli", "coliflor", "espinaca",
    "calabacin", "pepino", "berenjena", "pimiento", "tomate",
    "cebolla", "ajo", "patata", "batata", "calabaza",
    "judia", "guisante", "maiz", "lechuga", "rucula",
    "col", "repollo", "apio", "puerro", "champinon",
    "seta", "cebollin", "perejil", "cilantro", "menta",
    "albahaca", "oregano", "tomillo", "romero", "salvia",
    "pimienta", "sal", "azucar", "harina", "arroz",
    "pasta", "pan", "cereal", "avena", "trigo",
    "leche", "yogur", "queso", "huevo", "carne",
    "pollo", "pavo", "cerdo", "ternera", "pescado",
    "salmon", "atun", "camaron", "langosta", "cangrejo",
    "anchoa", "aceituna", "aceite", "vinagre", "salsa",
    "mostaza", "mayonesa", "ketchup", "soja", "miel",
    "nuez", "almendra", "cacahuete", "avellana", "castana",
    "huevo", "leon", "tigre", "oso", "lobo",
    "zorro", "ciervo", "jirafa", "elefante", "rinoceronte",
    "hipopotamo", "leopardo", "pantera", "tortuga", "cocodrilo",
    "lagarto", "serpiente", "rana", "sapo", "tortuga",
    "pinguino", "aguila", "buho", "cuervo", "colibri",
    "flor", "arbol", "pasto", "roca", "montana",
    "rio", "lago", "mar", "ocean", "isla",
    "desierto", "selva", "jardin", "parque", "bosque",
    "casa", "edificio", "ciudad", "calle", "carretera",
    "puente", "tunel", "estacion", "aeropuerto", "puerto",
    "escuela", "universidad", "biblioteca", "museo", "teatro",
    "cine", "estadio", "iglesia", "templo", "mezquita",
    "sinagoga", "castillo", "torre", "fortaleza", "palacio",
    "hotel", "restaurante", "cafeteria", "tienda", "mercado",
    "centro", "plaza", "parque", "jardin", "zoologico",
    "atracciones", "playa", "montaña", "campamento", "senderismo",
    "nadar", "correr", "caminar", "bailar", "cantar",
    "pintar", "escribir", "leer", "jugar", "dormir",
    "comer", "beber", "reir", "llorar", "sonar"
]

# Seleccionamos una palabra aleatoria de la lista palabras.
palabra = random.choice(palabras)

# Definimos una lista donde se almacenaren los caracteres del usuario.
lista_caracteres = []


# Creamos un pequeño menú explicativo para el usuario
print()
print("¡Bienvenido al ahorcado!")
print()
time.sleep(1)
print("Tendrás", len(palabra), "intentos para adivinar la palabra oculta.")
print()
print(palabra)

# Hacemos que el código siguiente tarde en aparecer 2 segundos para que el 
# usuario lea el texto anterior
time.sleep(2)

cont = 0

# Creamos un contador que tenga tantos intentos como letras 
# tiene la palabra seleccionada en la variable <palabra>
while cont < len(palabra):

#solicitamos al usuario que introduzca un caracter
  caracter_usuario = input("Introduce un caracter: ")

# Aquí almacenamos los caracteres que introduce el usuario en una lista
  lista_caracteres.append(caracter_usuario)

# En este apartado definimos la variable palabra 
# como una cadena de caracteres vacia.

#creamos un for para que recorra cada letra de la palabra y si la letra aparece en la lista de caracteres 
# añada a la palabra oculta (que es una cadena de caracteres vacia) 
# la palabra que coincida en el espacio y un espacio en blanco y si no 
# que añada una barra baja (_)
  palabra_oculta = ""
  for letra in palabra:
    if letra in lista_caracteres:
      palabra_oculta += letra + " "
    else:
      palabra_oculta += "_ "

# Mostramos por pantalla lo definido en el bloque anterior y mostramos los intentos que lleva el jugador.
  print("Palabra: ", palabra_oculta)
  print("Llevas",cont+1,"intentos")

# Hacemos que si el usuario introduce más de dos caracteres no cuente el intento y lo avise.
  if len(caracter_usuario) != 1:
    print("No puedes introducir más de un caracter.Introdúcelo de nuevo.")
    cont-=1
  
  # En este apartado sustituimos los espacios en blanco de la palabra oculta para poder comprobar
  # la palabra oculta con la palabra seleccionada de la lista.
  if palabra_oculta.replace(" ", "") == palabra:
    print("¡Enhorabuena, has acertado la palabra oculta!")
    break

  cont+=1
  # Aquí añadimos al juego la función de que cuando el jugador termine todos sus
  # intentos el script lo avise de que ha perdido.
  if cont == len(palabra):
    print("Has perdido, la palabra era", palabra)