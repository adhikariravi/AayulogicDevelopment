from config.ConnectionModule import DBHandler

# Conneciton Object
c_obj = DBHandler('test.db')
# Connection Cursor
c_cur = c_obj.get_Connection()
statement="""CREATE TABLE IF NOT EXISTS User(
	id INTEGER AUTO INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	phone VARCHAR(10) UNIQUE,
	email VARCHAR(100) UNIQUE,
	bio TEXT,
	dob DATE,
	gender INT NOT NULL,
	address VARCHAR(200),
	lat VARCHAR(100),
	long VARCHAR(100),
	image BLOB,
	hyperlink TEXT)"""
c_cur.execute(statement)
# c_obj.commit()
# print('Enter name')
# user_values['name']=input()
# print('Enter phone')
# user_values['phone']=input()
# print('Enter bio')
# user_values['bio']=input()
# print('Enter dob')
# user_values['dob']=input()
# print('Enter gender')
# user_values['gender']=input()
# print('Enter address')
# user_values['address']=input()
# print('Enter lat')
# user_values['lat']=input()
# print('Enter long')
# user_values['long']=input()
# print('Enter image')
# user_values['image']=input()
# print('Enter hyperlink')
# user_values['hyperlink']=input()
# import time
# time.sleep(5)
# INSERT_SEQUENCE = ['name', 'phone', 'bio', 'dob', 'gender', 
# 'address', 'lat', 'long', 'image', 'hyperlink']
# vals =[]
# for each_key in INSERT_SEQUENCE:
# 	vals.append(str(user_values[each_key]))
	# insert_statement+=''+user_values[each_key]
# print(insert_statement+','.join(vals))
user_values={
	'name':'ravi',
	'phone': '9849898007',
	'bio': ' Test String',
	'email': 'ravi.adhikari@aayulogic.com',
	'dob': '2063-94-05',
	'gender': 1,
	'address': 'Biratnagar',
	'lat': '87.0000192',
	'long': '83.035321',
	'image': 'fghjk',
	'hyperlink':'http://facebook.com/ravi.adhikary'
}
print(user_values)
insert_statement="""INSERT INTO User
(name, phone,email, bio, dob, gender, address, lat, long, image, hyperlink)
VALUES(:name, :phone, :email, :bio, :dob, :gender, :address, :lat, :long, 
:image, :hyperlink)"""
c_cur.execute(insert_statement,user_values)
c_obj.close_connection()
