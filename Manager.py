from Staff import Staff

class Manager(Staff):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary):
        super().__init__(first_name, last_name, date_of_birth, phone_number, employee_id, hire_date, salary)

    def manage_staff(self, action, branch, staff_member=None):
        """
        This method allows the manager to perform management-related tasks, such as hiring or firing staff members.

        :param action: A string indicating the action to perform: 'hire' or 'fire'.
        :param branch: The DentalBranch instance where the staff member is to be hired or fired.
        :param staff_member: The Staff instance to be hired or fired (required for 'fire' action).
        """
        if action == 'hire':
            if staff_member is not None:
                branch.add_staff(staff_member)
                print(f"{staff_member.get_full_name()} has been hired.")
            else:
                print("No staff member provided to hire.")
        elif action == 'fire':
            if staff_member is not None:
                staff = branch.get_staff()
                if staff_member in staff:
                    staff.remove(staff_member)
                    print(f"{staff_member.get_full_name()} has been fired.")
                else:
                    print(f"{staff_member.get_full_name()} not found in staff list.")
            else:
                print("No staff member provided to fire.")
        else:
            print("Invalid action.")