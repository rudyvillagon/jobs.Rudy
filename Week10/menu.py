from actions import new_student, percentages_stu, overall_percentage
from data import student_csv, read_students_csv





def main_menu():
     print("\n=== Student Management Menu ===")
     print("1- Register an new Student")
     print("2- View the information of all students")
     print("3- View the top 3 best students base in averages grades")
     print("4- View the overall average of grades of all students")
     print("5- Export all actual data to a CSV file")
     print("6- Import data from a previous file")

     try:
          menu_choice = int(input("Select an option: "))
          return menu_choice
     except ValueError:
          print(" Invalid input. Please enter a number.")
          return -1


def menu_actions():
     student_list = []
     

     while True:

          choice = main_menu()

          if choice == 1 :
               new_students = new_student()  
               if new_students:
                    student_list.extend(new_students)
          elif choice == 2 :
               if student_list:
                    print("Student List:")
                    for student in student_list:
                         print(student)
          elif choice == 3 :
               if student_list:
                    sorted_students, top_3 = percentages_stu(student_list)
                    for name, avg in top_3:
                         print(f"{name}: {avg:.2f}%")
          elif choice == 4 :
               if student_list:
                    sorted_students, _ = percentages_stu(student_list)
                    overall_percentage(sorted_students)    
          elif choice == 5 :
               student_csv("student_list.csv", student_list)
          else:    
               student_list = read_students_csv()
               print("Data imported successfully.")


menu_actions()
