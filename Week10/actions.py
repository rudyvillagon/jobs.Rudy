


def get_valid_int(prompt, min_val=0, max_val=100):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f" The Value most be between {min_val} and {max_val}.")
        except ValueError:
            print(" Please enter a valid integer.")


def new_student():

    student_list = []
    

    try:
        num_student = int(input("How many students do you want to register? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(num_student):
        print(f" Student Registration {i + 1}:")
        fullname = input("Name: ")
        section = input("Section: ")

        spa_grade = get_valid_int("Spanish Grade: ")
        eng_grade = get_valid_int("English Grade: ")
        social_grade = get_valid_int("Social studies Grade: ")
        sci_grade = get_valid_int("Sciences Grade: ")


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
    


def percentages_stu(student_list):
    top_3_students = []
    sorted_students = []
    student_percentages = {}
    students_data = student_list
    

    for student_record in students_data:
        name = student_record["Name"]
        grades = student_record["Grades"]
        
        if grades: 
            percentage = sum(grades) / len(grades)
        else:
            percentage = 0  

        
        student_percentages[name] = percentage
    
    sorted_students = sorted(student_percentages.items(), key=lambda item: item[1], reverse=True)

    
    top_3_students = sorted_students[:3]
    
    return sorted_students,top_3_students
    
    
    
def overall_percentage(sorted_students):
    

    total_of_averages = sum(student_tuple[1] for student_tuple in sorted_students)
    number_of_top_students = len(sorted_students)

    overall_average = total_of_averages / number_of_top_students
    print (overall_average)
    
#new_student()
#top_3_students, sorted_students = percentages_stu()
#overall_percentage(sorted_students)



