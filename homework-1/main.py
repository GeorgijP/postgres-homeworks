"""Скрипт для заполнения данными таблиц в БД Postgres."""

# Импортируем библиотеки
import psycopg2
import os
import csv

# Пароль храниться в переменной окружения
password = os.environ.get('PASSWORD_POSTGRESQL')

# Создаем списки для хранения данных
employees_data = []
custumers_data = []
orders_data = []

# Перекладываем данные из CSV файлов в словари
with open('north_data/employees_data.csv', 'r') as ed:
    data = csv.DictReader(ed)
    for i in data:
        employees_data.append(i)

with open('north_data/customers_data.csv', 'r') as cd:
    data = csv.DictReader(cd)
    for i in data:
        custumers_data.append(i)

with open('north_data/orders_data.csv', 'r') as od:
    data = csv.DictReader(od)
    for i in data:
        orders_data.append(i)

# Подключаемся к базе данных
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=password
)

# Передаем данные в базу
try:
    with conn:
        with conn.cursor() as cur:
            for i in range(len(employees_data)):
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s)', (employees_data[i]['first_name'],
                                                                                   employees_data[i]['last_name'],
                                                                                   employees_data[i]['title'],
                                                                                   employees_data[i]['birth_date'],
                                                                                   employees_data[i]['notes']))

            for i in range(len(custumers_data)):
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (custumers_data[i]['customer_id'],
                                                                          custumers_data[i]['company_name'],
                                                                          custumers_data[i]['contact_name']))

            for i in range(len(employees_data)):
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (orders_data[i]['order_id'],
                                                                               orders_data[i]['customer_id'],
                                                                               orders_data[i]['employee_id'],
                                                                               orders_data[i]['order_date'],
                                                                               orders_data[i]['ship_city']))
finally:
    conn.close()
