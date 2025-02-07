import requests
from requests.auth import HTTPBasicAuth

# Конфигурация API
HOST = "https://your-api-host.com/rest/api/employees/upload/json"
USERNAME = "wbs_username"
PASSWORD = "wbs_password"

def test_upload_employee():
    print("Запуск теста...")
    print("Отправка запроса...")

    # Формирование тела запроса
    payload = {
        "company": "Example Company",  # ОБЯЗАТЕЛЬНО: название компании, в которую добавляется сотрудник
        "confirm": True,  # ОБЯЗАТЕЛЬНО: если true - импорт без подтверждения, если false - анализ перед импортом.
        "incrementUpdate": True,  # ОБЯЗАТЕЛЬНО: разрешение на инкрементальное обновление (True/False)
        "employees": [  # ОБЯЗАТЕЛЬНО: список сотрудников для загрузки
            {
                "tabNum": "Test_User_001",
                "names": [
                    {
                        "lang": "RU",
                        "surname": "Иванов",
                        "name": "Иван",
                        "middleName": "Иванович"
                    }
                ],
                "birthday": "1990-01-01",
                "citizenshipCode": "RU",
                "gender": "MALE",
                "auth": {
                    "login": "testuser@example.com",
                    "password": "securepassword123",
                    "policy": "SELF",
                    "roles": ["test_role"],
                    "activeUser": True,
                    "detailPolicies": [
                        {
                            "type": "USER",
                            "value": "123456"
                        }
                    ]
                },
                "contacts": [
                    {
                        "type": "PHONE",
                        "value": "+10000000000",
                        "primary": True
                    }
                ],
                "service": {
                    "homeCity": "Test City"
                }
            }
        ]
    }

    response = requests.post(
        HOST,
        json=payload,
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    print(f"Ответ от сервера: {response.status_code}")
    print(f"JSON-ответ: {response.json()}")

    assert response.status_code == 200, f"Ошибка! Ожидался статус 200, но получен {response.status_code}"

    response_json = response.json()

    # Проверка, что сотрудник был успешно создан, обновлен или данные не изменились
    assert response_json["employees"][0]["action"] in ["CREATED", "UPDATED", "NO_CHANGES"], \
        f"Ошибка! Ожидался 'CREATED', 'UPDATED' или 'NO_CHANGES', но получен {response_json}"

if __name__ == "__main__":
    test_upload_employee()
    print("Тест пройден успешно.")
