import sqlite3


def create_database():
    pass


def register_new_user(user, password):
    try:
        conn = sqlite3.connect('admin_database.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users_and_passwords \
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
                    user VARCHAR(20), \
                    password VARCHAR(20))')
        check = cur.execute(f'SELECT user FROM users_and_passwords\
                            WHERE user = "{user}"')
        check = check.fetchall()
        if len(check) != 0:
            return False
        cur.execute(f'INSERT INTO users_and_passwords (user, password) \
                    VALUES ("{user}", "{password}")')
        conn.commit()
        cur.close()
        conn.close()
        conn = sqlite3.connect('C:/Users/thoma/Documents/GitHub/'
                               'family_finances/databases usuários/'
                               f'{user}_database.db')
        conn.commit()
        conn.close()
    except Exception:
        return False
    else:
        return True


def check_user(login, password):
    conn = sqlite3.connect('admin_database.db')
    cur = conn.cursor()
    try:
        check = cur.execute(f'SELECT user, password FROM users_and_passwords\
                            WHERE user = "{login}" and \
                            password = "{password}"')
        check = check.fetchall()
    except Exception:
        return False
    else:
        if len(check) == 0:
            return False
        else:
            return True
    finally:
        cur.close()
        conn.close()


def table_exists(db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        check = cur.execute(f'SELECT name FROM sqlite_sequence \
                            WHERE name="{table_name}"')
        check = check.fetchall()
        cur.close()
        conn.close()
    except Exception:
        return False
    else:
        if len(check) == 0:
            return False
        else:
            return True


print(table_exists('admin_database.db', 'users_and_passwords'))
print(register_new_user('thomaz', 123456))
print(table_exists('admin_database.db', 'users_and_passwords'))
