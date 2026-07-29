import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")
    
    print("What is the result of the expression?")
    
    correct_answers_count = 0
    operators = ["+", "-", "*"]
    
    while correct_answers_count < 3:
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        operator = random.choice(operators)
        
        question = f"{num1} {operator} {num2}"
        print(f"Question: {question}")
        
        user_answer = prompt.string("Your answer: ")
        
        if operator == "+":
            correct_answer = num1 + num2
        elif operator == "-":
            correct_answer = num1 - num2
        elif operator == "*":
            correct_answer = num1 * num2

        correct_answer_str = str(correct_answer)
        
        if user_answer == correct_answer_str:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer_str}'.")
            print(f"Let's try again, {player_name}!")
            return
            
    print(f"Congratulations, {player_name}!")


if __name__ == "__main__":
    main()
