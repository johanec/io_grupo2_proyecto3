
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
        puntuacion = 0
        config = self.getConfig()
        stringPass= config["passcode"]["correct_passcode"]  
        cromosomaModelo = list(stringPass)
        for index in range(len(cromosomaModelo)):
            if cromosomaModelo[index] == cromosoma[index]:
                puntuacion += 1
        return puntuacion/len(cromosomaModelo)
