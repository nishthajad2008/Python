og_price = float(input("Enter the Original price: $"))
discount = 0.15 * og_price
final_price = 0.85 * og_price
bool_price = final_price < 1000
print(f"Discount price is ${discount:.2f}")
print(f"The final price after discount is ${final_price:.2f}")
print(f"Final price below 1000? {bool_price}")
