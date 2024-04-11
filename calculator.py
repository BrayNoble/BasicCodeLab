print("math schmungus")
# This function adds 
def add(x, y):
    return x + y

# This function subtracts 
def subtract(x, y):
    return x - y

# This function multiplies 
def multiply(x, y):
    return x * y

# This function divides 
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    Math_schmungus = input("Enter choice(1/2/3/4): ")

  
    if Math_schmungus in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if Math_schmungus == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif Math_schmungus == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif Math_schmungus == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif Math_schmungus == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")