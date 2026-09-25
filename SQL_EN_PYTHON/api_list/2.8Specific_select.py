import psycopg2

from pprint import pprint

def create_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="123456",
        dbname="car_rental"
    )

    print("DataBASE Established Connection")
    return connection

def format_car(car_list):
    return {
        "id" : car_list[0],
        "brand" : car_list[1],
        "model" : car_list[2],
        "fabrication_year" : car_list[3]
    }

def get_available_cars(connection):

    cursor = connection.cursor()

    request_body = {
        "car_status" : 1
    }

    car_status = request_body.get("car_status")

    try:
        cursor.execute(
            "SELECT c.id, b.brand_name, c.model, c.fabrication_year FROM lyfter_car_rental.cars c JOIN lyfter_car_rental.Brands_cars b ON c.brand = b.id WHERE car_status= %s",
            (car_status,)
        )

        results = cursor.fetchall()

        formatted_results = [format_car(car_list) for car_list in results]

        cursor.close()

        return formatted_results
    
    except Exception as error:
        print("Error gatting all cars from the Database.", error)
        return False

    finally:
        cursor.close()

def get_rented_cars(connection):

    cursor = connection.cursor()

    request_body = {
        "car_status" : 2
    }

    car_status = request_body.get("car_status")

    try:
        cursor.execute(
            "SELECT c.id, b.brand_name, c.model, c.fabrication_year FROM lyfter_car_rental.cars c JOIN lyfter_car_rental.Brands_cars b ON c.brand = b.id WHERE car_status= %s",
            (car_status,)
        )

        results = cursor.fetchall()

        formatted_results = [format_car(car_list) for car_list in results]

        cursor.close()

        return formatted_results
    
    except Exception as error:
        print("Error gatting all rented cars from the Database.", error)
        return False

    finally:
        cursor.close()

connection = create_connection()

cars_available = get_available_cars(connection)

cars_rented = get_rented_cars(connection)

print("Cars Rented")
pprint(cars_rented)

print("Cars Available")
pprint(cars_available)


connection.close()    