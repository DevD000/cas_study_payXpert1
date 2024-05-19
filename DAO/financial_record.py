from datetime import datetime
from Util.DBConnUtil import DBconnection
from Exception.custom_exception import FinancialRecordException

class FinnancialRecordService(DBconnection):

    def add_finnancial_record(self,record_id,employee_id, description, amount, record_type):
        try:
            self.cursor.execute("insert into financialrecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType) values(?,?,?,?,?,?) ",(record_id,employee_id,datetime.now() ,description, amount, record_type))
            self.conn.commit
            print("Financial records added successfully.🎊")
        except Exception as e:
            print(e)

    def get_financial_record_by_id(self,record_id):
        try:
            self.cursor.execute("SELECT * FROM financialrecord WHERE recordid= ?",(record_id))
            record = self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)

    def get_financial_records_for_employee(self,employee_id):
        try:
            self.cursor.execute("select * from financialRecord where employeeid=?",(employee_id))
            records=self.cursor.fetchall()
            if not records:
                raise FinancialRecordException(
                    f"No any financial records found for Employee ID {employee_id}."
                )
            for record in records:
                print(record)
        except Exception as e:
            print(e)
    def get_financial_records_for_date (self,record_date):
        try:
            self.cursor.execute(
                "select * from financialrecord where recorddate = ?", (record_date)
            )
            records = self.cursor.fetchall()
            if not records:
                raise FinancialRecordException(
                    f"No any financial records found for date {record_date}."
                )
            for record in records:
                print(record)
        except Exception as e:
            print(e)
  