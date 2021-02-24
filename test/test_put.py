import requests

url = 'https://reqres.in/api/'
uri_put = url + 'users/2'

data_put_update = {
    "name": "morpheus",
    "job": "zion resident"
}


class TestPut:
    def test_put_update(self):
        responce = requests.put(uri_put, data_put_update)
        assert responce.status_code == 200
