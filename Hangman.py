import random

from MaxNrInList import length

word_list = ["aardvark", "baboon", "camel"]
#letter_tally = []
i = random.randint(0,2)
secret_word = word_list[i]
secret_word_string = str(secret_word)
print(f"secret word is: ",{word_list[i]})
# for letters in secret_word_string:
#     print(letters)
length_of_secret_word = len(word_list[i])
#print(f"Length of secret word: {length_of_secret_word}")
guessed_word = []
for i in range(length_of_secret_word):
    guessed_word.append("_")
nr_right = 0
nr_wrong = 0
done = False
while not done:
    guess = input("Guess a letter: ")
    for i in range(length_of_secret_word):
        if secret_word_string[i] == guess:
            guessed_word[i] = guess
            nr_right = nr_right + 1
            good_guess = True
    if not good_guess:
        nr_wrong = nr_wrong + 1
    good_guess = False
    print(guessed_word)
    if nr_wrong == 6:
        print("You lose")
        done = True
    elif nr_right == length_of_secret_word:
        print("You win")
        done = True