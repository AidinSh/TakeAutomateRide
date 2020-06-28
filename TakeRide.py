from hashlib import sha1
from APIs.PassengerAPIs import PassengerAPIs
from APIs.DriverAPIs import DriverAPIs


class TakeRide:

    def __init__(self, passenger_email, passenger_pass, driver_cellphone, driver_id, ode):
        passenger = PassengerAPIs(email=passenger_email, password=passenger_pass, ode=ode)
        driver = DriverAPIs(cellphone=driver_cellphone, ode=ode)
        self.driver_id = driver_id
        self.hri = passenger.passenger_ride()
        self.driver_accept_token = self.create_accept_token()
        driver.accept_token = self.driver_accept_token

    def create_accept_token(self):
        hash_items = "#di12" + self.driver_id + self.hri
        token_hash = sha1(hash_items.encode())
        token = f"{token_hash}__{self.hri}"
        print(token)
        return token

    #def accept_ride(self):


TakeRide(passenger_email="test350@test.com", passenger_pass=12345678, driver_id="125", driver_cellphone="09990000125", ode="009").create_accept_token()
