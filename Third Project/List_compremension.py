# Write a list comprehension to print a list which contains the multiplication table of a user
# entered number

try:
    multiply = int(input("Give the number for the table: "))
    multiplication_table = [i*multiply for i in range (1,11)]
    
    
    
    
    with open (r"C:\Users\User\Coding\Third Project\c.txt","w") as f:
        a = f.write(str(multiplication_table) + "/n")
except Exception as err:
    print(err)