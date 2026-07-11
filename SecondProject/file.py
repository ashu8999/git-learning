File = r"C:\Users\User\Coding\multiply table.txt"


# f = open(File)
# data = f.read()
# print(data)
# f.close()


# f = open(File, "a")
# f.write("\nThis is day 10 learning Python \n Thank you")
# f.close()

#code to find a keyword in the file from the user input
# user = input("Enter the text to be search: ")
# user = user.lower()
# if user in a:
#     print("word found", user)
# else: 
#     print("word not found")
# Use of with function
# with open (File) as f:
#     a = f.read()
#     a = a.lower()


#Code to write table in file
# f = open(File, "a")

User = int(input("Enter the number to get the table: "))

def tablegeneration():
    table = ""

    for i in range(1,11):
        table += f"{User}X{i} = {i*User}\n"

    return table

a = tablegeneration()
file_name = f"{File}"
# print(file_name)
with open (file_name, "a") as f:
    f.write(a)




