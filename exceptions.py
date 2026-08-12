class BankingSystemError(Exception):
    pass

class InsufficientFundsError(BankingSystemError):
    def __init__(self,balance,amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient Funds : Balance is {self.balance}, attempted {self.amount}"
        super().__init__(message)
class InvalidAmountError(BankingSystemError):
    def __init__(self,amount):
        self.amount = amount
        message = f"Invalid Amount : {self.amount}, Amount must be greater than zero."
        super().__init__(message)

class AccountNotFoundError(BankingSystemError):
    def __init__(self,account_number):
        self.account_number = account_number
        message = f"Account not found {self.account_number}."
        super().__init__(message)

class AuthenticationError(BankingSystemError):
    def __init__(self,message="Authentication failed: incorrect PIN"):
        self.message = message
        super().__init__(self.message)

class AccountFrozenError(BankingSystemError):
    def __init__(self,account_number):
        self.account_number = account_number
        message = f"Account {self.account_number} is Frozen or Closed."
        super().__init__(message)

class InvalidAccountTypeError(BankingSystemError):
    def __init__(self,account_type):
        self.account_type = account_type
        message = f"Invalid Account Type {self.account_type}"
        super().__init__(message)

class DuplicateAccountError(BankingSystemError):
    def __init__(self,account_number):
        self.account_number = account_number
        message = f"Account {self.account_number} already exists."
        super().__init__(message)