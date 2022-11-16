from utils import*
import string
import random

# Clase encargada de contener el algoritmo genetico 
class Algoritmo:
        
    def __init__(self):
        pass
  
    # Método encargado de mutar caracteres de los cromosomas 
    def mutacion(self, poblacion,rangoMutacion,contraseña):
        for i in range(len(poblacion)):
           if random.randint(0,100) > float(rangoMutacion)*100:
             continue
           else:
             posicionMutada = random.randint(0,len(contraseña)-1) # selecciona posicion de un caracter del cromosoma a mutar
             mutacion = random.choice(string.ascii_letters + string.digits) # digito o numero random para mutar
             poblacion[i][posicionMutada] = mutacion # se realiza la mutacion
        return poblacion


    # Método encargado de realizar el metodo de seleccion ruleta
    def metodoRuleta(self,cromosomasResultados, numPadres):
        suma = 0
        tabla = []
        isRandom = False
        seleccion = []
        for cromosoma in cromosomasResultados:
            suma += cromosoma[1]

        for cromosoma in cromosomasResultados:
            if suma !=0:
                tabla.append([(cromosoma[1]/suma)*100, cromosoma[0]])
            else:
                isRandom = True
        
        if isRandom:
            for i in range(numPadres):
                aleatorio = cromosomasResultados.pop(random.randint(0, len(cromosomasResultados)-1))
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
    
    # Método encargado de realizar el metodo de seleccion ranking
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
    
    # Método encargado de realizar el metodo de seleccion elitismo
    def metodoElite(self, poblacion, numPadres, tamañoElite):
        tabla = []
        resultado = []
        padres = []
        for cromosomaFitness in poblacion:
            tabla.append([cromosomaFitness[1], cromosomaFitness[0]])
        tabla.sort()
        for i in range(tamañoElite):
            seleccion1 = tabla.pop(-1)
            seleccion2 = tabla.pop(-1)
            resultado.append(seleccion1[1])
            resultado.append(seleccion2[1])
        for cromosoma in tabla:
            padres.append( [cromosoma[1], cromosoma[0]])
        padresN = self.metodoRuleta(padres, numPadres-tamañoElite)
        return resultado + padresN
    
    # Método encargado de realizar el metodo de cruzamiento one-point
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
    
    
    # Método encargado de realizar el metodo de cruzamiento two-point
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

    # Método encargado de realizar el metodo de cruzamiento uniform
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

    
    
  
