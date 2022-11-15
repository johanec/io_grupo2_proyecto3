import random
import numpy as np
import matplotlib.pyplot as plt
import time
import tomllib

with open ("config.toml" , mode="rb") as fp:
    config = tomllib.load(fp)
    
passcode_length = 10
passcode_lower_bound = 0
passcode_upper_bound = 9
population_size = 10
num_parents = 5
elite_size = 2
contraseñaCorrecta = config["passcode"]["correct_passcode"]
parents = []
secret_passcode = []

for caracter in contraseñaCorrecta:
    secret_passcode.append(int(caracter))
    
print(secret_passcode)


population = []
for i in range(population_size):
    chromosome = []
    for x in range(passcode_length):
        chromosome.append(int(round(random.uniform(passcode_lower_bound,passcode_upper_bound),0)))
    population.append(chromosome)
    
def fitness(population):
    fitness_scores = []
    for chromosome in population:
        matches = 0
        for index in range(passcode_length):
            if secret_passcode[index] == chromosome[index]:
                matches += 1
        result = [chromosome,matches]
        fitness_scores.append(result)
    return fitness_scores

def select_parents(fitness_scores):
    parents_list = []
    for chromosome in sorted(fitness_scores, key=lambda x: x[1], reverse = True)[:num_parents]:
        parents_list.append(chromosome[0])
    return(parents_list)

# breeding logic
def breed(parent1,parent2):
    child = []
    parent1 = parents[0]
    parent2 = parents[1]

    geneA = int(random.random() * passcode_length)
    geneB = int(random.random() * passcode_length)

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(0,passcode_length):
        if (i < startGene) or (i > endGene):
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

# breeding and elitism
def create_children(parents_pool):
    children = []
    num_new_children = len(population) - elite_size

    for i in range(0,elite_size):
        children.append(parents_pool[i])

    for i in range(0,num_new_children):
        parent1 = parents_pool[int(random.random() * len(parents_pool))]
        parent2 = parents_pool[int(random.random() * len(parents_pool))]
        children.append(breed(parent1,parent2))
    return children

def mutation(children_set):
    for i in range(len(children_set)):
        if random.random() > 0.1:
            continue
        else:
            mutated_position = int(random.random() * passcode_length)
            mutation = int(round(random.uniform(passcode_lower_bound,passcode_upper_bound+1),0))
            children_set[i][mutated_position] = mutation
    return children_set

success = []
generations = 0
t0 = time.time()
while True:
    fitness_scores = fitness(population)
    success.append(max([i[1] for i in fitness_scores]))
    if max([i[1] for i in fitness_scores]) == passcode_length:
        print("Cracked in {} generations, and {} seconds! \nSecret passcode = {} \nDiscovered passcode = {}".format(generations,time.time() - t0,secret_passcode,[i[0] for i in fitness_scores if i[1] == passcode_length][0]))
        break
    parents = select_parents(fitness_scores)
    print(parents)
    children = create_children(parents)
    population = mutation(children)
    generations += 1