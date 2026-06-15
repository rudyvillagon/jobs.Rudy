from flask import Flask, request, jsonify
import json

app = Flask(__name__)

#funcion para salvar datos
def save_data(tasks_list):
    with open("data_task.json", "w") as f:
        json.dump(tasks_list, f, indent=4)

#Funcion para cargar los datos
def load_data():
    try:
        with open("data_task.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
tasks_list = load_data()
# funcion para crear tasks 
@app.route("/tasks", methods=["POST"])
def tasks():
    
    try:
        if not request.is_json:
            return jsonify(message="The Information must be JSON Format"),400
        
        data = request.json

        required_fields = ["ID","Title","Description","Status"]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is missing from the information")
            
        if not data["Title"].strip():
            raise ValueError("It must have a Title")
        
        if not data["Description"].strip():
            raise ValueError("It must have a Description")

        valid_status = ["Pending", "In Progress", "Complete"]

        if data["Status"] not in valid_status:
            raise ValueError(
                "Invalid Status. Allowed values: Pending, In Progress, Complete"
            )

        for task in tasks_list:
            if task["ID"] == data["ID"]:
                return jsonify(message="ID is already in Use"),400
            
        new_task = {
                "ID" : data["ID"],
                "Title": data["Title"],
                "Description": data["Description"],
                "Status": data["Status"],
            }
        
        tasks_list.append(new_task)

        save_data(tasks_list)

        return jsonify(message="Task created successfully", task=new_task), 201
    
    except ValueError as ex:
        return jsonify(message=str(ex)), 400

#Funcion para que devuelva la lista
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_data())

#funcion para hacer un filtro con el parametro status
@app.route("/tasks", methods=["GET"])
def status_task():
    task_status = load_data()

    status_filter = request.args.get("Status")
    
    if status_filter:
        task_status = list(
            filter(lambda show: show["Status"] == status_filter, task_status)
            )

    return {"data": task_status}

#Funcion para modificar task ya registrado
@app.route("/tasks/<task_id>", methods=["PATCH"])
def patch_tasks(task_id):
    tasks_list = load_data()

    if not request.is_json:
            return jsonify(message="The Information must be JSON Format"),400

    data = request.json

    if not data:
        return jsonify(message="No data provided"), 400
    
    for task in tasks_list:
        if task["ID"] == task_id:

            if "Title" in data:
                task["Title"]= data["Title"]
            if "Description" in data:
                task["Description"]= data["Description"]
            if "Status" in data:
                valid_status = ["Pending", "In Progress", "Complete"]

                if data["Status"] not in valid_status:
                    return jsonify(
                        message="Invalid Status. Allowed values: Pending, In Progress, Complete"
                    ), 400

                task["Status"] = data["Status"]

            save_data(tasks_list)
    
            return  jsonify(message="task has been modified"), 200
    
    return jsonify(message="Task not found"), 404

#Funcion para eliminar algun task 
@app.route("/tasks/<task_id>", methods=["DELETE"])
def del_task(task_id):
    tasks_list = load_data()

    for task in tasks_list:
        if task["ID"] == task_id:
            tasks_list.remove(task)

            save_data(tasks_list)
            
            return jsonify(message="task has been deleted"),200
        
    return jsonify(message="Task not found"), 404



if  __name__ == "__main__":
    app.run(host="localhost", debug=True)