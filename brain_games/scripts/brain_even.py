import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers_count = 0
    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        
        correct_answer = "yes" if number % 2 == 0 else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
            
    print(f"Congratulations, {player_name}!")


if __name__ == "__main__":
    main()
