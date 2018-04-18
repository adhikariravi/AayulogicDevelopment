#
## Development of Interactive Shell for the User
#

from config.CrudModule import User_CRUD

class Interactive_Shell:
    def __init__(self):
        self.user_object = User_CRUD()

    def infinite_loop(self):
        while True:
            self.show_Menu()
            user_input=input()
            if(user_input=='1'):
                uv = self.get_user_input()
                self.user_object.insert(**uv)
            elif(user_input=='2'):
                args=[]
                kwargs={}
                print('Enter fields to be displayed\nPress Enter to show all columns')
                while True:
                    inp=input('>>> ')
                    if not inp:
                        break
                    args.append(inp)
                print('Enter filter fields to be selected seperated by space \nEnter to Quit ')
                while True:
                    inp=input('>>> ')
                    if not inp:
                        break
                    for key,value in inp.split(' '):
                        if key not in self.user_object.user_values:
                            print('Invalid Key!')
                            pass
                        kwargs[key]=value
                resultSet=self.user_object.read(*args,**kwargs)
                for row in resultSet.fetchall():
                    print(row)
            elif(user_input=='3'):
                pass
            elif(user_input=='4'):
                pass
            elif(user_input=='quit'):
                break
    
    def show_Menu(self):
        print("""
        Interactive Database Test
        Options:
        1. Insert INTO Database
        2. Read FROM Database
        3. Update User Info
        4. Delete User Info
        """)

    def get_user_input(self):
        user_values={}
        user_values['name']=input('Enter name  :')
        user_values['phone']=input('Enter phone  :')
        user_values['email']=input('Enter phone  :')
        user_values['bio']=input('Enter bio  :')
        user_values['dob']=input('Enter dob  :')
        user_values['gender']=input('Enter gender  :')
        user_values['address']=input('Enter address  :')
        user_values['lat']=input('Enter lat  :')
        user_values['long']=input('Enter long  :')
        user_values['image']=input('Enter image  :')
        user_values['hyperlink']=input('Enter hyperlink  :')
        return user_values

def main():
    ish=Interactive_Shell()
    ish.infinite_loop()


if __name__ == '__main__':
    main()