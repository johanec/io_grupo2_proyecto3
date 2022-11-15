import string
import tomllib
from utils import *
from Algoritmo import *
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

def metodoSeleccion(poblacionFitness, config, algoritmo):
    metodo =  config["ag"]["selection_method"]
    numPadres = config["ag"]["num_parents"]  
    contraseñaCorrecta = config["passcode"]["correct_passcode"]     # 234AHLp91n
    if metodo == "ruleta" :
        padres = algoritmo.metodoRuleta(poblacionFitness, numPadres)  
    elif metodo == "elite": 
        padres = algoritmo.metodoElite(poblacionFitness,contraseñaCorrecta ,numPadres)
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

def metodoCruces(padres, config, algoritmo):
    metodo = config["ag"]["crossover_method"]
    rangoCruce = config["ag"]["crossover_rate"]             # 90
    if metodo == "one-point" :
        nuevaPoblacion = algoritmo.metodoOne_point(padres,rangoCruce)  
    elif metodo == "two-point": 
        nuevaPoblacion= algoritmo.metodoTwo_point(padres,rangoCruce)
    elif metodo == "uniform":
        nuevaPoblacion = algoritmo.metodoUniform(padres,rangoCruce)
    else:
        raise Exception ("El método no se encuentra")
    return nuevaPoblacion

def main():
    config = leerArchivo("config.toml")
    utils = Utils(config)
    tamañoPoblacion = config["ag"]["population_size"]               #10
    contraseñaCorrecta = config["passcode"]["correct_passcode"]     # 234AHLp91n
                    # 5
    poblacion = generarPoblacionInicial(tamañoPoblacion,len(contraseñaCorrecta))
    poblacionFitness = calcularFitness(poblacion, utils )
    algoritmo = Algoritmo()
    padres = metodoSeleccion(poblacionFitness,config, algoritmo)
    nuevaPoblacion = metodoCruces(padres, config, algoritmo)
    #nuevaPoblacion.extend(padres)
    print(nuevaPoblacion)
   
main()