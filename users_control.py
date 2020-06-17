def enter_user():
    from useful import get_integer
    print('Olá.\nVocê já é usuário ou é sua primeira vez?\n'
          '1 - JÁ SOU USUÁRIO\n2 - NOVO USUÁRIO')
    choice = get_integer('Escolha: ')
    while not 0 < choice < 3:
        choice = get_integer('Digite apenas 1 ou 2: ')
    if choice == 1:
        print('')
        init_user()
    elif choice == 2:
        print('')
        new_user()


def init_user():
    import database
    c = 1
    login = input('Nome de usuário: ')
    password = input('Senha: ')
    check_situation = database.check_user(login, password)
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
        print('')
        print('Você pode agora acessar.')


def new_user():
    import database
    print('Bem-vindo! Vamos te cadastrar na nossa base de dados.')
    login = input('Digite um usuário: ')
    password = input('Digite uma senha: ')
    check_situation = database.register_new_user(login, password)
    while check_situation == 0:
        print('Esse nome de usuário já existe, digite outro nome '
              'de usuário, por favor.')
        login = input('Digite um usuário: ')
        password = input('Digite uma senha: ')
        check_situation = database.register_new_user(login, password)
    if check_situation == 1:
        print(f'Usuário"{login}" cadastrado com sucesso.')
    else:
        print(f'Erro inesperado: {check_situation} '
              'Contate o desenvolvedor.')
