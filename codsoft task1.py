import random
import string

def generate_strong_password():
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        
        if length < 4:
            print("Password length must be at least 4 to include all character types.")
            return
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation
        
        
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(symbols)
        ]
        
     
        all_characters = uppercase + lowercase + digits + symbols
        
        for _ in range(length - 4):
            password.append(random.choice(all_characters))
        
    
        random.shuffle(password)
        
       
        final_password = ''.join(password)
        
        print("\nStrong Generated Password:", final_password)
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
generate_strong_password()