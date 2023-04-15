class Appointment:
    def __init__(self, appointment_id, patient, date, time):
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__date = date
        self.__time = time
        self.__services = []

    # Add a new service to the list of services for this appointment.
    def add_service(self, service):
        self.__services.append(service)

    # Get the appointment id for this instance.
    def get_id(self):
        return self.__appointment_id

    # Get the patient name for this instance.
    def get_patient(self):
        return self.__patient

    # Get the appointment date for this instance.
    def get_date(self):
        return self.__date

    # Get the appointment time for this instance.
    def get_time(self):
        return self.__time

    # Get the list of services for this instance.
    def get_services(self):
        return self.__services