from customer import Customer
from coffee import Coffee


class Order:
    all_orders = []

    
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee.")
        if not isinstance(price,  float):
            raise TypeError("Price must be a float.")
        if not (1.0 <= price <= 10.0):
            raise TypeError("Price should be between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer
                  
    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"<Order customer={self.customer.name} coffee={self.coffee.name} price={self.price}>"               
    

