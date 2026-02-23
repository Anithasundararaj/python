import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    print("====================================")
    print(" Welcome to Rock-Paper-Scissors")
    print("====================================")
    print("Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("------------------------------------")
    
    while True:
        user_choice = input("\nEnter rock, paper, or scissors: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("Result: It's a Tie!")
        elif result == "user":
            print("Result: 🎉 You Win!")
            user_score += 1
        else:
            print("Result: 💻 Computer Wins!")
            computer_score += 1
        
        print("\nScore Board")
        print(f"You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! 👋")
            break

play_game()