import requests

url = 'https://reqres.in/api/'
uri_get_list_users = url + 'users?page=2'
uri_get_single_user = url + 'users/2'
uri_get_single_user_not_found = url + 'users/23'
uri_get_list_resource = url + 'unknown'
uri_get_single_resource = url + 'unknown/2'
uri_get_single_resource_not_found = url + 'unknown/23'
uri_get_delayed_responce = url + 'users?delay=3'


class TestGet:
    def test_get_list_users(self):
        responce = requests.get(uri_get_list_users)
        assert responce.status_code == 200

    def test_get_single_user(self):
        responce = requests.get(uri_get_single_user)
        assert responce.status_code == 200

    def test_get_single_user_not_found(self):
        responce = requests.get(uri_get_single_resource_not_found)
        assert responce.status_code == 404

    def test_get_list_resource(self):
        responce = requests.get(uri_get_list_resource)
        assert responce.status_code == 200

    def test_get_single_resource(self):
        responce = requests.get(uri_get_single_resource)
        assert responce.status_code == 200

    def test_get_single_resource_not_found(self):
        responce = requests.get(uri_get_single_user_not_found)
        assert responce.status_code == 404

    def test_get_delayed_responce(self):
        responce = requests.get(uri_get_delayed_responce)
        assert responce.status_code == 200
