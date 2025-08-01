import csv


def student_csv(student_list, filename="student_list.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Name", "Section", "Spanish", "English", "Social Studies", "Sciences"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list:
                writer.writerow({
                    "Name": student["Name"],
                    "Section": student["Section"],
                    "Spanish": student["Grades"][0],
                    "English": student["Grades"][1],
                    "Social Studies": student["Grades"][2],
                    "Sciences": student["Grades"][3],
                })

#student_list = []
        #student_csv("student_list.csv", student_list)



def read_students_csv(filename="student_list.csv"):

    student_list = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_stud = {
                "Name": row["Name"],
                "Section": row["Section"],
                "Grades": [
                    int(row["Spanish"]),
                    int(row["English"]),
                    int(row["Social Studies"]),
                    int(row["Sciences"])
            ]
        }
            student_list.append(new_stud)

    return student_list



