import csv


def new_student():
    num_student = int(input("Number of records you wanna do?: "))
    student_list = []
    counter = 0

    while counter < num_student:
        counter += 1
        fullname = input("Student Fullname:  ")
        section = input("Section:  ")
        spa_grade = int(input("Spanish Grade:  "))
        eng_grade = int(input("English Grade:  "))
        social_grade = int(input("Social Studies Grade:  "))
        sci_grade = int(input("Sciences Grade: "))

        if not (0 <= spa_grade <= 100 and
                0 <= eng_grade <= 100 and
                0 <= social_grade <= 100 and
                0 <= sci_grade <= 100):
                raise ValueError("Utilice un numero entre 0 y 100")


        new_stud ={
            "Name" : fullname,
            "Section" : section,
            "Grades" : [
            spa_grade,
            eng_grade,
            social_grade,
            sci_grade],
            
            
        }

        student_list.append(new_stud)

    return student_list
    

def student_csv(file_name,student_list):
    with open(file_name, "w" ,encoding="utf-8") as file:
        if student_list:
            writer = csv.DictWriter(file,fieldnames = student_list[0].keys())
            writer.writeheader()
            for school_list in student_list:

                writer.writerow(school_list)      
    
students = new_student()    


student_csv("student_list.csv",students)
