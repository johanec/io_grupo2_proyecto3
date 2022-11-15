
from typing import List


class Utils():
    """ Clase encargada de realizar el calculo del fitness
    """
    def _init_(self, config):
        self.setConfig(config)

    def getConfig(self):
        return self.__config
    
    def setConfig(self,config ):
        self.__config = config
    
    def calculate_fitness(self, cromosoma):
        matches = 0
        config = self.getConfig()
        contraseñaCorrecta = config["passcode"]["correct_passcode"]  
        for index in range(len(contraseñaCorrecta)):
            if contraseñaCorrecta[index] == cromosoma[index]:
                matches += 1
        return matches/8
