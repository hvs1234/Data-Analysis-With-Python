def fact(n):
    if n == 0 or n == 1: return 1
    return n*fact(n-1)

def fact2(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial

def prime(n):
    flag = 0
    for i in range(2,(n//2)+1):
        if i%2==0: flag = 1
    if flag==0: print(f"{n} is prime number")
    else: print(f"{n} is not a prime number")

n = int(input("Enter the number: "))
print(f"Factorial of n using recursion: {fact(n)}")
print(f"Factorial of n using iteration: {fact2(n)}")
print(f"{prime(n)}")