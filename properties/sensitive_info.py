class Patient:
    def __init__(self, social_security_number, date_of_birth, account_number, first_name, last_name, address):
        self.__social_security_number = social_security_number
        self.__date_of_birth = date_of_birth
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return ""

    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return ""

    @property
    def account_number(self):
        try:
            return self.__account_number
        except AttributeError:
            return ""

    @property
    def first_name(self):
        return ""

    @property
    def last_name(self):
        return ""
    
    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    

cashew = Patient("097-23-1003", "08/13/92", "7001294103", "Daniela","Agnoletti", "500 Infinity Way")

# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"

cashew.address = "200 Main Street"
print(cashew.address)
