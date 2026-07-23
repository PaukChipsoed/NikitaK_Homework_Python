from address import Address
from mailing import Mailing

from_address = Address(
    "620000",
    "Екатеринбург",
    "Ленина",
    "10",
    "15"
)

to_address = Address(
    "101000",
    "Москва",
    "Тверская",
    "20",
    "8"
)

mail = Mailing(
    to_address,
    from_address,
    450,
    "AB123456789RU"
)

print(
    f"Отправление {mail.track} "
    f"из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)