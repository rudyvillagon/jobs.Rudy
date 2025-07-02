import csv


def read_sudents_csv(student_list):

    with open(student_list, "r") as file_csv:
        reader_csv = csv.reader(file_csv)
        stu_data = list(reader_csv)
        return stu_data

read_sudents_csv()    