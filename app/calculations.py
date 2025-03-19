from app.customer import Customer
from app.shop import Shop


def calculate_trip_price(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float:
    distance = (
        (shop.location[0] - customer.location[0]) ** 2 +
        (shop.location[1] - customer.location[1]) ** 2
    ) ** 0.5

    litres_used = distance * customer.car.fuel_consumption / 100

    trip_price = round(litres_used * fuel_price, 2)
    return trip_price
