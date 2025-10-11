import FreeSimpleGUI as sg
import persistence
from logics import MoneyMovements,Category,Table


def _main_menu():

    sg.theme('DarkBlue14')
    reader = persistence.load_data_window()
    val = persistence.load_data()
    
    headings = list(reader[0].keys())
    
    key_val = [[item[key] for key in headings] for item in reader]

    layout = [
        [sg.Text("Spendings and Incomes")],
        [sg.Table( values=key_val, max_col_width=25,headings=headings,key="-TABLE-"),sg.Button("Refresh List")],
        [sg.Button("New Category"),sg.Button("Add Spent"),sg.Button("Add Entry")],
        
    ]

    window = sg.Window("Personal Finance Manager", layout)

    while True:
            event, _ = window.read()
            
            if event == sg.WIN_CLOSED:
                break
            if event == "New Category":
                Category.new_category(val)
            if event == "Add Spent":
                MoneyMovements.add_spend_log(val)
            if event == "Add Entry":
                MoneyMovements.add_entry_log(val)
            if event == "Refresh List":
                Table.resfresh_list_display(window)
                
                

    window.close()

