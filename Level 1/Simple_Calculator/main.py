# Simple Calculator
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2 
        if self.num2 !=0: 
            return self.num1 / self.num2
        else:
            with open("error_log.txt", "a") as log_file:
                log_file.write("Error: Division by zero\n") 
            return "Error: Division by zero"

# Example usage 
if __name__ == "__main__":
    num1 =  float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    calculator = Calculator(num1, num2)
    print(f"Addition: {calculator.add()}")
    print(f"Subtraction: {calculator.subtract()}")
    print(f"Multiplication: {calculator.multiply()}")
    print(f"Division: {calculator.divide()}")   