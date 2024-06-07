n = int(input("number of rows: "))

for i in range(n):
    for _ in range(0+i):
        print("\\",end="\\")
    for _ in range(1,n-i):
        print("!",end="!")
    for _ in range(n-i):
        print("!",end="!")
    for _ in range(0+i):
        print("/",end="/")
    print("")
