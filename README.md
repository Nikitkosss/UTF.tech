Задание

Тестовое задание backend разработчик UTF.tech
Стек Django\DRF
Даны модели "Категория Блюд" и "Блюдо" для ресторана.
Даны сериализаторы.
В выборку попадают только Блюда у которых is_publish=True.
Если в категории нет блюд (или все блюда данной категории имеют is_publish=False) - не включаем ее в выборку.
Запрос в БД сделать любым удобным способом:
Django ORM (предпочтительно), Raw SQL, Sqlalchemy…
Написать View который вернет для API 127.0.0.1/api/v1/foods/

Установка
```
git clone https://github.com/Nikitkosss/UTF.tech.git
python -m venv venv
pip intall -r requirements.txt
cd django_task
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
