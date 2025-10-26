"""Diet problem algorythm"""

import copy
from data import ELITISM, GENERATIONS, POPULATION_SIZE
from util import calculate_fitness, create_individual, crossover, mutate, select


def solve_diet_problem():
    """Main diet problem solving cycle."""
    # 1. First population
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    print(
        f"Starting algorythm... Generations: {GENERATIONS}, Population: {POPULATION_SIZE}"
    )

    for gen in range(GENERATIONS):
        # 2. Calculate fitnesses of overall population
        fitnesses = [calculate_fitness(ind) for ind in population]

        # Sort by fitness (from the best)
        sorted_population = [
            ind for _, ind in sorted(zip(fitnesses, population), key=lambda x: x[0])
        ]

        # Save the best fitness for statistics
        best_fitness_in_gen = calculate_fitness(sorted_population[0])
        if (gen + 1) % 50 == 0:
            print(
                f"Generation {gen+1:3d} | The best fitness (Cost + Penalty): {best_fitness_in_gen:.2f}"
            )

        # 3. New population
        new_population = []

        # 3a. Elitism: take the best N individuals without changes
        new_population.extend(copy.deepcopy(sorted_population[:ELITISM]))

        # 3b. Fill the rest with other's descendants
        while len(new_population) < POPULATION_SIZE:
            # 3c. selecting
            tries = 50
            try_n = 0
            while try_n < tries:
                parent1 = select(sorted_population, fitnesses)  # Take from the best
                parent2 = select(sorted_population, fitnesses)
                try_n += 1
                if parent1 is not parent2:
                    break

            # 3d. Crossover
            child = crossover(parent1, parent2)

            # 3e. Mutation
            child = mutate(child)

            new_population.append(child)

        # New population replaces the old
        population = new_population

    # 5. Finish. Find and print the best diet from the last population.
    final_fitnesses = [calculate_fitness(ind) for ind in population]
    best_individual = sorted(zip(final_fitnesses, population), key=lambda x: x[0])[0][1]

    return best_individual
