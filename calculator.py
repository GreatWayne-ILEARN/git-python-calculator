class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


def main():
    calc = Calculator()

    print(" BASIC CALCULATOR ")
    print("Available operations: add, subtract, multiply, divide")

    operation = input("Enter operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "add":
        result = calc.add(a, b)
    elif operation == "subtract":
        result = calc.subtract(a, b)
    elif operation == "multiply":
        result = calc.multiply(a, b)
    elif operation == "divide":
        result = calc.divide(a, b)
    else:
        result = "Invalid operation"

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
