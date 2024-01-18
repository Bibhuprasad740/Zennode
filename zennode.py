import math

products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50,
}

product_names = ["Product A", "Product B", "Product C"]

def get_checkout(cart, total_quantity, wrapping_price, total_price):
    discount_title = "Add some more items to the cart to get the discount"
    discount_amount = 0
    
    if total_price > 200:
        discount_title = "Flat $10 discount!"
        discount_amount = 10
    
    if total_quantity > 20:
        bulk10_discount_amount = total_price / 10.0
        if bulk10_discount_amount > discount_amount:
            discount_amount = bulk10_discount_amount
            discount_title = "Bulk 10 discount!"
    
    bulk_five_title = "Bulk 5 discount!"
    bulk_five_discount_amount = 0
    for product_name, (curr_qty, _) in cart.items():
        curr_price = products[product_name]
        if curr_qty > 10:
            bulk_price = curr_price * curr_qty
            bulk_five_discount_amount += (bulk_price / 20)
    if bulk_five_discount_amount > discount_amount:
        discount_amount = bulk_five_discount_amount
        discount_title = bulk_five_title
    
    tier50_discount_title = "Tiered 50 discount!"
    tiered50_discount_amount = 0
    if total_quantity > 30:
        for product_name, (curr_qty, _) in cart.items():
            curr_price = products[product_name]
            if curr_qty > 15:
                extra_qty = 15 - curr_qty
                tiered50_discount_amount += (extra_qty * curr_price / 2.0)
    if tiered50_discount_amount > discount_amount:
        discount_amount = tiered50_discount_amount
        discount_title = tier50_discount_title
    
    shipping_fee = math.ceil(total_quantity / 10.0) * 5
    
    print("\nYour Order details here:\n")
    
    print("PRODUCTS:\n")
    for product_name, (quantity, _) in cart.items():
        price = products[product_name]
        print(product_name)
        print("Quantity:", quantity)
        print("Total Price:", (price * quantity), "\n")
    print("Sub Total:", total_price, "\n")
    
    print("Discount:\n", discount_title)
    print("Discount Amount: $", discount_amount, "\n")
    
    print("Shipping and Wrapping Fee:\n")
    print("Shipping fee: $", shipping_fee)
    print("Wrapping fee: $", wrapping_price, "\n")
    print("Total: $", (total_price - discount_amount) + shipping_fee + wrapping_price)

def is_valid(s):
    return s.upper() in ("YES", "NO")    

if __name__ == "__main__":
    cart = {}
    total_quantity = 0
    wrapping_price = 0
    total_price = 0
    for product_name in product_names:
        quantity = int(input(f"\nHow many {product_name} you want to buy: "))
        total_quantity += quantity
        total_price += (quantity * products[product_name])
        should_wrap = ""
        while not is_valid(should_wrap):
            should_wrap = input(f"\nDo you want {product_name} to be wrapped? (yes or no): ")
            if not is_valid(should_wrap):
                print("Invalid input! Please write Yes or no")
        wrapping_price += (len(should_wrap) == 3)
        cart[product_name] = (quantity, len(should_wrap) == 3)
    get_checkout(cart, total_quantity, wrapping_price, total_price)


