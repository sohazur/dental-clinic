import Staff

class Receptionist(Staff):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary):
        super().__init__(first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary)

    def manage_appointments(self, action, branch, appointment=None, patient=None, date=None, time=None, services=None):
        """
        This method allows the receptionist to perform appointment-related tasks, such as scheduling or canceling appointments.

        :param action: A string indicating the action to perform: 'schedule' or 'cancel'.
        :param branch: The DentalBranch instance where the appointment is to be scheduled or canceled.
        :param appointment: The Appointment instance to be canceled (required for 'cancel' action).
        :param patient: The Patient instance for which the appointment is to be scheduled (required for 'schedule' action).
        :param date: The date of the appointment (required for 'schedule' action).
        :param time: The time of the appointment (required for 'schedule' action).
        :param services: A list of Service instances for the appointment (required for 'schedule' action).
        """
        if action == 'schedule':
            if patient is not None and date is not None and time is not None and services is not None:
                new_appointment = Appointment(len(branch.get_appointments()) + 1, patient, date, time)
                for service in services:
                    new_appointment.add_service(service)
                branch.add_appointment(new_appointment)
                print(f"Appointment scheduled for {patient.get_full_name()} on {date} at {time}.")
            else:
                print("Missing information to schedule an appointment.")
        elif action == 'cancel':
            if appointment is not None:
                appointments = branch.get_appointments()
                if appointment in appointments:
                    appointments.remove(appointment)
                    print(f"Appointment {appointment.get_id()} for {appointment.get_patient().get_full_name()} has been canceled.")
                else:
                    print(f"Appointment {appointment.get_id()} not found in appointments list.")
            else:
                print("No appointment provided to cancel.")
        else:
            print("Invalid action.")