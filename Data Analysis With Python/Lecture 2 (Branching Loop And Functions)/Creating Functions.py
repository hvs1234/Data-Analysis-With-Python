def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"Value of a= {a} and b= {b}")
a,b = swap(a,b)
print(f"Value after swapping a= {a} and b= {b}")


'''
Q- Radha is planning to buy a house that costs $1,260,000. She considering two options to finance her purchase:
.Option-1:- Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% (compounded monthly) for the remaining amount.
.Option-2:- Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount.
Both these loans have to paid back in equal monthly installments (EMIs). Which loan has a lower EMI among the two?'
'''

def loan_emi(amount):
    emi = amount/12
    print(f"The EMI is: {emi}")

amount = int(input("Enter the amount: "))
loan_emi(amount)

# Optional Arguments:- Argument in the function having default value is 0.
def func1(a,b,c=0):
    a = a*b
    b = a**2
    a = b*2
    c = a-b
    return a,b,c

a,b,c=2,3,4; a,b,c = func1(a,b,c)
print(f"Value of a = {a}, b = {b} , c = {c}")