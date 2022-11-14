import string
import tomllib
from utils import *
import math
from typing import List, Tuple, Iterator
import random
import sys

with open ("config.toml" , mode="rb") as fp:
    config = tomllib.load(fp)
    
tamañoPoblacion = config["ag"]["population_size"]           # 10
numeroParientes = config["ag"]["num_parents"]                   # 5
metodoSeleccion = config["ag"]["selection_method"]         # ruleta
tamañoElite = config["ag"]["elite_size"]                     # 2
rangoMutacion = config["ag"]["mutation_rate"]               # 0.5
rangoCruce = config["ag"]["crossover_rate"]             # 90
metodoCruce = config["ag"]["crossover_method"]         # uniform
contraseñaCorrecta = config["passcode"]["correct_passcode"]   # 234AHLp91n
alfabeto = string.ascii_letters + string.digits             # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789


class Poblacion:  
    
    def __init__(self, tamañoPoblacion):
        self.tamañoPoblacion = tamañoPoblacion
        
    @staticmethod
    def creaPoblacion() -> List[str]:
        poblacion = []
        for _ in range(tamañoPoblacion):
         conjeturas = ''.join([random.choice(alfabeto) for _ in range(len(contraseñaCorrecta))])
         poblacion.append(conjeturas)

        return poblacion
    
    @staticmethod
    def mutacion(conjeturas: List[str]) -> List[str]:
       """Muta las conjeturas cambiando un carácter aleatorio a un valor aleatorio."""
       adivinaParaMutar = math.floor(len(conjeturas) * 0.05)

       for _ in range(adivinaParaMutar):
             guess_to_mutate_index = random.randint(0, len(conjeturas) - 1)
             char_to_mutate_index = random.randint(0, len(conjeturas[0]) - 1)
             mutant = list(conjeturas[guess_to_mutate_index])
             mutant[char_to_mutate_index] = random.choice(alfabeto)
             conjeturas[guess_to_mutate_index] = ''.join(mutant)

       return conjeturas
    
    @staticmethod
    def choose_mates(guesses: List[str],
                 password: str) -> Iterator[Tuple[str, str]]:
     """Returns a list of randomly chosen mates for crossover.
     Guesses that are more similar to the password (more fit) are given a higher
     chance of mating.
     Args:
     guesses: the population of guesses to choose the winners from.
     password: the password that we're attempting to guess.
     Returns: a list of pairs (tuples) containing the chosen mates.
     """

    # Create a list of guesses, where each guess is given a certain number of
    # spots, as determined by the similarity score of that guess.
     weighted_guesses = []
     for guess in guesses:
      weighted_guesses += [guess] * Utils.similarity_score(password, guess)

    # Randomly select the desired number of mates from weighted_guesses.
     number_of_winners_to_choose = math.floor(len(guesses) * 0.10)
     chosen = []
     for _ in range(number_of_winners_to_choose):
      chosen.append(random.choice(weighted_guesses))

    # Create mate pairs using (index, index+1)
     return zip(chosen[::2], chosen[1::2])

    @staticmethod
    def crossover(guesses: List[str], password: str) -> List[str]:
     """Selects mates and performs crossover with each pair of mates.
     Guesses that are more similar to the password (more fit) are given a higher
     chance of mating.
     Mates perform crossover by selecting a random index, then copying all the
     characters to the left of that index from one mate, and then copying all the
     characters from the right of that index from the other mate. The second mate
     is copied by doing the opposite.
     Example: (ABCDE, VWXYZ) with random crossover index at 3
     - Child 1: ABCYZ
     - Child 2: VWXDE
     Args:
     guesses: the population of guesses to select mates from.
     password: the password that we are trying to guess.
     Returns:
     new population with next generation introduced, with new generation
     incorporated by randomly replacing some existing guess.
     """
     
     mates = Poblacion.choose_mates(guesses, password)
     for mate1, mate2 in mates:
      crossover_point = random.randint(0, len(mate1))

     replacee_index1 = random.randint(0, len(guesses) - 1)
     replacee_index2 = random.randint(0, len(guesses) - 1)

     guesses[replacee_index1] = mate1[0:crossover_point] + mate2[crossover_point:]
     guesses[replacee_index2] = mate2[0:crossover_point] + mate1[crossover_point:]

     return guesses
 
class Main:
    
   @staticmethod
   def main():
 
    if set(config["passcode"]["correct_passcode"]) - set(alfabeto):
     print("The given password contains characters that aren't in the alphabet=" + alfabeto)
     return 
   
    population = Poblacion.creaPoblacion()
    for generation in range(10000):
     population = Poblacion.crossover(population, config["passcode"]["correct_passcode"])
     population = Poblacion.mutacion(population)

     if config["passcode"]["correct_passcode"] in population:
      print('\n*** FOUND PASSWORD ON GENERATION=' + str(generation), '***')
      Utils.print_pop(population, config["passcode"]["correct_passcode"])
      return 
  
     if generation % 100 == 0:
      print('\n*** GENERATION=' + str(generation), '***')
      Utils.print_pop(population, config["passcode"]["correct_passcode"])

if __name__ == '__main__':
  Main.main()