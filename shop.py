def calculate_item_cost(item):
    name, quantity, price = item
    return name, quantity * price

def calculate_totals(cart_costs):
    subtotal = sum(cost for _, cost in cart_costs)
    discount = 0
    if subtotal > 3000:
        discount = subtotal * 0.10
    tax = (subtotal - discount) * 0.05
    total = subtotal - discount + tax
    return subtotal, discount, tax, total

def get_user_input_cart():
    cart = []
    while True:
        try:
            item_name = input("Enter item name (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            quantity = int(input(f"Enter quantity for {item_name}: "))
            price = float(input(f"Enter price per unit for {item_name}: "))
            cart.append((item_name, quantity, price))
        except ValueError:
            print("Invalid input. Please enter valid numbers for quantity and price.")
    return cart

def display_bill(cart_costs, subtotal, discount, tax, total):
    print("\n--- Online Shopping Bill ---")
    for name, cost in cart_costs:
        print(f"{name:<20s} Cost: Rs {cost:.2f}")
    print("-" * 30)
    print("Subtotal: Rs.",subtotal)
    print('Discount (10%): Rs.',discount)
    print('GST (5%): Rs.',tax)
    print("-" * 30)
    print('Total: Rs.',total)
    print("----------------------------")

def main():
    user_cart = get_user_input_cart()
    if not user_cart:
        print("Cart is empty. Exiting.")
        return
    cart_costs = [calculate_item_cost(item) for item in user_cart]
    subtotal, discount, tax, total = calculate_totals(cart_costs)
    display_bill(cart_costs, subtotal, discount, tax, total)


if __name__ == "__main__":
    main()
