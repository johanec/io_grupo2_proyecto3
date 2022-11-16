from utils import*
import string
import random
import time
class Algoritmo:
    """ Clase encargada de contener el algoritmo genetico 
    """
    
    def __init__(self):
        self.seleccionPadres = []
        
    
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
    
    def metodoElite(self, poblacion, numPadres):
        tabla = []
        resultado = []
        padres = []
        for cromosomaFitness in poblacion:
            tabla.append([cromosomaFitness[1], cromosomaFitness[0]])
        tabla.sort()
        seleccion1 = tabla.pop(-1)
        seleccion2 = tabla.pop(-1)
        resultado.append(seleccion1[1])
        resultado.append(seleccion2[1])
        for cromosoma in tabla:
            padres.append( [cromosoma[1], cromosoma[0]])
        padresN = self.metodoRuleta(padres, numPadres-2)
        return resultado + padresN
    
    def metodoOne_point(self, padres):
        hijos = []
        viejos = []
        while len(padres) >= 2:
            padre1 = padres.pop(0)
            padre2 = padres.pop(0)
            hijo1 = []
            hijo2 = []
            punto = random.randint(0, len(padre1)-1)
            hijo1.extend(padre1[0:punto])
            hijo1.extend(padre2[punto:])
            hijo2.extend(padre2[punto:])
            hijo2.extend(padre1[0:punto])
            viejos.append(padre1)
            viejos.append(padre2)
            hijos.append(hijo1)
            hijos.append(hijo2)
        
        return hijos + viejos + padres

    def metodoTwo_point(self, padres):
        hijos = []
        viejos = []
        while len(padres) >= 2:
            padre1 = padres.pop(0)
            padre2 = padres.pop(0)
            hijo1 = []
            hijo2 = []
            punto1 = random.randint(0, len(padre1)//2-1)
            punto2 = random.randint(punto1, len(padre1)-1)
            #hijo1
            hijo1.extend(padre1[0:punto1])
            hijo1.extend(padre2[punto1:punto2])
            hijo1.extend(padre1[punto2:])
            #hijo2
            hijo2.extend(padre2[0:punto1])
            hijo2.extend(padre1[punto1:punto2])
            hijo2.extend(padre2[punto2:])
            viejos.append(padre1)
            viejos.append(padre2)
            hijos.append(hijo1)
            hijos.append(hijo2)

        return hijos + viejos + padres

    def metodoUniform(self, padres):
        hijos = []
        viejos = []
        while len(padres) > 2: 
            hijo1 = []
            hijo2 = []
            padre1 = padres.pop(0)
            padre2 = padres.pop(0)
            for index in range(len(padre1)):
                cambiar = random.randint(0, 100)
                if cambiar < 50:
                    hijo1.append(padre1[index])
                    hijo2.append(padre2[index])
                else:
                   hijo2.append(padre1[index])  
                   hijo1.append(padre2[index])  
            hijos.append(hijo1)
            hijos.append(hijo2)
            viejos.append(padre1)
            viejos.append(padre2)
        
        return hijos + viejos + padres

    def mutacion(self, poblacion,rangoMutacion,contraseña):
        for i in range(len(poblacion)):
           if random.randint(0,100) > float(rangoMutacion)*100:
             continue
           else:
             posicionMutada = random.randint(0,len(contraseña)-1)
             mutacion = random.choice(string.ascii_letters + string.digits)
             poblacion[i][posicionMutada] = mutacion
        return poblacion
    
  
