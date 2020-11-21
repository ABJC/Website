import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import json

class Mailchimp:
    def __init__(self):
        self.client = MailchimpMarketing.Client()
        self.client.set_config({
            "api_key": "44ad8d0b35971bba8bea7faa0e76980f-us7",
            "server": "us7"
        })

        # print(json.dumps(response, indent=2))

    def addSubscriber(self, fname: str, lname: str, mail: str) -> bool:        
        list_id = "f14ab28484"

        member_info = {
            "email_address": mail,
            "status": "pending",
            "merge_fields": {
                "FNAME": fname,
                "LNAME": lname
            }
        }

        try:
            self.client.lists.add_list_member(list_id, member_info)
            return True
        except:
            return False

# api = Mailchimp()
# success = api.addSubscriber("Test", "Test", "test@login.noahkamara.com")