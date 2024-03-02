# example1.py

class Calculator:
    def add(self, x, y):
        """Add two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtract two numbers."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide two numbers."""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
    
# Prompt the user to enter the value for 'a' and 'b'
x = float(input("Enter the value for 'x': "))
y = float(input("Enter the value for 'y': "))

# Usage example
if __name__ == "__main__":
    # Create an instance of Calculator
    calc = Calculator()

    # Perform some calculations
    num1 = 5
    num2 = 2

    print("Addition:", calc.add(x, y))
    print("Subtraction:", calc.subtract(x, y))
    print("Multiplication:", calc.multiply(x, y))
    try:
        print("Division:", calc.divide(x, y))
    except ValueError as e:
        print("Error:", e)
