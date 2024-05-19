from Util.DBConnUtil import DBconnection
from Exception.custom_exception import TaxCalculationException , InvalidInputException, EmployeeNotFoundException

class TaxService(DBconnection):
    def read_taxes (self):
        try:
            self.cursor.execute("select * from Tax")
            taxes=self.cursor.fetchall()
            for tax in taxes:
                print(tax)
        except Exception as e:
            print(e)
    
    def calculate_tax (self,employee_id,tax_year):
        try:
            self.cursor.execute("select sum(TaxableIncome) from Tax where EmployeeId=? and TaxYear=? ",(employee_id,tax_year))
            result = self.cursor.fetchone()
            if result and result[0] is not None:
                total_taxable_income = float(result[0])
           #  print(type(total_taxable_income))
            tax_rate = 0.18
            tax_amount = total_taxable_income * tax_rate

            print(
                f"Tax calculated for Employee ID {employee_id} for Tax Year {tax_year}:"
            )
            print(f"Total Taxable Income: {total_taxable_income}")
            print(f"Tax Rate: {tax_rate}")
            print(f"Tax Amount: {tax_amount}")
            
            if total_taxable_income is None:
                raise TaxCalculationException(
                    f"No taxable income found for Employee ID {employee_id} in Tax Year {tax_year}"
                )
            if tax_year < 0:  # Example condition for invalid tax year
                raise InvalidInputException("Tax year cannot be negative")
            
            
        except Exception as e:
            print(e)

    def get_tax_by_id (self,tax_id):
        try:
            self.cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id))
            tax = self.cursor.fetchone()
            print(tax)
        except Exception as e:
            print(e)    

    def get_taxes_for_employee(self,employee_id) :
        try:
            self.cursor.execute("select * from tax where employeeId=?",(employee_id))  
            taxes=self.cursor.fetchall()
            for tax in taxes:
                print(tax)
            if employee_id < 0:
                raise EmployeeNotFoundException("Employee id cannot be negative")     
        except Exception as e:
            print(e)


    def get_taxes_for_year(self,tax_year): 
        try:
            self.cursor.execute("select * from tax where taxYear=?",(tax_year))
            taxes= self.cursor .fetchall()
            for tax in taxes:
                print(tax)
            if tax_year < 0:  # Example condition for invalid tax year
                raise InvalidInputException("Tax year cannot be negative")     
        except Exception as e :
            print(e)



