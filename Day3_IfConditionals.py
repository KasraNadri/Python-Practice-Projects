print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input().strip().lower()
if direction == "left":
    print("Do you want to swim or wait?")
    action = input().strip().lower()
    if action == "wait":
        print("Which door do you choose? Red? Blue? Yellow?")
        choice = input().strip().lower()
    else:
        print("You were attacked by trout. Game over!")
else:
    print("You fell into a hole. Game over!")