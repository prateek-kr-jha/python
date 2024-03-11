import sys

print(type(sys.argv))

if len(sys.argv) >= 2:
    print("Hello, world!")
else:
        print("Please provide proper input")
