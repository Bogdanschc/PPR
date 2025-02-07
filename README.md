# 🛠️ API Autotests

Здесь я храню автотесты для различных API и планирую постепенно их дополнять.  
Тесты написаны на **Python** с использованием `pytest` и `requests`.

---

## 📂 Структура проекта

- **`OBT/`** – автотесты для **Online Booking System API**  
- **`RequestsTest/`** – автотесты для **Pokémons API**  

---

## 📌 Тесты в репозитории

### 🔹 OBT (Online Booking System API)

📂 **Папка:** `OBT/`  
**Тестируемый API:** `/employees/upload/json`  
Проверяет загрузку сотрудников с обязательными параметрами и валидирует ответ (`CREATED`, `UPDATED` или `NO_CHANGES`).

### 🔹 RequestsTest (Pokémons API)

📂 **Папка:** `RequestsTest/`  
**Тестируемый API:** `/v2/pokemons` и `/trainers/add_pokeball`  
Тестирует функциональность, проверяет создание, обновление и изменение покемонов.
