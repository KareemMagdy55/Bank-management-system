from DBMS.handleDB import *

class BankUser:
    def __init__(self, name, ssn, password, bankCode):
        self.name = name
        self.ssn = ssn
        self.password = password
        self.bankCode = bankCode
