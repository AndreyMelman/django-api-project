# API управления собаками и породами
## Описание

### Этот проект представляет собой REST API для работы с собаками и их породами. API позволяет:
- Создавать, просматривать, обновлять и удалять собак.
- Создавать, просматривать, обновлять и удалять породы.
- Получать средний возраст собак по породам.
- Получать количество собак в каждой породе.

## Технологии
- Python 3.12+
- Django 4+
- Django REST Framework
- PostgreSQL
- Docker, Docker Compose
- Git
- dotenv (для хранения конфигураций в .env)

## Установка и запуск
1. Клонирование репозитория:
```bash
git clone https://github.com/AndreyMelman/django-api-project.git
```
2. Создание виртуального окружения (если без Docker):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```
3. Установка зависимостей:
```bash
pip install -r requirements.txt
```
4. Настройка окружения:
Создайте .env в корне проекта:
```bash
DEBUG=True
SECRET_KEY=your-secret-key
DB_DATABASE=name_db
DB_USER=name_user
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port
```
Пример .env в .env.example.

5. Применение миграций и создание суперпользователя:
```bash
python manage.py migrate
python manage.py createsuperuser
```
6. Запуск сервера:
```bash
python manage.py runserver
```

### Запуск в Docker
```bash
docker-compose up --build
```
### Использование API
Получение списка собак
```bash
GET /api/dogs/
```
Добавление собаки
```bash
POST /api/dogs/
```
Пример запроса:
```bash
{
  "name": "Rex",
  "age": 3,
  "breed": 1,
  "gender": "Male",
  "color": "Brown",
  "favorite_food": "Beef",
  "favorite_toy": "Ball"
}
```
Получение деталей собаки
```bash
GET /api/dogs/{id}/
```
Обновление собаки
```bash
PUT/PATCH /api/dogs/{id}/
```
Удаление собаки
```bash
DELETE /api/dogs/{id}/
```