from Bank import Bank
from Admin import Admin
from User import User

bank = Bank()
admin = Admin(bank)
user = User(bank)

#-------------------
def admin_menu():
    admin_name = 'nisan'
    admin_pass = '1234'
    
    while True:
        print('1. ADMIN LOGIN')
        print('2. EXIT')

        ch = int(input('\nEnter your choice: '))
        if ch == 1:
            name = input('Enter your name: ')
            password = (input('Enter your password: '))

            if name == admin_name and password == admin_pass:
                print(f"\n****** WELCOME {name.upper()} ******")
                while True: 
                    print("\nADMIN MENU:")
                    print("1. Create Account")
                    print("2. Delete Account")
                    print("3. See All User Accounts")
                    print("4. Total Available Balance")
                    print("5. Total Loan Amount")
                    print("6. Enable Loan Feature")
                    print("7. Disable Loan Feature")
                    print("8. Exit")

                    admin_choice = int(input("\nEnter your choice: "))
                    
                    if admin_choice == 1:
                        admin.create_account()
                    
                    elif admin_choice == 2:
                        admin.delete_account()
                    
                    elif admin_choice == 3:
                        admin.see_all_accounts()
                    
                    elif admin_choice == 4:
                        admin.total_available_balance()
                    
                    elif admin_choice == 5:
                        admin.total_loan_amount()
                    
                    elif admin_choice == 6:
                        admin.loan_on()
                    
                    elif admin_choice == 7:
                        admin.loan_off()
                    
                    elif admin_choice == 8:
                        break
                    else:
                        print("Invalid choice!")
            else:
                print("Admin name or pass not match")
                
        elif ch == 2:
            break
        else:
            print("Invalid choice!")


def user_menu():
    while True:
        print("1. Create account")
        print("2. Login")
        print("3. Exit")
        
        ch = int(input("\nEnter your choice: "))
        if ch == 1:
            user.create_account()
            
        elif ch == 2:
            if user.login():
                print(f"\n********** WELCOME {user.bank.accounts[user.bank.curr_account]['name']} **********")
                while True:
                    print("\nUser Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check balance")
                    print("4. Transaction History")
                    print("5. Take Loan")
                    print("6. Transfer Money")
                    print("7. Exit")

                    user_choice = int(input("\nEnter your choice: "))
                        
                    if user_choice == 1:
                        user.deposit()
                        
                    elif user_choice == 2:
                        user.withdraw()
                        
                    elif user_choice == 3:
                        user.balance_check()
                        
                    elif user_choice == 4:
                        user.transaction_history()
                        
                    elif user_choice == 5:
                        user.take_loan()
                        
                    elif user_choice == 6:
                        user.transfer_money()
                        
                    elif user_choice == 7:
                        break
                    else:
                        print("Invalid choice!")                   
            else:
                print("Email or pass not match!")
        elif ch == 3:
            break
        else:
            print("Invalid choice!")

                        
print("***** WELCOME TO THE BANK MANAGEMENT SYSTEM *****")
while True:
    print("1. ADMIN MENU")
    print("2. USER MENU")
    print("3. EXIT")
    
    ch = int(input("\nEnter your choice: "))
    
    if ch == 1:
        admin_menu()
    elif ch == 2:
        user_menu()
    elif ch == 3:
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
    
        