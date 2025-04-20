import psycopg2
import csv

# === Настройка подключения ===
try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="lab 10",        # Название твоей базы данных
        user="postgres",       # Имя пользователя (обычно postgres)
        password="140506",  # 🔐 ЗАМЕНИ на свой пароль
        port=5432
    )
    cur = conn.cursor()
    print("✅ Успешное подключение к базе данных.")
except Exception as e:
    print("❌ Ошибка подключения к базе:", e)
    exit()

# === Создание таблицы ===
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
""")
conn.commit()

# === Основные функции ===
def load_from_csv(path):
    try:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("✅ Данные из CSV успешно загружены.")
    except Exception as e:
        print("❌ Ошибка загрузки из CSV:", e)

def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("✅ Данные добавлены.")

def update_data():
    name = input("Введите имя, которое хотите обновить: ")
    new_phone = input("Введите новый номер телефона: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("✅ Данные обновлены.")

def query_data():
    filter_name = input("Введите имя (или часть): ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{filter_name}%",))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("❗ Записей не найдено.")

def delete_data():
    value = input("Введите имя или номер для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    print("✅ Запись удалена (если была найдена).")

# === Меню ===
def menu():
    while True:
        print("\n📘 Меню:")
        print("1. Загрузить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить запись")
        print("4. Поиск записей")
        print("5. Удалить запись")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            path = input("Введите путь к CSV файлу: ")
            load_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "0":
            break
        else:
            print("❌ Неверный выбор.")

# === Запуск ===
if __name__ == "__main__":
    menu()
    cur.close()
    conn.close()
    print("📦 Соединение закрыто.")
