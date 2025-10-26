"""Algorythm entrypoint."""

from algorythm import solve_diet_problem
from util import print_solution

best_diet = solve_diet_problem()

print_solution(best_diet)
