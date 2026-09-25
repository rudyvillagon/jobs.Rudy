import csv
from actions import Student

def student_csv(student_list, filename="student_list.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Name", "Section", "Spanish", "English", "Social Studies", "Sciences"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list:
                writer.writerow({
                "Name": student.fullname,
                "Section": student.section,
                "Spanish": student.spa_grade,
                "English": student.eng_grade,
                "Social Studies": student.social_grade,
                "Sciences": student.sci_grade
            })

#student_list = []
        #student_csv("student_list.csv", student_list)



def read_students_csv(filename="student_list.csv"):

    student_list = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_student = Student (
                fullname=row["Name"],
                section=row["Section"],
                spa_grade=int(row["Spanish"]),
                eng_grade=int(row["English"]),
                social_grade=int(row["Social Studies"]),
                sci_grade=int(row["Sciences"])
            )
            student_list.append(new_student)

    return student_list


