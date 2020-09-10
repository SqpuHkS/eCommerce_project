import requests

from conf import (
    MAILCHIMP_API_KEY,
    MAILCHIMP_DATA_CENTER,
    MAILCHIMP_EMAIL_LIST_ID
)



class MailChimp(object):
    def __init__(self):
        super(MailChimp, self).__init__()
        self.key = MAILCHIMP_API_KEY
        self.api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
        self.list_id = MAILCHIMP_EMAIL_LIST_ID

    def check_subscription_status(self, email):
        endpoint = ''
        r = requests.get(endpoint, auth=('', self.key))
        return r.json()

    def add_email(self, email):
        data = {
            'email': email
        }
        endpoint = self.api_url
        r = requests.post(endpoint, auth=('', self.key), data=data)
        return r.json()