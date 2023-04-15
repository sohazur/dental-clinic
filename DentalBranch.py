class DentalBranch:
    def __init__(self, address, phone_number, manager):
        self.__address = address
        self.__phone_number = phone_number
        self.__manager = manager
        self.__staff = []
        self.__patients = []
        self.__appointments = []
        self.__services = []

    def add_staff(self, staff):
        self.__staff.append(staff)

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    def add_service(self, service):
        self.__services.append(service)

    def get_staff(self):
        return self.__staff

    def get_patients(self):
        return self.__patients

    def get_appointments(self):
        return self.__appointments

    def get_services(self):
        return self.__services

    def get_service_by_name(self, service_name):
        for service in self.__services:
            if service.get_name() == service_name:
                return service
        return None