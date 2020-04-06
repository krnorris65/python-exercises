# Practice: Convert Student Object to a String

class Student:
    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in Cohort {self.cohort_number}"

    # First name (string)
    @property
    def first_name(self):
        try:
            return self.__first_name 
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Please provide a string value for first name")
    
    # Last name (string)
    @property 
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Please provide a string value for last name")

    # Age (integer)
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    
    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide an integer value for age")
    
    # Cohort number (integer)
    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0
    
    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError("Please provide an integer value for cohort")

    # Full name (read-only string)
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return "full name not available"

kristen = Student()
kristen.first_name = "Kristen"
kristen.last_name = "Norris"
kristen.age = 29
kristen.cohort_number = 22

print(kristen)
