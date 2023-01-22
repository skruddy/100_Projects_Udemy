
def add(num1, num2):
    """This function returns the value after addition of both numbers"""
    return num1+num2


def subtract(num1, num2):
    """This function returns the value after subtraction of both numbers"""
    return num1-num2


def multiply(num1, num2):
    """This function returns the value after multiplication of both numbers"""
    return num1*num2


def divide(num1, num2):
    """This function returns the value after division of both numbers"""
    return num1/num2


symbol = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


num1 = int(input("Please enter first number!"))
num2 = int(input("Please enter second number!"))
for operator in symbol:
    print(operator+"\n")
operator = input("Please select one operator from above values")

operation = symbol[operator]
answer = operation(num1, num2)
print(f"{num1} {operator} {num2} = {answer}")
