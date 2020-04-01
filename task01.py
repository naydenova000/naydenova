import math

a = 1
b = 2686
c = - 1345320

discr =  b ** 2 - 4 * a * c
print(f"Дискриминант D = {discr}")

if discr > 0:
  x1 = (-b + math.sqrt(discr)) / (2 * a)
  x2 = (-b - math.sqrt(discr)) / (2 * a)
  print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
  x = -b / (2 * a)
  print(f"x = {x}")
else:
    print("Корней нет")