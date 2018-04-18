#
## Import SQlite3 for Python and Test Connectivity
#

import sqlite3
from sqlite3 import Error
import logging

'''
    Author: Ravi Adhikari
    Description: CRUD Module Designed facilitating Create, Read, Update and Delete
                 Unique Identifier Used: email
                 User_CRUD
                    |-__init__()
                    |-create() # Creates Table
                    |-get_kwargs(**kwargs) #create a dictionary containing '' for values not provided by User
                    |-insert(**kwargs) # Inserts rows into Database based on kwargs sent by user
                    |-read(**kwargs) # Returns all matching records matching criteria
                    |-update() # Update fields based on matching criteria | email
                    |-delete() # Delete row value based on matching criteria | email
'''
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_file_handler = logging.FileHandler('test.log')
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.ERROR)
logger.addHandler(log_file_handler)
logger.addHandler(console_handler)

class User_CRUD:
    def __init__(self):
        self.conn_obj = sqlite3.connect('/home/developer/Aayulogic/AayulogicDevelopment/Week0/config/web.db')
        self.cursor_obj = self.conn_obj.cursor()
        self.user_values=['name', 'phone','email', 'bio',
                          'dob', 'gender', 'address', 'lat', 'long', 'image', 'hyperlink']
    def create(self):
        create_statement="""CREATE TABLE IF NOT EXISTS User(
                            id INTEGER PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            phone VARCHAR(10) ,
                            email VARCHAR(100),
                            bio TEXT,
                            dob DATE,
                            gender INT NOT NULL,
                            address VARCHAR(200),
                            lat VARCHAR(100),
                            long VARCHAR(100),
                            image BLOB,
                            hyperlink TEXT)"""
        self.cursor_obj.execute(create_statement)
    
    def insert(self,**kwargs):
        for field in self.user_values:
            kwargs[field]=kwargs.get(field,'')
        logger.info(kwargs)
        insert_statement="""
        INSERT INTO User (name, phone,email, bio, dob, gender, address, lat, long, image, hyperlink) 
        VALUES(:name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, :image, :hyperlink)"""
        resultset=self.cursor_obj.execute(insert_statement,kwargs)
        if(resultset):
            logger.info('Inserted Successfully')
        self.conn_obj.commit()

    def read(self,*selectvalues,**kwargs):
        read_statement="SELECT "+', '.join(selectvalues)+' FROM User '
        selectives=[]
        for field, value in kwargs.items():
            selectives.append(str(str(field)+' = "'+str(value)+'"'))
        if selectives:
            read_statement+='WHERE '+' AND '.join(selectives)
        print(read_statement)
        resultset = self.cursor_obj.execute(read_statement)
        return resultset
        
    def update(self,email_criteria, **uservalues):
        update_stmt = "UPDATE User SET"
        updates=[]
        for keys,values in uservalues.items():
            updates.append(' '+keys+' = "'+values+'"')
        update_stmt+=','.join(updates)+f' WHERE email="{email_criteria}"'
        self.cursor_obj.execute(update_stmt)

    def delete(self,email_criteria):
        delete_statement='DELETE FROM User WHERE email="'+email_criteria+'"'
        self.cursor_obj.execute(delete_statement)