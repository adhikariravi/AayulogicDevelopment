from argparse import ArgumentParser
from ishell import InteractiveShell
from sortDataRadix import Data_Result_Searching
from config.CrudModule import UserCrud
from Library import SearchMethods
#
## Create a class that reads and responds to user arguments
## Acts like a modified form of ishell.py
#

class ArgParser:
    def __init__(self, *args, **kwargs):
        self.ish = InteractiveShell()
    
    def read_arguments(self):
        drs = Data_Result_Searching()
        ag_parser = ArgumentParser()
        ag_parser.add_argument('-i','--insert',help='Insert UserInfo Into Database',
        action='store_true')
        ag_parser.add_argument('-u','--update',help='update UserInfo From Database')
        ag_parser.add_argument('-d','--delete', help='delete UserInfo From Database')
        ag_parser.add_argument('-se','--search', help='search UserInfo From Database using email')
        ag_parser.add_argument('-so','--sort',help='sort UserInfo From Database',
        choices=['name','email'])
        agpa=ag_parser.parse_args()
        if(agpa.insert):
            self.ish.insert_into_user()
            affrow=self.ish.user_object.cursor_obj.rowcount
            print(f'{affrow} row affected')
        elif(agpa.update):
            self.ish.update_user_info(email=agpa.update)
        elif(agpa.delete):
            self.ish.delete_user_info(email=agpa.delete)
        elif(agpa.search):
            # print(SearchMethods.binary_search(emails,agpa.search))
            ## Call Library to search for email
            drs.generate_all_results()
            sorted_emails = drs.sorted_keys
            print(f'Email to search for {agpa.search}')
            index_of_key=SearchMethods.binary_search(sorted_emails,drs.remove_special(agpa.search))
            if index_of_key:
                print(f'The Email was found at index {index_of_key}')
                res = drs.get_result_by_email(drs.remove_special(agpa.search))
                print(res)    
            else:
                print('The Key was Not Found.')
            
        elif(agpa.sort):
            # emails = self.ish.emails
            ## Call Library to sort the values
            sorted_results=drs.return_all_results(agpa.sort)
            print(sorted_results)
            # print(f'Fetched {len(sorted_emails)} emails in {drs.total_time_to_fetch} seconds.')
            print(f'Sorted {len(sorted_results)} {agpa.sort} in {drs.total_time_to_sort} seconds.')


        
def main():
    ag = ArgParser()
    ag.read_arguments()

if __name__ == '__main__':
    main()


