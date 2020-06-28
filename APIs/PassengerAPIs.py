import os
from requests import post, get, patch


class PassengerAPIs:

    def __init__(self, email, password, ode):
        self.email = email
        self.password = password
        self.ode = ode
        self.token = self.passenger_get_token()
        self.hri = self.passenger_ride()

    def passenger_get_token(self):
        header = {'Content-Type': 'application/json'}
        body = {"grant_type": "password",
                'client_id': "ios_sadjfhasd9871231hfso234",
                'client_secret': "23497shjlf982734-=1031nln",
                'username': "{}".format(self.email),
                'password': "{}".format(self.password)}
        url = "https://passenger-oauth-snapp-ode-{}.apps.private.teh-1.snappcloud.io/v1/auth".format(self.ode)
        response = post(url=url, headers=header, json=body)
        token = "Bearer {}".format(response.json()['access_token'])
        return token

    def passenger_ride(self):
        header = {'Content-Type': 'application/json', 'Authorization': self.token}
        body = {'origin_lat': 35.7787340000,
                'origin_lng': 51.413938000,
                'destination_lat': 35.731114818832828,
                'destination_lng': 51.321558939002366,
                'round_trip': False,
                'is_paid_by_recipient': False,
                'destination_place_id': 0,
                'service_type': 1,
                'services': False,
                'waiting': "",
                'is_for_friend': False,
                'friend_info': {
                    'name': "",
                    'cellphone': ""
                }
                }
        url = "https://base-api-snapp-ode-{}.apps.private.teh-1.snappcloud.io/v2/passenger/ride".format(self.ode)
        response = post(url=url, json=body, headers=header)
        hri = response.json()['data']['ride_id']
        return hri

