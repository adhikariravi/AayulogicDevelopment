import sys
import time
from re import sub as substitute
from faker import Faker

from config.CrudModule import UserCrud

class MultiInsert:
    def process_insert(self,no_records):
        uc=UserCrud()
        uc.create() # Create table if not exists
        counter=1
        st = time.process_time()
        while counter<no_records+1:
            insert_list=self.get_thousand_list_rows()            
            for fd in insert_list:
                uc.pg_insert(fd,counter)
                ## Print the inserted rows after every 10,000 rows inserted.
                if(counter%10000==0):
                    ed=time.process_time()
                    print('[Batch:10,000]Inserted ',counter,' Records In Total ',ed-st,' sec.')
                counter+=1

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

def main():
    mi = MultiInsert()
    mi.process_insert(int(sys.argv[1]))

if __name__ == '__main__':
    main()