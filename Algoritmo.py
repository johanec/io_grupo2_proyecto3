class Utils:
    """ Clase encargada de contener el algoritmo genetico 
    """
    def __init__(self, config, poblacion):
        self.setConfig(config)
        self.setpoblacion(poblacion)

    def getConfig(self):
        return self.__config
    
    def setConfig(self,config ):
        self.__config = config
    
    def getpoblacion(self):
        return self.__poblacion
    
    def setpoblacion(self,poblacion ):
        self.__poblacion = poblacion
    
    def metodoRuleta(self, fitness):
        return []
    
    def metodoElite(self, elite):
        return []
    
    def metodoRanking(self, fitness):
        return []

    def metodoSeleccion(self,fitness ):
        config = self.getConfig()
        metodo = config["ag"]["selection_method"]
        if metodo == "ruleta" :
            self.metodoRuleta(fitness)  
        elif metodo == "elite": 
            self.metodoElite(fitness)
        elif metodo == "ranking":
            self.metodoRanking(fitness)
        else:
             raise Exception ("El método no se encuentra")
  