
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
        """ Metodo encargado de realizar el calculo del fitness
        """
        puntuacion = 0
        config = self.getConfig()
        contraseñaCorrecta = config["passcode"]["correct_passcode"]  
        for index in range(len(contraseñaCorrecta)):
            if contraseñaCorrecta[index] == cromosoma[index]:
                puntuacion += 1
        return puntuacion/8
