class Admin: 
    def __init__(self, bank):
        self.bank = bank
        
    def create_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings or Current): ")
        password = input("Enter your password: ")
        self.bank.create_account(name, email, address, account_type, password)
        
    def delete_account(self):
        account_num = int(input("Enter account number: "))
        self.bank.delete_account(account_num)
        
    def see_all_accounts(self):
        print("Show all users: ")
        for account_num , user in self.bank.accounts.items():
            print(f"Account num: {account_num}, Name: {user['name']}, Email: {user['email']}, Address: {user['address']}")  
            
    def total_available_balance(self):
        self.bank.total_balance()
        
    def total_loan_amount(self):
        self.bank.total_loan()
    
    def loan_on(self):
        self.bank.loan_enable()
    
    def loan_off(self):
        self.bank.loan_disable()
    
    
    