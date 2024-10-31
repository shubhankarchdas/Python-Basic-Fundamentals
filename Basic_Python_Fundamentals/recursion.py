#factorial(n) = n* factorial (n-1)
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

# n=(3)
n = int(input("Enter a number : "))
print(f"factorial of this number is : {factorial(n)}")