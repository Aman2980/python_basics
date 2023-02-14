# Define a function to find the nth Fibonacci number
def fibonacci(n):
  # Base cases
  if n == 0:
    return 0
  elif n == 1:
    return 1
  # Recursive case
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Ask the user for the value of n
n = int(input("Enter the value of n: "))

# Print the nth Fibonacci number
print(f"The {n}th Fibonacci number is {fibonacci(n)}.")

