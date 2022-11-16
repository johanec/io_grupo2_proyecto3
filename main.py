import string
import tomllib
from utils import *
from algoritmo import *
import random

alfabeto = string.ascii_letters + string.digits   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# Función para leer y poder utilizar los datos del archivo confi.toml
def leerArchivo(nombre):
    with open (nombre , mode="rb") as fp:
            config = tomllib.load(fp)
    return config


 # Se crea una lista población, la cual contiene listas cromosomas que son posibles soluciones
def generarPoblacionInicial(tamañoPoblacion, largoContraseña):
    poblacion = []
    for i in range(tamañoPoblacion):
        cromosomas = []
        for x in range(largoContraseña):
            cromosomas.append(random.choice(alfabeto)) # agrega caracteres a la lista cromosoma
        poblacion.append(cromosomas) # agrega cromosomas a la lista poblacion
    return poblacion

 # Función que valida el tipo de metodo de selección a utilizar
def metodoSeleccion(cromosomasResultados, config, algoritmo):
    metodo =  config["ag"]["selection_method"]
    numPadres = config["ag"]["num_parents"] 
    tamañoElite = config["ag"]["elite_size"]  
    if metodo == "ruleta" :
        padres = algoritmo.metodoRuleta(cromosomasResultados, numPadres)  
    elif metodo == "elite": 
        padres = algoritmo.metodoElite(cromosomasResultados ,numPadres, tamañoElite)
    elif metodo == "ranking":
        padres = algoritmo.metodoRanking(cromosomasResultados,numPadres)
    else:
        raise Exception ("El método no se encuentra")
    return padres 

 # Función que agrega a una lista todos los cromosomas de la población con su respectivo valor de fitness
def calcularFitness(poblacion, utils):
    resultado = []
    for cromosoma in poblacion:
        resultado.append([cromosoma, utils.calculate_fitness(cromosoma)]) # agrega un cromosoma y su fitness a la lista resultado
    return  resultado 

# Función que valida el tipo de crossover a utilizar
def metodoCruces(poblacion, config, algoritmo):
    metodo = config["ag"]["crossover_method"]   # "uniform", "one-point", "two-point"
    rangoCruce = config["ag"]["crossover_rate"] # 90      
    total = len(poblacion)
    padres = []
    for i in range( total): 
        if i/total < rangoCruce:
            padres.append(poblacion.pop(random.randint(0, len(poblacion)-1)))

    if metodo == "one-point" :
        nuevaPoblacion = algoritmo.metodoOne_point(padres)  
    elif metodo == "two-point": 
        nuevaPoblacion= algoritmo.metodoTwo_point(padres)
    elif metodo == "uniform":
        nuevaPoblacion = algoritmo.metodoUniform(padres)
    else:
        raise Exception ("El método no se encuentra")
    return nuevaPoblacion + poblacion


# Funcion main que crea objetos, llama funciones y metodos necesarios para el desarrollo del algoritmo genetico
def main():
    config = leerArchivo("config.toml")
    utils = Utils(config)
    tamañoPoblacion = config["ag"]["population_size"]  # 10
    metodo = config["ag"]["crossover_method"]           # "uniform", "one-point", "two-point"
    contraseñaCorrecta = config["passcode"]["correct_passcode"]     # 234AHLp91n
    rangoMutacion = config["ag"]["mutation_rate"]               # 0.5   
    tamañoElite = config["ag"]["elite_size"]           # 2
    poblacion = generarPoblacionInicial(tamañoPoblacion,len(contraseñaCorrecta))
    algoritmo = Algoritmo()
    gen = 0
    while utils.isContraseña(poblacion) == False:
        cromosomasResultados = calcularFitness(poblacion, utils )
        padres = metodoSeleccion(cromosomasResultados,config, algoritmo)
        nuevaPoblacion = metodoCruces(padres, config, algoritmo)
        algoritmo.mutacion(nuevaPoblacion, rangoMutacion,contraseñaCorrecta)
        if metodo == "elite":
            for i in range (tamañoElite):
                nuevaPoblacion.append(padres[i])

        poblacion = nuevaPoblacion  
        gen += 1
        
    print("La contraseña fue encontrada en la generación: " + str(gen))
    
main()
