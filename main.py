shopping_dict = {
    "piekarnia": ["chleb", "pączek", "bułki", "bagietka"],
    "warzywniak": ["marchew", "pomidor", "ogórek"]
}

total_quantity = 0

for shop in shopping_dict:
    products = [item.capitalize() for item in shopping_dict[shop]]
    print(f"Idę do {shop.capitalize()} i kupuję tam: {', '.join(products)}.")
    total_quantity += len(products)

print(f"W sumie kupuję: {total_quantity} produktów.")

print("Greetings form the test branch !!")

# First test comment.

# Second test comment.
