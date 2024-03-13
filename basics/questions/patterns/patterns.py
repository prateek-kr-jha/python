def printTrinagle(n):
    for num1 in range(n) :
        for num2 in range(n) :
            if(num2 <= num1):
                print("*", end=" ")
        print()

def printHourGlass(n):
    x = 1
    y = n - 2
    for num1 in range(n):
        for num2 in range(n):
            if (num1 == 0 or num1 == n - 1)
                or (num2 == 0 or num2 == n - 1)
                or (num1 == num2)
                or (num1 + num2 == n - 1):
                print("*", end=" ")
            elif(num2 >= x and num2 <= y) and (y >= x):
                print("*", end=" ")
            else:
                print(" ",end=" ")
        x += 1
        y -= 1
        print()

def main() :
    num = int(input("enter a number: "))
    #printTrinagle(num)
    printHourGlass(num)



main()
