from urllib.parse import urlencode
from urllib.request import Request, urlopen

class Bot:
    def __init__(self, token):
        self.__token = token
        self.url_api = f'https://api.telegram.org/bot{self.__token}'
    
    def _sendApi(self, method, data):
        url = f'{self.url_api}/{method}'
        print(url)
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
        return json
    
    def sendMessage(self, chat_id, text):
        post_fields = {
            'chat_id':chat_id,
            'text':text
        }

        self._sendApi('sendMessage', post_fields)
    
    def sendPhoto(self, chat_id, photo, 
                    caption=None, 
                    parse_mode='html'):
        post_fields = {
            'chat_id':chat_id,
            'photo':photo,
            'caption':caption,
            'parse_mode':parse_mode
        }

        self._sendApi('sendPhoto', post_fields)
