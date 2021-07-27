quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}
groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}
for item in groceries:
    print(
        # f"{item}: {quantity[item]} @ ${groceries[item]}. Total is ${round(quantity[item] * groceries[item], 2)}")
        f"{item}: {quantity[item]} @ ${groceries[item]}. Total is ${quantity[item] * groceries[item]:.2f}")
    # 2 is the way to say how many decimal points you need
