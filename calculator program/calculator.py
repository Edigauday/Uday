# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"

    return x / y

def history(n1,operation,n2,result):
    with open("calculator_results.txt", "a") as file:
        file.write(f"{n1} {operation} {n2} = {result}\n")

# Function to perform the calculation
def calculator():
    while True:
        user_input = input("Enter operation (+, -, *, /,exit):")

        if user_input in ("+", "-", "*", "/"):
            n1 = float(input("Enter first number: "))

            n2 = float(input("Enter second number: "))

            if user_input == "+":
                result = add(n1, n2)

            elif user_input == "-":
                result = subtract(n1, n2)

            elif user_input == "*":
                result = multiply(n1, n2)

            elif user_input == "/":
                result = divide(n1, n2)
            print(result)
            history(n1,user_input , n2, result)

        elif user_input == 'history':

            file_path = 'calculator_results.txt' # Replace 'your_file.txt' with the actual file path

            try:

            # Open the file in read mode

                with open(file_path, 'r') as file:

                # Read and print each line of the file

                    for line in file:
                        print(line, end='') # Use end='' to avoid adding extra line breaks



            except FileNotFoundError:
                (print(f"File '{file_path}' not found."))

            except Exception as e:
                (print(f"An error occurred: {e}"))

        elif user_input == "exit":

            print("Exiting calculator.")

            break
        else:

            print("Invalid input")



# Call the calculate function to start the calculator
if __name__ == "__main__":
    calculator()
