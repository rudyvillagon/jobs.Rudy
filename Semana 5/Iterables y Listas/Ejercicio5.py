

counter = 0
numbers_user= []
final_list = []
group_number =[]
while True:
    numbers_user = int(input("Ingrese un numeros: "))
    counter += 1  
    group_number.append(numbers_user)

    if counter == 10:
     break  


final_list = sorted(group_number)
print(f"{final_list}. El Más alto fue {final_list[9]}")


