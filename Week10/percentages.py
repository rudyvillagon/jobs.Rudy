import ast
from read_csv_stu import read_students_csv

def percentages_stu():

    student_percentages = {}
    students_data = read_students_csv()
    

    for student_record in students_data:
        name = student_record["Name"]
        grades_string = student_record["Grades"]
        grades = []

        parsed_grades_collection = ast.literal_eval(grades_string)

        if isinstance(parsed_grades_collection, (list, tuple)):
            for g_str in parsed_grades_collection:
                
                grades.append(float(g_str))
        else:
        
            grades.append(float(grades_string))
        
        if grades: 
            percentage = sum(grades) / len(grades)
        else:
            percentage = 0  

        
        student_percentages[name] = percentage
    
    sorted_students = sorted(student_percentages.items(), key=lambda item: item[1], reverse=True)

    
    top_3_students = sorted_students[:3]

    print (top_3_students)
    
    


percentages_stu()