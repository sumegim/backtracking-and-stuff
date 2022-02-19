from termcolor import colored, cprint
import copy
from random import randrange

board_4x4 = [0,0,0,0]
board_8x8 = [0,0,0,0,0,0,0,0]
board_16x16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def pprint(board):
    for index in board:
        for i in range(len(board)):
            if i == index:
                print(colored("Q", "cyan"), end = " ")
            else:
                print(colored(".", "white"), end = " ")
        print()
    print()

def count_overlap_up_to(board, depth):
    current_queen = board[depth]
    overlap_ctr = 0
    for i in range(depth):
        if current_queen == board[i]:
            overlap_ctr += 1
        if current_queen == board[i] + (depth - i):
            overlap_ctr += 1
        if current_queen == board[i] - (depth - i):
            overlap_ctr += 1

    return overlap_ctr

def count_overlap(board):
    overlap_counter = 0
    for i in range(len(board)):
        overlap_counter += count_overlap_up_to(board, i)
    return overlap_counter

def create_random_population(board, population_size):
    l = len(board)
    population_0 = []
    for _ in range(population_size):
        random_board = [randrange(l) for i in range(l)]
        population_0.append((random_board, count_overlap(random_board)))
    return sorted(population_0, key=lambda b: -b[1])

def play_tournament(population, size):
    l = len(population)
    random_players = [population[randrange(l)] for i in range(size)]
    return sorted(random_players, key=lambda b: b[1])[0]

def create_parents_through_tournament(population, tournament_size):
    winner_dad = play_tournament(population, tournament_size)
    winner_mom = play_tournament(population, tournament_size)
    return (winner_dad, winner_mom)

def flatten(l):
    return [item for sublist in l for item in sublist]

def cross_breed(parents):
    dad, mom = parents
    l = len(mom[0])
    child1 = flatten([dad[0][:l//2], mom[0][l//2:]])
    child2 = flatten([mom[0][:l//2], dad[0][l//2:]])
    return (child1, child2)

def mutate(child, percent):
    for i in range(len(child)):
        if randrange(100) < percent:
            child[i] = randrange(len(child))

def has_result(population):
    solution_candidate = sorted(population, key=lambda b: b[1])[0]
    if solution_candidate[1] == 0:
        pprint(solution_candidate[0])
        return True
    return False

population = create_random_population(board_8x8, 200)
# for p in population:
#     print(p)

generation = 0
while(not has_result(population)):
    new_population = []
    for i in range(len(population)//2):
        parents = create_parents_through_tournament(population, 4)
        child1, child2 = cross_breed(parents)
        mutate(child1, 10)
        mutate(child2, 5)
        new_population.append((child1, count_overlap(child1)))
        new_population.append((child2, count_overlap(child2)))
    population = new_population
    generation += 1
    if generation > 500:
        print("This generation failed")
        break

print(f"gen {generation}")
