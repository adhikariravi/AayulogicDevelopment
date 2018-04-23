import psycopg2 as psql
import sqlite3 as sqll

from config.Config import PsqlConnectionParameters,SqliteConnectionParameters

class DatabaseConnection:
    
    def __init__(self,database_connection):
        #
        ## Dynamic Connection Selector
        #
        ## SQLITE Paramters
        #
        if(database_connection=='SQLITE'):
            self.engine=sqll
            self.connection=self.get_sqlite_connection()

        # POSTGRES Parameters
        elif(database_connection=='POSTGRES'):
            self.engine=psql
            self.connection=self.get_postgres_connection()
 
        # UNDEF Engine
        else:
            self.engine=None
        self.cursor=self.get_cursor()

    def get_postgres_connection(self):
        return self.engine.connect(
            database=PsqlConnectionParameters.DATABASE,
            user=PsqlConnectionParameters.USERNAME,
            password=PsqlConnectionParameters.PASSWORD,
            host=PsqlConnectionParameters.HOST,
            port=PsqlConnectionParameters.PORT)

    def get_sqlite_connection(self):
        return self.engine.connect(SqliteConnectionParameters.DATABASE)
    
    def get_cursor(self):
        return self.connection.cursor()