# class Details:
#     @property
#     def name(self):
#         return f"{self.fname},{self.lname}"
    
#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]



# employee = Details()

# # q = "Ashutosh Jadhav"
# employee.name = "Ashutosh Jadhav"
# print(employee.fname, employee.lname)

class maths:

    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    def __mul__(self, num):
        return self.n * num.n

a = int(input(" ")) 
b = int(input(" "))

n = maths(a) 
m = maths(b)

print(n-m)