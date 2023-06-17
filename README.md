# Коллок
## Амирханов Никита БПИ219

### Требования
 - Flask==2.3.2
 - Requests==2.31.0
 - SQLAlchemy==2.0.15
 - (Опционально) Докер

### Структура
 - `database.py` - Питон файл с объявлением БД
 - `init_script.py` - Питон файл для создания БД
 - `migrate.py` - Питон файл для первичного заполнения БД
 - `models.py` - Питон файл содержащий описание используемых сущностей (Отель, Бронь, Отзыв)
 - `server.py` - Основной файл для запуска АПИ
 - `test_post.py` - Питон файл для исполнения POST запросов `POST /bookings`, `POST /reviews`
### Запуск
#### Через докер
Есть докерфайл который в теории должен работать, но нет возможности проверить его работу
```sh
docker build -t hotel_app .
docker run -d -p 5000:5000 hotel_app
```
#### Руками
```sh
py init_script.py
py migrate.py
py server.py
```
Сервер будет запущен на `localhost:5000`. Можно выполнять запросы и получать json ответы
 - `POST /bookings` принимает параметры `hotel_id`:int, `in_date`:float (timestamp), `out_date`: float (timestamp)
 - `POST /reviews` принимает параметры `hotel_id`:int, `rating`:float, `text`:string 
