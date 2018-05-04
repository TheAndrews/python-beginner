import random, string

def generator():
    letter_one = random.choice(string.ascii_lowercase)
    letter_two = random.choice(string.ascii_lowercase)
    letter_three = random.choice(string.ascii_lowercase)
    name = letter_one + letter_two + letter_three
    return (name)

print(generator())

