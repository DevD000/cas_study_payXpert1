class Tax:
    def __init__(self, TaxID=None, EmployeeID=None, TaxYear=None, TaxableIncome=None, TaxAmount=None):
        self.__TaxID = TaxID
        self.__EmployeeID = EmployeeID
        self.__TaxYear = TaxYear
        self.__TaxableIncome = TaxableIncome
        self.__TaxAmount = TaxAmount

    # Getters and Setters
    def get_TaxID(self):
        return self.__TaxID

    def set_TaxID(self, TaxID):
        self.__TaxID = TaxID

    def get_EmployeeID(self):
        return self.__EmployeeID

    def set_EmployeeID(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def get_TaxYear(self):
        return self.__TaxYear

    def set_TaxYear(self, TaxYear):
        self.__TaxYear = TaxYear

    def get_TaxableIncome(self):
        return self.__TaxableIncome

    def set_TaxableIncome(self, TaxableIncome):
        self.__TaxableIncome = TaxableIncome

    def get_TaxAmount(self):
        return self.__TaxAmount

    def set_TaxAmount(self, TaxAmount):
        self.__TaxAmount = TaxAmount
