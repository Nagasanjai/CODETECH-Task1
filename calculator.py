def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Welcome to the Basic Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == '1':
                print(f"The result of {num1} + {num2} is {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Invalid choice. Please choose a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thank you for using the calculator!")

calculator()
