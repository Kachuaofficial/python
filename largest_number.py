# write a program to find largest number among 3

num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is larggest")
elif num2 > num1 and num2>num3:
    print(f"The number {num2} is the largest number")
else:
    print(f"The number {num3} is the largest")
            