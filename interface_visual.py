import tkinter as tk
from tkinter import ttk


class Aplication:

    def __init__(self, master=None):
        super().__init__()
        self.font = ('Arial', '10')
        self.master = master
        self.container1 = tk.Frame(self.master)
        self.container2 = tk.Frame(self.master)
        self.container3 = tk.Frame(self.master)
        self.container4 = tk.Frame(self.master)
        self.container5 = tk.Frame(self.master)
        self.container6 = tk.Frame(self.master)
        self.container7 = tk.Frame(self.master)
        self.container8 = tk.Frame(self.master)
        self.first_window()

    '''
    Tela de entrada:

    Nessa tela, o usuário poderá optar em fazer log-in ou
    se cadastrar no sistema.
    '''
    def first_window(self):

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # primeiro container (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.titulo_1 = tk.Label(
            self.container1,
            text='Family-Finances',
            font=('Arial', '10', 'bold')
        )
        self.titulo_1.pack(side='top')
        self.titulo_2 = tk.Label(
            self.container1,
            text='Bem-vindo. O que deseja fazer?',
            font=self.font
        )
        self.titulo_2.pack()

        # segundo container (opções)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 10
        self.container2['padx'] = 20
        self.container2.pack()

        self.bt_login = tk.Button(
            self.container2,
            text='Fazer Log-In',
            font=self.font,
            command=self.log_in,
            width=15,
            padx=5
        )
        self.bt_login.pack(side='left')
        self.bt_signin = tk.Button(
            self.container2,
            text='Cadastrar',
            font=self.font,
            command=self.sign_in,
            width=15,
            padx=5
        )
        self.bt_signin.pack(side='right')

        # terceiro container (sair)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 10
        self.container3.pack()

        self.bt_sair = tk.Button(
            self.container3,
            text='Sair',
            font=self.font,
            command=self.master.destroy
        )
        self.bt_sair.pack()

    '''
    Tela de cadastro:

    A tela possibilita ao usuário o cadastro no sistema
    para posterior acesso.
    '''
    def sign_in(self):

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # primeiro container (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.titulo = tk.Label(
            self.container1,
            text='Cadastro no Sistema',
            font=('Arial', '10', 'bold')
        )
        self.titulo.pack()

        # segundo container (nome)
        self.container2 = tk.Frame(self.master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()

        self.nome = tk.Label(
            self.container2,
            text='Nome:',
            font=self.font,
            width=10
        )
        self.nome.pack(side='left')
        self.ins_nome = tk.Entry(
            self.container2,
            font=self.font,
            width=40
        )
        self.ins_nome.pack()

        # terceiro container (sobrenome)
        self.container3 = tk.Frame(self.master)
        self.container3['padx'] = 20
        self.container3['pady'] = 5
        self.container3.pack()

        self.sobrenome = tk.Label(
            self.container3,
            text='Sobrenome:',
            font=self.font,
            width=10
        )
        self.sobrenome.pack(side='left')
        self.ins_sobrenome = tk.Entry(
            self.container3,
            font=self.font,
            width=40
        )
        self.ins_sobrenome.pack()

        # quarto container (e-mail)
        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 5
        self.container4.pack()

        self.email = tk.Label(
            self.container4,
            text='E-mail:',
            font=self.font,
            width=10
        )
        self.email.pack(side='left')
        self.ins_email = tk.Entry(
            self.container4,
            font=self.font,
            width=40
        )
        self.ins_email.pack()

        # quinto container (usuario)
        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 5
        self.container5.pack()

        self.usuario = tk.Label(
            self.container5,
            text='Usuário:',
            font=self.font,
            width=10
        )
        self.usuario.pack(side='left')
        self.ins_usuario = tk.Entry(
            self.container5,
            font=self.font,
            width=15
        )
        self.ins_usuario.pack(side="left")

        # sexto container (senha)
        self.container6 = tk.Frame(self.master)
        self.container6['pady'] = 5
        self.container6.pack()

        self.senha = tk.Label(
            self.container6,
            text='Senha:',
            font=self.font,
            width=10
        )
        self.senha.pack(side='left')
        self.ins_senha = tk.Entry(
            self.container6,
            font=self.font,
            show='*',
            width=15
        )
        self.ins_senha.pack(side='left')

        # sétimo container (botão confirma e voltar)
        self.container7 = tk.Frame(self.master)
        self.container7['pady'] = 10
        self.container7.pack()

        self.btvoltar = tk.Button(
            self.container7,
            text='Voltar',
            font=self.font,
            width=10
        )
        self.btvoltar['command'] = self.first_window
        self.btvoltar.pack(side='left')
        self.btconfirma = tk.Button(
            self.container7,
            text='Cadastrar',
            font=self.font,
            width=10
        )
        self.btconfirma['command'] = self.sign_in_bd
        self.btconfirma.pack(side='left')

        # oitavo container (status)
        self.container8 = tk.Frame(self.master)
        self.container8['pady'] = 5
        self.container8.pack()

        self.status = tk.Label(self.container8, text='', font=self.font)
        self.status.pack(side='bottom')

    '''
    Tela de log-in:

    Nessa tela, o usuário poderá entrar com os seus dados
    (usuário e senha), e logar no sistema.
    '''
    def log_in(self):

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # primeiro container (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.titulo = tk.Label(
            self.container1,
            text='Log-In',
            font=('Arial', '10', 'bold')
        )
        self.titulo.pack()

        # segundo container (nome de usuário)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 20
        self.container2.pack()

        self.usuario = tk.Label(
            self.container2,
            text='Usuário: ',
            font=self.font,
            width=10
        )
        self.usuario.pack(side='left')
        self.ins_usuario = tk.Entry(
            self.container2,
            width=20,
            font=self.font
        )
        self.ins_usuario.pack()

        # terceiro container (senha)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 5
        self.container3['padx'] = 20
        self.container3.pack()

        self.senha = tk.Label(
            self.container3,
            text='Senha: ',
            font=self.font,
            width=10
        )
        self.senha.pack(side='left')
        self.ins_senha = tk.Entry(
            self.container3,
            width=20,
            font=self.font,
            show='*'
        )
        self.ins_senha.pack()

        # quarto container (botoes)
        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 10
        self.container4['padx'] = 20
        self.container4.pack()

        self.bt_voltar = tk.Button(
            self.container4,
            text='Voltar',
            font=self.font,
            command=self.first_window
        )
        self.bt_voltar.pack(side='left')
        self.bt_confirmar = tk.Button(
            self.container4,
            text='Confirmar',
            font=self.font,
            command=self.log_in_bd
        )
        self.bt_confirmar.pack(side='left')

        self.user = self.ins_usuario.get()

        # container 5 (confirmação do login)
        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 5
        self.container5['padx'] = 20
        self.container5.pack()

        self.status = tk.Label(
                self.container5,
                text='',
                font=self.font
            )
        self.status.pack(side='bottom')

    '''
    Tela do usuário:

    Nessa tela, o usuário poderá escolher qual funcionalidade
    ele deseja executar no programa.
    '''
    def user_window(self):

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # container 1 (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.titulo = tk.Label(
            self.container1,
            text=f'Bem-vindo, {self.user}.',
            font=('Arial', 10, 'bold')
        )
        self.titulo.pack()
        self.titulo_2 = tk.Label(
            self.container1,
            text='O que deseja fazer?',
            font=self.font
        )
        self.titulo_2.pack()

        # segundo container (verificar contas)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 20
        self.container2.pack()

        self.bt_opcao_1 = tk.Button(
            self.container2,
            text='Contas cadastradas',
            font=self.font,
            width=20,
            command=self.all_bills_window
        )
        self.bt_opcao_1.pack(side='left')
        self.opcao_1 = tk.Label(
            self.container2,
            text='    Verifica contas cadastradas no seu banco de dados.',
            font=self.font,
            width=45,
            anchor='w'
        )
        self.opcao_1.pack(side='left')

        # terceiro container (verificar contas a pagar)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 5
        self.container3['padx'] = 20
        self.container3.pack()

        self.bt_opcao_2 = tk.Button(
            self.container3,
            text='Pagamentos pendentes',
            font=self.font,
            width=20
        )
        self.bt_opcao_2.pack(side='left')
        self.opcao_2 = tk.Label(
            self.container3,
            text=' Verifica contas com pagamento pendente no mês vigente.',
            font=self.font,
            width=45
        )
        self.opcao_2.pack(side='left')

        # quarto container (informar pagamento)
        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 5
        self.container4['padx'] = 20
        self.container4.pack()

        self.bt_opcao_3 = tk.Button(
            self.container4,
            text='Informar pagamento',
            font=self.font,
            width=20,
            command=self.payment_inform
        )
        self.bt_opcao_3.pack(side='left')
        self.opcao_3 = tk.Label(
            self.container4,
            text='    Informa a efetivação de um pagamento.',
            font=self.font,
            width=45,
            anchor='w'
        )
        self.opcao_3.pack(side='left')

        # quinto container (adiciona conta a pagar)
        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 5
        self.container5['padx'] = 20
        self.container5.pack()

        self.bt_opcao_4 = tk.Button(
            self.container5,
            text='Adicionar conta',
            font=self.font,
            width=20,
            command=self.add_bill
        )
        self.bt_opcao_4.pack(side='left')
        self.opcao_4 = tk.Label(
            self.container5,
            text='    Adiciona conta mensal ao banco de dados do usuário.',
            font=self.font,
            width=45,
            anchor='w'
        )
        self.opcao_4.pack(side='left')

        # sexto container (alterar conta a pagar)
        self.container6 = tk.Frame(self.master)
        self.container6['pady'] = 5
        self.container6['padx'] = 20
        self.container6.pack()

        self.bt_opcao_5 = tk.Button(
            self.container6,
            text='Alterar conta',
            font=self.font,
            width=20,
            command=self.update_bill_infos
        )
        self.bt_opcao_5.pack(side='left')
        self.opcao_5 = tk.Label(
            self.container6,
            text='    Altera informações de conta já existente.',
            font=self.font,
            width=45,
            anchor='w'
        )
        self.opcao_5.pack(side='left')

        # sétimo container (alterar usuário e senha)
        self.container7 = tk.Frame(self.master)
        self.container7['pady'] = 5
        self.container7['padx'] = 20
        self.container7.pack()

        self.bt_opcao_6 = tk.Button(
            self.container7,
            text='Alterar IDs',
            font=self.font,
            width=20,
            command=self.update_user_ids
        )
        self.bt_opcao_6.pack(side='left')
        self.opcao_6 = tk.Label(
            self.container7,
            text='    Altera nome de usuário e/ou senha.',
            font=self.font,
            width=45,
            anchor='w'
        )
        self.opcao_6.pack(side='left')

        # oitavo container (sair)
        self.container8 = tk.Frame(self.master)
        self.container8['pady'] = 10
        self.container8.pack()

        self.bt_sair = tk.Button(
            self.container8,
            text='Sair',
            font=self.font,
            command=self.master.destroy,
            width=10
        )
        self.bt_sair.pack()

    def all_bills_window(self):
        '''
        A tela mostra ao usuário todas as contas cadastradas
        em seu banco de dados.
        '''

        import backend

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # consultado dados no banco de dados
        tb = backend.Table(f'{self.user}_database', f'{self.user}_bills')
        rec = tb.consult_all_data()

        # criando janela
        # container 1 (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 10
        self.container1['padx'] = 20
        self.container1.pack()

        self.titulo = tk.Label(
            self.container1,
            text='Contas cadastradas:',
            font=self.font
        )
        self.titulo.pack()

        # container 2 (tabela)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 20
        self.container2.pack()

        try:
            self.tabela = ttk.Treeview(
                self.container2,
                columns=('ID', 'Contas', 'Vencimentos', 'Frequencia'),
            )
            self.tabela.column('#0', width=0, minwidth=0)
            self.tabela.column('ID', width=100, minwidth=25)
            self.tabela.column('Contas', width=100, minwidth=25)
            self.tabela.column('Vencimentos', width=100, minwidth=25)
            self.tabela.column('Frequencia', width=100, minwidth=25)
            self.tabela.heading('ID', text='ID', anchor=tk.W)
            self.tabela.heading('Contas', text='Contas', anchor=tk.W)
            self.tabela.heading('Vencimentos', text='Vencimentos', anchor=tk.W)
            self.tabela.heading('Frequencia', text='Frequencia', anchor=tk.W)
            for register in rec:
                self.tabela.insert('', 'end', values=register)
        except Exception:
            self.status = tk.Label(
                self.container2,
                text='Desculpe. Ainda não existem contas cadastradas.',
                font=('Arial', 8)
            )
            self.status.pack()
        else:
            self.tabela.pack()

        # container 3 (botoes)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 10
        self.container3['padx'] = 20
        self.container3.pack()

        self.bt_voltar = tk.Button(
            self.container3,
            text='Voltar',
            font=self.font,
            command=self.user_window,
            width=10
        )
        self.bt_voltar.pack(side='left')
        self.bt_sair = tk.Button(
            self.container3,
            text='Sair',
            font=self.font,
            command=self.master.destroy,
            width='10'
        )
        self.bt_sair.pack(side='left')

    def payment_inform(self):
        '''
        Tela de informe de pagamentos:

        A tela possibilita ao usuário que informe ao sistema o
        pagamento de uma conta cadastrada.
        '''

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # container 1 (título)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 15
        self.container1['padx'] = 20
        self.container1.pack()

        self.titulo1 = tk.Label(
            self.container1,
            text='Informar pagamento',
            font=('Arial', 10, 'bold')
        )
        self.titulo1.pack(side='top')
        self.titulo2 = tk.Label(
            self.container1,
            text='Preencha os campos abaixo para informar o pagamento:',
            font=self.font
        )
        self.titulo2.pack(side='bottom')

        # container 2 (conta)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 10
        self.container2.pack()

        self.conta = tk.Label(
            self.container2,
            text='Conta: ',
            font=self.font,
            width=12,
            anchor='w'
        )
        self.conta.grid(row=0, column=0)
        rec_contas = self.avaiable_bills_bd()
        self.ins_conta = ttk.Combobox(
            self.container2,
            font=self.font,
            width=15,
            values=rec_contas
        )
        self.ins_conta.grid(row=0, column=1)

        # container 3 (referente ao mes)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 5
        self.container3['padx'] = 10
        self.container3.pack()

        self.mes = tk.Label(
            self.container3,
            text='Referente ao mês: ',
            font=self.font,
            width=15,
            anchor='w'
        )
        self.mes.pack(side='left')
        rec_mes = [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12'
        ]
        self.ins_mes = ttk.Combobox(
            self.container3,
            font=self.font,
            width=5,
            values=rec_mes
        )
        self.ins_mes.pack(side='left')

        # container 4 (referente ao ano)
        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 5
        self.container4['padx'] = 10
        self.container4.pack()

        self.ano = tk.Label(
            self.container4,
            text='Referente ao ano: ',
            font=self.font,
            width=15,
            anchor='w'
        )
        self.ano.pack(side='left')
        ano_atual = actual_year()
        rec_ano = [
            ano_atual - 1, ano_atual,
            ano_atual + 1, ano_atual + 2
        ]
        self.ins_ano = ttk.Combobox(
            self.container4,
            font=self.font,
            width=5,
            values=rec_ano
        )
        self.ins_ano.pack(side='left')

        # container 5 (valor)
        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 5
        self.container5['padx'] = 10
        self.container5.pack()

        self.valor = tk.Label(
            self.container5,
            text='Valor do pagamento: ',
            font=self.font,
            width=15,
            anchor='w'
        )
        self.valor.grid(row=0, column=0)
        self.ins_valor = tk.Entry(
            self.container5,
            font=self.font,
            width=15
        )
        self.ins_valor.grid(row=0, column=1)
        self.formato_valor = tk.Label(
            self.container5,
            text='Formato: 100.00',
            font=('Arial', 7),
            anchor='w'
        )
        self.formato_valor.grid(row=1, column=1)

        # container 6 (data)
        self.container6 = tk.Frame(self.master)
        self.container6['pady'] = 3
        self.container6['padx'] = 10
        self.container6.pack()

        self.data = tk.Label(
            self.container6,
            text='Data do pagamento: ',
            font=self.font,
            width=15,
            anchor='w'
        )
        self.data.grid(row=0, column=0)
        self.ins_data = tk.Entry(
            self.container6,
            font=self.font,
            width=15
        )
        self.ins_data.grid(row=0, column=1)
        self.formato_data = tk.Label(
            self.container6,
            text='Formato: 01-01-2020',
            font=('Arial', 7),
            anchor='w'
        )
        self.formato_data.grid(row=1, column=1)

        # container 7 (botoes)
        self.container7 = tk.Frame(self.master)
        self.container7['pady'] = 5
        self.container7['padx'] = 10
        self.container7.pack()

        self.bt_voltar = tk.Button(
            self.container7,
            text='Voltar',
            font=self.font,
            width=10,
            command=self.user_window
        )
        self.bt_voltar.pack(side='left')
        self.bt_confirmar = tk.Button(
            self.container7,
            text='Confirmar',
            font=self.font,
            width=10,
            command=self.payment_inform_bd
        )
        self.bt_confirmar.pack(side='left')

        # container 8 (status)
        self.container8 = tk.Frame(self.master)
        self.container8['pady'] = 10
        self.container8.pack()

        self.status = tk.Label(
            self.container8,
            font=self.font
        )
        self.status.pack()

    def add_bill(self):
        '''
        A tela possibilita ao usuário que adicione uma
        nova conta ao seu banco de dados.
        '''

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # container 1 (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 15
        self.container1.pack()

        self.titulo = tk.Label(
            self.container1,
            text='Adicionar conta ao Banco de Dados',
            font=('Arial', 10, 'bold'),
        )
        self.titulo.pack()

        # container 2 (nome da conta)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 20
        self.container2.pack()

        self.conta = tk.Label(
            self.container2,
            text='Nome da conta: ',
            font=self.font,
            width=20
        )
        self.conta.pack(side='left')
        self.ins_conta = tk.Entry(
            self.container2,
            font=self.font,
            width=25
        )
        self.ins_conta.pack(side='left')

        # container 3 (vencimento)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 5
        self.container3['padx'] = 20
        self.container3.pack()

        self.vencimento = tk.Label(
            self.container3,
            text='Vencimento: ',
            font=self.font,
            width=20
        )
        self.vencimento.pack(side='left')
        self.ins_vencimento = tk.Entry(
            self.container3,
            font=self.font,
            width=25
        )
        self.ins_vencimento.pack(side='left')

        # container 4 (frequencia)
        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 5
        self.container4['padx'] = 20
        self.container4.pack()

        self.frequencia = tk.Label(
            self.container4,
            text='Frequencia de pagamento: ',
            font=self.font,
            width=20
        )
        self.frequencia.pack(side='left')
        self.ins_frequencia = tk.Entry(
            self.container4,
            font=self.font,
            width=25
        )
        self.ins_frequencia.pack(side='left')

        # container 5 (botoes)
        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 10
        self.container5.pack()

        self.bt_voltar = tk.Button(
            self.container5,
            text='Voltar',
            font=self.font,
            command=self.user_window,
            width=10
        )
        self.bt_voltar.pack(side='left')
        self.bt_adicionar = tk.Button(
            self.container5,
            text='Adicionar',
            font=self.font,
            width=10,
            command=self.add_bill_bd
        )
        self.bt_adicionar.pack(side='left')

        # container 6 (status da adição de conta)
        self.container6 = tk.Frame(self.master)
        self.container6['pady'] = 5
        self.container6.pack()

        self.status = tk.Label(
            self.container6,
            font=self.font
        )
        self.status.pack()
        self.status2 = tk.Label(
            self.container6,
            font=self.font
        )
        self.status2.pack()

    def update_bill_infos(self):
        """
        A tela serve para alterar informações de uma conta
        que já foi adicionada.
        """

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # container 1 (título)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 15
        self.container1['padx'] = 20
        self.container1.pack()

        self.titulo1 = tk.Label(
            self.container1,
            text='Alterar informações de conta',
            font=('Arial', 10, 'bold')
        )
        self.titulo1.pack(side='top')
        self.titulo2 = tk.Label(
            self.container1,
            text='Selecione a conta abaixo e realize as devidas alterações:',
            font=self.font
        )
        self.titulo2.pack(side='bottom')

        # container 2 (conta)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 10
        self.container2.pack()

        self.conta = tk.Label(
            self.container2,
            text='Conta: ',
            font=self.font,
            width=20,
            anchor='w'
        )
        self.conta.pack(side='left')
        rec_contas = self.avaiable_bills_bd()
        self.ins_conta = ttk.Combobox(
            self.container2,
            font=self.font,
            width=17,
            values=rec_contas
        )
        self.ins_conta.pack(side='left')

        # container 3 (vencimento)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 5
        self.container3['padx'] = 20
        self.container3.pack()

        self.vencimento = tk.Label(
            self.container3,
            text='Vencimento: ',
            font=self.font,
            width=20,
            anchor='w'
        )
        self.vencimento.pack(side='left')
        self.ins_vencimento = tk.Entry(
            self.container3,
            font=self.font,
            width=20
        )
        self.ins_vencimento.pack(side='left')

        # container 4 (frequencia)
        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 5
        self.container4['padx'] = 20
        self.container4.pack()

        self.frequencia = tk.Label(
            self.container4,
            text='Frequencia de pagamento: ',
            font=self.font,
            width=20,
            anchor='w'
        )
        self.frequencia.pack(side='left')
        self.ins_frequencia = tk.Entry(
            self.container4,
            font=self.font,
            width=20
        )
        self.ins_frequencia.pack(side='left')

        # container 5 (botoes)
        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 5
        self.container5['padx'] = 10
        self.container5.pack()

        self.bt_voltar = tk.Button(
            self.container5,
            text='Voltar',
            font=self.font,
            width=10,
            command=self.user_window
        )
        self.bt_voltar.pack(side='left')
        self.bt_confirmar = tk.Button(
            self.container5,
            text='Confirmar',
            font=self.font,
            width=10,
            command=self.update_bill_infos_bd
        )
        self.bt_confirmar.pack(side='left')

        # container 6 (status)
        self.container6 = tk.Frame(self.master)
        self.container6['pady'] = 10
        self.container6.pack()

        self.status = tk.Label(
            self.container6,
            font=self.font
        )
        self.status.pack()

    def update_user_ids(self):
        '''
        Tela de alteração de IDs:

        A tela serve para que o usuário troque seu usuário
        ou senha.
        '''

        self.container1.destroy()
        self.container2.destroy()
        self.container3.destroy()
        self.container4.destroy()
        self.container5.destroy()
        self.container6.destroy()
        self.container7.destroy()
        self.container8.destroy()

        # container 1 (titulo)
        self.container1 = tk.Frame(self.master)
        self.container1['pady'] = 15
        self.container1['padx'] = 20
        self.container1.pack()

        self.titulo = tk.Label(
            self.container1,
            text='Alterar usuário e/ou senha',
            font=('Arial', 10, 'bold')
        )
        self.titulo.pack()

        # container 2 (usuário)
        self.container2 = tk.Frame(self.master)
        self.container2['pady'] = 5
        self.container2['padx'] = 30
        self.container2.pack()

        self.var = tk.IntVar()
        self.checkbt_usuario = tk.Radiobutton(
            self.container2,
            text='Alterar usuário',
            font=self.font,
            variable=self.var,
            value=0,
            command=self.change_user_ids_entry_check,
            width=15,
            anchor='w'
        )
        self.checkbt_usuario.grid(row=0, column=0)
        self.usuario_antigo = tk.Label(self.container2)
        self.usuario_novo = tk.Label(self.container2)
        self.ins_usuario_antigo = tk.Entry(self.container2)
        self.ins_usuario_novo = tk.Entry(self.container2)

        # container 3 (senha)
        self.container3 = tk.Frame(self.master)
        self.container3['pady'] = 5
        self.container3['padx'] = 30
        self.container3.pack()

        self.checkbt_senha = tk.Radiobutton(
            self.container3,
            text='Alterar senha',
            font=self.font,
            variable=self.var,
            value=1,
            command=self.change_user_ids_entry_check,
            width=15,
            anchor='w'
        )
        self.checkbt_senha.grid(row=0, column=0)
        self.senha_antiga = tk.Label(self.container3)
        self.senha_nova = tk.Label(self.container3)
        self.ins_senha_antiga = tk.Entry(self.container3)
        self.ins_senha_nova = tk.Entry(self.container3)
        self.usuario_antigo2 = tk.Label(self.container2)
        self.ins_usuario_antigo2 = tk.Entry(self.container2)

        # container 4 (botoes)

        self.container4 = tk.Frame(self.master)
        self.container4['pady'] = 10
        self.container4['padx'] = 20
        self.container4.pack()

        self.bt_voltar = tk.Button(
            self.container4,
            text='Voltar',
            font=self.font,
            command=self.user_window,
            width=10
        )
        self.bt_voltar.pack(side='left')
        self.bt_confirmar = tk.Button(
            self.container4,
            text='Confirmar',
            font=self.font,
            width=10,
            command=self.update_user_ids_bd
        )
        self.bt_confirmar.pack(side='left')

        # container 5 (status)

        self.container5 = tk.Frame(self.master)
        self.container5['pady'] = 5
        self.container5['padx'] = 20
        self.container5.pack()

        self.status = tk.Label(
            self.container5,
            font=self.font
        )
        self.status.pack()

    def avaiable_bills_bd(self):
        '''
        Função para coletar contas disponíveis no banco de dados
        do usuário e gravar em uma lista.
        '''

        import mysql.connector
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        cur = conn.cursor()
        cur.execute(f'USE {self.user}_database;')
        cur.execute(
            f'SELECT conta FROM {self.user}_bills ORDER BY vencimento;'
        )
        rec = cur.fetchall()
        bills = list()
        for row in rec:
            bills.append(row[0])
        return bills

    def payment_inform_bd(self):
        '''
        Função para inserir o pagamento realizado pelo usuário
        no banco de dados
        '''
        import backend
        mes = str(self.ins_mes.get()) + '-' + str(self.ins_ano.get())
        conta = self.ins_conta.get().replace(' ', '_')
        try:
            tb = backend.Table(
                f'{self.user}_database',
                f'{self.user}_{conta}_bill'
            )
            tb.insert_data_1(3, (
                f'{mes}',
                f'{self.ins_valor.get()}',
                f'{self.ins_data.get()}'
            ))
        except Exception as error:
            self.status['text'] = error
        else:
            self.status['text'] = 'Pagamento informado com sucesso.'

    def change_user_ids_entry_check(self):
        '''
        Função para mostrar/esconder as opções de entrada para
        a troca de usuário ou senha (Alterar IDs)
        '''

        if self.var.get() == 0:
            self.ins_usuario_antigo = tk.Entry(
                self.container2,
                font=self.font,
                width=20
            )
            self.ins_usuario_antigo.grid(row=0, column=2)
            self.ins_usuario_novo = tk.Entry(
                self.container2,
                font=self.font,
                width=20
            )
            self.ins_usuario_novo.grid(row=1, column=2)
            self.usuario_antigo = tk.Label(
                self.container2,
                text='Usuário atual: ',
                font=self.font,
                width=13,
                anchor='w'
            )
            self.usuario_antigo.grid(row=0, column=1)
            self.usuario_novo = tk.Label(
                self.container2,
                text='Usuário novo: ',
                font=self.font,
                width=13,
                anchor='w'
            )
            self.usuario_novo.grid(row=1, column=1)
        else:
            self.ins_usuario_antigo.destroy()
            self.ins_usuario_novo.destroy()
            self.usuario_antigo.destroy()
            self.usuario_novo.destroy()

        if self.var.get() == 1:
            self.ins_usuario_antigo2 = tk.Entry(
                self.container3,
                font=self.font,
                width=20
            )
            self.ins_usuario_antigo2.grid(row=0, column=2)
            self.ins_senha_antiga = tk.Entry(
                self.container3,
                font=self.font,
                width=20,
                show='*'
            )
            self.ins_senha_antiga.grid(row=1, column=2)
            self.ins_senha_nova = tk.Entry(
                self.container3,
                font=self.font,
                width=20,
                show='*'
            )
            self.ins_senha_nova.grid(row=2, column=2)
            self.usuario_antigo2 = tk.Label(
                self.container3,
                text='Usuário atual: ',
                font=self.font,
                width=13,
                anchor='w'
            )
            self.usuario_antigo2.grid(row=0, column=1)
            self.senha_antiga = tk.Label(
                self.container3,
                text='Senha antiga: ',
                font=self.font,
                width=13,
                anchor='w'
            )
            self.senha_antiga.grid(row=1, column=1)
            self.senha_nova = tk.Label(
                self.container3,
                text='Nova senha: ',
                font=self.font,
                width=13,
                anchor='w'
            )
            self.senha_nova.grid(row=2, column=1)
        else:
            self.ins_senha_antiga.destroy()
            self.ins_senha_nova.destroy()
            self.senha_antiga.destroy()
            self.senha_nova.destroy()
            self.ins_usuario_antigo2.destroy()
            self.usuario_antigo2.destroy()

    def sign_in_bd(self):
        import backend
        self.user = self.ins_usuario.get()
        tb = backend.Table('family_finances', 'admin_users')
        if tb.check_spec_column('user', self.user):
            self.status['text'] = 'O nome de usuário já existe.'
        elif ' ' in self.user:
            self.status['text'] = 'O nome de usuário não pode conter espaços.'
        elif ' ' in self.ins_email.get():
            self.status['text'] = 'O e-mail não é válido.'
        elif (
            self.user == '' or
            self.ins_nome.get() == '' or
            self.ins_sobrenome.get() == '' or
            self.ins_email.get() == '' or
            self.ins_senha.get() == ''
        ):
            self.status['text'] = 'Por favor, preencha todos os campos.'
        else:
            try:
                tb.insert_data_1(6, (
                    'DEFAULT',
                    self.ins_nome.get(),
                    self.ins_sobrenome.get(),
                    self.ins_email.get(),
                    self.user,
                    self.ins_senha.get()
                ))
            except Exception:
                self.status['text'] = 'Erro ao acessar banco de dados.'
            else:
                self.status['text'] = 'Usuário cadastrado com sucesso.'
                try:
                    tb = backend.Table(
                        f'{self.ins_usuario.get()}_database',
                        f'{self.ins_usuario.get()}_bills'
                    )
                    tb.crate_table(
                        'id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,'
                        'conta VARCHAR(30) NOT NULL,'
                        'vencimento INT NOT NULL,'
                        'frequencia INT NOT NULL DEFAULT 1'
                    )
                except Exception as error2:
                    self.status['text'] = error2
                else:
                    self.user_window()

    def log_in_bd(self):
        import backend
        self.user = self.ins_usuario.get()
        try:
            tb = backend.Table('family_finances', 'admin_users')
            if tb.check_two_columns(
                'user', 'password',
                self.user,
                self.ins_senha.get()
            ):
                self.user_window()
            else:
                self.status['text'] = 'Usuário e/ou senha incorretos.'
        except Exception:
            self.status['text'] = 'Erro ao acessar banco de dados.'

    def add_bill_bd(self):
        import backend
        conta = self.ins_conta.get().replace(' ', '_')
        try:
            tb = backend.Table(f'{self.user}_database', f'{self.user}_bills')
            tb.insert_data_1(4, (
                'default',
                f'{self.ins_conta.get()}',
                f'{self.ins_vencimento.get()}',
                f'{self.ins_frequencia.get()}'
            ))
        except Exception as error:
            self.status['text'] = error
        else:
            self.status['text'] = f'Dados inseridos em "{self.user}_bills".'
        try:
            tb = backend.Table(
                f'{self.user}_database',
                f'{self.user}_{conta}_bill'
            )
            tb.crate_table(
                f'mes VARCHAR(10) NOT NULL DEFAULT \'{actual_month()}\', '
                'valor FLOAT NOT NULL, '
                f'data VARCHAR(12) NOT NULL DEFAULT \'{actual_date()}\''
            )
        except Exception as error2:
            self.status2['text'] = error2
        else:
            self.status2['text'] = 'Conta adicionada com sucesso.'

    def update_user_ids_bd(self):
        import backend
        if self.var.get() == 0:
            tb = backend.Table('family_finances', 'admin_users')
            if tb.check_spec_column('user', self.ins_usuario_antigo.get()):
                if not tb.check_spec_column(
                    'user', self.ins_usuario_novo.get()
                ):
                    try:
                        tb.update_column(
                            'user',
                            self.ins_usuario_antigo.get(),
                            self.ins_usuario_novo.get()
                        )
                    except Exception as error:
                        self.status['text'] = error
                    else:
                        try:
                            db = backend.DataBase(
                                f'{self.ins_usuario_antigo.get()}_database'
                            )
                            db.rename_db(
                                f'{self.ins_usuario_novo.get()}_database'
                            )
                            rec = db.show_db_tables()
                            for table in rec:
                                tb = backend.Table(
                                    f'{self.ins_usuario_novo.get()}_database',
                                    f'{table}'
                                )
                                table = table.replace(
                                    f'{self.ins_usuario_antigo.get()}',
                                    f'{self.ins_usuario_novo.get()}'
                                )
                                tb.rename_table(
                                    f'{table}'
                                )
                        except Exception as error:
                            self.status['text'] = error
                        else:
                            self.status['text'] = (
                                'Usuário alterado com sucesso.'
                            )
                else:
                    self.status['text'] = 'Nome de usuário novo já existe.'
            else:
                self.status['text'] = 'Nome de usuário atual não encontrado.'
        elif self.var.get() == 1:
            tb = backend.Table('family_finances', 'admin_users')
            if tb.check_spec_column('user', self.ins_usuario_antigo2.get()):
                if tb.check_two_columns(
                    'user', 'password',
                    self.ins_usuario_antigo2.get(),
                    self.ins_senha_antiga.get()
                ):
                    try:
                        tb = backend.Table('family_finances', 'admin_users')
                        tb.update_column(
                            'password',
                            self.ins_senha_antiga.get(),
                            self.ins_senha_nova.get()
                        )
                    except Exception as error:
                        self.status['text'] = error
                    else:
                        self.status['text'] = 'Usuário alterado com sucesso.'
                else:
                    self.status['text'] = 'Usuário e senha não batem.'
            else:
                self.status['text'] = 'Nome de usuário não encontrado.'

    def update_bill_infos_bd(self):
        import backend
        try:
            tb = backend.Table(
                f'{self.user}_database',
                f'{self.user}_bills'
            )
            tb.update_alternative_column(
                'conta', self.ins_conta.get(),
                'vencimento', self.ins_vencimento.get()
            )
            tb.update_alternative_column(
                'conta', self.ins_conta.get(),
                'frequencia', self.ins_frequencia.get()
            )
        except Exception as error:
            self.status['text'] = error
        else:
            self.status['text'] = (
                f'Informações de "{self.ins_conta.get()}" '
                'alteradas com sucesso.'
            )


def actual_month():
    from datetime import datetime
    month_year = str(datetime.now().month) + '-' + str(datetime.now().year)
    return month_year


def actual_date():
    from datetime import datetime
    date = (
        str(datetime.now().day) +
        '-' + str(datetime.now().month) +
        '-' + str(datetime.now().year)
    )
    return date


def actual_year():
    from datetime import datetime
    return datetime.now().year


root = tk.Tk()
root.title('Family-finances')
Aplication(root)
root.mainloop()
