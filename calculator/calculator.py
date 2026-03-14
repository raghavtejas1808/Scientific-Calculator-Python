import math
import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def square_root(x):
    logging.info(f"Square root of {x}")
    return math.sqrt(x)


def factorial(x):
    logging.info(f"Factorial of {x}")
    return math.factorial(x)

def natural_log(x):
    logging.info(f"Log of {x}")
    return math.log(x)

def power(a, b):
    logging.info(f"{a} power {b}")
    return a ** b


def main():
    while True:
        print("Scientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Log")
        print("4. Power")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            x = float(input("Enter number: "))
            print(square_root(x))

        elif choice == "2":
            x = int(input("Enter number: "))
            print(factorial(x))

        elif choice == "3":
            x = float(input("Enter number: "))
            print(natural_log(x))

        elif choice == "4":
            a = float(input("Base: "))
            b = float(input("Power: "))
            print(power(a, b))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
