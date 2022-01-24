carros = ['uno', 'palio', 'corsa', 'passat', 'fiesta']

for car in carros:
  print(car)

print("_________________________iteratorcarros___________________________")

interatorCarros = iter(carros)

contador = 1
try:
   print(next(interatorCarros))
except StopIteration:
   print("fim")
