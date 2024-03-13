def fibonacci(num):
    if(num <= 0):
        return []

    curr = fibonacci(num -1)

    if len(curr) == 0:
        curr.append(0)
    elif len(curr) == 1:
        curr.append(1)
    else:
        curr.append(curr[-1] + curr[-2])

    return curr

def main():
    num = int(input("enter a number: "))
    try:
        if(num < 2):
            raise ValueError("enter a number greater than 1")
    except ValueError:
            print("invalid input")
    print(fibonacci(num))

main()
