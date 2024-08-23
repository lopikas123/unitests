import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        # Проверяем успешность запроса
        if response.status_code == 200:
            data = response.json()
            # Предполагаем, что ответ содержит список с одним элементом
            if data and isinstance(data, list):
                return data[0].get('url')
        else:
            return None
    except requests.RequestException:
        return None