"""
Zadanie 4:

Rozwiń zadanie 2, w taki sposób by nie można było wypłacić więcej niż jest w kasie. W takim przypadku program powinien wyrzucić wyjątek.
"""

import pytest

class Bank:
  def __init__(self):
    self.amount = 0

  def add_money(self, money: int):
    self.amount += money

  def withdraw_money(self, money):
    self.amount -= money
    if money > self.amount:
      raise NotEnoughCash('Nie mam tyle w kasie...')
    return money

class NotEnoughCash(Exception):
  pass

class TestBank: 
  def test_withdraw_over_amount(self):
      with pytest.raises(NotEnoughCash):
        bank = Bank()
        bank.withdraw_money(200)