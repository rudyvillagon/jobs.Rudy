import psycopg2


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name= db_name
        self.user= user
        self.password = password
        self.host = host
        self.port = port
        
        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")
        
    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

