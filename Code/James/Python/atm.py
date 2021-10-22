'''
Part 1
Let's represent an ATM with a class containing two attributes: 
a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
The REPL below calls the methods of the class to simulate an ATM.
'''

class ATM:
    
    def __init__(self, act_balance=0, interest=0.1, years=0):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.act_balance = balance
        self.interest = interest
        self.years = years
    
    def balance(self):
        # return the account balance
        return atm.act_balance
    
    def deposit(self, amount):
        # add the given amount to the balance
        atm.act_balance += atm.amount + atm.act_balance
        return atm.act_balance
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if atm.balance - atm.amount >= 0:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        atm.post_withdrawal = atm.balance - atm.amount
        return atm.post_withdrawal
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        atm.new_interest = atm.balance * atm.interest
        atm.balance = atm.balance * (1 + atm.interest)
        # return the amount of interest added
        return atm.balance and atm.new_interest

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Deposited ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

'''
# Part 2
# Have the ATM maintain a list of transactions. 
transactions = []
# Every time the user makes a deposit or withdrawal, 
# add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
transactions.append(f'user deposited {amount}')
transactions.append(f'user withdrew {amount}')
# Add a new method print_transactions() 
# to your class for printing out the list of transactions.
    def print_transactions():
        print(transactions)
'''