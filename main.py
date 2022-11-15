import string
import tomllib
from utils import *
import math
from typing import List, Tuple, Iterator
import random
import sys

alfabeto = string.ascii_letters + string.digits             # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

def leerArchivo(nombre):
    with open (nombre , mode="rb") as fp:
            config = tomllib.load(fp)
    
    return config

def generarPoblacionInicial(lenPoblacion, lenContraseña):
    # Se crea una lista poblacion, la cual contiene listas cromosomas que son posibles soluciones
    poblacion = []
    for i in range(lenPoblacion):
        cromosomas = []
        for x in range(lenContraseña):
            cromosomas.append(random.choice(alfabeto))
        poblacion.append(cromosomas)
    
    return poblacion


def main():
    poblacion = generarPoblacionInicial(10,10)
    config = leerArchivo("config.toml")
    fitness = Utils(config)
    for i in poblacion:
        print(i)
        print (fitness.calculate_fitness(i))
   


    

main()