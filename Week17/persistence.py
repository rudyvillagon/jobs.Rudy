import json
import os 



#data_arch = "data.json"
#data_table = "data_table.json"



def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)



def load_data_window():
    if os.path.exists("data_table.json"):
        try:
            with open("data_table.json", "r", encoding="utf-8") as f:
                reader = json.load(f)
                if isinstance(reader, dict):
                    return [reader]  
                elif isinstance(reader, list):
                    return reader
        except json.JSONDecodeError:
            pass  
    return []         


def save_data_window(new_file):
    reader = load_data_window()
    reader.append(new_file)

    with open("data_table.json", 'w', encoding='utf-8') as file:
        json.dump(reader, file, ensure_ascii=False, indent=4)