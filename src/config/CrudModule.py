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
        # dbObject = DatabaseConnection('SQLITE')
        dbObject=DatabaseConnection('POSTGRES')
        self.conn_obj = dbObject.connection
        self.cursor_obj = dbObject.cursor

    def create(self):
        # id INTEGER PRIMARY KEY,
        create_statement="""CREATE TABLE IF NOT EXISTS Userinfo(
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
        insert_statement="""
        INSERT INTO Userinfo (name, phone,email, bio, dob, gender, address, lat, long, image, hyperlink) 
        VALUES(:name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, :image, :hyperlink)"""
        self.cursor_obj.execute(insert_statement,kwargs)
        self.conn_obj.commit()
    
    @staticmethod
    def quote(field):
        return "'"+field+"'" if type(field) is str else str(field)

    def pg_insert(self,values,counter):
        #
        ## Skipping Field values to directly supply id
        #
        ins='INSERT INTO Userinfo(name, phone,email, bio, dob, gender, address, lat, long, image, hyperlink) values ('
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
        multi_insert_stmt="""
        INSERT INTO Userinfo (name, phone,email, bio, dob, gender, address, lat, long, image, hyperlink) 
        VALUES(:name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, :image, :hyperlink)"""
        self.cursor_obj.executemany(multi_insert_stmt,dictionary_list)
        self.conn_obj.commit()


    def read(self,*selectvalues,**kwargs):
        sv=['*'] if selectvalues is () else selectvalues
        read_statement='SELECT '+', '.join(sv)+' FROM Userinfo'
        selectives=[]
        for field, value in kwargs.items():
            selectives.append(str(str(field)+" = '"+str(value)+"'"))
        if selectives:
            read_statement+=' WHERE '+' AND '.join(selectives)
        self.cursor_obj.execute(read_statement)
        return self.cursor_obj.fetchall()
        
    def update(self,email_criteria, **uservalues):
        update_stmt = "UPDATE Userinfo SET"
        updates=[]
        for keys,values in uservalues.items():
            updates.append(' '+keys+' = "'+values+'"')
        update_stmt+=','.join(updates)+f' WHERE email="{email_criteria}"'
        self.cursor_obj.execute(update_stmt)

    def delete(self,email_criteria):
        delete_statement='DELETE FROM Userinfo WHERE email="'+email_criteria+'"'
        self.cursor_obj.execute(delete_statement)