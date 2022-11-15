from utils import*
import random
import time


class Algoritmo:
    """ Clase encargada de contener el algoritmo genetico 
    """
    
    def __init__(self, config, poblacion):
        self.config = config
        self.poblacion = poblacion
        self.contraseña = []
        
    def fitness(self, poblacion):
        resultados = []
        for cromosoma in poblacion: #itera por cada lista cromosoma que se encuentran en la lista poblacion 
            valor = Utils.calculate_fitness(cromosoma)
            resultadoTemporal = [cromosoma,valor] # lista que contiene el cromosoma en que se encuentra el for y su puntuacion
            resultados.append(resultadoTemporal) # lista que contiene todas las listas resultado 
        return resultados
    
    def select_parents(self, fitness_scores):
        parents_list = []
        numeroParientes = self.config["ag"]["num_parents"] 
        for cromosomas in sorted(fitness_scores, key=lambda x: x[1], reverse = True)[:numeroParientes]: #primeros 4 ":numeroParientes"
          parents_list.append(cromosomas[0])
        return(parents_list) #retorna lista con 4 mejores cromosomas
    
    # breeding logic
    def breed(self, parent1, parent2):
        contraseñaCorrecta = self.contraseña
        child = []
        parent1 = parents[0]
        parent2 = parents[1]
        geneA = int(random.random() * len(contraseñaCorrecta))
        geneB = int(random.random() * len(contraseñaCorrecta))
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)
        for i in range(0,len(contraseñaCorrecta)):
            if (i < startGene) or (i > endGene):
             child.append(parent1[i])
            else:
             child.append(parent2[i])
        return child

    # breeding and elitism
    def create_children(self, parents_pool):
        tamañoElite = self.config["ag"]["elite_size"]     
        children = []
        num_new_children = len(self.poblacion) - tamañoElite

        for i in range(0,tamañoElite):
            children.append(parents_pool[i])

        for i in range(0,num_new_children):
            parent1 = parents_pool[int(random.random() * len(parents_pool))]
            parent2 = parents_pool[int(random.random() * len(parents_pool))]
            children.append(self.breed(parent1,parent2))
        return children

    def mutation(self, children_set):
        contraseñaCorrecta = self.contraseña
        for i in range(len(children_set)):
            if random.random() > 0.1:
                continue
        else:
            mutated_position = int(random.random() * len(contraseñaCorrecta))
            mutation = int(round(random.uniform(0,9+1),0))
            children_set[i][mutated_position] = mutation
        return children_set

    def metodoRuleta(self, fitness):
        return []    
    
    def metodoRanking(self, fitness):
        return []
    
    def metodoElite(self, poblacion):
        contraseñaCorrecta = self.config["passcode"]["correct_passcode"]
        for caracter in contraseñaCorrecta:
            self.contraseña.append(int(caracter))
        success = []
        generations = 0
        t0 = time.time()
        while True:
            fitness_scores = self.fitness(poblacion)
            success.append(max([i[1] for i in fitness_scores]))
            if max([i[1] for i in fitness_scores]) == len(contraseñaCorrecta):
                print("Cracked in {} generations, and {} seconds! \nSecret passcode = {} \nDiscovered passcode = {}".format(generations,time.time() - t0,contraseña,[i[0] for i in fitness_scores if i[1] == len(contraseñaCorrecta)][0]))
                break #condicion de parada
            parents = self.select_parents(fitness_scores)
            children = self.create_children(parents)
            poblacion = self.mutation(children)
            generations += 1
        return 
    

    def metodoSeleccion(self,fitness):
        metodo = self.config["ag"]["selection_method"]
        if metodo == "ruleta" :
            self.metodoRuleta(fitness)  
        elif metodo == "elite": 
            self.metodoElite(self.poblacion)
        elif metodo == "ranking":
            self.metodoRanking(fitness)
        else:
             raise Exception ("El método no se encuentra")
  
  
    


