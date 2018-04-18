#
## Load json Data into db
## Success
#

import json
import sqlite3

class JSONLoader:
    def __init__(self,file):
        self.file=file
        self.conn_obj = sqlite3.connect('web.db')
        self.cursor_obj = self.conn_obj.cursor()

    def insert_json_data(self):
        #
        ## Implementing Multi Batch Insert
        # 
        ## Directly using crud object's cursor to execute statement
        all_data=self.get_json_data_from_file()
        self.cursor_obj.executemany('''INSERT INTO User (
            name, phone,email, bio, dob, gender, address, lat, long, image, hyperlink)
            VALUES(:name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, :image, :hyperlink)''',all_data)
        self.conn_obj.commit()
        self.conn_obj.close()
        exit(0)
        
    def get_json_data_from_file(self):
        all_data=json.load(open(self.file))
        return all_data

    def load(self):
        self.insert_json_data()

jsn = JSONLoader('/home/developer/Aayulogic/AAYULOGIC_BACKUP_MODULES/data1.json')
jsn.insert_json_data()