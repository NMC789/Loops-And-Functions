n = int(input("What is your number?: "))

def multTable(n) :
    for r in range(1, n+1) :
        for c in range(1, n+1) :
            print(r*c,end=" ")
        print()
 
multTable(n)
