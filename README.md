# Python Road-map (Can be used for any language)

- [x] variable declaration
- [x] operators and casting
- [ ] print function
- [ ] data types
- [ ] declaration and operation on data types
- [ ] conditionals and looping
- [ ] functions
- [ ] classes
- [ ] testing
- [ ] error handling
- [ ] i/o
- [ ] project(as per the need)



# Operators & Casting

### Operators
1. Arithmetic Operators:
    - addition: 5 + 3
    - subtraction: 5 -3
    - multiplication: 5 * 3
    - division: 5/3
    - floor division: 5 // 2 = 2;  It performs division between two numbers and rounds down the result to the nearest integer
    - remainder: 5 % 3
    - exponentiation: 5 ** 3

2. Comparison Operators:
    - equals to 5 == 3
    - not equals to 5 != 3
    - greater than 5 > 3
    - less than 5 < 3
    - greater or equal to 5 >= 3
    - less than equal to 5 <= 3

3. Logical operator:
    - and: True and False
    - or: True or False
    - not: not True

4. Assignment Operators:
    - assignment: x = 5
    - add and assign: x += 3
    - subtract and assign: x -= 2
    - multiply and assign: x *= 4
    - divide and assign: x /= 2

5. Membership Operators:
    - in : 5 in [1,2,3,4,5]
    - not in: 5 not in [1,2,3,4]

### Casting
- converts to integer:

```python
    num_str = "123"
    num_int = int(num_str)
```

- converts to float:

```python3
    num_float = float(num_str)
```

- converts to String

```python3
    num_int = 123
    num_str = str(num_int)
```

- converts to Boolean

```python3
    value = 0
    bool_value = bool(value)
```
in general any non-zero numeric value will be converted to "True"

# Print function

### formatted string or f string
-  an f-string, also known as a formatted string literal, is a way to embed expressions inside string literals, using curly braces {}

```python3
message = f"Hello, my name is {name} and I am {age} years old."
print(message)
pi = 3.14159

# Formatting numeric values in f-string
formatted_pi = f"The value of pi is approximately {pi:.2f}."
print(formatted_pi)

```

# Variable Declaration & Data types

### declaration
        my_variable = 10

### Data Types
        1. Numeric Types:
            - int -> 1
            - float -> 2.0
        2. String:
            Ordered, immutables
            - str -> "Hello world"
        3. Boolean:
            - True/False
        4. List:
            Ordered collection of items
            - [1, 2, 3, "Python"]
        5. Tuple:
            Ordered, immutable collection of items
            - (1, 2, "Python")
        6. Set:
            Unordered collection of unique items.
            - {1, 2, 3, 4}
        7. Dictionary:
            unordered collection of key-value pairs.
            - {"name": "John", "age": 25, "city": "New York"}
        8. None:
            Absence of a value or a null value.
            - None

### checking data types:
    __print(type(variable))__<br>
    **isinstance(num1, (int, float))**

# Operation on Data types:

## List:
1. Itteration:
- for loop:
```python3
    my_list = [1, 2, 3, 4, 5]

# Iterating over the list using a for loop
for item in my_list:
    print(item)
```

- List Comprehension:

```python3
my_list = [1, 2, 3, 4, 5]

# Iterating over the list using list comprehension
squared_values = [item ** 2 for item in my_list]
```

- Using Enumerate for Index and values:
```python3
my_list = ['apple', 'banana', 'cherry']

# Iterating over the list using enumerate to get both index and value
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
```

- Using "While" loop:
```python3
my_list = [1, 2, 3, 4, 5]

# Iterating over the list using a while loop
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
```
