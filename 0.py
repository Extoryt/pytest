"""
Zadanie 0:

Przygotuj funkcję sprawdzająca czy osoba o przekazanym wieku jest osobą pełnoletnią.
"""

def is_adult(age: int) -> bool:
  return age >= 18

def test_is_adult():
  # given
  age = 18

  # when
  result = is_adult(age)

  # then
  assert result
  assert is_adult(20)


def test_is_not_adult():
  assert not is_adult(17)
  assert not is_adult(3)