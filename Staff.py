from Person import Person

class Staff(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.__employee_id = employee_id
        self.__hire_date = hire_date
        self.__salary = salary

    # Get the employee id for this Staff instance.
    def get_employee_id(self):
        return self.__employee_id

    # Get the hire date for this Staff instance.
    def get_hire_date(self):
        return self.__hire_date

    # Get the salary for this Staff instance.
    def get_salary(self):
        return self.__salary

    # Set the salary for this Staff instance.
    def set_salary(self, salary):
        self.__salary = salary