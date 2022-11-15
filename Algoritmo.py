class Algoritmo:
    """ Clase encargada de contener el algoritmo genetico 
    """
    
    def __init__(self, config, poblacion):
        self.config = config
        self.poblacion = poblacion

    def metodoRuleta(self, fitness):
        return []
    
    def metodoElite(self, elite):
        return []
    
    def metodoRanking(self, fitness):
        return []

    def metodoSeleccion(self,fitness ):
        metodo = self.config["ag"]["selection_method"]
        if metodo == "ruleta" :
            self.metodoRuleta(fitness)  
        elif metodo == "elite": 
            self.metodoElite(fitness)
        elif metodo == "ranking":
            self.metodoRanking(fitness)
        else:
             raise Exception ("El método no se encuentra")
  