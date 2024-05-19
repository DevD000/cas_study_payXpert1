class Payroll:
    def __init__(self, PayrollID=None, EmployeeID=None, PayPeriodStartDate=None, PayPeriodEndDate=None, BasicSalary=None, OvertimePay=None, Deductions=None, NetSalary=None):
        self.__PayrollID = PayrollID
        self.__EmployeeID = EmployeeID
        self.__PayPeriodStartDate = PayPeriodStartDate
        self.__PayPeriodEndDate = PayPeriodEndDate
        self.__BasicSalary = BasicSalary
        self.__OvertimePay = OvertimePay
        self.__Deductions = Deductions
        self.__NetSalary = NetSalary

    # Getters and Setters
    def get_PayrollID(self):
        return self.__PayrollID

    def set_PayrollID(self, PayrollID):
        self.__PayrollID = PayrollID

    def get_EmployeeID(self):
        return self.__EmployeeID

    def set_EmployeeID(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def get_PayPeriodStartDate(self):
        return self.__PayPeriodStartDate

    def set_PayPeriodStartDate(self, PayPeriodStartDate):
        self.__PayPeriodStartDate = PayPeriodStartDate

    def get_PayPeriodEndDate(self):
        return self.__PayPeriodEndDate

    def set_PayPeriodEndDate(self, PayPeriodEndDate):
        self.__PayPeriodEndDate = PayPeriodEndDate

    def get_BasicSalary(self):
        return self.__BasicSalary

    def set_BasicSalary(self, BasicSalary):
        self.__BasicSalary = BasicSalary

    def get_OvertimePay(self):
        return self.__OvertimePay

    def set_OvertimePay(self, OvertimePay):
        self.__OvertimePay = OvertimePay

    def get_Deductions(self):
        return self.__Deductions

    def set_Deductions(self, Deductions):
        self.__Deductions = Deductions

    def get_NetSalary(self):
        return self.__NetSalary

    def set_NetSalary(self, NetSalary):
        self.__NetSalary = NetSalary
