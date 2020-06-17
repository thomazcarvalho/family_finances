class Bills:

    def __init__(self, bill_name, bill_expiration, frequency=1, bill_end=999):
        self.bill_name = bill_name
        self.bill_expiration = bill_expiration
        self.frequency = frequency
        self.bill_end = bill_end
        print(f'Conta a pagar "{self.bill_name}" adicionada.')
