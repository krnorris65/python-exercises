class Employee:
    def __init__ (self, first_name, last_name, title, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.start_date = start_date
    

class Company:
    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry =  industry
        self.employees = list()
    
    def report(self):
        print(f"{self.name} is in the {self.industry} industry and has the following employees")
        for employee in self.employees:
            print(f"* {employee.first_name} {employee.last_name}")
        print()

acme = Company("Acme Explosives", "101 TNT Blvd", "chemical")
jetways = Company("Jetways", "200 Airplane Drive", "transportation")

michael = Employee("Michael", "Chang", "CEO", "2017-03-04")
martina = Employee("Martina", "Navritilova", "CFO", "2016-05-14")

serena = Employee("Serena", "Williams", "Assistant", "2017-02-15")
roger = Employee("Roger", "Federer", "CEO", "2018-04-19")
pete = Employee("Pete", "Sampras", "Pilot", "2017-03-4")

acme.employees.append(michael)
acme.employees.append(martina)

jetways.employees.append(serena)
jetways.employees.append(roger)
jetways.employees.append(pete)

acme.report()
jetways.report()