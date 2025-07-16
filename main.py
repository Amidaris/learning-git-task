shopping_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "pomidor", "ogórek"]
}

for shop in shopping_dict:
    products = [item.capitalize() for item in shopping_dict[shop]]
    print(f"Idę do {shop.capitalize()} i kupuję tam: {', '.join(products)}.")
