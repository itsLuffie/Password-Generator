import string
import random

def generate_password(length=None, num_letters=None, num_digits=None, num_symbols=None):
    """Generate a random password with the given length and character distribution."""
    # Define the character sets
    letter_set = string.ascii_letters
    digit_set = string.digits
    symbol_set = string.punctuation
    
    # Get the user's input for the password length and character distribution
    if length is None:
        length = int(input('Enter the number of characters: '))
    if num_letters is None:
        num_letters = int(input('Enter the number of letters: '))
    if num_digits is None:
        num_digits = int(input('Enter the number of digits: '))
    if num_symbols is None:
        num_symbols = int(input('Enter the number of symbols: '))
    
    # Generate the password by randomly selecting characters from the sets
    password = [random.choice(char_set) for char_set in (letter_set, digit_set, symbol_set) for _ in range(num_letters, num_digits, num_symbols)]
    
    # Shuffle the password characters to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and pad with random characters if necessary
    password_str = ''.join(password)
    if len(password_str) < length:
        padding = random.choices(letter_set + digit_set + symbol_set, k=length - len(password_str))
        password_str += ''.join(padding)
    elif len(password_str) > length:
        password_str = password_str[:length]
    
    return password_str

# Example usage: generate a password with the user's specified length, num_letters, num_digits, and num_symbols
print(generate_password())