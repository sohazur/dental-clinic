class DentalCompany:
    def __init__(self, company_name):
        self.__company_name = company_name
        self.__branches = []

    # Add a branch to the list of branches for this DentalCompany.
    def add_branch(self, branch):
        self.__branches.append(branch)

    # Get the list of branches for this DentalCompany.
    def get_branches(self):
        return self.__branches