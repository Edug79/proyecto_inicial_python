import csv
import random

# primera opcion 

def leer_palabra_secreta(csvfilename):

    archivo = 'palabras.csv'
    with open(archivo) as f:
        palabras = list(f)
        
    palabra_secreta = random.choice(palabras)

    palabra_secreta = palabra_secreta.strip()

    return(palabra_secreta)

# segunda alternativa

def leer_palabra_secreta(csvfilename):

    archivo = 'palabras.csv'
    with open(archivo) as f:
        palabras = list(f)
        
    palabra_secreta = random.choice(palabras)

    palabra_secreta = palabra_secreta.replace("\n", "")

    return(palabra_secreta)

# tercer alternativa

def leer_palabra_secreta(csvfilename):

    archivo = 'palabras.csv'
    with open(archivo) as f:
        palabras = list(f)
        palabras = [x.strip() for x in palabras]

    palabra_secreta = random.choice(palabras)

    return(palabra_secreta)


# cuarta alternativa

