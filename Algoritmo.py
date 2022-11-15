from utils import*
import random
import time
class Algoritmo:
    """ Clase encargada de contener el algoritmo genetico 
    """
    
    def __init__(self):
        self.contraseña = []
        
    
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

    def metodoRuleta(self,poblacionFitness, numPadres):
        suma = 0
        tabla = []
        isRandom = False
        seleccion = []
        for cromosomaFitness in poblacionFitness:
            suma += cromosomaFitness[1]

        
        for cromosomaFitness in poblacionFitness:
            if suma !=0:
                tabla.append([(cromosomaFitness[1]/suma)*100, cromosomaFitness[0]])
            else:
                isRandom = True
        
        if isRandom:
            for i in range(numPadres):
                aleatorio = poblacionFitness.pop(random.randint(0, len(poblacionFitness)-1))
                seleccion.append(aleatorio[0])
        else: 
            tabla.sort()
            sumatoria = 0
            ruleta = []
            for registros in tabla:
                registros[0] = registros[0]  + sumatoria
                sumatoria = registros[0]
                ruleta.append(registros)
            for i in range(numPadres):
                aleatorio = random.randint(0, 100)
                isEncontrado = False
                for elemento in ruleta:
                    if aleatorio <= elemento[0]: 
                        seleccion.append(elemento[1])
                        ruleta.remove(elemento)
                        isEncontrado = True
                        break
                if (isEncontrado == False):
                    aleatorio = ruleta.pop(random.randint(0, len(ruleta)-1))
                    seleccion.append(aleatorio[1])
        return seleccion
    
    def metodoRanking(self, poblacionFitness, numPadres ):
        tabla = []
        resultado = []
        for cromosomaFitness in poblacionFitness:
            tabla.append([cromosomaFitness[1], cromosomaFitness[0]])
        tabla.sort()
        for i in range (numPadres):  
            elemento = tabla.pop(-1)
            resultado.append(elemento[1])
        return resultado
    
    def select_parents(self, fitness_scores, numeroParientes):
        parents_list = []
        for cromosomas in sorted(fitness_scores, key=lambda x: x[1], reverse = True)[:numeroParientes]: #primeros 4 ":numeroParientes"
          parents_list.append(cromosomas[0])
        return(parents_list) #retorna lista con 5 mejores cromosomas
    
    def metodoElite(self, poblacion, contraseñaCorrecta, numPadres):
        for caracter in contraseñaCorrecta:
            self.contraseña.append(caracter)
        fitness_scores = poblacion
        parents = self.select_parents(fitness_scores, numPadres)
        return parents
    
    def metodoOne_point(self, padres,rangoCruce):
        print("One_point")
        return []
    def metodoTwo_point(self, padres,rangoCruce):
        print("Two_point")
        return[]
    def metodoUniform(self, padres,rangoCruce):
        print("uniforme")
        return[]

    def mutacion(self, poblacion, rangoMutacion):
        return []    
    
  
