import pytest
import requests
from requests.auth import HTTPBasicAuth

# Конфигурация API
HOST = "https://your-api-host.com/rest/api/employees/upload/json"
USERNAME = "your_username"
PASSWORD = "your_password"

# ОБЯЗАТЕЛЬНЫЕ параметры: company, confirm, incrementUpdate, employees
@pytest.fixture
def employee_payload():
    """Фикстура для генерации тестового тела запроса"""
    return {
        "company": "Example Company",  # ОБЯЗАТЕЛЬНО: название компании
        "confirm": True,  # ОБЯЗАТЕЛЬНО: подтверждение внесения изменений
        "incrementUpdate": True,  # ОБЯЗАТЕЛЬНО: разрешение на инкрементальное обновление
        "employees": [  # ОБЯЗАТЕЛЬНО: список сотрудников
            {
                "tabNum": "Test_User_001",
                "names": [
                    {
                        "lang": "EN",
                        "surname": "Doe",
                        "name": "John",
                        "middleName": "Test"
                    }
                ],
                "birthday": "1990-01-01",
                "citizenshipCode": "XX",
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

def test_upload_employee(employee_payload):
    """Тест загрузки сотрудника через API"""

    response = requests.post(
        HOST,
        json=employee_payload,
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    # Проверяем, что API вернул код 200
    assert response.status_code == 200, f"Ошибка! Ожидался статус 200, но получен {response.status_code}"

    response_json = response.json()

    # Проверяем, что в ответе указано успешное состояние
    assert response_json["employees"][0]["action"] in ["CREATED", "UPDATED", "NO_CHANGES"], \
        f"Ошибка! Ожидался 'CREATED', 'UPDATED' или 'NO_CHANGES', но получен {response_json}"

