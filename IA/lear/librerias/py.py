def primos(limite):
  for num in range(2, limite):
    no_primo = False
    for div in range(2, num):
      if(num%div == 0):
        no_primo = True
    if(not no_primo):
      print(num)

primos(100)

def cambiar(texto):
  ans = ""
  for car in texto:
    if(car.isupper()):
      ans += car.lower()
    else:
      ans += car.upper()
  return ans

print(cambiar("HAloHalO"))

def busqueda(lista, target):
  for pos in range(0, len(lista)):
    if(lista[pos] == target): #LO ENCONTRE
      return pos
  return -1

print(busqueda([1, 2, 3, 4, 5], 6))