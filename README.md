# stepik_final_task
The final task from "Автоматизация тестирования с помощью Selenium и Python" course

Если не хочешь, что при прогоне тестов появлялось окно браузера, укажи в терминале --headless=true

Для запуска тестов:
pytest -v --tb=line --language=en -m need_review test_main_page.py
pytest -v --tb=line --language=en -m need_review test_product_page.py