import FreeSimpleGUI as sg
import persistence

def fourth_menu_add_entry():
    sg.theme('DarkBlue14')



    layout = [
        [sg.Text("Title:")],
        [sg.Input(key = "Input_title")],
        [sg.Text("Amount:")],
        [sg.Input(key = "Input_amount")],
        [sg.Text("Category:")],
        [sg.Combo(values=persistence.load_data(), key='-COMBO-', readonly=True, size=(30, 1))],
        [sg.Button("Add File"),sg.Button("Cancel")],
        
    ]

    window = sg.Window("New Entry", layout)
    

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Add File":
            try:
                if values["-COMBO-"] == "":
                    sg.popup_error("You need to select a Category ❌")
                else:
                    new_file = {
                        "Title" : values["Input_title"],
                        "Amount" : values["Input_amount"],
                        "Category" : values["-COMBO-"],
                    }
                    
                    
                    if new_file and new_file not in val:
                        persistence.save_data_window(new_file)
                        sg.popup("File Added:", values["Input_title"])
                        break
            except ValueError:
                sg.popup_error("The Amount most be a Number")
            new_file = {
                "Title" : values["Input_title"],
                "Amount" : values["Input_amount"],
                "Category" : values["-COMBO-"],
            }

            
            persistence.save_data_window(new_file)
            sg.popup("Category Added:", values["Input_title"])
            break

    window.close()

def third_menu_add_spent(reader):
    sg.theme('DarkBlue14')

    

    layout = [
        [sg.Text("Title:")],
        [sg.Input(key = "Input_title")],
        [sg.Text("Amount:")],
        [sg.Input(default_text="-",key = "Input_amount")],
        [sg.Text("Category:")],
        [sg.Combo(values=persistence.load_data(), key='-COMBO-', readonly=True, size=(30, 1))],
        [sg.Button("Add File"),sg.Button("Cancel")],
        
    ]

    window = sg.Window("New Spent", layout)


    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Add File":
            try:
                if values["-COMBO-"] == "":
                    sg.popup_error("You need to select a Category ❌")
                else:
                    new_file = {
                        "Title" : values["Input_title"],
                        "Amount" : values["Input_amount"],
                        "Category" : values["-COMBO-"],
                    }
                    
                    
                    if new_file and new_file not in val:
                        persistence.save_data_window(new_file)
                        sg.popup("File Added:", values["Input_title"])
                        break
            except ValueError:
                sg.popup_error("The Amount most be a Number")
    window.close()

def second_manu_add_category(val):
    sg.theme('DarkBlue14')

    

    layout = [
        [sg.Text("New Category")],
        [sg.Input(key ="Input_Category")],
        [sg.Button("Add"),sg.Button("Cancel")],
        
    ]

    window = sg.Window("Personal Finance Manager", layout)


    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Add":
            text = values["Input_Category"].strip()
            if text and text not in val:
                val.append(text)
                persistence.save_data(val)
                sg.popup("Category Added:", text)
            break
        

    window.close()


def _main_manu(val,reader):
    sg.theme('DarkBlue14')

    headings = list(reader[0].keys())
    
    key_val = [[item[key] for key in headings] for item in reader]

    layout = [
        [sg.Text("Spendings and Incomes")],
        [sg.Table( values=key_val, max_col_width=25,headings=headings,key="-TABLE-"),sg.Button("Refresh List")],
        [sg.Button("New Category"),sg.Button("Add Spent"),sg.Button("Add Entry")],
        
    ]

    window = sg.Window("Personal Finance Manager", layout)


    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        if event == "New Category":
            second_manu_add_category(val)
        if event == "Add Spent":
            third_menu_add_spent(reader)
        if event == "Add Entry":
            fourth_menu_add_entry()   
        
    window.close()

reader = persistence.load_data_window()
val = persistence.load_data()
_main_manu(val,reader)