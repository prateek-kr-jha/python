def printTrinagle(n):
    for num1 in range(n) :
        for num2 in range(n) :
            if(num2 <= num1):
                print("*", end=" ")
        print()

def printM(n):
    for num1 in range(n):
        for num2 in range(n):
            if(num2 == 0 or num2 == n - 1) or (num1 == num2) or (num1 + num2 == n - 1):
                print(f"{num1 + num2}", end=" ")
            else:
                print(" ",end=" ")
        print()

def main() :
    num = int(input("enter a number: "))
    #printTrinagle(num)
    printM(num)



main()
