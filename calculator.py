
#Simple Calculator
#Author - Shivam Mishra 
def calculator(num1, num2, operator):
    if operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 + num2
    elif operator == "%":
        return num1 % num2
    elif operator == "/":
        return num1 / num2
    elif operator == "*":
        return num1 / num2
    else:
        return print("wrong operator used")


def main():
    num1 = int(input("Enter the number 1"))
    num2 = int(input("Ente the numer 2"))

    operator = input("Enter the operator from %,*,-,+,/ :- ")
    
    print(calculator(num1, num2, operator))


main()