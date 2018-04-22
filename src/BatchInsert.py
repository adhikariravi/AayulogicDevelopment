import time
from re import sub as substitute
from faker import Faker

from config.CrudModule import UserCrud

class MultiInsert:
    def process_insert(self,no_records):
        uc=UserCrud()
        counter=0
        st = time.process_time()
        while counter<no_records:
            insert_list=self.get_thousand_list_rows()            
            for fd in insert_list:
                uc.pg_insert(fd,counter)
                if(counter%1000==0):
                    ed=time.process_time()
                    print('Inserted ',counter,' Records In Total ',ed-st,' sec.')
                counter+=1
        
    #
    ## Check modulo 1000 to insert data every 1000 iterations
    #

    #
    ## Check Time to Calculate for each 1000 iterations
    #

    # @staticmethod
    # def get_thousand_dict_rows():
    #     fake = Faker()
    #     append_list=list()
    #     st = time.process_time()
    #     for counter in range(1000):
    #         data=dict()
    #         data['name']=fake.name()
    #         data['phone']=substitute('[^0-9\-\(\)]','',fake.phone_number())
    #         data['bio']=fake.sentence()
    #         data['dob']=fake.date()
    #         data['gender']='M' if counter%3==0 else 'F' if counter %2==0 else 'O' 
    #         data['address']=substitute('\\n',' ',fake.address())
    #         data['lat']=float(fake.latitude()) 
    #         data['long']=float(fake.longitude())
    #         data['image']=fake.image_url()
    #         data['hyperlink']=fake.uri()
    #         append_list.append(data)
    #     ed = time.process_time()
    #     print('\nGenerated 1000 Fake Data in ' ,ed -st,' sec.\n' )
    #     return append_list

    @staticmethod
    def get_thousand_list_rows():
        fake = Faker()
        append_list=list()
        st = time.process_time()
        for counter in range(10000):
            data=list()
            data.append(fake.name())
            data.append(substitute('[^0-9\-\(\)]','',fake.phone_number()))
            data.append(fake.email())
            data.append(fake.sentence())
            data.append(fake.date())
            data.append('M' if counter%3==0 else 'F' if counter %2==0 else 'O' )
            data.append(substitute('\\n',' ',fake.address()))
            data.append(float(fake.latitude()) )
            data.append(float(fake.longitude()))
            data.append(fake.image_url())
            data.append(fake.uri())
            append_list.append(data)
        ed = time.process_time()
        print('\nGenerated 10,000 Fake Data in ' ,ed -st,' sec.\n' )
        return append_list
