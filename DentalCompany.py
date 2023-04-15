class DentalCompany:
    def __init__(self, company_name):
        self.__company_name = company_name
        self.__branches = []

    def add_branch(self, branch):
        self.__branches.append(branch)

    def get_branches(self):
        return self.__branches
