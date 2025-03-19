from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.products_cart = products_cart
        self.location = location
        self.money = money
        self.car = Car(
            car["brand"],
            car["fuel_consumption"]
        )

    def have_enough_money_to_perform(self, cheapest_trip: float) -> bool:
        if self.money > cheapest_trip:
            self.money -= cheapest_trip
            return True
        return False

    bo