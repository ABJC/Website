import requests
from jose import jwt
from datetime import datetime
from math import floor
import os

class ConnectAPI:
    def __init__(self):
        self.issuer = "aee29330-0d2a-4844-87ef-7ae92e10846a"
        self.secret = os.environ.get('CONNECT_PRIVATEKEY', None)
        self.kid = "BX7HTG9XK8"
        self.__token = None
        self.exp = datetime.now()

        self.app_id = "1538141397"
        self.beta_group_id = "ba171e4c-d684-4b71-b329-f3d2c90071de"

        self.__refresh_token__()

    def __refresh_token__(self):
        unix_timestamp = int(datetime.now().timestamp() + (19 * 60) )
        claims = {
            "iss": self.issuer,
            "exp": unix_timestamp,
            "aud": "appstoreconnect-v1"
        }
        self.__token = jwt.encode(claims=claims, key=self.secret, algorithm="ES256", headers={"kid": self.kid})

    def token(self):
        if self.exp <= datetime.now():
            self.__refresh_token__()
        return self.__token

    def invite_tester(self, email: str, fname: str, lname: str):
        url = "https://api.appstoreconnect.apple.com/v1/betaTesters"
        json = {
            "data": {
                "type": "betaTesters",
                "attributes": {
                    "email": email,
                    "firstName": fname,
                    "lastName": lname
                },
                "relationships": {
                    "betaGroups": {
                        "data": [
                            {
                                "id": self.beta_group_id,
                                "type": "betaGroups"
                            }
                        ]
                    }
                }
            }
        }

        headers = {
            "Authorization": f"Bearer {self.token()}"
        }

        response = requests.post(url=url, json=json, headers=headers)

        if response.status_code != 201:
            return False

        return True


