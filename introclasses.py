'''
Create a simple class
attributes - variables
methods - functions working usually with attributes
'''

print("Welcome! Today we have a 25% discount on all items. Please have a look around.")

class CashRegister:
    global rate # Here should be the global variables, they are accessible throughout the whole class
    rate = 0.078
    def __init__(self):  # after def is a space " "

        self.items = 0
        self.price = 0
        self.gold = 100
        self.discount = .25  # 80% as the price, so 20% is off
        self.taxes = .95

#Methods
    def update_register(self, price):  # Important to put the
        self.items += 1
        self.price += price

    def display_register(self):
        return print("Number of items = ", self.items, "\n Total price without taxes =", self.price,
                     'Rate of taxes', rate)

    def clear_register(self):
        CashRegister.final_price_tax(self)
        self.items = 0
        self.price = 0

    def discounted_price(self):
        self.price = self.price - self.price * self.discount
        return print('Discounted price is', self.price)


    def final_price_tax(self):
        self.price = (1 + rate)*self.price   ####same as self.price + self.price*rate
        return print('Final Price, taxes included =', round(self.price, 2))  #rounds 2 spots after decimal



    # def current_money(self):
    #     self.gold += register1.price
    #     print("You have", self.gold)
    #
    # def discounted(self):
    #     self.price = self.price * self.discount
    #     print("The discounted price is", self.price)
    #
    # def price_after_taxes(self):
    #     self.taxes = self.price * self.taxes
    #     print("The final taxed price is", self.taxes)




register1 = CashRegister()   # Don't forget ()
register1.update_register(7.84)
register1.update_register(50.50)
register1.update_register(100)

register1.display_register()

register1.clear_register()




# register2 = CashRegister()   #Creates another attribute
# register2.update_register(25000)
#
# register2.display_register()
# print(register2.items)
#
# register1.discounted()
# register1.price_after_taxes()
# #Show the money/profits
# print("Customer from register 1 has bought the items.")
# register1.current_money()
#
# #Clear
# print("Clear register 1 and 2")
# register1.clean_register()
#
# register2.clean_register()
#
# register1.display_register()
# register2.display_register()


