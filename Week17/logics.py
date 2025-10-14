
 
import persistence
import FreeSimpleGUI as sg

class Category:
    
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Category):
            return self.name == other.name
        return False

    @staticmethod
    def new_category(val):

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

class MoneyMovements:


    @staticmethod
    def add_spend_log(val):

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
                    if values["Input_title"] == "":
                        sg.popup_error("You must complete all the information ❗")
                        break
                    if values["Input_amount"] == "":
                        sg.popup_error("You must complete all the information ❗")
                        break
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

    
    @staticmethod
    def add_entry_log(val):
        
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
                    if values["Input_title"] == "":
                        sg.popup_error("You must complete all the information ❗")
                        break
                    if values["Input_amount"] == "":
                        sg.popup_error("You must complete all the information ❗")
                        break
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

