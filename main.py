import string
import tomllib
from utils import *
import math
from typing import List, Tuple, Iterator
import random
import sys

alfabeto = string.ascii_letters + string.digits          # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

def leerArchivo(nombre):
    with open (nombre , mode="rb") as fp:
            config = tomllib.load(fp)
    return config

def generarPoblacionInicial(tamañoPoblacion, largoContraseña):
    # Se crea una lista poblacion, la cual contiene listas cromosomas que son posibles soluciones
    poblacion = []
    for i in range(tamañoPoblacion):
        cromosomas = []
        for x in range(largoContraseña):
            cromosomas.append(random.choice(alfabeto))
        poblacion.append(cromosomas)
    return poblacion


def main():
    config = leerArchivo("config.toml")
    tamañoPoblacion = config["ag"]["population_size"]               #10
    contraseñaCorrecta = config["passcode"]["correct_passcode"]     # 234AHLp91n
    poblacion = generarPoblacionInicial(tamañoPoblacion,len(contraseñaCorrecta))
    utils = Utils(config)
    for cromosoma in poblacion:
        print(cromosoma)
        print (utils.calculate_fitness(cromosoma))
   
main()

