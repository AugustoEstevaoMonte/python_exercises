more_selled = {'tecnology': 'iphone', 'refrigerator': 'brastemp', 'food': 'pizza', 'library': 'the alchemist'}
selled_tecnology = {'iphone': 100, 'samsung': 50, 'xiaomi': 30, 'asus': 9000, 'ipad': 100000}

for item_name, description in more_selled.items():
    if item_name.lower() == 'library':
        print(description)

for brand, selled_quantity in selled_tecnology.items():
    if brand.lower() == 'asus' or brand.lower() == 'ipad':
        print("The {} it's sold for {} U$".format(brand, selled_quantity))
