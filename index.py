def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        dis = price * (discount_percent / 100)
        finalPrice = price - dis
        print(f"The final price after discount is: {finalPrice:.2f}")
        return finalPrice
    else:
        print("Discount is less than 20%. No discount applied. Final price is:", price)
        return price

price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
calculate_discount(price, discount_percent)   
