
name = input("ingrese su nombre:")
last_name = input("Ahora su primer apellido:")
age = int(input ("Por ultimo su edad:"))

if  age <= 2:
    group= "Bebé"
elif age <= 6:
    group= "Niño"
elif age <= 12:
    group= "Preadolecente"
elif age <= 20:
    group= "Adolecente"
elif age <= 25:
    group= "Adulto joven"
elif age <= 60:
    group= "Adulto"
else:
    group= "Adulto mayor" 

print(f"Eres un {group}")    

                 

# Bebe (0 a 2 años de edad)
# niño (3 a 6 años de edad)
# Preadolecente (6 a 12 años de edad)
# Adolecente (12 a 20 años de edad)
# Adulto joven (20 a 25 años de edad)
# Adulto (25 a 60 años de edad)
# Adulto mayor (60 años en adelante)