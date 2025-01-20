def add_product(product_list, name, price, quantity):
    product_info =  {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    product_list.append(product_info)
    print("Product added successfully!")
    
def total_inventory_value(product_list):
    total_value = 0
    for product in product_list:
        total_value += product['price'] * product['quantity']
        
    return total_value

def find_most_expensive_product(product_list):
    most_expensive_product = product_list[0]
    
    for product in product_list:
        if product["price"] > most_expensive_product["price"]:
            most_expensive_product = product
            
    return most_expensive_product

def search_product(product_list, name):
    for product in product_list:
        if product["name"] == name:
            return product
        
    return "Product not found!"