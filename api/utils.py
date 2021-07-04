import requests

import json

class GetStackExchange:

    EP = 'https://api.stackexchange.com/2.3/{}'  

    def get_all_questions(self, page, order="desc", sort="activity", site="stackoverflow"):
        param={
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('questions'), params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Other error occurred: {err}')


    def search(self, page, tagged, order="desc", sort="activity", site="stackoverflow"):
        param={
            "tagged" : "python",
            "page": page,
            "order": order,
            "sort" : sort,
            "site" : "stackoverflow"
        }
        try:
            response = requests.get(self.EP.format('search'), params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Other error occurred: {err}')