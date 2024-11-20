def calculate(num1, op, num2):
    try:
        result = 0
        if op == "*":
            result += num1 * num2
        elif op == "/":
            result += num1 / num2
        elif op == "-":
            result += num1 - num2
        elif op == "+":
            result += num1 + num2
        print(f"{num1} {op} {num2} = {result}")
        return result
    except ValueError:
        print("Enter integers!")
        return
    


def calculate_2(op, num2):
    result = 0
    if op == "*":
        result += result_all * num2
    elif op == "/":
        result += result_all / num2
    elif op == "-":
        result += result_all - num2
    elif op == "+":
        result += result_all + num2
    print(f"{result_all} {op} {num2} = {result}")
    return result

result_all = 0
repetition = 1

result_all = calculate(float(input("What's the first number?: ")), input(" +\n-\n*\n/\nPick an operation : ").strip(), float(input("What's the next number?: ")))

while repetition == 1:
    print(f"Type 'yes' to continue calculating with {result_all}, or type 'no' to start a new calculation:")
    answer = input().strip().lower()
    if answer == "no":
        repetition = 0
        break
    elif answer == "yes":
        result = calculate_2(input("+\n-\n*\n/\nPick an operation : ").strip(),float(input("What's the next number?: ")))
    else:
        print("Wrong Response!")
        break
print(f"Result: {result_all}")
