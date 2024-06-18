def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def percentage(a, b):
    return (a / 100) * b

def power(a, b):
    return a ** b

def square_root(a):
    import math
    if a < 0:
        raise ValueError('Cannot compute square root of a negative number')
    return math.sqrt(a)

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Power")
    print("7. Square Root")
    print("0. Exit")

    while True:
        choice = input("Enter choice (0-7): ")

        if choice == '0':
            print("Exiting calculator.")
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                if choice != '7':
                    num1 = float(input("Enter first number: "))
                if choice in ['1', '2', '3', '4', '5', '6']:
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                except ValueError as e:
                    print(e)
            elif choice == '5':
                result = percentage(num1, num2)
                print(f"{num2}% of {num1} = {result}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                try:
                    num1 = float(input("Enter number to find square root: "))
                    result = square_root(num1)
                    print(f"Square root of {num1} = {result}")
                except ValueError as e:
                    print(e)

        else:
            print("Invalid input. Please enter a valid choice (0-7).")

if __name__ == "__main__":
    main()
