import requests

url = 'https://reqres.in/api/'
uri_delete = url + 'users/2'


class TestDelete:
    def test_delete(self):
        responce = requests.delete(uri_delete)
        assert responce.status_code == 204
