class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []
        self.bank_transactions = {}
        

class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f'{name} {surname}'
        self.user_banks = []
        self.transactions = {}
        self.balans = {}
        self.pays = {}
    
    def add_bank(self, bank):
        if isinstance(bank, Bank):
            self.user_banks.append(bank.bank_name)
            bank.accounts.append(self.full_name)
            self.balans[bank.bank_name] = 0
    
    def transaction(self, bank, summ):
        if (isinstance(bank, Bank) and bank.bank_name in self.user_banks and self.full_name in bank.accounts):
            if bank.bank_name not in self.transactions:
                self.transactions[bank.bank_name] = []
            self.transactions[bank.bank_name].append(summ)
                
            if self.full_name not in bank.bank_transactions:
                bank.bank_transactions[self.full_name] = []
            bank.bank_transactions[self.full_name].append(summ)
            
            if bank.bank_name not in self.balans:
                self.balans[bank.bank_name] = sum(summ)
            else:
                self.balans[bank.bank_name] += sum(summ)
    
    def pay(self, summ, bank, to_user, user_bank):
        if (isinstance(bank, Bank) and isinstance(to_user, User) and isinstance(user_bank, Bank) and bank.bank_name in self.user_banks and user_bank.bank_name in to_user.user_banks):
            if to_user.full_name not in self.pays:
                self.pays[to_user.full_name] = {}
            if user_bank.bank_name not in self.pays[to_user.full_name]:
               self.pays[to_user.full_name][user_bank.bank_name] = []
            self.pays[to_user.full_name][user_bank.bank_name] += [summ]
            self.balans[bank.bank_name] -= summ
            to_user.balans[user_bank.bank_name] += summ

bank_1 = Bank('Сбер')
bank_2 = Bank('Тинек')

user_1 = User('Дональд', 'Трамп')
user_2 = User('Павел', 'Дуров')
user_1.add_bank(bank_1)
user_1.add_bank(bank_2)
user_2.add_bank(bank_1)
user_2.add_bank(bank_2)

print(user_1.balans)
user_1.pay(500, bank_1, user_2, bank_1)
user_1.pay(200, bank_1, user_2, bank_1)
print(user_1.pays)
print(user_1.balans)
print(user_2.balans)


""" user_1.transaction(bank_1, [700, 800])
user_1.transaction(bank_1, [500, 900])
user_1.transaction(bank_2, [249, 518])
user_1.transaction(bank_2, [104, 89])
user_1.transaction(bank_1, [5, 9])

user_2.transaction(bank_1, [11, 23])
user_2.transaction(bank_1, [43, 35])
user_2.transaction(bank_2, [14, 57])
user_2.transaction(bank_2, [456, 45])
user_2.transaction(bank_1, [55, 94])

print(user_1.transactions)
print(bank_1.bank_transactions)
print(bank_2.bank_transactions)

print(user_2.transactions)
print(bank_2.bank_transactions)
print(bank_2.bank_transactions)

print(user_1.balans[bank_1.bank_name])
print(user_1.balans[bank_2.bank_name])

print(user_2.balans[bank_1.bank_name])
print(user_2.balans[bank_2.bank_name]) """


