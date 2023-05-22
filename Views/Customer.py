from Views.BankUser import *


class Customer(BankUser):
    def __init__(self, name, ssn, password, bankCode):
        super().__init__(name, ssn, password, bankCode)
