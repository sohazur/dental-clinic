class Appointment:
    def __init__(self, appointment_id, patient, date, time):
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__date = date
        self.__time = time
        self.__services = []

    def add_service(self, service):
        self.__services.append(service)

    def get_id(self):
        return self.__appointment_id

    def get_patient(self):
        return self.__patient

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_services(self):
        return self.__services