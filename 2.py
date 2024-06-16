"""
Zadanie 2:

Przygotuj klasę Bank. Klasa powinna mieć możliwość wpłacania oraz wypłacania. W chwili inicjalizacji bank powinien zawierać puste saldo.
Nie testuj sytuacji w której wypłacasz więcej niż to możliwe :)
"""

class Bank:
  def __init__(self):
    self.amount = 0

  def add_money(self, money: int):
    self.amount += money

  def withdraw_money(self, money):
    self.amount -= money
    return money

class TestBank: 
  def test_create_bank(self):
    bank = Bank()
    assert bank.amount == 0 
    assert isinstance(bank, Bank)

  def test_add_money(self):
    # given
    bank = Bank()

    # when
    bank.add_money(100)

    # then
    assert bank.amount == 100

  def test_add_money_twice(self):
    # given
    bank = Bank()

    # when
    bank.add_money(100)
    bank.add_money(100)

    # then
    assert bank.amount == 200

  def test_withdraw_money(self):
    # given
    bank = Bank()
    bank.add_money(100)

    # when
    money = bank.withdraw_money(100)

    # then 
    assert money == 100
    assert bank.amount == 0