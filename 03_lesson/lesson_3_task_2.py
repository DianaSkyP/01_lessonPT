from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 13Pro", "+77001112233"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+77072223344"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+77773334455"))
catalog.append(Smartphone("Google", "Pixel 7", "+7004445566"))
catalog.append(Smartphone("OnePlus", "11", "+789005556677"))


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")