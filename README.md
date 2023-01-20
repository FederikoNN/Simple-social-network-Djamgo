# Простая соцсеть с комментариями и фотографиями

## Задача: 
Реализовать соцсеть с комментариями и фотографиями.
Соцсеть должна содержать в себе:
1. авторизацию пользователя
2. поддерживать и отображать публикацию фотографий пользователя
3. добавления комментарий к фото
4. рейтингк фото и комментариям
5. топ 10 фотографий авторов по рейтингу
6. возможность подписаться на автора и вывести подписки, только на подписанных авторов. 

### Дополнительно: 
Чат в реальном времени с возможностью просматривать в чате все сообщения из админки.

### Сторонние библиотеки:
Только при усложнении (socketio)

### Стек: 
1. django_rest_framework

### Срок исполнения:
Без усложнений: 3 дня + 1 день на исправления

# Простая соцсеть с комментариями и фотографиями
## Установка pipenv:

```
pip install pipenv
```

## Установка зависимостей:

```
pipenv install
```

## Создание оболочки виртуальной среды:

```
pipenv shell
```
## Провести миграцию:

```
python manage.py makemigrations
python manage.py migrate
```

## Создать суперпользователя:

```
python manage.py createsuperuser
```

## Запуск веб-сервера проекта:

```
python manage.py runserver
```

## Инструкция по использованию:

1. Главная страница: ```../```
2. Регистрация пользователя: ```../register/```
3. Авторизация пользователя: ``../login/``
4. Публикация фотографии:```../post_creation_page/```
5. Просмотр фотографии с возможностью оформления подписки на автора, просмотра и добавления комментариев и лайков: ```../<int:pk>/post_single_page/```
6. ТОП-10 фотографий по рейтингу: ```../top10```
7. Просмотр оформленных подписок: ```../subscribe/```
8. API доступ к списку фотографий (сортировка по дате создания: ```..api/posts/```
9. API доступ к отдельной фотографии: ```../api/posts/<int:pk>```
10. API доступ к списку пользователей (сортировка по ID): ```api/users/```
11. API доступ к отдельному пользователю: ```..api/users/<int:pk>```

## Проверить работу проекта.