from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16", "+79000000001"),
    Smartphone("Samsung", "Galaxy S25", "+79000000002"),
    Smartphone("Xiaomi", "14 Ultra", "+79000000003"),
    Smartphone("Honor", "Magic7", "+79000000004"),
    Smartphone("Google", "Pixel 9", "+79000000005")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")