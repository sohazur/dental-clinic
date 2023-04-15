from Staff import Staff

class Dentist(Staff):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary, license_number, specialty):
        super().__init__(first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary)
        self.__license_number = license_number
        self.__specialty = specialty

    # Get the license number for this Dentist instance.
    def get_license_number(self):
        return self.__license_number

    # Get the specialty for this Dentist instance.
    def get_specialty(self):
        return self.__specialty