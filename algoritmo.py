from utils import*
import random
import time

parents = [5]

class Algoritmo:
    """ Clase encargada de contener el algoritmo genetico 
    """
    
    def __init__(self, config, poblacion):
        self.config = config
        self.poblacion = poblacion
        self.contraseña = []
        
    def fitness(self, poblacion):
        resultados = []
        utils = Utils(self.config)
        for cromosoma in poblacion: #itera por cada lista cromosoma que se encuentran en la lista poblacion 
            valor = utils.calculate_fitness(cromosoma)
            resultadoTemporal = [cromosoma,valor] # lista que contiene el cromosoma en que se encuentra el for y su puntuacion
            resultados.append(resultadoTemporal) # lista que contiene todas las listas resultado 
        return resultados
    
    def select_parents(self, fitness_scores):
        parents_list = []
        numeroParientes = self.config["ag"]["num_parents"] 
        for cromosomas in sorted(fitness_scores, key=lambda x: x[1], reverse = True)[:numeroParientes]: #primeros 4 ":numeroParientes"
          parents_list.append(cromosomas[0])
        return(parents_list) #retorna lista con 5 mejores cromosomas
    
    
    def metodoRuleta(self):
        return []    
    
   
    def metodoRanking(self):
        print("fitness Ranking")
        return []
    
    def metodoElite(self):
        contraseñaCorrecta = self.config["passcode"]["correct_passcode"]
        for caracter in contraseñaCorrecta:
            self.contraseña.append(caracter)
        fitness_scores = self.fitness(self.poblacion)
        parents = self.select_parents(fitness_scores)
        print(parents)
        return parents
    
     
    def metodoSeleccion(self):
        metodo = self.config["ag"]["selection_method"]
        
        if metodo == "ruleta" :
            self.metodoRuleta()  
        elif metodo == "elite": 
            self.metodoElite()
        elif metodo == "ranking":
            self.metodoRanking()
        else:
             raise Exception ("El método no se encuentra")
  
  
    


