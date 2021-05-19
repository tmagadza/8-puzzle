from typing import List

from flask import json
from api import puzzle
import json
import random

def test_solution():
    initial_state =  random.sample(range(9), 9)
    agent = puzzle.EightPuzzle(initial_state)

    assert type(agent.solution()) is list

def test_solution1():

    initial_state = [3, 1, 2, 6, 4, 5, 7, 8, 0]
    solution = ["LEFT", "LEFT", "UP", "UP"]

    agent = puzzle.EightPuzzle(initial_state)
    agent_solution = [s.upper() for s in agent.solution()]

    assert all([a ==b for a, b in zip(solution, agent_solution)])


def test_solution2():

    initial_state = [1, 4, 2, 3, 5, 0, 6, 7, 8]
    solution = ["LEFT", "UP", "LEFT"]

    agent = puzzle.EightPuzzle(initial_state)
    agent_solution = [s.upper() for s in agent.solution()]

    assert all([a ==b for a, b in zip(solution, agent_solution)])


def test_solution3():

    initial_state = [1, 4, 2, 3, 5, 0, 6, 7, 8]
    solution = ["Right", "Right", "Up", "Left", "Left"]

    agent = puzzle.EightPuzzle(initial_state)
    agent_solution = [s.upper() for s in agent.solution()]

    assert all([a ==b for a, b in zip(solution, agent_solution)])