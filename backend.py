class DataBase:

    def __init__(self, database_name):
        super().__init__()
        self.database_name = database_name

    def db_connect(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            print(f'Conecting to database {self.database_name}: ', end='')
            cursor = conn.cursor()
            cursor.execute(
                f'CREATE DATABASE IF NOT EXISTS {self.database_name} '
                'DEFAULT CHARACTER SET utf8 '
                'DEFAULT COLLATE utf8_general_ci'
            )
        except Exception as error:
            print(error)
        else:
            print('Ok.')
            conn.commit()
            cursor.close()
            conn.close()

    def rename_db(self, new_database):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            print(
                f'Renaming database "{self.database_name}" to '
                f'"{new_database}": ', end=''
            )
            cursor = conn.cursor()
            cursor.execute(
                f'CREATE DATABASE IF NOT EXISTS {new_database} '
                'DEFAULT CHARACTER SET utf8 '
                'DEFAULT COLLATE utf8_general_ci'
            )
        except Exception as error:
            print(error)
        else:
            conn.commit()
            try:
                cursor.execute(f'USE {self.database_name}')
                cursor.execute('SHOW TABLES')
                rec = cursor.fetchall()
                reclist = list()
                for table in rec:
                    reclist.append(table[0])
                for table in reclist:
                    cursor.execute(
                        f'RENAME TABLE {self.database_name}.{table} '
                        f'TO {new_database}.{table}'
                    )
                cursor.execute(f'DROP DATABASE {self.database_name}')
                self.database_name = new_database
            except Exception as error:
                print(error)
            else:
                conn.commit()
                cursor.close()
                conn.close()
                print('Ok')

    def show_db_tables(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            print(
                'Returning all tables from '
                f'{self.database_name}: ', end=''
            )
            cursor = conn.cursor()
            cursor.execute(f'USE {self.database_name}')
            cursor.execute('SHOW TABLES')
            rec = cursor.fetchall()
            reclist = list()
            for table in rec:
                reclist.append(table[0])
        except Exception as error:
            print(error)
        else:
            cursor.close()
            conn.close()
            return reclist


class Table(DataBase):

    def __init__(self, db_name, table_name):
        super().__init__(db_name)
        self.table_name = table_name
        self.db_connect()

    def crate_table(self, columns):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Creating table "{self.table_name}":', end=' ')
            cursor.execute(
                f'USE {self.database_name}'
            )
            cursor.execute(
                f'CREATE TABLE {self.table_name} ('
                f'{columns}'
                ') '
                'DEFAULT CHARSET = utf8'
            )
        except Exception as error:
            print(error)
        else:
            print('Ok')
            conn.commit()
            cursor.close()
            conn.close()

    def insert_data_1(self, ndata, data_string):
        """Insere uma linha de dados na tabela.

        Args:
            ndata (int): quantidade de colunas a serem inseridas.
            data_string (tuple): conjunto de dados a serem inseridos.
        """
        import mysql.connector
        quant = '%s, '*(ndata - 1)
        quant = quant + '%s'
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Inserting data on table "{self.table_name}":', end=' ')
            cursor.execute(
                f'USE {self.database_name}'
            )
            cursor.execute(
                f'INSERT INTO {self.table_name} '
                f'VALUES ({quant})',
                data_string
            )
        except Exception as error:
            print(error)
        else:
            print('Ok')
            conn.commit()
            cursor.close()
            conn.close()

    def insert_data_2(self, data_list):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Inserting data on table "{self.table_name}":', end=' ')
            cursor.execute(
                f'USE {self.database_name}'
            )
            for r in data_list:
                cursor.execute(
                    f'INSERT INTO {self.table_name} '
                    'VALUES (%s, %s, %s)',
                    r
                )
        except Exception as error:
            print(error)
        else:
            print('Ok')
            conn.commit()
            cursor.close()
            conn.close()

    def consult_all_data(self):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Consulting all data on "{self.table_name}"...')
            cursor.execute(
                f'USE {self.database_name}'
            )
            cursor.execute(
                f'SELECT * FROM {self.table_name}'
            )
            rec = cursor.fetchall()
            print(type(rec))
            for data in rec:
                print(data)
        except Exception as error:
            print(error)
        else:
            print('Ok.')
            return rec
        finally:
            cursor.close()
            conn.close()

    def check_spec_column(self, column, data):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Checking data on column "{column}"...', end=' ')
            cursor.execute(
                f'USE {self.database_name}'
            )
            cursor.execute(
                f'SELECT * FROM {self.table_name} '
                f'WHERE {column} = \'{data}\''
            )
            msg = cursor.fetchall()
        except Exception as error:
            print(error)
            return False
        else:
            if len(msg) >= 1:
                print('Found data.')
                return True
            else:
                print('Didn\'t found data.')
                return False
        finally:
            cursor.close()
            conn.close()

    def check_two_columns(self, column1, column2, data1, data2):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Checking data on {column1} and {column2}...', end=' ')
            cursor.execute(
                f'USE {self.database_name}'
            )
            cursor.execute(
                f'SELECT * FROM {self.table_name} '
                f'WHERE {column1} = \'{data1}\' '
                'AND '
                f'{column2} = \'{data2}\''
            )
            msg = cursor.fetchall()
        except Exception as error:
            print(error)
            return False
        else:
            if len(msg) >= 1:
                print('Found data.')
                return True
            else:
                print('Didn\'t found data.')
                return False
        finally:
            cursor.close()
            conn.close()

    def update_column(self, column, old_value, new_value):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Changing value on {self.table_name}:', end=' ')
            cursor.execute(f'USE {self.database_name}')
            cursor.execute(
                f'update {self.table_name} '
                f'set {column} = "{new_value}" '
                f'where {column} = "{old_value}" '
            )
        except Exception as error:
            print(error)
        else:
            print('Ok')
            conn.commit()
            cursor.close()
            conn.close()

    def update_alternative_column(
        self, column_where, value_where,
        column_new_value, new_value
    ):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Changing value on {self.table_name}:', end=' ')
            cursor.execute(f'USE {self.database_name}')
            cursor.execute(
                f'update {self.table_name} '
                f'set {column_new_value} = "{new_value}" '
                f'where {column_where} = "{value_where}" '
            )
        except Exception as error:
            print(error)
        else:
            print('Ok')
            conn.commit()
            cursor.close()
            conn.close()

    def rename_table(self, new_name):
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            print(f'Renaming table "{self.table_name}": ', end='')
            cursor.execute(f'USE {self.database_name}')
            cursor.execute(
                f'RENAME TABLE {self.table_name} '
                f'TO {new_name}'
            )
        except Exception as error:
            print(error)
        else:
            conn.commit()
            cursor.close()
            conn.close()
            print('Ok.')


if __name__ == "__main__":
    db = DataBase('admin_users')
    db.db_connect()
