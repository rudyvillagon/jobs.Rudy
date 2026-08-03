from werkzeug.security import generate_password_hash

class AddUser:

    def __init__(self, database):
        self.connection = database.connection
        

    def add_user(self, data):

        user_fullname = data.get("user_fullname")
        email = data.get("email")
        user_name = data.get("user_name")
        password = data.get("password")
        date_birth = data.get("date_birth")
        user_status = data.get("user_status")

        password_hash = generate_password_hash(password)

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT email FROM lyfter_car_rental.users WHERE email = %s",
                (email,)
            )

            result =  cursor.fetchone()

            if result is not None:
                print("The email is already in Use.")

            else:

                cursor.execute(
                    "INSERT INTO lyfter_car_rental.Users (user_fullname, email, user_name, password, date_birth, user_status) values (%s, %s, %s, %s, %s, %s);", (user_fullname, email, user_name, password_hash, date_birth, user_status)
                )

                self.connection.commit()
                print("Query executed")
                print("Successful Commit, User added")

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

