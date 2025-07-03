import csv



def read_students_csv():
    stu_data = {}
    

    with open("student_list.csv" , 'r', encoding="cp1252") as f:
        reader_csv = csv.DictReader(f)
        stu_data = list(reader_csv)
    return stu_data

read_students_csv()    