orders = [
    {"customer": "Alice", "item": "Laptop", "quantity": 1, "price": 1200},
    {"customer": "Bob", "item": "Mouse", "quantity": 5, "price": 25},
    {"customer": "Alice", "item": "Keyboard", "quantity": 1, "price": 100},
    {"customer": "Charlie", "item": "Monitor", "quantity": 2, "price": 150},
    {"customer": "Bob", "item": "Desk", "quantity": 1, "price": 200},
    {"customer": "Charlie", "item": "Chair", "quantity": 4, "price": 50},
    {"customer": "Charlie", "item": "Chair", "quantity": 2, "price": 50},
    {"customer": "Charlie", "item": "Chair", "quantity": 3, "price": 50},
]
total_order_values = {}
for order in orders:
    customer = order["customer"]
    total_price = order["quantity"] * order["price"] 
    if customer in total_order_values:
        total_order_values[customer] =total_order_values[customer]+ total_price
    else:
        total_order_values[customer] = total_price
filtered_order_values = {customer: value for customer, value in total_order_values.items() if value > 100}
print(filtered_order_values)