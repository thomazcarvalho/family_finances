import sqlite3


def register_new_user(user, password):
    """Registra um novo usuário no banco de dados do admin caso não exista.

    Args:
        user: Usuário que deseja cadastrar;
        password: Senha que deseja cadastrar.

    Returns:
        Integer: 0 -> usuário já existente
                 1 -> cadastrado com sucesso
                 descrição do erro -> existência de erro
    """
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
            cur.close()
            conn.close()
            return 0
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
    except Exception as error:
        return error
    else:
        return 1


def check_user(login, password):
    """A função confere se o usuário e senha estejam cadastrados e batendo no
        banco de dados SQLite.

    Args:
        login ([type]): login que está cadastrado;
        password ([type]): senha cadastrada.

    Returns:
        Boolean: Retorna True para caso o usuário e senha confiram
                ou False caso não confiram ou em casos de exceção.
    """
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


def check_login(login):
    conn = sqlite3.connect('admin_database.db')
    cur = conn.cursor()
    try:
        check = cur.execute(f'SELECT user, password FROM users_and_passwords\
                            WHERE user = "{login}"')
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
