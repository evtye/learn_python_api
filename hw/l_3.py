import pytest
import requests
from requests import Response


class TestHW3:
    @pytest.mark.skip('#1')
    def test_phrase(self):
        phrase = 'dfggg'
        assert len(phrase) < 15, "Длина не меньше 15 символов"

    @pytest.mark.skip('#2')
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookies_dict = dict(response.cookies)
        assert "HomeWork" in cookies_dict, f'Нет поля homework'
        assert cookies_dict["HomeWork"] == "hw_value", "Неверное значение куки"

    @pytest.mark.skip('#3')
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        assert 'x-secret-homework-header' in response.headers
        assert response.headers['x-secret-homework-header'] == 'Some secret value'

    exclude_params = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like'
         ' Gecko) Version/4.0 Mobile Safari/534.30', {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
         ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 '
          'Mobile/15E148 Safari/604.1', {'platform': 'Mobile', 'browser': 'No', 'device': 'iOS'})
    ]

    @staticmethod
    def check_user_id(response: Response, key, value):
        assert key in response.json(), "Нет ключа в ответе"
        assert response.json()[key] == value, f"Фактическое значение поля {key} '{response.json()[key]}' " \
                                              f"не совпадает с ождаемым '{value}'"

    @pytest.mark.parametrize('user_agent, exp_values', exclude_params)
    def test_user_agent(self, user_agent, exp_values):
        data = {"User-agent": user_agent}
        expected_result = exp_values

        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers=data
        )

        for i in expected_result:
            self.check_user_id(response, i, expected_result[i])
