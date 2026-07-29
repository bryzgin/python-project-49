import random
from brain_games.engine import run_game

RULES = "What number is missing in the progression?"


def make_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(str(current_element))
    return progression


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = make_progression(start, step, length)
    
    hidden_index = random.randint(0, len(progression) - 1)
    
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    
    return question, correct_answer


def main():
    run_game(RULES, generate_round)


if __name__ == "__main__":
    main()
