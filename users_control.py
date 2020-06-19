class User:

    def __init__(self):
        from database import check_login
        from time import sleep
        import useful
        print('Olá.')
        print('O que você deseja fazer?')
        print('1 - Efetuar Log-In\n2 - Realizar cadastro no sistema')
        choice = useful.get_integer('Escolha: ')
        while not 0 < choice < 3:
            choice = useful.get_integer('Digite apenas 1 ou 2: ')
        if choice == 2:
            print('')
            self.new_user()
        print('')
        self.user = input('Digite o nome de usuário: ')
        print('')
        check = check_login(self.user)
        if check:
            print('Conferindo nome de usuário...')
            sleep(1)
            print(f'Usuário "{self.user}" existente.')
            sleep(1)
            print('Procedendo para o login...')
            sleep(1)
            self.init_user()
        if not check:
            answer = str(input(f'Usuário "{self.user}" não existente. Deseja '
                               'cadastrá-lo? [S / N] ')).strip().lower()
            while answer not in 'sn':
                answer = str(input('(Digite apenas "S" ou "N") '
                                   f'Usuário {self.user} não existente. '
                                   'Deseja cadastrá-lo? '
                                   '[S / N] ')).strip().lower()
            if answer == 's':
                print('')
                self.new_user()
            elif answer == 'n':
                print('')
                print('Obrigado por usar nosso programa. :)')
                exit()

    def init_user(self):
        import database
        c = 1
        password = input('Senha: ')
        check_situation = database.check_user(self.user, password)
        while not check_situation:
            if c > 4:
                print('Você excedeu o número de tentativas '
                      'tente novamente mais tarde.')
                exit()
            print(f'O usuário e/ou senha não conferem. ({c}ª de 4 tentativas)')
            login = input('Nome de usuário: ')
            password = input('Senha: ')
            check_situation = database.check_user(login, password)
            c += 1
        if check_situation:
            self.password = password
            self.user_menu()

    def new_user(self):
        import database
        print('Bem-vindo! Vamos te cadastrar na nossa base de dados.')
        login = input('Digite o nome de usuário: ')
        password = input('Digite uma senha: ')
        check_situation = database.register_new_user(login, password)
        while check_situation == 0:
            print('Esse nome de usuário já existe, digite outro nome '
                  'de usuário, por favor.')
            login = input('Digite um usuário: ')
            password = input('Digite uma senha: ')
            check_situation = database.register_new_user(login, password)
        if check_situation == 1:
            self.user = login
            self.password = password
            print(f'Usuário "{login}" cadastrado com sucesso.')
        else:
            print(f'Erro inesperado: {check_situation} '
                  'Contate o desenvolvedor.')

    def user_menu(self):
        from useful import get_integer
        print('')
        print('Login efetuado. Pronto para acessar.\n')
        print('O que deseja fazer?')
        print(
            '1 - Fazer check de pagamentos de contas\n'
            '2 - Adicionar conta\n'
            '3 - Remover conta\n'
            '4 - Verificar contas atuais\n'
            '5 - Verificar senha atual\n'
            '6 - Alterar senha'
            '7 - Sair\n'
        )
        choice = get_integer('Escolha: ')
        while not 0 < choice < 8:
            choice = get_integer('Digite apenas os números de 1 a 7: ')
        if choice == 1:
            pass
        if choice == 2:
            pass
        if choice == 3:
            pass
        if choice == 4:
            pass
        if choice == 5:
            pass
        if choice == 6:
            pass
        if choice == 7:
            exit()
