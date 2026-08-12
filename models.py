from abc import ABC, abstractmethod
from exceptions import InsufficientFundsError, InvalidAmountError


class Account(ABC):
    def __init__(self, account_number, customer_id, balance=0.0, pin_hash="", status="ACTIVE"):
        self.account_number = account_number
        self.customer_id = customer_id
        self._balance = balance
        self.pin_hash = pin_hash
        self.status = status

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        self._balance += amount
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError

    @abstractmethod
    def account_type(self):
        raise NotImplementedError


class SavingsAccount(Account):
    MIN_BALANCE = 500.00

    def __init__(self, account_number, customer_id, balance=0.0, pin_hash="", status="ACTIVE", interest_rate=0.04):
        super().__init__(account_number, customer_id, balance, pin_hash, status)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if self._balance - amount < self.MIN_BALANCE:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "SAVINGS"


class CurrentAccount(Account):
    def __init__(self, account_number, customer_id, balance=0.0, pin_hash="", status="ACTIVE", overdraft_limit=5000.0):
        super().__init__(account_number, customer_id, balance, pin_hash, status)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if self._balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "CURRENT"


class Customer:
    def __init__(self, customer_id, name, email, phone=""):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer#{self.customer_id} | {self.name} | {self.email}"