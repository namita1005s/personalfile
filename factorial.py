def factorial(n):
    """This is a recursive function
    to find the factorial of an integer"""

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
n = 4
print("The factorial of", n, "is", factorial(n))
