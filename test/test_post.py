import requests

url = 'https://reqres.in/api/'
uri_post_create = url + 'users'
uri_post_register_succesful = url + 'register'
uri_post_register_unsuccesful = url + 'register'

data_post_create = {
    "name": "morpheus",
    "job": "leader"
}
data_post_register_succesful = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
data_post_register_unsuccesful = {
    "email": "sydney@fife"
}


class TestPost:
    def test_post_create(self):
        response = requests.post(uri_post_create, data_post_create)
        assert response.status_code == 201

    def test_post_register_succesful(self):
        response = requests.post(uri_post_register_succesful, data_post_register_succesful)
        assert response.status_code == 200

    def test_post_register_unsuccesful(self):
        response = requests.post(uri_post_register_unsuccesful, data_post_register_unsuccesful)
        assert response.status_code == 400
