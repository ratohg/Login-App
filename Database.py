import mysql.connector as connector

class DataBase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.status_connection = False
    def connect(self):
        if self.status_connection:
            print("Is \033[31mconnected\033[m")
            return
        self.connection = connector.connect(host=self.host, user=self.user, password=self.password,
                                            database=self.database)
        self.cursor = self.connection.cursor()
        self.status_connection = True
        print("\033[32mConnected to Data Base\033[m")
    def disconnect(self):
        if not self.status_connection:
            print("Is \033[31mdisconnected\033[m")
            return
        self.connection.close()
        self.cursor.close()
        self.status_connection = False
        print("\033[33mDisconnected to Data Base\033[m")
    def edit(self, command):
        self.cursor.execute(command)
        self.connection.commit()
    def read(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()
