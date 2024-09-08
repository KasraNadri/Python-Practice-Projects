import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

def to_str(list):
    str = ""
    for i in list:
        str += i
    return str

lives_left = 4
count = 0
placeholder = []
for _ in chosen_word:
    placeholder.append("_")
str_placeholder = to_str(placeholder)
print(str_placeholder)

while count < 4:
    guessed_letter = input("Guess a letter: ").strip().lower()
    for i in range(len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            placeholder[i] = guessed_letter
    str_placeholder = to_str(placeholder)
    print(str_placeholder)
    if str_placeholder == chosen_word:
        break
    if guessed_letter not in chosen_word:
        print("WRONG!")
        count += 1
        lives_left -= 1
        if lives_left == 1:
            print(f"YOU'VE GOT {lives_left} LIFE LEFT!")
        print(f"YOU'VE GOT {lives_left} LIVES LEFT!")

if str_placeholder == chosen_word:
    print("You've won!")
else:
    print("You've lost!")