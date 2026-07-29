import random
from brain_games.engine import run_game

RULES = "What is the result of the expression?"


def generate_round():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operator = random.choice(["+", "-", "*"])
    
    question = f"{num1} {operator} {num2}"
    
    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    elif operator == "*":
        correct_answer = num1 * num2
        
    return question, str(correct_answer)


def main():
    run_game(RULES, generate_round)


if __name__ == "__main__":
    main()
