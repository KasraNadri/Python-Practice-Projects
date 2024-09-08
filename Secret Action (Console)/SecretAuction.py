import os 
clear = lambda: os.system('cls')

print("Welcome to the secret auction program.")

repetition = 1
prompt_repetition = 1

bids_details = {}

while repetition == 1:
    name = input("What is your name?: ").strip().lower()
    bid = int(input("What's your bid?: "))
   
    
    while prompt_repetition == 1:
        print("Are there any bidders? Type 'yes' or 'no'.")

        bids_details[name.title()] = bid
        answer = input().strip().lower()
        if answer == "no":
            repetition = 0
            prompt_repetition = 0
        elif answer == "yes":
            repetition = 1
            prompt_repetition = 0
            clear()
        else:
            print("Wrong Answer! Try Again.\n")
    
max_bid = max(bids_details.values())

for name in bids_details.keys():
    if bids_details[name] == max_bid:
        print(f"The winner is {name} with a bid of ${bids_details[name]}.")