import mysql.connector


class MySqlDB:

    def __init__(self):
        self.connectToDatabase()

    def connectToDatabase(self):
        try:

            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="dmsproject"
            )
            self.dbcursor = self.db.cursor()
            self.db.autocommit = True

            print("Connected to Database Successfully")

            return self.dbcursor

        except Exception as e:
            print("Error connecting to database")
            print(e)
            quit(-1)