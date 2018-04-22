#
## Import SQlite3 for Python and Test Connectivity
#

import sqlite3

from config.Connection import DatabaseConnection

'''
    Author: Ravi Adhikari
    Description: CRUD Module Designed facilitating Create, Read, Update and Delete
                 Unique Identifier Used: email
                 UserCrud
                    |-__init__()    # Initialization 
                    |-create()      # Creates User Table
                    |-get_kwargs()  # Create a dictionary containing '' for values not provided by User
                    |-insert()      # Inserts rows into Database based on kwargs sent by user
                    |-read()        # Returns all matching records matching criteria
                    |-update()      # Update fields based on matching criteria | email
                    |-delete()      # Delete row value based on matching criteria | email
'''
#
## Convert the methods to accept and modify a dynamic model
#

class UserCrud:
    user_values=['name', 'phone','email', 'bio', 'dob','gender',
                 'address', 'lat', 'long', 'image', 'hyperlink']
    
    def __init__(self):
        # self.dbEngine='SQLITE' 
        self.dbEngine='POSTGRES'
        dbObject = DatabaseConnection(self.dbEngine)
        self.conn_obj = dbObject.connection
        self.cursor_obj = dbObject.cursor
        self.insert_statement='INSERT INTO Userinfo ('+','.join(self.user_values)+') VALUES ('

    def create(self):
        # id INTEGER PRIMARY KEY,
        auto_inc_field='id INTEGER PRIMARY KEY,' if self.dbEngine =='SQLITE'\
         else 'id SERIAL PRIMARY KEY,' if self.dbEngine=='POSTGRES' else 'id INT PRIMARY KEY,'
        create_statement="CREATE TABLE IF NOT EXISTS Userinfo("+auto_inc_field+"""
                            name VARCHAR(50) NOT NULL,
                            phone VARCHAR(50) ,
                            email VARCHAR(100),
                            bio TEXT,
                            dob DATE,
                            gender CHAR(1) ,
                            address VARCHAR(200),
                            lat VARCHAR(100),
                            long VARCHAR(100),
                            image VARCHAR(100),
                            hyperlink TEXT)"""
        self.cursor_obj.execute(create_statement)
        self.conn_obj.commit()
    
    def insert(self,**kwargs):
        for field in self.user_values:
            kwargs[field]=kwargs.get(field,'')
        insert_statement=self.insert_statement
        insert_statement+=' :name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, :image, :hyperlink)'
        self.cursor_obj.execute(insert_statement,kwargs)
        self.conn_obj.commit()
    
    def multi_insert_query(self,list_values):
        multi_insert_stmt=self.insert_statement
        additives=list()
        for row in list_values:
            tuple_ = list()
            for field in row.values():
                tuple_.append(self.quote(field))
            additives.append(','.join(tuple_))
        self.cursor_obj.execute(multi_insert_stmt+'),('.join(additives)+')')
        self.conn_obj.commit()

    def insert_query(self,**kwargs):
        values=list()
        for field in self.user_values:
            values.append(self.quote(kwargs[field]))
        insert_statement=self.insert_statement+','.join(values)+')'
        print(insert_statement)
        self.cursor_obj.execute(insert_statement)
        self.conn_obj.commit()

    @staticmethod
    def quote(field):
        return "'"+field+"'" if type(field) is str else str(field)

    def pg_insert(self,values,counter=100):
        #
        ## Skipping Field values to directly supply id
        ## Counter -> Commits to database every 100th record
        #
        ins=self.insert_statement
        insertees=list()
        for each_value in values:
            insertees.append(self.quote(each_value))
        final_stmt=ins+','.join(insertees)+')'
        self.cursor_obj.execute(final_stmt)
        if(int(counter%100)==0):
            self.conn_obj.commit()
        
    # @staticmethod
    # def get_kwargs(**kwargs):
    #     for field in self.user_values:
    #         kwargs[field]=kwargs.get(field,'')
    #     return kwargs

    def batch_insert(self,dictionary_list):
        #
        ## Considering the batch insert is automated using a module
        ## We will not check if all the values in kwargs are set.
        #
        multi_insert_stmt='INSERT INTO Userinfo ('+','.join(self.user_values)+' ) VALUES (' 
        multi_insert_stmt+=':name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, :image, :hyperlink)'
        self.cursor_obj.executemany(multi_insert_stmt,dictionary_list)
        self.conn_obj.commit()


    def read(self,*selectvalues,**kwargs):
        sv=['*'] if selectvalues is () else selectvalues
        read_statement='SELECT '+', '.join(sv)+' FROM Userinfo'
        selectives=[]
        for field, value in kwargs.items():
            selectives.append(str(field)+" = '"+str(value)+"'")
        if selectives:
            read_statement+=' WHERE '+' AND '.join(selectives)
        self.cursor_obj.execute(read_statement)
        return self.cursor_obj.fetchall()
        
    def update(self,email_criteria, **uservalues):
        update_stmt = "UPDATE Userinfo SET"
        updates=[]
        for keys,values in uservalues.items():
            updates.append(' '+keys+' = "'+values+'"')
        update_stmt+=','.join(updates)+f" WHERE email='{email_criteria}'"
        self.cursor_obj.execute(update_stmt)

    def delete(self,email_criteria):
        delete_statement="DELETE FROM Userinfo WHERE email='"+email_criteria+"'"
        self.cursor_obj.execute(delete_statement)
    
class CrudModuleModelized:
    #
    ## Create a new file Models.py to store the models and their definitions
    ## __ALPHA__
    #

    class UserInfo:
        #
        ## Define Field name and set its value to desired property
        #

        NAME='VARCHAR(100)'
        PHONE='VARCHAR(50)'
        EMAIL='VARCHAR(50)'
        BIO='TEXT'
        DOB='DATE'
        GENDER='CHAR(1)'
        ADDRESS='VARCHAR(200)'
        LAT='VARCHAR(30)'
        LONG='VARCHAR(30)'
        IMAGE='VARCHAR(100)' # CHANGE IT TO BLOB
        HYPERLINK='VARCHAR(500)'