import string
import tomllib
from utils import *
from algoritmo import *
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

def metodoSeleccion(poblacionFitness, metodo, algoritmo, numPadres):
    if metodo == "ruleta" :
        padres = algoritmo.metodoRuleta(poblacionFitness, numPadres)  
    elif metodo == "elite": 
        padres = algoritmo.metodoElite(poblacionFitness,numPadres)
    elif metodo == "ranking":
        padres = algoritmo.metodoRanking(poblacionFitness,numPadres)
    else:
        raise Exception ("El método no se encuentra")
    return padres 
def calcularFitness(poblacion, utils):
    resultado = []
    for cromosoma in poblacion:
        resultado.append([cromosoma, utils.calculate_fitness(cromosoma)]) 
    return  resultado 
        

def main():
    config = leerArchivo("config.toml")
    utils = Utils(config)
    tamañoPoblacion = config["ag"]["population_size"]               #10
    contraseñaCorrecta = config["passcode"]["correct_passcode"]     # 234AHLp91n
    numeroPadres = config["ag"]["num_parents"]                   # 5
    poblacion = generarPoblacionInicial(tamañoPoblacion,len(contraseñaCorrecta))
    poblacionFitness = calcularFitness(poblacion, utils )
    metodo =  config["ag"]["selection_method"]
    algoritmo = Algoritmo()
    print(metodoSeleccion(poblacionFitness, metodo, algoritmo, numeroPadres))
    
   
main()