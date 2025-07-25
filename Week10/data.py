import csv



def student_csv(filename,student_list):
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Section", "Spanish", "English", "Social Studies", "Sciences"])
        for student in student_list:
            writer.writerow([
                student["Name"],
                student["Section"],
                *student["Grades"]
            ])


    student_csv("student_list.csv",student_list)


def read_students_csv():
    
    try:
        with open("student_list.csv" , 'r', encoding="cp1252") as f:
            reader_csv = csv.DictReader(f)
            stu_data = list(reader_csv)
        return stu_data
    except FileNotFoundError:
        print("No hay Archivos Guardados")
        return []
    

students = read_students_csv()
print(students) 