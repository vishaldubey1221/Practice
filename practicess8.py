#task 1  : create  5 product 
product = {"Laptop":55000,
           "Mouse":500,
           "Keyboard":1200,
           "Monitor":15000,
           "Headphone":2500}
# print(product)
# task 2 :Find total price of all product 
# print(sum(product.values()))

#task 3 : Find product highest price 
# a = max(product.values())
# print(a)

# task 4 : update price mouse = 650
# product["Mouse"] = 650
# print("Change price of the mouse :",product)
product.pop("Keyboard")
print(product)


