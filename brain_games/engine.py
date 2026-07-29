import prompt

ROUNDS_COUNT = 3


def run_game(rules, generate_round):
    print("Welcome to the Brain Games!")
    player_name = prompt.string("May I have your name? ")
    print(f"Hello, {player_name}!")
    
    print(rules)
    
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
            
    print(f"Congratulations, {player_name}!")
