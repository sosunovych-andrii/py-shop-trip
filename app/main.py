import json
from datetime import datetime
from app.customer import Customer
from app.shop import Shop
from app.calculations import calculate_trip_price

def shop_trip():
    with open("config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ) for customer in data["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in data["shops"]
    ]


    for customer in customers:
        print(f"{customer.name} has {customer.money} money")

        trip_prices = {}
        for shop in shops:
            trip_price = calculate_trip_price(customer, shop, fuel_price)
            print(f"{customer.name}'s trip"
                f" to the {shop.name} costs"
                f" {trip_price}"
            )
            trip_prices[shop.name] = trip_price

        closest_shop = min(trip_prices, key=trip_prices.get)
        cheapest_trip = min(trip_prices.values())

        if customer.have_enough_money_to_perform(cheapest_trip):
            print(f"{customer.name} rides to the {closest_shop}")
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {current_time}")
            print("You have bought:")
            print(f"Thanks {customer.name}, for your purchase!")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
