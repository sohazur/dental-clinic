from Person import Person

class Patient(Person):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, patient_id):
        super().__init__(first_name, last_name, date_of_birth, phone_number)
        self.__patient_id = patient_id

    def get_patient_id(self):
        return self.__patient_id