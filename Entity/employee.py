class Employee:
    def __init__(self, EmployeeID=None, FirstName=None, LastName=None, DateOfBirth=None, Gender=None, Email=None, PhoneNumber=None, Address=None, Position=None, JoiningDate=None, TerminationDate=None):
        self.__EmployeeID = EmployeeID
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__DateOfBirth = DateOfBirth
        self.__Gender = Gender
        self.__Email = Email
        self.__PhoneNumber = PhoneNumber
        self.__Address = Address
        self.__Position = Position
        self.__JoiningDate = JoiningDate
        self.__TerminationDate = TerminationDate

    # Getters and Setters
    def get_EmployeeID(self):
        return self.__EmployeeID

    def set_EmployeeID(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def get_FirstName(self):
        return self.__FirstName

    def set_FirstName(self, FirstName):
        self.__FirstName = FirstName

    def get_LastName(self):
        return self.__LastName

    def set_LastName(self, LastName):
        self.__LastName = LastName

    def get_DateOfBirth(self):
        return self.__DateOfBirth

    def set_DateOfBirth(self, DateOfBirth):
        self.__DateOfBirth = DateOfBirth

    def get_Gender(self):
        return self.__Gender

    def set_Gender(self, Gender):
        self.__Gender = Gender

    def get_Email(self):
        return self.__Email

    def set_Email(self, Email):
        self.__Email = Email

    def get_PhoneNumber(self):
        return self.__PhoneNumber

    def set_PhoneNumber(self, PhoneNumber):
        self.__PhoneNumber = PhoneNumber

    def get_Address(self):
        return self.__Address

    def set_Address(self, Address):
        self.__Address = Address

    def get_Position(self):
        return self.__Position

    def set_Position(self, Position):
        self.__Position = Position

    def get_JoiningDate(self):
        return self.__JoiningDate

    def set_JoiningDate(self, JoiningDate):
        self.__JoiningDate = JoiningDate

    def get_TerminationDate(self):
        return self.__TerminationDate

    def set_TerminationDate(self, TerminationDate):
        self.__TerminationDate = TerminationDate
