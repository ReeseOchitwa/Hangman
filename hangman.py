from random import*

words = ["giraffe", "month", "carrot", "day", "mime", "clown", "first", "apple", "king"]
correct_letters = []
letter_guess = ""
life = 5
guessed_letters = []
empty = []

word_index = randint(0, 8)

hangman_word = words[word_index]

for letter in hangman_word:
    correct_letters.append(letter)
    empty.append("_")

while life > 0 and "_" in empty:
    print(empty)
    print(" ")
    letter_guess = input("Guess a letter: ")
    if letter_guess in correct_letters:
        print("You guessed a letter, correct letter was: " + letter_guess + ".")
        guessed_letters.append(letter_guess)
    if letter_guess not in hangman_word:
        life -= 1
        print("You guessed a wrong letter, life is now " + str(life) + ".\n")
    for letter in correct_letters:
        for num in range(len(hangman_word)):
            if letter == letter_guess and correct_letters[num] == letter_guess:
                empty[num] = correct_letters[num]


if "_" not in empty:
    print(empty)
    print("You guessed the word! The word was " + hangman_word + "!")


if life == 0:
    print("You ran out of life and lost the game. The word was " + hangman_word + "!")

