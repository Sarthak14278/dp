import random

def generate_password(num_words, min_word_length=3, max_word_length=8):
    try:
        with open('pass.txt', 'r') as file:
            content = file.read()
            words = content.split()  # Split the entire file content into words

        if len(words) < num_words:
            raise ValueError(f"Not enough words in the file to generate a password with {num_words} words.")

        random_words = random.sample(words, num_words)
        password = ' '.join(random_words)
        return password

    except FileNotFoundError:
        return "Error: The file 'GeneratePass.txt' was not found."
    except ValueError as e:
        return str(e)

print("Password Generator")
pass_length = int(input("Enter the number of words for the password: "))

password = generate_password(pass_length)
print(f"Generated Password: {password}")
