import random
word_list = ["aardvark", "baboon", "camel"]
i = random.randint(0,2)
secret_word = word_list[i]
print(f"secret word is: ",{word_list[i]})
for letters in secret_word:
    print(letters)
