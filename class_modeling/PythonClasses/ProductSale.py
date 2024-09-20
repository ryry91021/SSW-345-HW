# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None

    def __init__(self, sale: Sale):
        self.__lastSale = sale

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self

    # New additions for inventory management
    __inventory: int = 0  # Adding an inventory attribute

    def setInventory(self, amount: int):
        """Set the inventory for the product."""
        self.__inventory = amount

    @property
    def getInventory(self) -> int:
        """Get the current inventory level."""
        return self.__inventory

    def reduceInventory(self, amount: int):
        """Reduce inventory by a certain amount."""
        if self.__inventory - amount >= 0:
            self.__inventory -= amount
        else:
            raise ValueError("Insufficient inventory")

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  # , saleNumber: int = 1):
        Sale.__saleTimes += 1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            # New addition: Reduce inventory for each product sold
            product[index].reduceInventory(1)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


# Example usage
productOne = Product(sale=None)
productTwo = Product(sale=None)

# Set initial inventory levels
productOne.setInventory(10)
productTwo.setInventory(5)

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print(f"{productOne.getLastSale.getSaleNumber}, {productTwo.getLastSale.getSaleNumber}")
print(f"ProductOne Inventory: {productOne.getInventory}, ProductTwo Inventory: {productTwo.getInventory}")
