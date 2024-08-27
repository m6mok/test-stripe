# Проект Пример использования StripeAPI
## Описание
Небольшой сайт по оплате предметов Item при помощи сервиса Stripe.

URL по взаимодействию:

- /admin/api/item/ - административная панель для создания предметов Item;
- /item/{id} - обзор и интерфейс для оплаты уже существующего предмета Item;
- /buy/{id} - API-интерфейс для создания Stripe-сессии по оплате Item, выдаёт ответ {session_id: str}

## Требования к запуску
1. Наличие приложения Docker: https://docs.docker.com/engine/install/
2. Наличие приложения Make:
    - Debian/Ubuntu
        ```sh
        apt install make
        ```
    - Fedora/RHEL
        ```sh
        yum install make
        ```
    - Arch/Manjaro
        ```sh
        pacman -S make
        ```
3. (опционально) Для разработки рекомендеутся использовать утилиту UV: https://docs.astral.sh/uv/getting-started/installation/

## Как запустить локально
```sh
# Определение файла виртуального окружения проекта
cp ./env/production/project.env.dev ./env/production/project.env

# Заполнение переменных окружения при помощи текстового редактора
# Подразумевается, что уже имеются нужные ключи к сервису Stripe
# В том числе идёт заполнение реквизитов суперпользователя по умочанию
vi ./env/local/project.env

# Короткий запуск docker compose
make up
```

## Как запустить в продакшн
```sh
# Определение файла виртуального окружения проекта
cp ./env/production/.env.dev ./env/production/.env

# Заполнение переменных окружения при помощи текстового редактора
# Подразумевается, что уже имеются нужные ключи к сервису Stripe
# В том числе идёт заполнение реквизитов суперпользователя по умочанию
# Подразумевается, что уже запущенн сервис PostgreSQL, и для него имеются соответствующие реквизиты
vi ./env/production/.env

# Короткий запуск docker compose
make prod
```

## Как начать разработку на Python с UV
Разработка велась на операционной системе Ubuntu 24.04, по причине чего используются команды, описанные ниже. Для других операционных систем процесс разработки может вестись иначе.
```sh
# установка Python версии 3.10
uv python install 3.10

# создание виртуального окружения с Python версии 3.10
uv venv -p $(uv python list | grep 3.10 | awk '{print $2}' | head -n 1)

# активация виртуального окружения
source .venv/bin/activate

# установка зависимостей pip
uv pip install -r ./requirements.txt
```
