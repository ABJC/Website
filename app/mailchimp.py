import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import json
import os


class Mailchimp:
    def __init__(self):
        api_key = os.environ.get('MAILCHIMP_APIKEY', None)
            
        if api_key == None:
            raise Exception("No API Key Specified")


        self.client = MailchimpMarketing.Client()
        self.client.set_config({
            "api_key": api_key,
            "server": "us7"
        })

        # print(json.dumps(response, indent=2))

    def addSubscriber(self, email: str, fname: str, lname: str) -> bool:        
        list_id = "f14ab28484"

        member_info = {
            "email_address": email,
            "status": "pending",
            "merge_fields": {
                "FNAME": fname,
                "LNAME": lname
            }
        }

        try:
            self.client.lists.add_list_member(list_id, member_info)
            return True
        except ApiClientError as e:
            return False

# api = Mailchimp()
# success = api.addSubscriber("Test", "Test", "test@login.noahkamara.com")