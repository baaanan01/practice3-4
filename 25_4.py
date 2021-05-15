import random, string

def generate_password(m):
  x = random.randint(1, m-2)
  y = random.randint(1, m - x - 1)
  z = m - x - y
  mass = []
  i = 0
  while i < x:
    n = random.choice(string.digits)
    if n != '1' and n != '0':
      mass.append(n)
      i += 1
  i = 0
  while i < y:
    u = random.choice(string.ascii_uppercase)
    if u != 'I' and u != 'O':
      mass.append(u)
      i += 1
  i = 0
  while i < z:
    w = random.choice(string.ascii_lowercase)
    if w != 'l' and w != 'o':
      mass.append(w)
      i += 1
  random.shuffle(mass)
  return ''.join(mass)

def main(n, m):
  list_of_passwords = []
  for i in range(n):
    list_of_passwords.append(generate_password(m))
  return list_of_passwords