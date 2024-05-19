class FinancialRecord:
    def __init__(self, RecordID=None, EmployeeID=None, RecordDate=None, Description=None, Amount=None, RecordType=None):
        self.__RecordID = RecordID
        self.__EmployeeID = EmployeeID
        self.__RecordDate = RecordDate
        self.__Description = Description
        self.__Amount = Amount
        self.__RecordType = RecordType

    # Getters and Setters
    def get_RecordID(self):
        return self.__RecordID

    def set_RecordID(self, RecordID):
        self.__RecordID = RecordID

    def get_EmployeeID(self):
        return self.__EmployeeID

    def set_EmployeeID(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def get_RecordDate(self):
        return self.__RecordDate

    def set_RecordDate(self, RecordDate):
        self.__RecordDate = RecordDate

    def get_Description(self):
        return self.__Description

    def set_Description(self, Description):
        self.__Description = Description

    def get_Amount(self):
        return self.__Amount

    def set_Amount(self, Amount):
        self.__Amount = Amount

    def get_RecordType(self):
        return self.__RecordType

    def set_RecordType(self, RecordType):
        self.__RecordType = RecordType
