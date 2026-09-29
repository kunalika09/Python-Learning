#PASSWORD GENERATOR
import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    #Always include lowercase letters as the baseline
    character_pool = string.ascii_lowercase

    #Add optional characters based on user preference
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    #Ensure the user has selected at least one character type
    if not character_pool:
        print("Error: You must select at least one character type")
        return None

    #Randomly select characters from the pool and join them into a string
    password ="".join(random.choice(character_pool) for _ in range(length))
    return password

#--- Example Usage ---
print("--- Custom Password Generator ---")

#You can change these variables to customise your password
desired_length = 16
include_caps = True
include_numbers = True
include_symbols = True

#Generate and display the password
generated_password = generate_password(
    length=desired_length,
    use_uppercase=include_caps,
    use_numbers=include_numbers,
    use_special=include_symbols
)
if generated_password:
    print(f"Your secure password is: {generated_password}")
