
class Cart:
    def __init__(self):
        self.__list_cart = {}

    def tambahProduk(self, namaProduk, quantity):
        try:
            qty = int(quantity)
        except Exception:
            print("Quantity must integer")
            return

        if namaProduk in self.__list_cart:
            self.__list_cart[namaProduk] = self.__list_cart[namaProduk]+qty
        else:
            self.__list_cart[namaProduk] = qty

    def hapusProduk(self, namaProduk):
        if namaProduk in self.__list_cart:
            del self.__list_cart[namaProduk]

    def tampilkanCart(self):
        for key, value in self.__list_cart.items():
            print(key +"("+ str(value)+")")