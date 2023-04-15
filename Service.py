class Service:
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost
