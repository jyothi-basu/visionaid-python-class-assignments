# Program to manage automobile details using object-oriented principles,
# allowing update and retrieval of vehicle information.

class Automobile:
    def __init__(self, n, m, p):
        self.__brand_name= n
        self.__model_name= m
        self.__price= p
        print("New vehicle has created!")

    def modify_price(self, new_price):
        self.__price= new_price

    def retrieve_data(self):
        return(self.__brand_name, self.__model_name, self.__price)