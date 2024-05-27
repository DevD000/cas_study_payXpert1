
INSERT INTO Employee (EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) VALUES
(1, 'John', 'Doe', '1985-01-15', 'M', 'john.doe@example.com', '555-1234', '123 Maple St, Springfield', 'Software Engineer', '2010-06-01', NULL),
(2, 'Jane', 'Smith', '1990-07-22', 'F', 'jane.smith@example.com', '555-5678', '456 Oak St, Springfield', 'Product Manager', '2012-09-15', NULL),
(3, 'Robert', 'Brown', '1978-03-10', 'M', 'robert.brown@example.com', '555-8765', '789 Pine St, Springfield', 'HR Manager', '2008-03-23', '2022-11-30'),
(4, 'Emily', 'Johnson', '1995-12-05', 'F', 'emily.johnson@example.com', '555-4321', '321 Birch St, Springfield', 'Marketing Specialist', '2015-01-12', NULL),
(5, 'Michael', 'Lee', '1982-08-18', 'M', 'michael.lee@example.com', '555-6789', '654 Cedar St, Springfield', 'Sales Executive', '2009-07-01', NULL);


INSERT INTO Payroll (PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) VALUES
(1, 1, '2023-01-01', '2023-01-15', 5000.00, 200.00, 150.00, 5050.00),
(2, 2, '2023-01-01', '2023-01-15', 6000.00, 150.00, 100.00, 6050.00),
(3, 3, '2023-01-01', '2023-01-15', 5500.00, 100.00, 200.00, 5400.00),
(4, 4, '2023-01-01', '2023-01-15', 4500.00, 250.00, 50.00, 4700.00),
(5, 5, '2023-01-01', '2023-01-15', 5200.00, 300.00, 100.00, 5400.00);


INSERT INTO Tax (TaxID, EmployeeID, TaxYear, TaxableIncome, TaxAmount) VALUES
(1, 1, 2022, 60000.00, 12000.00),
(2, 2, 2022, 72000.00, 14400.00),
(3, 3, 2022, 66000.00, 13200.00),
(4, 4, 2022, 54000.00, 10800.00),
(5, 5, 2022, 62400.00, 12480.00);


INSERT INTO FinancialRecord (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType) VALUES
(1, 1, '2023-01-10', 'Bonus for Q4 performance', 1000.00, 'Bonus'),
(2, 2, '2023-01-11', 'Reimbursement for travel expenses', 300.00, 'Reimbursement'),
(3, 3, '2023-01-12', 'Purchase of office supplies', 150.00, 'Expense'),
(4, 4, '2023-01-13', 'Health insurance premium', 200.00, 'Insurance'),
(5, 5, '2023-01-14', 'Commission for sales', 500.00, 'Commission');

use payXpert1
select * from financialrecord  