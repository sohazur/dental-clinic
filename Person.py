class Person:
    def __init__(self, first_name, last_name, date_of_birth, phone_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number

    # Get the full name of this Person instance.
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    # Get the date of birth for this Person instance.
    def get_date_of_birth(self):
        return self.__date_of_birth

    # Get the phone number for this Person instance.
    def get_phone_number(self):
        return self.__phone_number

    # Set the phone number for this Person instance.
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number