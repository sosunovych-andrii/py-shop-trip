import json
from app.customer import Customer
from app.shop import Shop
from app.calculations import calculate_trip_price, purchase_info


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"],
        )
        for customer in data["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_prices = {}
        for shop in shops:
            trip_price = calculate_trip_price(customer, shop, fuel_price)
            print(f"{customer.name}'s trip"
                  f" to the {shop.name} costs {trip_price}")
            trip_prices[trip_price] = shop

        cheapest_trip = min(trip_prices.keys())
        closest_shop = trip_prices[cheapest_trip]

        if customer.have_enough_money_to_perform_operation(cheapest_trip):
            customer.money -= cheapest_trip
            print(f"{customer.name} rides to the {shop.name}\n")
            purchase_info(customer, closest_shop)
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )


shop_trip()
