class Employee:

    def __init__(self, sal):
        self.sal = sal
    

    def show(self):
        print(f"Salary of the employee is {self.sal}")

class salaryincrement(Employee):

    def  __init__(self, sal, increment):
        self.increment = increment
        super().__init__(sal)

    @property
    def sal(self):
        return self._sal
    
    @sal.setter
    def sal(self, value):

        if value >= 10000:
            self.increment = (value * self.increment)/100
            self._sal = value + self.increment

        else:
            print("No salary increment")


        # if self.sal >= 10000:
        #     increment = (self.sal * increment)/100
        #     self.sal = self.sal + increment

        # else:
        #     print("No salary increment")


    def show(self):
        print(f"Revised Salary of the employee is {self.sal}, {self.increment}")


a = Employee(int(900000))
b = salaryincrement(int(900000), float(30))

b.show()
