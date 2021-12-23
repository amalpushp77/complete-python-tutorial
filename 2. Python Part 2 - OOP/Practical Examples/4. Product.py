class Product:

    def __init__(self):
        self.__ProductID = None
        self.__ProductName = None
        self.__Price = None

    def setProduct(self, pid, pname, price):
        self.__ProductID = pid
        self.__ProductName = pname
        self.__Price = price

    def getProduct(self):
        print(f"Product ID: {self.__ProductID} \n"
              f"Product Name: {self.__ProductName} \n"
              f"Product Price: {self.__Price:,} \n")


phone = Product()
phone.setProduct("p101", "OnePlus 9", 49999)
phone.getProduct()
