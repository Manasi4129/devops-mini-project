def calculate_total(price, quantity):
    subtotal = price * quantity
    discount = subtotal * 0.10
    return subtotal + discount


if __name__ == "__main__":
    print("ShopSmart Checkout")
    print(calculate_total(10, 3))