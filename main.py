shopping_dict = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ["Marchew", "Pomidor", "Ogórek"]
}

for shop in shopping_dict:
    products = shopping_dict[shop]
    print(f"Idę do {shop} i kupuję tam {products}.")