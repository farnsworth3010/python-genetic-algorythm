"""Initial data and genetic algorythm constraints."""

# Price, calories, proteins, fats, vitamin C (100g)
PRODUCTS = {
    "Apple": (5, 52, 0.3, 0.2, 5),
    "Chicken": (20, 239, 27, 14, 0),
    "Rice": (8, 130, 2.7, 0.3, 0),
    "Milk": (7, 42, 3.4, 1.0, 1),
    "Orange": (6, 47, 0.9, 0.1, 53),
}

PRODUCT_NAMES = list(PRODUCTS.keys())
N_PRODUCTS = len(PRODUCT_NAMES)

REQUIREMENTS = {"MIN_CALORIES": 2000, "MIN_PROTEIN": 50, "MAX_FAT": 70, "MIN_VIT_C": 45}

POPULATION_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.1
ELITISM = 2
MAX_UNITS = 20  # Max units of one product (2kg)
