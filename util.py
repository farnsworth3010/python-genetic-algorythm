"""Genetic algorythm helpers."""

import random

from data import (
    MAX_UNITS,
    MUTATION_RATE,
    N_PRODUCTS,
    PRODUCT_NAMES,
    PRODUCTS,
    REQUIREMENTS,
)


def create_individual():
    """Create one random individual diet with all products."""
    return [random.uniform(0, MAX_UNITS) for _ in range(N_PRODUCTS)]


def calculate_fitness(individual):
    """
    Calculate the diet fitness.
    The goal is to minimize this value.
    Fitness = cost + penalty
    """
    total_cost = 0
    total_calories = 0
    total_protein = 0
    total_fat = 0
    total_vit_c = 0

    for i in range(N_PRODUCTS):
        product_name = PRODUCT_NAMES[i]
        quantity = individual[i]
        stats = PRODUCTS[product_name]

        total_cost += quantity * stats[0]
        total_calories += quantity * stats[1]
        total_protein += quantity * stats[2]
        total_fat += quantity * stats[3]
        total_vit_c += quantity * stats[4]

    # Calculate penalty for broken constraints
    penalty = 0

    # Calories penalty
    if total_calories < REQUIREMENTS["MIN_CALORIES"]:
        penalty += (REQUIREMENTS["MIN_CALORIES"] - total_calories) * 2

    # Protein penalty
    if total_protein < REQUIREMENTS["MIN_PROTEIN"]:
        penalty += (
            REQUIREMENTS["MIN_PROTEIN"] - total_protein
        ) * 5  # Protein is important, the penalty is higher

    # Fat penalty
    if total_fat > REQUIREMENTS["MAX_FAT"]:
        penalty += (total_fat - REQUIREMENTS["MAX_FAT"]) * 3

    # Vitamin C penalty
    if total_vit_c < REQUIREMENTS["MIN_VIT_C"]:
        penalty += (REQUIREMENTS["MIN_VIT_C"] - total_vit_c) * 1

    return total_cost + penalty


def select(population, fitnesses, k=3):
    """
    Selecting k random diets, take the best.
    """
    # K random indexes
    tournament_indices = random.sample(range(len(population)), k)

    # Find the index of the best among them
    best_index = tournament_indices[0]
    for i in tournament_indices[1:]:
        if fitnesses[i] < fitnesses[best_index]:
            best_index = i

    return population[best_index]


def crossover(parent1, parent2):
    """Crossover two diets."""
    child = []

    for i in range(N_PRODUCTS):
        child.append((parent1[i] + parent2[i]) / 2)

    return child


def mutate(individual):
    """
    Mutation: a small random diet change
    """
    for i in range(N_PRODUCTS):
        if random.random() < MUTATION_RATE:
            # Add/remove a small amount
            change = random.uniform(-0.5, 0.5)
            individual[i] = max(0, individual[i] + change)  # Don't let it be negative
    return individual


def print_solution(individual):
    """Print the final diet and parameters."""
    print("\n--- THE BEST DIET ---")

    total_cost = 0
    total_calories = 0
    total_protein = 0
    total_fat = 0
    total_vit_c = 0

    print("Products:")
    for i in range(N_PRODUCTS):
        product_name = PRODUCT_NAMES[i]
        quantity = individual[i]
        stats = PRODUCTS[product_name]

        total_cost += quantity * stats[0]
        total_calories += quantity * stats[1]
        total_protein += quantity * stats[2]
        total_fat += quantity * stats[3]
        total_vit_c += quantity * stats[4]

        print(f"  - {product_name:10s}: {quantity*100:6.1f} g")

    print("Final metrics:")
    print(f"  Total Cost: {total_cost:7.2f} (goal: minimum)")
    print(
        f"  Calories:   {total_calories:7.2f} (need: > {REQUIREMENTS['MIN_CALORIES']})"
    )
    print(
        f"  Protein:     {total_protein:7.2f} g (need: > {REQUIREMENTS['MIN_PROTEIN']})"
    )
    print(f"  Fat:      {total_fat:7.2f} g (need: < {REQUIREMENTS['MAX_FAT']})")
    print(f"  Vitamin C: {total_vit_c:7.2f} mg (need: > {REQUIREMENTS['MIN_VIT_C']})")
