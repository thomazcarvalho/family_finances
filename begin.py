class User:

    def __init__(self):
        print('Olá.\nVocê já é usuário ou é sua primeira vez?\n'
              '1 - JÁ SOU USUÁRIO\n2 - NOVO USUÁRIO')
        choice = int(input('Escolha: '))
        while choice != 1 and choice != 2:
            choice = int(input('Digite apenas 1 ou 2: '))
        if choice == 1:
            self.init_user()
        else:
            self.new_user()

    def init_user(self):
        import database
        login = input('Nome de usuário: ')
        password = input('Senha: ')
        return database.check_user(login, password)

    def new_user(self):
        import database
        print('Bem-vindo! Vamos te cadastrar na nossa base de dados.')
        login = input('Digite um usuário: ')
        password = input('Digite uma senha: ')
        print(database.register_new_user(login, password))

    def init_database(self):
        import sqlite3
        sqlite3.connect(f'{self.user}_finances')


class Bills:

    def __init__(self, bill_name, bill_expiration, frequency=1, bill_end=999):
        self.bill_name = bill_name
        self.bill_expiration = bill_expiration
        self.frequency = frequency
        self.bill_end = bill_end
        print(f'Conta a pagar "{self.bill_name}" adicionada.')


if __name__ == "__main__":
    thomaz = User()
