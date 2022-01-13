Инструкция по развёртыванию приложения:
---
1) Проверим, установлен ли postgresql. Если postgresql установлен, приступим к пункту 3.
```
psql --version
```
2) Установка postgresql:
```
sudo apt install postgresql
```
3) Зайдём в консоль postgres. Создадим базу данных, выполнив последовательно команды:
```
sudo -i -u postgres
psql
create database company
\q
```
4) Необходимо проверить наличие питона, для этого в терминале ввести команду ниже. Иначе пропустим пункт 4.
```
python3 --version
```
5) Если python3 не установлен, то установим его:
```
sudo apt-get install python3.9.5
```
6) Развернём виртуальное окружение. Для этого перейдём в директорию с проектом и последовательно выполним команды:
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -U -r requirements.txt
```
7) Выполним миграции:
```
python manage.py migrate
```
8) Запустим проект:
```
python manage.py runserver
```
