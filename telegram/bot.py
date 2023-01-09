# Imports libraries
import requests
class Bot:
    def __init__(self,token:str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"

    def getMe(self):
        """
        A simple method for testing your bot's auth token. Requires no parameters. 
        Returns basic information about the bot in form of a User object.
        """
        url = f'{self.base_url}getMe'
        # Requesting the url
        response = requests.get(url)
        # Converting the response to json
        response = response.json()
        # Returning the response
        return response



