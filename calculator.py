def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    choice = input("Choose an operation (1-2): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()