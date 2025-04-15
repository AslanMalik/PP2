

import csv
import psycopg2


def connect_db():
    return psycopg2.connect(
        dbname="suppliers",       
        user="postgres",
        password="Python2006!",   
        host="localhost",
        port="5432"
    )



def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("✅ Таблица создана.")
    except Exception as error:
        print("❌ Ошибка:", error)


# --- Вставка с input ---
def insert_from_input():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s);", (name, phone))
                print("✅ Контакт добавлен.")
    except Exception as error:
        print("❌ Ошибка:", error)


# --- Вставка из CSV ---
def insert_from_csv():
    filename = input("Введите имя CSV-файла (например, phonebook_data1.csv): ")
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s);", (row['name'], row['phone']))
                print("✅ Данные из CSV добавлены.")
    except Exception as error:
        print("❌ Ошибка:", error)


# --- Обновление данных ---
def update_contact():
    print("1 - Изменить имя\n2 - Изменить телефон")
    choice = input("Выберите действие: ")
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    old_name = input("Старое имя: ")
                    new_name = input("Новое имя: ")
                    cur.execute("UPDATE phonebook SET name = %s WHERE name = %s;", (new_name, old_name))
                    print("✅ Имя обновлено.")
                elif choice == '2':
                    name = input("Имя: ")
                    new_phone = input("Новый телефон: ")
                    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s;", (new_phone, name))
                    print("✅ Телефон обновлён.")
    except Exception as error:
        print("❌ Ошибка:", error)


# --- Удаление ---
def delete_contact():
    print("1 - Удалить по имени\n2 - Удалить по номеру")
    choice = input("Выберите: ")
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    name = input("Имя: ")
                    cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
                elif choice == '2':
                    phone = input("Телефон: ")
                    cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
                print("✅ Контакт удалён.")
    except Exception as error:
        print("❌ Ошибка:", error)


# --- Вывод всех записей ---
def select_all():
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone FROM phonebook ORDER BY id;")
                rows = cur.fetchall()
                print("📞 Телефонная книга:")
                for row in rows:
                    print(f"{row[0]}. {row[1]} — {row[2]}")
    except Exception as error:
        print("❌ Ошибка:", error)


# --- Меню ---
if __name__ == '__main__':
    while True:
        print("\n📘 Меню:")
        print("1 - Создать таблицу")
        print("2 - Добавить контакт вручную")
        print("3 - Загрузить контакты из CSV")
        print("4 - Обновить контакт")
        print("5 - Удалить контакт")
        print("6 - Показать все контакты")
        print("0 - Выход")

        option = input("Выбор: ")
        if option == '1':
            create_table()
        elif option == '2':
            insert_from_input()
        elif option == '3':
            insert_from_csv()
        elif option == '4':
            update_contact()
        elif option == '5':
            delete_contact()
        elif option == '6':
            select_all()
        elif option == '0':
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор.")
