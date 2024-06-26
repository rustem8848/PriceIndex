# Предсказание индекса потребительских цен на шесть месяцев  
  
Программа автоматически скачивает исторические данные индекса потребительских цен из сайта Федеральной службы государственной статистики и предсказывает значение на следующие шесть месяцев.  
  
  
## Инструкции по развертыванию Docker контейнера  
  
### Требования для запуска контейнера  
Для запуска проекта из образа price_index_app.tar необходимо наличие установленного Docker.  
  
### Установка Docker-образа  
1. Скачайте архивный файл Docker-образа price_index_app.tar на локальный компьютер.  
https://drive.google.com/drive/folders/17ejxtrIAr1j1eYxYYS7cWkkqNPpH2kST?usp=sharing  
2. Загрузите Docker-образ в Docker:  
docker load -i /path/to/ price_index_app.tar  
Замените /path/to/image.tar путем к загруженному архивному файлу Docker-образа на компьютере.  
3. Запуск:  
Запустите контейнер с загруженным Docker-образом:  
docker run -d -p 5000:5000 price_index_app.tar  
4. После запуска контейнера:  
Перейдите по адресу http://localhost:5000/ в браузере для доступа приложению.  
  
  
## Инструкции по развертыванию исходного кода  
  
### Требования для запуска исходного кода  
Для запуска проекта в исходном коде, убедитесь, что у вас установлены следующие зависимости:  
Python==3.9  
flask==2.0.3  
pandas==1.3.5  
numpy==1.21.5  
requests==2.28.1  
bokeh==3.4.0  
statsmodels==0.13.1  
scikit-learn==0.24.1  
werkzeug==2.1.2  
openpyxl==3.0.10  
  
### Установка приложения  
1. Скачайте проект:  
Скачайте ZIP-архив с проектом: https://github.com/rustem8848/PriceIndex  
Либо склонируйте репозиторий с проектом с помощью следующей команды:  
git clone https://github.com/rustem8848/PriceIndex.git  
2. При необходимости установите зависимости:  
Перейдите в директорию проекта и установите необходимые зависимости:  
pip install -r requirements.txt  
3. Запустите приложение:  
С помощью командной строки перейдите в корневую директорию проекта и выполните скрипт для запуска веб-приложения:   
python website.py  
  
  
## Использование  
1. Запуск проекта:  
После запуска контейнера или запуска приложения website.py откройте веб-браузер и перейдите по адресу http://localhost:5000/.  
2. Взаимодействие с приложением:  
Нажмите на кнопку "Проанализировать ИПЦ", чтобы скачать данные, отобразить графики и статистические данные ИПЦ.  
Будет выведена информация о максимальном и минимальном значении ИПЦ, среднем значении ИПЦ, а также индексы точности модели на тестовых данных.  
В таблице "Ретроспективный анализ надежности модели" представлены результаты оценки модели за предыдущие периоды.  
На графике отображены данные ИПЦ с предсказаниями и доверительным интервалом.  
3. Интерактивное взаимодействие с графиком:  
На графике вы можете скроллировать периоды, увеличивать и уменьшать масштаб для более детального анализа.  
4. Прогнозирование данных:  
После загрузки страницы, автоматически выводятся прогнозируемые значения ИПЦ на будущие месяцы.  
Следуя этим шагам, вы сможете воспользоваться функциональностью и анализировать данные ИПЦ с помощью веб-приложения.  
  
  
## Структура проекта
#### Проект PriceIndex содержит следующую структуру: 
* PricesIndex /:  
    * templates/: Директория для HTML-шаблонов веб-страниц.  
    * modeled_data/: Директория содержит модули для скачивания и подготовки данных  
        + initial_dataset.py: Скачивает исходный датасет с Росстата  
        + statistic_data.py: Подготавливает статистические данные на основе исходного датасета  
        + ml_model.py: На основании созданной модели прогнозирует показатели и производит оценку качества модели  
    * website_content/: Директория содержит модули формирования контента для сайта  
        + text_content.py: Формирует текстовый контент  
        + table_content.py: Формирует данные для таблицы о надежности модели  
        + graphic.py формирует график  
    * data_for_website.py: Формирует итоговый датасет для сайта. Использует модули из modeled_data  
    * website.py: Главный исполняемый файл для запуска веб-приложения. Использует модули из website_content  
* requirements.txt:  
Файл с перечислением зависимостей проекта, необходимых для установки.  
* README.md:  
Основной файл с описанием проекта, инструкциями по развертыванию и использованию.  
* Dockerfile:  
Файл для сборки Docker-образа  
  
### Структура итогового датасета для сайта, сформированного с помощью приложения data_for_website.py
#### Итоговый датасет, передаваемый из data_for_website.py в website.py представлен в виде списка. Обозначим его как dataset. Структура следующая   
* dataset[0] – статистические данные  
    * dataset[0][0] – информация о максимальном значении  
        * dataset[0][0][0] – максимальное значение  
        * dataset[0][0][1] – год  
        * dataset[0][0][2] – месяц  
    * dataset[0][1] информация о минимальном значении  
        * dataset[0][1][0] – минимальное значение  
        * dataset[0][1][1] – год  
        * dataset[0][1][2] – месяц  
        * dataset[0][2] – среднее значение  
* dataset[1] – оценка модели машинного обучения  
    * dataset[1][0] – оценки на тестовых данных  
        * dataset[1][0][0] – mae  
        * dataset[1][0][1] – rmse  
    * dataset[1][1] – ретроанализ надежности модели в виде списка из четырех параметров  
* dataset[2] – данные для графика в виде Series. ИПЦ за весь период + предсказанные на шесть месяцев  
* dataset[3] – доверительный интервал для предсказанных значений  
    * dataset[3][0] – нижние значения доверительного интервала  
    * dataset[3][1] – верхние значения доверительного интервала  
  

