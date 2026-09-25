import random

while True:
      number_random = random.randint(1,10)
      number_user = int(input("Intente adivinar el numero secreto:"))
      if number_user == number_random:
         print("¡¡Correcto es era!!")
         break
      else:
         print("No es el número intenta de nuevo") 
    