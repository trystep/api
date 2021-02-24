import requests


def test_get_list_users():
    # Проверяем, что для существующей страницы код ответа = 200
    response = requests.get("https://reqres.in/api/users?page=3")
    assert response.status_code == 200


def test_get_single_user_negative():
    # Проверяем, что для несуществующего id будет код ответа = 404
    response = requests.get("https://reqres.in/api/users/11111111111111111111")
    assert response.status_code == 404
