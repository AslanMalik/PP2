

import csv
import psycopg2
import re 

def connect_db():
    return psycopg2.connect(
        dbname="suppliers",       
        user="postgres",
        password="Python2006!",   
        host="localhost",
        port="5432"
    )

def create_sql_objects():
    sql_code = """
    CREATE OR REPLACE FUNCTION insert_many_users_return_bad(
        names TEXT[],
        phones TEXT[]
    )
    RETURNS TABLE(bad_name TEXT, bad_phone TEXT)
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INT := 1;
    BEGIN
        WHILE i <= array_length(names, 1) LOOP
            IF phones[i] ~ '^\\+\\d[\\d\\s\\-]{9,15}$' THEN
                INSERT INTO phonebook(name, phone)
                VALUES (names[i], phones[i])
                ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;
            ELSE
                -- Возвращаем плохую запись
                bad_name := names[i];
                bad_phone := phones[i];
                RETURN NEXT;
            END IF;
            i := i + 1;
        END LOOP;
    END;
    $$;



    CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
            UPDATE phonebook
            SET phone = p_phone
            WHERE name = p_name;
        ELSE
            INSERT INTO phonebook(name, phone)
            VALUES (p_name, p_phone);
        END IF;
    END;
    $$;





    CREATE OR REPLACE PROCEDURE delete_contact_by_name_or_phone(
        p_name TEXT,
        p_phone TEXT
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        -- Если передано имя, удаляем по имени
        IF p_name IS NOT NULL THEN
            DELETE FROM phonebook WHERE name = p_name;
        END IF;

        -- Если передан номер, удаляем по номеру
        IF p_phone IS NOT NULL THEN
            DELETE FROM phonebook WHERE phone = p_phone;
        END IF;
    END;
    $$;



    CREATE OR REPLACE FUNCTION find_pattern(p_pattern TEXT)
    RETURNS TABLE (id INT, name TEXT, phone TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT pb.id, pb.name::TEXT, pb.phone::TEXT
        FROM phonebook pb
        WHERE pb.name LIKE '%' || p_pattern || '%'
        OR pb.phone LIKE '%' || p_pattern || '%'
        ORDER BY pb.id;
    END;
    $$;




    CREATE OR REPLACE FUNCTION limit_offset(p_limit INT, p_offset INT)
    RETURNS TABLE (id INT, name TEXT, phone TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT pb.id, pb.name::TEXT, pb.phone::TEXT FROM phonebook pb
        ORDER BY pb.id
        LIMIT p_limit OFFSET p_offset;
    END;
    $$;


    """
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(sql_code)
                print("✅ SQL-функции и процедуры успешно созданы.")
    except Exception as error:
        print("❌ Ошибка при создании SQL-объектов:", error)



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


# Ищем по патерну
def pattern_thing():
    pattern_symbol = input("Input pattern: ")
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                    cur.execute("SELECT * FROM find_pattern(%s);", (pattern_symbol,))
                    rows = cur.fetchall()
                    for row in rows:
                        print(f"{row[0]}.  {row[1]}-{row[2]}")
    except Exception as error:
        print("Ошибка: ", error)

# Проверка
def insert_or_update_user():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")

    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
                print("✅ Процедура выполнена.")
    except Exception as error:
        print("❌ Ошибка:", error)

def insert_many():
    names = ['Error', 'Erro1r', 'Error2', 'Error3']
    phones = ['+77071112233', 'notaphone', '123', '77778889900']

    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM insert_many(%s, %s);", (names, phones))
                bad_rows = cur.fetchall()

                if bad_rows:
                    print("❌записи:")
                    for name, phone in bad_rows:
                        print(f" - {name} : {phone}")
                else:
                    print("✅")
    except Exception as error:
        print("❌", error)


def limit_offset():
    try:
        limit = int(input("Введите лимит: "))
        offset = int(input("Введите offset: "))
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM limit_offset(%s, %s);", (limit, offset))
                rows = cur.fetchall()
                for row in rows:
                    print(f"{row[0]}.  {row[1]}-{row[2]}")
    except Exception as error:
        print("❌ Ошибка:", error)


def call_delete_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact_by_name_or_phone(%s, %s);", (name, phone))
                print("✅ Контакт удалён")
    except Exception as error:
        print("❌ Ошибка при удалении:", error)



# --- Меню ---
if __name__ == '__main__':

    create_sql_objects()

    while True:
        print("\n📘 Меню:")
        print("1 - Создать таблицу")
        print("2 - Добавить контакт вручную")
        print("3 - Загрузить контакты из CSV")
        print("4 - Обновить контакт")
        print("5 - Удалить контакт через Пайтон")
        print("6 - Показать все контакты")
        print("7 - Ищем по патерну")
        print("8 - Проверяем контакт")
        print("9 - Процедура")
        print("10 - Limit and Offset")
        print("11 - Удалить контакт через PostgreSQL")
        print("0 - Выход")

        option = int(input("Выбор: "))
        if option == 1:
            create_table()
        elif option == 2:
            insert_from_input()
        elif option == 3:
            insert_from_csv()
        elif option == 4:
            update_contact()
        elif option == 5:
            delete_contact()
        elif option == 6:
            select_all()
        elif option == 7:
            pattern_thing()
        elif option == 8:
            insert_or_update_user()
        elif option == 9:
            insert_many()
        elif option == 10:
            limit_offset()
        elif option == 11:
            call_delete_contact()
        elif option == 0:
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор.")
