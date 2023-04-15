class Receipt:
    def __init__(self, appointment):
        self.__appointment = appointment
        self.__services = appointment.get_services()
        self.__vat_rate = 0.05

    # Calculate the total cost of services for this Receipt instance.
    def calculate_total(self):
        total = 0
        for service in self.__services:
            total += service.get_cost()
        return total

    # Calculate the VAT (Value Added Tax) for this Receipt instance.
    def calculate_vat(self):
        return self.calculate_total() * self.__vat_rate

    # Calculate the final total cost for this Receipt instance including VAT.
    def calculate_final_total(self):
        return self.calculate_total() + self.calculate_vat()

    # Print the receipt for this Receipt instance, including appointment information, services, subtotal, VAT, and final total.
    def print_receipt(self):
        print("Receipt for Appointment", self.__appointment.get_id())
        print("Patient:", self.__appointment.get_patient().get_full_name())
        print("Date:", self.__appointment.get_date())
        print("Time:", self.__appointment.get_time())
        print("\nServices:")
        for service in self.__services:
            print(f"- {service.get_name()}: ${service.get_cost():.2f}")
        print("\nSubtotal: ${:.2f}".format(self.calculate_total()))
        print("VAT (5%): ${:.2f}".format(self.calculate_vat()))
        print("Total: ${:.2f}".format(self.calculate_final_total()))