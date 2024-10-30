class User:
    def __init__(self, bank):
        self.bank = bank
        # self.account_data = None

    def create_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings or Current): ")
        password = input("Enter your password: ")
        self.bank.create_account(name, email, address, account_type, password)
        
    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        self.bank.deposit(amount)
        
    def withdraw(self):
        amount = float(input("Enter withdraw amount: "))
        self.bank.withdraw(amount)
        
    def balance_check(self):
        self.bank.balance_check()
        
    def take_loan(self):
        amount = float(input("Enter loan amount: "))
        self.bank.take_loan( amount)
        
    def transaction_history(self):
        self.bank.transaction_history()
        
    def transfer_money(self):
        receive_account_num = int(input("Enter received account number: "))
        amount = int(input("Enter transfer amount: "))
        self.bank.transfer_money( receive_account_num, amount)
        
    def login(self):
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        
        return self.bank.login(email, password)
    