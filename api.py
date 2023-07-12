import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON с уникальным ключем
        пользователя, найденного по указанным email и паролем"""

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат со списком найденных питомцев,
        совпадающих с фильтром. На данный момент фильтр принимает пустое значение - получить всех питомцев, либо
        'my pets' - получить список моих питомцев"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
