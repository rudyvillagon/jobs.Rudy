first_number = int(input("Ingrese un numero: "))
Second_number =int(input("Un segundo numero: "))
third_number = int(input("y por ultimo un tercer numero: "))

if (first_number>Second_number) and (first_number>third_number):
    print(f"El numero mayor es {first_number}")

elif (Second_number>first_number) and (Second_number>third_number):
        print(f"El numero mayor es {Second_number}")
else:
        print(f"El numero mayor es {third_number}")


      