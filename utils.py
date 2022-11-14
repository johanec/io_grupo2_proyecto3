import tomllib
from typing import List

with open ("config.toml" , mode="rb") as fp:
    config = tomllib.load(fp)
    
#global variable to save the correct passcode
class Utils():
    
    def __init__(self, config):
        
        self.correct_passcode = config['passcode']['correct_passcode']
        if len(self.correct_passcode) > 0:
            print("MESSAGE: correct passcode read")
    
    @staticmethod
    def similarity_score(password: str, guess: str) -> int:
         """Returns a score that describes how good the given guess is."""
         score = 0

        # Award 1 point for every letter in the guess that also appears somewhere (in
        # any position) in the password.
         letters_in_common = set(password) & set(guess)
         score += len(letters_in_common)

        # Award 2 point for every letter in the right location.
         for i in range(min(len(password), len(guess))):
          if password[i] == guess[i]:
           score += 2

         return score

     #@params
    #   cromosome - type list, example: [character, character, character, ..., character-n]
    @staticmethod
    def calculate_fitness(self, cromosome): 
         """Prints the top N most fit members of a population."""
         """Returns a score that describes how good the given guess is."""
         cromosome.sort(key=lambda guess: self.similarity_score(self.correct_passcode, guess), reverse=True)
         for guess in cromosome[:10]:
          print(guess, self.similarity_score(self.correct_passcode, guess))

        #your code here    
         return self.similarity_score
     
    @staticmethod
    def print_pop(population: List[str], password: str, samples_to_print=10):
        """Prints the top N most fit members of a population."""
        population.sort(key=lambda guess:  Utils.similarity_score(password, guess), reverse=True)
        for guess in population[:samples_to_print]:
          print(guess, Utils.similarity_score(password, guess))
