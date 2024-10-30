import random
class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature_on = True
        self.curr_account = None
        
    def create_account(self, name, email, address, account_type, password):
        account_num = random.randint(100000, 999999)
        self.accounts[account_num] = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'password': password,
            'balance': 0,
            'loan_balance': 0,
            'loan_count': 0,
            'transaction_history': []
        }
        print(f"Account created successfully. Your account num: {account_num}")
        
    def delete_account(self, account_num):
        if account_num in self.accounts:
            del self.accounts[account_num]
            print(f"({account_num}) Account deleted successfully.")
        else:
            print("Account not found!!")
            
        
    def deposit(self, amount):
        if self.curr_account:
            self.accounts[self.curr_account]['balance'] += amount
            self.accounts[self.curr_account]['transaction_history'].append(f"Deposit: {amount}")
            print(f"{amount} BDT deposit successfully!")
         
    
    def withdraw(self, amount):
        if self.curr_account:
            if self.accounts[self.curr_account]['balance'] >= amount:
                self.accounts[self.curr_account]['balance'] -= amount
                self.accounts[self.curr_account]['transaction_history'].append(f"Withdraw: {amount}")
                print(f"{amount}BDT withdraw successfully!")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("Account not found!!")   
            
        
    def balance_check(self):
        if self.curr_account:
            print(f"Available balance: {self.accounts[self.curr_account]['balance']}")
        else:
            print("Account not found!!")
    
    def total_balance(self):
        t_balance = 0
        for acce in self.accounts.values():
            t_balance += acce['balance']
        print(f"Total available balance: {t_balance}")
        
    def total_loan(self):
        total_loan = 0
        for acce in self.accounts.values():
            total_loan += acce['loan_balance']
        print(f"Total loan amount: {total_loan}")
        
    def transaction_history(self):
        if self.curr_account:
            print("Transaction History: ")
            for history in self.accounts[self.curr_account]['transaction_history']:
                print(history)
        else:
            print("Account not found!!")
            
    def loan_enable(self):
        self.loan_feature_on = True
        print("Loan feature enable!")
    
    def loan_disable(self):
        self.loan_feature_on = False
        print("Loan feature disable!!")

            
    def take_loan(self, amount):
        if self.curr_account:
            if self.loan_feature_on:
                if self.accounts[self.curr_account]['loan_count'] < 2:
                    self.accounts[self.curr_account]['balance'] += amount
                    self.accounts[self.curr_account]['loan_balance'] += amount
                    self.accounts[self.curr_account]['loan_count'] += 1
                    self.accounts[self.curr_account]['transaction_history'].append(f"Take loan: {amount}")
                    print("Loan taken successfully!")
                else:
                    print("You are not eligible for loan!!")
            else: 
                print("The loan feature is disable!")
        else:
            print("Account not found!")
            
        
    def transfer_money(self, receive_account_num, amount):
        if self.curr_account and receive_account_num in self.accounts:
            if self.accounts[self.curr_account]['balance'] >= amount:
                self.accounts[self.curr_account]['balance'] -= amount
                self.accounts[receive_account_num]['balance'] += amount
                self.accounts[self.curr_account]['transaction_history'].append(f"Transferred: {amount} to {receive_account_num}")
                self.accounts[receive_account_num]['transaction_history'].append(f"Received: {amount} to {self.curr_account}")
                print("Money transferred successfully!!")
            else:
                print("Not enough money!")
        else:
            print("Account not found!!")  
    
    
    def find_account(self, email):
        for account_num, user in self.accounts.items():
            if user['email'] == email:
                return account_num
        return None
    
    def login(self, email, password):
        account_num = self.find_account(email)
        if account_num and self.accounts[account_num]['password'] == password:
            self.curr_account = account_num
            return self.accounts[account_num]
        else:
            print("Invalid email or pass")
            return None
            