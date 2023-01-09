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

    def sendMessage(self,chat_id:int,text:str):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            text: Text of the message to be sent
        returns:
            A message object
        """
        pass
    


