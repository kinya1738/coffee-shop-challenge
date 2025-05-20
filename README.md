# coffee-shop-challenge

## Description

This project models a coffee shop system using Python's object-oriented programming principles. It includes three core classes:

- Customer: People who buy coffee.
- Coffee: Different coffee drinks available in the shop.
- Order: Each individual purchase, linking a customer to a coffee with a specific price.

The objective is to implement proper data validation, encapsulation, and relationships across these classes.

---

## Domain Model

### Entities and Validations

**Customer**

- Attributes:
  - `name`: Must be a string between 1 and 15 characters.
- Methods:
  - `orders()` – Returns a list of all `Order` instances associated with this customer.
  - `coffees()` – Returns a unique list of `Coffee` instances ordered by this customer.
  - `create_order(coffee, price)` – Creates a new order linked to this customer and a specified coffee at a given price.

**Coffee**

- Attributes:
  - `name`: Must be a string with at least 3 characters. Immutable after initialization.
- Methods:
  - `orders()` – Returns all `Order` instances for this coffee.
  - `customers()` – Returns a unique list of `Customer` instances who have ordered this coffee.
  - `num_orders()` – Returns the number of orders for this coffee.
  - `average_price()` – Returns the average price of all orders for this coffee.

**Order**

- Attributes:
  - `customer`: Must be a valid `Customer` instance.
  - `coffee`: Must be a valid `Coffee` instance.
  - `price`: Must be a float between 1.0 and 10.0. Immutable after initialization.
- Properties:
  - `customer` – Returns the customer who placed the order.
  - `coffee` – Returns the coffee associated with the order.

**Bonus Method (Optional)**

- `Customer.most_aficionado(coffee)` – Class method that returns the customer who spent the most on the given coffee.

---

## Project Structure

