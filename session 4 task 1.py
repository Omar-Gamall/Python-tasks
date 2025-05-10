def is_prime(n):
  """
  Checks if a given number n is prime.
  A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
  """
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True