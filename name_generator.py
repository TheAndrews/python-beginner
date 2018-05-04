import random, string

vowels = 'aeiouy'
consonants = 'qwrtyipsdfghjklçzxcvbnmm'
letters = string.ascii_lowercase
letter_input_one = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letters: ")
letter_input_two = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letters: ")
letter_input_three = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letters: ")

def create():    
    letter_one = randomize_letter(letter_input_one)
    letter_two = randomize_letter(letter_input_two)
    letter_three = randomize_letter(letter_input_three)
    name = letter_one + letter_two + letter_three
    return (name)

def randomize_letter(letter_type):
    if (letter_type == 'v'):
        return random.choice(vowels)
    
    if (letter_type == 'c'):
        return random.choice(consonants)

    if (letter_type == 'l'):
        return random.choice(letters)

    return letter_type


def generator():
    for i in range(100):
        print(create())


generator()

