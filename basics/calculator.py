def calculator(num1, num2, operator):
    """
    This function calculates the o/p as per the numbers provided
    and operator given
    """
    try:
        if(
            not isinstance(num1, (int, float))
            or not isinstance(num2, (int, float))
        ):
            raise ValueError("not a number")

        if(
            operator != "+"
            and operator != "-"
            and operator != "/"
            and operator != "//"
            and operator != "%"
            and operator != "**"
        ):
            raise ValueError("unknown operator")

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "/":
            return num1 / num2
        elif operator == "//":
            return num1 // num2
        elif operator == "%":
            return num1 % num2
        elif operator == "**":
            return num1 ** num2
        elif operator == "*":
            return num1 * num2
    except ValueError as e:
        print(f"Error: {e}")




num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))
operator = input("enter operator: ")

print(calculator(num1, num2, operator))
