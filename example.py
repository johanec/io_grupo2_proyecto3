"""Simple proof-of-concept genetic algorithm that guesses passwords."""

import sys
import math
import random
import string
from typing import List, Tuple, Iterator

import tomllib
with open ("config.toml" , mode="rb") as fp:
    config = tomllib.load(fp)
    

# Number of crossover, mutate cycles to go through before giving up.
GENERATIONS = 10000

# Number of solutions to keep in a generation.
POPULATION_SIZE = 1000

# Ratio of guesses in the population that should mate by performing crossover.
MATE_RATE = 0.10

# Ratio of guesses that should be impacted by mutation.
MUTATION_RATE = 0.05

# Set of characters allowed in the password.
ALPHABET = string.ascii_letters + string.digits + string.punctuation


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


def create_population(size_of_password: int) -> List[str]:
  """Generates a population of guesses by chosing random characters."""

  population = []
  for _ in range(POPULATION_SIZE):
    guess = ''.join([random.choice(ALPHABET) for _ in range(size_of_password)])
    population.append(guess)

  return population


def mutate(guesses: List[str]) -> List[str]:
  """Mutates guesses by changing a random character to a random value."""
  guesses_to_mutate = math.floor(len(guesses) * MUTATION_RATE)

  for _ in range(guesses_to_mutate):
    guess_to_mutate_index = random.randint(0, len(guesses) - 1)
    char_to_mutate_index = random.randint(0, len(guesses[0]) - 1)

    mutant = list(guesses[guess_to_mutate_index])
    mutant[char_to_mutate_index] = random.choice(ALPHABET)

    guesses[guess_to_mutate_index] = ''.join(mutant)

  return guesses


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
    weighted_guesses += [guess] * similarity_score(password, guess)

  # Randomly select the desired number of mates from weighted_guesses.
  number_of_winners_to_choose = math.floor(len(guesses) * MATE_RATE)
  chosen = []
  for _ in range(number_of_winners_to_choose):
    chosen.append(random.choice(weighted_guesses))

  # Create mate pairs using (index, index+1)
  return zip(chosen[::2], chosen[1::2])


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
  mates = choose_mates(guesses, password)
  for mate1, mate2 in mates:
    crossover_point = random.randint(0, len(mate1))

    replacee_index1 = random.randint(0, len(guesses) - 1)
    replacee_index2 = random.randint(0, len(guesses) - 1)

    guesses[
        replacee_index1] = mate1[0:crossover_point] + mate2[crossover_point:]
    guesses[
        replacee_index2] = mate2[0:crossover_point] + mate1[crossover_point:]

  return guesses


def print_pop(population: List[str], password: str, samples_to_print=10):
  """Prints the top N most fit members of a population."""
  population.sort(
      key=lambda guess: similarity_score(password, guess), reverse=True)
  for guess in population[:samples_to_print]:
    print(guess, similarity_score(password, guess))


def main():
  
  password = config["passcode"]["correct_passcode"]
  if set(password) - set(ALPHABET):
    print(
        "The given password contains characters that aren't in the alphabet=" +
        ALPHABET)
    return

  population = create_population(size_of_password=len(password))

  for generation in range(GENERATIONS):
    population = crossover(population, password)
    population = mutate(population)

    if password in population:
      print('\n*** FOUND PASSWORD ON GENERATION=' + str(generation), '***')
      print_pop(population, password)
      return
    if generation % 100 == 0:
      print('\n*** GENERATION=' + str(generation), '***')
      print_pop(population, password)


if __name__ == '__main__':
  main()