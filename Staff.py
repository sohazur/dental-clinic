from Person import Person

class Staff(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.__employee_id = employee_id
        self.__hire_date = hire_date
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_hire_date(self):
        return self.__hire_date

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary