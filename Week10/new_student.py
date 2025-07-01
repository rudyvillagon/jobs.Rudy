import csv


def new_student():
    num_student = int(input("Number of records you wanna do?: "))
    student_list = []
    counter = 0

    while counter < num_student:
        counter += 1
        fullname = input("Student Fullname:  ")
        section = input("Section:  ")
        spa_grade = input("Spanish Grade:  ")
        eng_grade = input("English Grade:  ")
        social_grade = input("Social Studies Grade:  ")
        sci_grade = input("Sciences Grade: ")

        new_stud ={
            "Name" : fullname,
            "Section" : section,
            "Spanish Grade" : spa_grade,
            "English Grade" : eng_grade,
            "Social Studies Grade" : social_grade,
            "Sciences Grade" : sci_grade       

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
