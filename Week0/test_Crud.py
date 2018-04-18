#
## Module to Test the functionality of User_CRUD class
#

from config.CrudModule import User_CRUD
crudObj = User_CRUD()

uservalues={
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
# crudObj.cursor_obj.execute('DROP TABLE User')
# ex=crudObj.create()
# for _ in range(10):
    # ex =crudObj.insert(**uservalues)
result=crudObj.read(*['id','name','email'],**{'id':1,'name':'ravi'})
print(result.fetchall())
# crudObj.update('ravi.adhikary@aayulogic.com',**{'name': 'Ravi','email':'raviadhiakry1996@gmail.com'})
# crudObj.delete('ravi.adhikari@aayulogic.com')
crudObj.conn_obj.commit()
crudObj.conn_obj.close()