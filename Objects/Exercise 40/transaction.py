class Transaction:
    current_balance = 0

    def __init__(self, amount):
        Transaction.current_balance += amount


t1 = Transaction(20)
t2 = Transaction(30)
t3 = Transaction(-10)
print(Transaction.current_balance)
