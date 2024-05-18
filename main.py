class MainMenu:
    def employee_management(self):
        while true:
            print("1] Create an employee")
            print("2] Delete an employee")
            print("3] Read employee")
            print("4] Update an employee")
            print("5] Back to main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                employee_data = (
                    input("Enter EmployeeID5: "),
                    input("Enter first name: "),
                    input("Enter last name: "),
                    input("Enter date of birth (YYYY-MM-DD): "),
                    input("Enter gender: "),
                    input("Enter email: "),
                    input("Enter phone number: "),
                    input("Enter address: "),
                    input("Enter position: "),
                    input("Enter joining date (YYYY-MM-DD): "),
                    input("Enter termination date (YYYY-MM-DD, if any): "),
                )






def main():

    while True:
        print(
            """Main Menu:
            1. Employee Management
            2. Payroll Management
            3. Tax Management
            4. Financial Record Management
            5. Exit"""
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            main_menu.employee_management()
        elif choice == "2":
            main_menu.payroll_management()
        elif choice == "3":
            main_menu.tax_management()
        elif choice == "4":
            main_menu.financial_record_management()
        elif choice == "5":
            print("Goodbye! Come back soon")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    print("Welcome to payroll management system")
    main()