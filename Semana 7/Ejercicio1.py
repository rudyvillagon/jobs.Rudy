actual_number = 0  
menu_option =  0
user_selection = 0

def sumar():
    global actual_number                        
    Process_number = input("ingrese numero para a SUMAR: ")
    Process_number = int(Process_number)
    actual_number += (Process_number)
    print(actual_number)
            
def restar():
    global actual_number                         
    Process_number = input("ingrese numero para a RESTAR: ")
    Process_number = int(Process_number)
    actual_number -= (Process_number)
    print(actual_number)

def multiplicar():    
    global actual_number                        
    Process_number = input("ingrese numero para a MULTIPLICAR: ")
    Process_number = int(Process_number)
    actual_number *= (Process_number)
    print(actual_number)

def dividir():    
    global actual_number                           
    Process_number = input("ingrese numero para a DIVIDIR: ")
    Process_number = int(Process_number)
    actual_number /= (Process_number)      
    print(actual_number)

def borrar():    
    global actual_number               
    actual_number = 0
    print("Borró el numero acumulado")
    print(actual_number)   

def Error():
             
    if user_selection >= 6:

        raise ValueError()

def calulate(menu_option):
 
 while menu_option != 6:
 
    try: 
 
            menu_option = input("Ingrese una opcion  " 
            "1.Suma  "
            "2.Resta  "
            "3.Multiplicación  "
            "4.División  "
            "5.Borrar resultado:  "   )

            global user_selection
            user_selection = int(menu_option)
            
            if user_selection == 1:
                sumar()
            elif user_selection == 2:
                restar()
            elif user_selection == 3:
                multiplicar()
            elif user_selection == 4: 
                dividir()
            elif user_selection == 5:
                borrar()
            elif user_selection >= 6:
                Error()


    except ValueError as ex:
           print("**OPCIÓN INVALIDA** Ingrese un Numero Disponible") 




            
            
            

      
calulate(menu_option)




