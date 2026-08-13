item=input("enter the item you want to order: ")
price=float(input("what is the price:  "))
quantity=int(input("how many would you like: "))
total=price*quantity
print("_________________________________________________________________")


print(f"you have brough: {quantity,} X {item}/s")
print(f"your total price is ${total}")