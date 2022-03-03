# stepik_final_task
The final task from "Автоматизация тестирования с помощью Selenium и Python" course

Если не хочешь, что при прогоне тестов появлялось окно браузера, укажи в терминале --headless=true

Для запуска тестов:

pytest -v --tb=line --language=en test_main_page.py

pytest -v --tb=line --language=en -m need_review test_product_page.py

Если при проверке шага 3 возвращает 1 failed, попробуй прогнать тесты еще раз. Я не знаю почему тесты падают при первом прогоне, я столкнулась с этим, проверяя работы других.  
