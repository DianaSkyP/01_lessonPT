# Lesson 10 - PageObject with Allure Reporting

Этот проект содержит автоматизированные тесты с использованием паттерна PageObject и отчетности Allure.

## Структура проекта

```
lesson_10/
├── calculator_page.py    # Page Object для калькулятора
├── shop_pages.py         # Page Objects для интернет-магазина
├── test_calculator.py    # Тесты калькулятора
├── test_shop.py          # Тесты интернет-магазина
├── requirements.txt      # Зависимости проекта
└── README.md            # Документация проекта
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

### Обычный запуск тестов

```bash
# Запуск всех тестов
pytest

# Запуск конкретного теста
pytest test_calculator.py
pytest test_shop.py

# Запуск с подробным выводом
pytest -v
```

### Запуск тестов с генерацией отчета Allure

```bash
# Запуск тестов с генерацией Allure отчета
pytest --alluredir=allure-results

# Запуск с указанием конкретных тестов
pytest test_calculator.py --alluredir=allure-results
pytest test_shop.py --alluredir=allure-results
```

## Просмотр отчета Allure

### Установка Allure Commandline

**Windows:**
```bash
# Через Scoop
scoop install allure

# Или через Chocolatey
choco install allure
```

**macOS:**
```bash
# Через Homebrew
brew install allure
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install allure

# Или через Snap
sudo snap install allure
```

### Генерация и просмотр отчета

```bash
# 1. Запустить тесты с генерацией результатов
pytest --alluredir=allure-results

# 2. Сгенерировать HTML отчет
allure generate allure-results -o allure-report --clean

# 3. Открыть отчет в браузере
allure open allure-report
```

### Альтернативный способ (без установки Allure CLI)

```bash
# Запуск тестов
pytest --alluredir=allure-results

# Просмотр отчета через Python сервер
python -m http.server 8080 -d allure-results
# Затем открыть http://localhost:8080 в браузере
```

## Описание тестов

### test_calculator.py
- **Функция:** `test_calculator()`
- **Описание:** Тестирует функциональность калькулятора с задержкой
- **Шаги:**
  1. Открытие страницы калькулятора
  2. Установка задержки 45 секунд
  3. Выполнение операции 7 + 8
  4. Проверка результата (15)

### test_shop.py
- **Функция:** `test_shop_purchase()`
- **Описание:** Тестирует полный процесс покупки в интернет-магазине
- **Шаги:**
  1. Авторизация в системе
  2. Добавление товаров в корзину
  3. Переход в корзину
  4. Оформление заказа
  5. Проверка итоговой суммы

## Page Object классы

### CalculatorPage
- `open(url)` - открытие страницы калькулятора
- `set_delay(delay_value)` - установка задержки
- `click_button(button_text)` - нажатие кнопки
- `get_result()` - получение результата
- `wait_for_result(expected_result)` - ожидание результата

### LoginPage
- `open(url)` - открытие страницы авторизации
- `enter_username(username)` - ввод имени пользователя
- `enter_password(password)` - ввод пароля
- `click_login()` - нажатие кнопки входа
- `login(username, password)` - полный процесс авторизации

### MainPage
- `wait_for_page_load()` - ожидание загрузки страницы
- `add_to_cart(product_name)` - добавление товара в корзину
- `go_to_cart()` - переход в корзину

### CartPage
- `click_checkout()` - переход к оформлению заказа
- `get_cart_items_count()` - получение количества товаров
- `handle_alert_if_present()` - обработка уведомлений

### CheckoutPage
- `fill_personal_data(first_name, last_name, postal_code)` - заполнение данных
- `click_continue()` - продолжение оформления
- `get_total_price()` - получение итоговой суммы

## Особенности

- Все методы классов полностью документированы с указанием типов параметров и возвращаемых значений
- Использованы Allure декораторы для создания подробных отчетов
- Тесты разбиты на логические шаги с помощью `allure.step()`
- Добавлены проверки с детальным описанием в отчетах

## Требования

- Python 3.7+
- Chrome браузер
- ChromeDriver (автоматически управляется Selenium 4+)
