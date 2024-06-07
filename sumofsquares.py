n = int(input("What is your number?:"))

def sumofsquares(n):
    for i in range(1,n):
        print(i, end="² + ")
    print(n,"² = ", int((n*(n+1)*(2*n+1)/6)), sep='')
    
sumofsquares(n)
