import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("Welcome to Pythonista!")
print(art.logo)
n1 = float(input("Insert the first number: \n"))


def calculator(n1):
    for operation in operations:
        print(operation)
    operation = input("Inform the operation:\n")
    n2 = float(input("Insert the second number:\n"))

    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}.")
    use_previous_result = input("Want to continue working with the previous result? Press Enter to finish\n")
    if use_previous_result == "yes":
        result_final = calculator(result)
    elif use_previous_result == "no":
        print("\n"*35)
        print(art.logo)
        n1 = float(input("Insert the first number: \n"))
        result_final = calculator(n1)
    else:
        print("Thanks for using Pythonista!")
        result_final =  result
    return result_final


results = calculator(n1)

print(f"The final calculation result is: {results}")