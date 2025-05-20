class Coffee():
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) <3:
            raise TypeError("Name must be atleast 3 characters ")
        self._name = value

    def __repr__(self):
        return f"<coffee name='{self.name}'>"    
    
    def orders(self):
      from order import Order
      return [order for order in Order.all_orders if order.coffee == self]
    

    def customers(self):
      from order import Order
      return list({order.customer for order in Order.all_orders if order.coffee == self})

    def num_orders(self):
        from order import Order
        return len([order for order in Order.all_orders if order.coffee == self])
    
    def average_price(self):
        prices = "[order.price for order in Order.all_orders if order.coffee == self]"
        if not prices:
         return 0
        return sum(prices) / len(prices)




coffee1 = Coffee("mocha")
coffee2 = Coffee("latte")
coffee3 = Coffee("espresso")



print(coffee1)   