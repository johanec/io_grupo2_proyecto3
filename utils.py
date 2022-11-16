from typing import List

# Clase encargada de realizar el calculo del fitness
class Utils:
    
    def __init__(self, config):
        self.config = config
   
    # Metodo encargado de realizar el calculo del fitness
    def calculate_fitness(self, cromosoma):        
        puntuacion = 0
        contraseña = self.config["passcode"]["correct_passcode"]  
        for index in range(len(contraseña)):
            if list(contraseña)[index] == cromosoma[index]:
                puntuacion += 1
        return puntuacion/len(contraseña)

    # Metodo para verificar que se encontró la contraseña
    def isContraseña(self, poblacion):
        for cromosoma in poblacion:
            if self.calculate_fitness(cromosoma) == 1:
                print("Se encontró la contraseña: " + str(cromosoma))
                return True
        return False
            
