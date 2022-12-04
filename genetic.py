from copy import deepcopy

import numpy.random as random


class Organism:

    def __init__(self, alleles, fitness, likelihood):
        self.alleles = alleles
        self.fitness = fitness
        self.likelihood = likelihood
        self.result = 0


    def to_string(self):
        return '%s [%s - %s]' % (self.alleles, self.fitness, self.likelihood)


def organism_fitness(gene, coefs, result):
    gene.result = 0
    for i in range(0, len(coefs)):
        gene.result += coefs[i] * gene.alleles[i]
    gene.fitness = abs(gene.result - result)
    return gene.fitness


def fitness(organisms, coefs, result):
    for organism in organisms:
        organism.fitness = organism_fitness(organism, coefs, result)
        if organism.fitness == 0:
            return organism
    return None

def multiply_fitness(organisms):
    coefficient_sum = 0
    for organism in organisms:
        coefficient_sum += 1 / float(organism.fitness)
    return coefficient_sum


def generate_likelihoods(organisms):
    multiplyFitness = multiply_fitness(organisms)
    for organism in organisms:
        organism.likelihood = ((1 / float(organism.fitness) / multiplyFitness) * 100)
    return organisms


def breed(coefs, parentOne, parentTwo):
    crossover = random.randint(1, len(coefs) - 1)
    child = deepcopy(parentOne)

    child.alleles = parentOne.alleles[:crossover] + parentTwo.alleles[crossover:]

    return child


def choose_parent(organisms):
    parent_number = random.randint(0, 100)
    cur_number = float(0)
    for i in range(0, len(organisms)):
        if cur_number <= parent_number <= cur_number + organisms[i].likelihood:
            return organisms[i]
        cur_number += organisms[i].likelihood


def create_new_generation(organisms, coefs):
    temp_population = []
    for _ in organisms:
        father = choose_parent(organisms)
        mother = choose_parent(organisms)
        while father.alleles == mother.alleles:
            father = choose_parent(organisms)
            mother = choose_parent(organisms)

        kid = breed(coefs, father, mother)
        temp_population.append(kid)
    return temp_population


def solve_diophantine_equation(coefs, result, population_count):
    organisms = []

    for i in range(0, population_count):
        alleles = []
        for j in range(0, len(coefs)):
            alleles.append(random.randint(0, result / coefs[j]))
        organisms.append(Organism(alleles, 0, 0))

    solution = fitness(organisms, coefs, result)
    iterations = 0
    iterations_max = 1500

    while not solution and iterations < iterations_max:
        organisms = generate_likelihoods(organisms)
        organisms = create_new_generation(organisms, coefs)
        solution = fitness(organisms, coefs, result)
        iterations += 1

    if solution:
        print('SOLUTION FOUND IN %s ITERATIONS' % iterations)
        return solution.alleles
    else:
        print('SOLUTION NOT FOUND')
        for organism in organisms:
            print(organism.to_string())

        return -1


if __name__ == '__main__':
    coefs = [1, 2, 3, 4, 5]
    result = 87
    population_count = 70

    solution = solve_diophantine_equation(coefs, result, population_count)
    print(solution)