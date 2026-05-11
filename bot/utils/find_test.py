import requests
import json

# Твои данные из файла
INFINITY_API_URL = "https://infinity-check.online/find.php"
INFINITY_TOKEN = "R8fK2Lm9QWv3E7ZpD1yU4C6VtX5H0BJ3s"

DEPSEARCH_TOKEN = "WDTHx2vqZGE38gchBe7oAewzB9ZPNpxU"
DEPSEARCH_BASE_URL = "https://api.depsearch.sbs/"

BIGBASE_URL = "https://bigbase.top/api/search"
BIGBASE_TOKEN = "BOqMzQ63vPTPKs7gfUDrJru62SX2Jaqc"


def search_infinity(query):
    """Поиск через Infinity API"""
    headers = {
        "Authorization": f"Bearer {INFINITY_TOKEN}",
        "Content-Type": "application/json"
    }

    # Параметры запроса (уточни в документации сервиса)
    data = {
        "query": query,
        "limit": 10  # количество результатов
    }

    try:
        response = requests.post(
            INFINITY_API_URL,
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к Infinity: {e}")
        return None


def search_depsearch(query):
    """Поиск через Depsearch API"""
    headers = {
        "Authorization": f"Bearer {DEPSEARCH_TOKEN}",
        "Content-Type": "application/json"
    }

    # Пример эндпоинта (уточни в документации)
    url = f"{DEPSEARCH_BASE_URL}/search"

    params = {
        "q": query,
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к Depsearch: {e}")
        return None


def search_bigbase(query):
    """Поиск через Bigbase API"""
    headers = {
        "Authorization": f"Bearer {BIGBASE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "query": query,
        "page": 1,
        "limit": 20
    }

    try:
        response = requests.post(
            BIGBASE_URL,
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к Bigbase: {e}")
        return None


# Пример использования
if __name__ == "__main__":
    search_term = input("Введите поисковый запрос: ")

    print("\n🔍 Ищем в Infinity...")
    infinity_result = search_infinity(search_term)
    if infinity_result:
        print(json.dumps(infinity_result, indent=2, ensure_ascii=False))

    print("\n🔍 Ищем в Depsearch...")
    depsearch_result = search_depsearch(search_term)
    if depsearch_result:
        print(json.dumps(depsearch_result, indent=2, ensure_ascii=False))

    print("\n🔍 Ищем в Bigbase...")
    bigbase_result = search_bigbase(search_term)
    if bigbase_result:
        print(json.dumps(bigbase_result, indent=2, ensure_ascii=False))