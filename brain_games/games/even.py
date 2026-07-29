import random
from brain_games.engine import run_game

RULES = """Answer "yes" if the number is even, otherwise answer "no"."""


def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    
    correct_answer = "yes" if number % 2 == 0 else "no"
    
    return question, correct_answer


def main():
    run_game(RULES, generate_round)


if __name__ == "__main__":
    main()
