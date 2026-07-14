def div(a: int, b : int):
    try:
        print(f" {a/b}")
    except ZeroDivisionError as err:
        print("Cannot be divided by zero")
        pass

e = int(input("Enter the number for division:"))
f = int(input("Enter the number for division:"))

div(e,f)