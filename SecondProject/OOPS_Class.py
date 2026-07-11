class programmer:

    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company
        
    def name():
        name = "Ashutosh"
        company = "Microsoft"
        salary = 1200000

        return name

Employeee_name = input("Enter employee name: ") 
Employeee_salary = input("Enter employee Salary: ")
Employeee_company = input("Enter employee company name: ")    

# name = Employeee_name
employee_details = programmer(Employeee_name,Employeee_salary,Employeee_company)
print(employee_details.name, employee_details.salary, employee_details.company, employee_details.name)