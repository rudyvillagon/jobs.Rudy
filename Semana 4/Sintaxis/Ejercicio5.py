
count_grades = 0
bad_grade = 0
good_grade = 0
total_count = int(input("increse el total de notas: "))
all_notes = 0
all_bad = 0
all_good = 0
avarege_bad = 0
avarege_good = 0

while count_grades < total_count:
    total_grades = int(input("Ingrese la calificacion: "))
    all_notes += total_grades
    avarege_grade = all_notes/total_count
   
    if total_grades < 70:
         bad_grade += 1
         all_bad += total_grades
         avarege_bad = all_bad/bad_grade
     
    else: 
         good_grade += 1
         all_good += total_grades
         avarege_good = all_good/good_grade

    count_grades += 1 

    print(f"el conteo es de {total_count} y las rondas echas son {count_grades}")  

    print(f"Notas aprovadas: {good_grade}")

    print(f"Notas desaprovadas: {bad_grade}")

    print(f"el porcentaje de todas notas es: {avarege_grade}")

    print(f"El promedio de las notas aprovadas es: {avarege_good}")

    print(f"El promedio de las notas desaprovadas es: {avarege_bad}")
    
 
         
    
    

  