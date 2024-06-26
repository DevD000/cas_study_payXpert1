from Util.DBConnUtil import DBconnection
from Exception.custom_exception import PayrollGenerationException

class PayrollService(DBconnection):
    def read_payroll(self):
        try:
            self.cursor.execute("select * from payroll")
            payrolls=self.cursor.fetchall()
            for payroll in payrolls:
                print(payroll)
        except Exception as e:
            print(e)


    def payroll_by_id(self,payroll_id):
        try:
            self.cursor.execute("select * from payroll where payrollId =?",(payroll_id))
            payroll=self.cursor.fetchone()
            print(payroll)
        except Exception as e:
            print(e) 

    def payroll_by_employee(self,employee_id):
        try:
            self.cursor.execute("select * from payroll where employeeId =?",(employee_id))
            payrolls=self.cursor.fetchall()
            for payroll in payrolls:
                print(payroll)
        except Exception as e:
            print(e) 

    def generate_payroll(self, employee_id, start_date, end_date):
        try:
            self.cursor.execute(
                "SELECT BasicSalary, OvertimePay, Deductions FROM Payroll WHERE EmployeeID = ? AND PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?",
                (employee_id, start_date, end_date),
            )
            payroll_data = self.cursor.fetchall()
            if not payroll_data:  # Check if payroll data is empty
                raise PayrollGenerationException(
                    f"No payroll data found for Employee ID {employee_id} within the specified period"
                )
            total_basic_salary = sum([record[0] for record in payroll_data])
            total_overtime_pay = sum([record[1] for record in payroll_data])
            total_deductions = sum([record[2] for record in payroll_data])
            net_salary = total_basic_salary + total_overtime_pay - total_deductions
            print(
                f"Payroll generated for Employee ID {employee_id} for the period from {start_date} to {end_date}:"
            )
            print(f"Total Basic Salary: {total_basic_salary}")
            print(f"Total Overtime Pay: {total_overtime_pay}")
            print(f"Total Deductions: {total_deductions}")
            print(f"Net Salary: {net_salary}")

        except Exception as e:
            print(e)
            

    def get_payrolls_for_period(self, start_date, end_date):
        try:
            self.cursor.execute(
                "SELECT * FROM Payroll WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?",
                (start_date, end_date),
            )
            payrolls = self.cursor.fetchall()
            for payroll in payrolls:
                print(payroll)
        except Exception as e:
            print(e)            


                   
