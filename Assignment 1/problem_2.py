# Simple Shopping Cart

cust_name = input("Customer's Name: ")

pdt_1 = input("\nProduct 1: ")
price_1 = int(input("Price: "))

pdt_2 = input("\nProduct 2: ")
price_2 = int(input("Price: "))

pdt_3 = input("\nProduct 3: ")
price_3 = int(input("Price: "))

subtotal = price_1 + price_2 + price_3

if subtotal >= 5000:
    discout = subtotal * 20 / 100
elif subtotal >= 3000:
    discout = subtotal * 10 / 100
elif subtotal >= 1000:
    discout = subtotal * 5 / 100
else:
    discout = 0

print(f"\nSubtotal: {subtotal:.0f}")
print(f"Discount: {discout:.0f}")
print(f"Final Total: {subtotal-discout:.0f}")



