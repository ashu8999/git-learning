# class employee():
#     companys = "ITC"    
#     def show(names):
#         print(f"The Name of the employee is {names}")


# class prgrammer(employee):
#     companyss = "Jifjaff"

# a = employee()
# b = prgrammer()
# # b.names("ash")
# print(a.companys, b.companys)


class Employee:
    Name = "Ash"
    print(f"Name of the Employee is {Name}")

class programmer(Employee):
    Program = "Python"
    print(f"{Employee.Name} works on {Program}")

class manager(programmer):
    Manager = "Access"
    print(f"He has Manager {Manager}")


m = manager()

#print(m.Name, m.Program, m.Manager)