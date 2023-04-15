class DentalBranch:
    def __init__(self, address, phone_number, manager):
        self.__address = address
        self.__phone_number = phone_number
        self.__manager = manager
        self.__staff = []
        self.__patients = []
        self.__appointments = []
        self.__services = []

    # Add a staff member to the list of staff for this DentalBranch.
    def add_staff(self, staff):
        self.__staff.append(staff)

    # Add a patient to the list of patients for this DentalBranch.
    def add_patient(self, patient):
        self.__patients.append(patient)

    # Add an appointment to the list of appointments for this DentalBranch.
    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    # Add a service to the list of services for this DentalBranch.
    def add_service(self, service):
        self.__services.append(service)

    # Get the list of staff for this DentalBranch.
    def get_staff(self):
        return self.__staff

    # Get the list of patients for this DentalBranch.
    def get_patients(self):
        return self.__patients

    # Get the list of appointments for this DentalBranch.
    def get_appointments(self):
        return self.__appointments

    # Get the list of services for this DentalBranch.
    def get_services(self):
        return self.__services

    # Get a specific service by name from the list of services for this DentalBranch.
    def get_service_by_name(self, service_name):
        for service in self.__services:
            if service.get_name() == service_name:
                return service
        return None