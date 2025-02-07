import requests

# База
host = "https://api.pokemonbattle.ru/v2"
trainer_id = "16528"

# Проверка, что GET возвращает 200
def test_get_trainers_status():
    response = requests.get(f"{host}/trainers")
    assert response.status_code == 200, f"Ошибка! Ожидался код 200, а получен {response.status_code}"

# Проверка, что в ответе есть тренер с заданным trainer_id
def test_get_trainer_by_id():
    params = {"trainer_id": trainer_id}
    response = requests.get(f"{host}/trainers", params=params)
    
    assert response.status_code == 200, f"Ошибка! Ожидался код 200, а получен {response.status_code}"
    
    trainers_data = response.json().get("data", [])
    
    # Ищем нужного тренера в списке
    trainer = next((t for t in trainers_data if str(t.get("id")) == trainer_id), None)
    
    assert trainer, f"Ошибка! Тренер с id {trainer_id} не найден"
    assert "trainer_name" in trainer, "Ошибка! В ответе нет trainer_name"
    
    print(f"Тренер найден: {trainer['trainer_name']}")
