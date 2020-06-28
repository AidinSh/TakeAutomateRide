from urllib.parse import urljoin
from requests import get, post, patch
from TakeRide import TakeRide


class DriverAPIs:
    def __init__(self, cellphone, ode):
        self.cellphone = cellphone
        self.ode = ode
        self.accept_token = None
        self.token = self.get_driver_token()

    def get_driver_token(self):
        body = {'client_id': 'android_293ladfa12938176yfgsndf',
                'client_secret': 'as;dfh98129-9111.*(U)jsflsdf',
                'grant_type': 'password',
                'username': self.cellphone,
                'password': '12345678'
                }
        header = {'Content-Type': 'application/json'}
        url = "https://driver-oauth-snapp-ode-{}.apps.private.teh-1.snappcloud.io/v1/auth".format(self.ode)
        r = post(url=url, json=body, headers=header)
        token = 'Bearer {}'.format(r.json()['access_token'])
        return token

    def driver_ride_accept(self):
        header = {'Content-Type': 'application/json',
                  'Authorization': self.token}
        url = "https://base-api-snapp-ode-{}.apps.private.teh-1.snappcloud.io/v2/driver/ride/{}/accept".format(self.ode, self.accept_token)
        r = patch(url=url, headers=header)
        print(r)
