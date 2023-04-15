# Import all the classes
from Appointment import Appointment
from DentalBranch import DentalBranch
from DentalCompany import DentalCompany
from Manager import Manager
from Patient import Patient
from Receipt import Receipt
from Service import Service
from Dentist import Dentist
from Hygienist import Hygienist
from Receptionist import Receptionist


# Test case a: Addition of branches to the dental company
bright_smiles = DentalCompany("Bright Smiles")

branch1 = DentalBranch("123 Main St", "555-1234", Manager("John", "Doe", "1980-01-01", "555-5678", "M001", "2020-01-01", 80000))
branch2 = DentalBranch("456 Market St", "555-2345", Manager("Jane", "Doe", "1981-02-02", "555-6789", "M002", "2020-01-02", 82000))

bright_smiles.add_branch(branch1)
bright_smiles.add_branch(branch2)

# Test case b: Addition of dental services, staff, and patients to a branch
cleaning = Service("Cleaning", 100)
implants = Service("Implants", 2000)
crowns = Service("Crowns", 800)
fillings = Service("Fillings", 200)

branch1_services = [cleaning, implants, crowns, fillings]
for service in branch1_services:
    branch1.add_service(service)

dentist1 = Dentist("Alice", "Smith", "1990-03-03", "555-7890", "D001", "2018-06-01", 120000, "D12345", "General")
hygienist1 = Hygienist("Bob", "Johnson", "1991-04-04", "555-8901", "H001", "2019-07-01", 60000, "H12345")
receptionist1 = Receptionist("Carol", "Williams", "1992-05-05", "555-9012", "R001", "2020-08-01", 40000)

branch1_staff = [dentist1, hygienist1, receptionist1]
for staff_member in branch1_staff:
    branch1.add_staff(staff_member)

patient1 = Patient("David", "Brown", "1993-06-06", "555-0123", "P001")
patient2 = Patient("Eva", "Davis", "1994-07-07", "555-1234", "P002")

branch1_patients = [patient1, patient2]
for patient in branch1_patients:
    branch1.add_patient(patient)

# Test case c: Patients booking appointments
appointment1 = Appointment(1, patient1, "2023-04-16", "10:00")
appointment1_services = [cleaning, crowns]
for service in appointment1_services:
    appointment1.add_service(service)

appointment2 = Appointment(2, patient2, "2023-04-16", "14:00")
appointment2_services = [cleaning, fillings]
for service in appointment2_services:
    appointment2.add_service(service)

branch1_appointments = [appointment1, appointment2]
for appointment in branch1_appointments:
    branch1.add_appointment(appointment)

# Test case d: Display of payment receipts for patient services
receipt1 = Receipt(appointment1)
receipt1.print_receipt()

print("\n" + "-" * 50 + "\n")

receipt2 = Receipt(appointment2)
receipt2.print_receipt()