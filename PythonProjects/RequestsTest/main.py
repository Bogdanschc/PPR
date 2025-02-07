import requests

# База
trainer_token = "21ed94e42624da0892e589a1a9fb7f65"
host = "https://api.pokemonbattle.ru/v2"

# Хэдеры
headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

# Создание покемона
create_pokemon_data = {
    "name": "Боба",
    "photo_id": -1
}

create_response = requests.post(f"{host}/pokemons", json=create_pokemon_data, headers=headers)
print("Создание покемона:", create_response.json())

# Получаем ID созданного покемона
pokemon_id = create_response.json().get("id")

# Смена имени
if pokemon_id:
    update_pokemon_data = {
        "pokemon_id": str(pokemon_id),
        "name": "Биба",
        "photo_id": -1
    }
    update_response = requests.put(f"{host}/pokemons", json=update_pokemon_data, headers=headers)
    print("Обновление покемона:", update_response.json())

# Поймать покемона
if pokemon_id:
    catch_pokemon_data = {
        "pokemon_id": str(pokemon_id)
    }

    catch_response = requests.post(f"{host}/trainers/add_pokeball", json=catch_pokemon_data, headers=headers)
    print("Поймали покемона в покебол:", catch_response.json())
