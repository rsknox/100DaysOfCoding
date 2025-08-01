import random

from MaxNrInList import length

word_list = ["aardvark", "baboon", "camel"]
i = random.randint(0,2)
secret_word = word_list[i]
secret_word_string = str(secret_word)
print(f"secret word is: ",{word_list[i]})
for letters in secret_word_string:
    print(letters)
length_of_secret_word = len(word_list[i])
print(f"Length of secret word: {length_of_secret_word}")
