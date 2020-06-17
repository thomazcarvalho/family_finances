import sqlite3


def create_database():
    pass


def register_new_user(user, password):
    try:
        conn = sqlite3.connect('admin_database.db')
        cur = conn.cursor()
        breakpoint
        cur.execute('CREATE TABLE users_and_passwords IF NOT EXISTS ('
                    'id PRIMARY KEY AUTOINCREMENT NOT NULL,'
                    'user VARCHAR(20),'
                    'password VARCHAR(20)'
                    ')')
        cur.execute('INSERT INTO users_and_passwords (user, password) '
                    f'VALUES ({user}, {password}) ')
        conn.commit()
        conn = sqlite3.connect('C:/Users/thoma/Documents/GitHub/'
                               'family_finances/databases usuários/'
                               f'{user}_database')
        conn.commit()
    except Exception:
        return False
    else:
        return True


def check_user(login, password):
    conn = sqlite3.connect('admin_database.db')
    cur = conn.cursor()
    check = cur.execute('SELECT user, password FROM users_and_passwords'
                        f'WHERE user = {login} and password = {password}')
    if check == 1:
        return True
    else:
        return False


def table_exists(db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
    except Exception:
        return False
    else:
        test = cur.execute('SELECT name FROM sqlite_master '
                           f'WHERE type="table" AND name=\'{table_name}\'')
        if test == 0:
            return False
        elif test == 1:
            return True
