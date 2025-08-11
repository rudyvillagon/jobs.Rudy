class Student():
    def __init__(self, fullname, section, spa_grade, eng_grade, social_grade, sci_grade):
        self.fullname = fullname
        self.section = section
        self.spa_grade = spa_grade
        self.eng_grade = eng_grade
        self.social_grade = social_grade
        self.sci_grade = sci_grade

    
    def __str__(self):
        return (f"{self.fullname} | Section: {self.section} | "
                f"SPA: {self.spa_grade}, ENG: {self.eng_grade}, "
                f"SOC: {self.social_grade}, SCI: {self.sci_grade}")

    @staticmethod
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

    @staticmethod
    def new_student():

        student_list = []
        

        try:
            num_student = int(input("How many students do you want to register? "))
        except ValueError:
            print("Please enter a valid number.")
            return []

        for i in range(num_student):
            print(f" Student Registration {i + 1}:")
            fullname = input("Name: ")
            section = input("Section: ")
            spa_grade = Student.get_valid_int("Spanish Grade: ")
            eng_grade = Student.get_valid_int("English Grade: ")
            social_grade = Student.get_valid_int("Social studies Grade: ")
            sci_grade = Student.get_valid_int("Sciences Grade: ")


            student_list.append(Student(fullname,section,spa_grade,eng_grade,social_grade,sci_grade))

        return student_list
        

    
    @staticmethod
    def percentages_stu(student_list):
        student_percentages = {}
        
        for student in student_list:
            name = student.fullname
            grades = [
                student.spa_grade,
                student.eng_grade,
                student.social_grade,
                student.sci_grade
            ]
            percentage = sum(grades) / len(grades)
            student_percentages[name] = percentage
        
        
        sorted_students = sorted(student_percentages.items(), key=lambda item: item[1], reverse=True)

        
        top_3_students = sorted_students[:3]
        
        return sorted_students, top_3_students
        
        
    @staticmethod    
    def overall_percentage(sorted_students):
        
        total_of_averages = sum(student_tuple[1] for student_tuple in sorted_students)
        number_of_top_students = len(sorted_students)

        overall_average = total_of_averages / number_of_top_students
        print(f"Overall Average Grade: {overall_average:.2f}%")
        
    #new_student()
    #top_3_students, sorted_students = percentages_stu()
    #overall_percentage(sorted_students)



