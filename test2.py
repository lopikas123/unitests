import pytest
from unittest.mock import patch
from main2 import get_random_cat_image


# Тест успешного запроса
def test_get_random_cat_image_success():
    # Создаем фиктивный ответ
    mock_response = [{"url": "https://example.com/cat.jpg"}]

    # Используем patch для замены requests.get на фиктивную функцию
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        url = get_random_cat_image()
        assert url == "https://example.com/cat.jpg"


# Тест неуспешного запроса (например, статус код 404)
def test_get_random_cat_image_failure():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = None

        url = get_random_cat_image()
        assert url is None