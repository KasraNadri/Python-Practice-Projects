print("Welcome to the tip calculator!")
total_bill = float(input("What was the totall bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10? 12? 15? ")) / 100
num_of_people = int(input("How many people to split the bill? "))
share = (total_bill + (total_bill * tip_percentage)) / num_of_people
print(f"Each person should pay: ${round(share, 2)}")