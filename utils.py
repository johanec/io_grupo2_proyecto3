from typing import List


class Utils:
    """ Clase encargada de realizar el calculo del fitness
    """
    def __init__(self, config):
        self.config = config
   
   
    def calculate_fitness(self, cromosoma):
        """ Metodo encargado de realizar el calculo del fitness
        """
        puntuacion = 0
        contraseña = self.config["passcode"]["correct_passcode"]  
        for index in range(len(contraseña)):
            if list(contraseña)[index] == cromosoma[index]:
                puntuacion += 1
        return puntuacion/len(contraseña)
