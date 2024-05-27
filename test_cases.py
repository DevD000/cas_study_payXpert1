import unittest
from datetime import datetime
from Entity import Employee
from DAO import EmployeeService, FinnancialRecordService, TaxService, PayrollService
from Exception.custom_exception import EmployeeNotFoundException


class TestPayrollSystem(unittest.TestCase):
    def setUp(self):
        self.employee_service = EmployeeService()
        self.financial_service = FinnancialRecordService()
        self.tax_service = TaxService()
        self.payroll_service = PayrollService()

    def test_calculate_gross_salary_for_employee(self):
        test_employee = Employee(
            "11"
            "Ethan",
            "Hunt",
            "1995-01-11",
            "Male",
            "hunnt@example.com",
            "1234567890",
            "123 Street",
            "Manager",
            "2022-11-19",
            None,
        )
        self.employee_service.create_employee(test_employee)
        print("test_createIncident_success passed")

if __name__ == "__main__":
    unittest.main()