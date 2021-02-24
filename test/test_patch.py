import requests

url = 'https://reqres.in/api/'
uri_patch_update = url + 'users/2'

data_patch_update = {
    "name": "morpheus",
    "job": "zion resident"
}


class TestPatch:
    def test_patch_update(self):
        responce = requests.patch(uri_patch_update, data_patch_update)
        assert responce.status_code == 200
