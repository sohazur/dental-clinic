class Service:
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    # Get the name of this Service instance.
    def get_name(self):
        return self.__name

    # Get the cost of this Service instance.
    def get_cost(self):
        return self.__cost