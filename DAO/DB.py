import mysql.connector as mysql

class DB:
    
    def __init__(self) -> None:
        pass
    
    def connectToDB(self,host,user,password,databse):
        self.connection = mysql.connect(
        host=host,
        user=user,
        password=password,
        database=databse
        )
        return self.connection
    
    def closeDB(self):
        self.connection = self.connection.close()
        return self.connection
    