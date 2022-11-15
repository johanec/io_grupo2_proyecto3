
from typing import List


class Utils:
    """ Clase encargada de realizar el calculo del fitness
    """
    def __init__(self, config):
        self.setConfig(config)

    def getConfig(self):
        return self.__config
    
    def setConfig(self,config ):
        self.__config = config
    
    
    def calculate_fitness(self, cromosoma):
        """ Metodo encargado de realizar el calculo del fitness
        """
        numero =["1","2","3","4","5","6","7","8","9","0"]
        puntuacion = 0
        config = self.getConfig()
        stringPass= config["passcode"]["correct_passcode"]  
        cromosomaModelo = list(stringPass)
        for index in range(len(cromosomaModelo)):
            if cromosomaModelo[index] in numero:
                cromosomaModelo[index] = int(cromosomaModelo[index])
            if cromosomaModelo[index] == cromosoma[index]:
                puntuacion += 1
        return puntuacion/len(cromosomaModelo)
