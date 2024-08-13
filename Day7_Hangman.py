import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

def to_str(list):
    str = ""
    for i in list:
        str+= i
    return str

placeholder = []
for _ in chosen_word:
    placeholder.append("_")
str_placeholder = to_str(placeholder)
print(str_placeholder)
guessed_letter = input("Guess a letter: ").strip().lower()

for i in range(len(chosen_word)):
    if guessed_letter == chosen_word[i]:
        placeholder[i] = guessed_letter
str_placeholder = to_str(placeholder)
print(str_placeholder)
