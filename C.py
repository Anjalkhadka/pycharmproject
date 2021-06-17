
# No parameter and no return
def add():
    a = int(input("a: "))
    b = int(input("b: "))
    add = a + b
    print(f"The sum of {a} and {b} is {add}.")


add()


# Parameter but no returm
def sub(a, b):
    sub = a - b
    print(f"The difference of {a} and {b} is {sub}.")


sub(8, 3)


# No parameter but return present
def mul():
    a = int(input("a: "))
    b = int(input("b: "))
    product = a * b
    return product


mul()


# Parameter and return
def div(a, b):
    division = a / b
    return division


div(10, 2)


