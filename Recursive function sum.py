# print sum using recursivve function

# def sum(n):
#     if n == 1:
#         return 1
#     return n * (n + 1) / 2


n = int (input("Give the number: "))
print(f"sum of n natural number is : {sum(n)}")

# print start pattern using function

def star(n):
        for i in range (n, 0,-1):
            print("*"*i)
            #return ("*"*i)

print(star(3))