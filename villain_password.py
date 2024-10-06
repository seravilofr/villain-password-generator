import random


# Read villain names from file
def read_villain_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().replace(' ', '_') for line in file.readlines()]


# Load villain names
villain_names = read_villain_names('villains.txt')

# Set of possible characters
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
symbols = '!@#$%^&*_+-=;:,./?'

# Minimum password length (by default 7)
min_password_length = 7

# Combine all characters into a single string
def generate_password(length):
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    return ''.join(random.choice(all_characters) for _ in range(length))

# Choose a random villain name
def choose_random_villain(villain_names):
    return random.choice(villain_names)


# Generate the final password
def generate_final_password(villain_name, length):
    random_part_length = length - len(villain_name) - 1
    if random_part_length <= 0:
        print("Password length is too short to include the villain name.")
        return None
    random_part = generate_password(random_part_length)
    return f"{villain_name}-{random_part}"

#Ask the user for the password length
while True:
    try:
        length = int(input(f"Enter the desired length of the password (min. {min_password_length} caracters): "))
        if length < min_password_length:
            print(
                f"Invalid input. Your password must be at least {min_password_length} characters long."
            )
        else:
            # Filter villain names based on the desired password length
            filtered_villain_names = [name for name in villain_names if len(name) < length -1]
            if not filtered_villain_names:
                print("No villain names are suitable for the given password length")
                continue
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Choose a random villain name for the filtered list
villain_name = random.choice(filtered_villain_names)

# Generate and print the password
generated_password = generate_final_password(villain_name, length)
if generated_password:
    print("Your new password is:", generated_password)
