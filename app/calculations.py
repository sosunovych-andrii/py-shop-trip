from datetime import datetime
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


def purchase_info(
        customer: Customer,
        shop: Shop
) -> None:
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {current_time}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    total_price = 0
    for product_cart in customer.products_cart:
        for product in shop.products:
            if product_cart == product:
                price = customer.products_cart[product] * shop.products[product]
                if customer.have_enough_money_to_perform_operation(price):
                    total_price += price
                    print(f"{customer.products_cart[product_cart]} {product_cart}s for {price}")
    print(f"Total cost is {total_price} dollars")
    print("See you again!\n")
    print(f"{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars")
