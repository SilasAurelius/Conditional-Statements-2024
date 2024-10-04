# Task 1: Identify the Greatest: Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    largest_num = max(num1, num2, num3)
# Task 2: Identify the lowest number:
    lowest_num = min(num1, num2, num3)
    print(f"{largest_num} is the largest number.")
    print(f"{lowest_num} is the lowest number.")
    
    end_loop = input("Do you want to try again? (Yes or No): ").lower()
    if end_loop == "yes":
        continue
    else:
        break
