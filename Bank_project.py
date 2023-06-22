class Person:
    def __init__(self, email, password) -> None:
        self.email= email
        self.password = password


class Bank:
    def __init__(self):
        self.users = []

    def create_user(self, email, password):
        user = User(email, password)
        self.users.append(user)
        return user

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def deposit(self, user_email, amount):
        user = self.get_user_by_email(user_email)
        if user:
            user.deposit(amount)
            return f'Deposited {amount} to {user_email}'
        else:
            return f'User with email {user_email} not found'
        
    def withdraw(self, user_email, amount):
        user = self.get_user_by_email(user_email)
        if user:
            user.withdraw(amount)
            return f'withdraw {amount} to {user_email}'
        else:
            return f'User with email {user_email} not found'
    
    def take_loan(self, user_email, amount):
        user = self.get_user_by_email(user_email)
        if user:
            user.take_lone(amount)
            return f'took_loan {amount} to {user_email}'
        else:
            return f'User with email {user_email} not found'
        
    
    def get_user_balance(self, user_email):
        user = self.get_user_by_email(user_email)
        if user:
            return user.get_balance()
        else:
            return f'User with email {user_email} not found'

    def get_total_bank_balance(self):
        total_balance = 0
        for user in self.users:
            total_balance += user.get_balance()
        return total_balance
    
   

    def get_total_loan(self):
        total_loan = 0
        for user in self.users:
            total_loan += user.total_loan()
        return total_loan

class User(Person):
    def __init__(self, email, password) -> None:
        
        self.__total_balance= 0
        self.__total_lone = 0
        self.transaction_history = []
        super().__init__(email, password)

    def deposit(self, amount):
        if amount>0:
            self.__total_balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            


    def withdraw(self, amount):
        if amount > self.__total_balance:
            return f'You cannot withdraw more than {self.__total_balance}'
            
        elif amount<= self.__total_balance:
            self.__total_balance -=amount
            
            self.transaction_history.append(f"Withdrawn: {amount}")
            return f'Here is your money {amount}'
        
        else:
            return f'Bank is bankrupt'
    
    def get_balance(self):
        return self.__total_balance
    
    def total_loan(self):
        return self.__total_lone
    
    def take_lone(self, amount):
        if amount<= self.__total_balance*2:
            self.__total_lone += amount
            
            self.transaction_history.append(f"Took loan: {amount}")
            return f'Here is your lone {amount}'
        else:
            return f'You cannot take lone'
    
    def tansfer_money(self, trans_user, amount):
        if amount<= self.__total_balance:
            self.__total_balance -= amount
            
            trans_user.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount}")
            return f'{amount} Transfer to {trans_user}'
        else:
            return f'Unavailable'
        
    def get_transaction_history(self):
        return self.transaction_history
        
    def __repr__(self) -> str:
        return f'Balance {self.__total_balance} Transaction_history {self.transaction_history}'


class Admin(Person):
    def __init__(self, email, password) -> None:

        self.loan_feature_enabled = True

        super().__init__(email, password)

    def get_balance(self,bank):
        total_balance= bank.get_total_bank_balance()
        return f'Total balance {total_balance}'

    def get_loan(self, bank):
        total_loan= bank.get_total_loan()
        return f'Total loan {total_loan}'
        
    def enable_loan_feature(self):
        self.loan_feature_enabled = True
        print(f"Loan feature enabled")

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
        print(f"Loan feature disabled")
   


bank=Bank()


admin = Admin("admin@dgk,com", 123456)
user1 = bank.create_user('user1@example.com', 112)
user2 = bank.create_user('user2@example.com', 122)
user3 = bank.create_user('user3@example.com', 133)
user4 = bank.create_user('user4@example.com', 123)

bank.deposit('user1@example.com', 10000)
bank.deposit('user2@example.com', 200)
bank.deposit('user3@example.com', 300)
bank.deposit('user4@example.com', 400)
print(bank.get_user_balance('user1@example.com'))

bank.withdraw('user1@example.com', 2000)
print(bank.get_user_balance('user1@example.com'))

bank.take_loan('user1@example.com', 4000)

total_lon= admin.get_loan(bank)

print(f"total loan {total_lon}")

total_bank_balance = admin.get_balance(bank)
print(f"Total Bank Balance: {total_bank_balance}")

admin.enable_loan_feature()