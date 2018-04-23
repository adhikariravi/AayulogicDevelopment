## Aayulogic Development Week0: Apr16-Apr23

### Description of the Program


The program allows the manipulation of data in Userinfo table. The table contains the following structure:

|id| name| phone| email| bio| dob| gender| address| lat| long| image| hyperlink| 
|---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| ---| 
|integer                |character varying(50)  |character varying(50)  |character varying(100) |text                   |date                   |character(1)           |character varying(200) |character varying(100) |character varying(100) |character varying(100) |text                  |

There are multiple ways to interact with the database.

#### Interactive Shell
Interactive Shell can be run by using the following command:
```bash
root@system ~# python3 ishell.py
```
The Interactive Shell provides the following Menu:

Press one of the Menu keys and press Enter to proceed.
```
============================================================
Interactive Database
Options:
1. Insert INTO Database
2. Read FROM Database
3. Update User Info
4. Delete User Info

Type quit to close the program

root@web# 
```
Example :-
```
root@web# 1
```

### Arguments
Argument Shell has following parameters:

```
  -i, --insert          Insert UserInfo Into Database
  -u ,--update UPDATE	Update UserInfo From Database
  -d ,--delete DELETE	Delete UserInfo From Database using email
  -se,--search SEARCH	Search UserInfo From Database using email
  -so,--sort 			Sort UserInfo From Database using name or email as key
 ```
 Examples:-
 ```bash
 root@system ~# python3 argshell.py --insert
 root@system ~# python3 argshell.py --update someone@somewhere.com
 root@system ~# python3 argshell.py --delete someone@somewhere.com
 root@system ~# python3 argshell.py --search someone@somewhere.com
 root@system ~# python3 argshell.py --sort	 email|name
 ```
 ### Batch Insert
 Batch Insert the desired number of fake data into the database.
 ```bash
 root@system ~# python3 BatchInsert.py 50000 
 ```
 ### Dependencies
 The program relies on two external libraries:
 ```
 |- python3
 |- psycopg2
 |- faker
 ```
 Install the dependencies with:
 ```bash
 root@system ~# pip3 install psycopg2-binary faker
 ```
  
 ## Configuration
 
 The following file needs to be modified for establising the database connection:
 
 ./config/Config.py
 
 ```python3
 class PsqlConnectionParameters:
    USERNAME='postgres'
    PASSWORD='postgres'
    DATABASE='milrows'
    HOST='127.0.0.1'
    PORT='5432'

class SqliteConnectionParameters:
    DATABASE='config/web.db'
 
 ```
 
 Modify the selection of database from file ./config/CrudModule.py inside __init__ method in CrudModule class.
 ```python3
#self.dbEngine='SQLITE' 
self.dbEngine='POSTGRES'
```


 ## Folder Structure

```
|-README.md # This README file
|-sortDataRadix.py # Helper function to read and sort data retrieved from the database
|-argshell.py # Interaction Module 1
|-test_Crud.py # Helper program to test the connectivity of CrudModule
|-test_Connectivity.py	#Helper program to test the connectivity of Database.
|-config # The files containing database connection modules
|_______-load_json_data.py # The file that loads json data into sqlite.
|_______-Config.py # The file that defines database connectivity parameters
|_______-Connection.py # The database interaction Module
|_______-row200.json # json dump of 200 rows of data. Used for inserting with load_json_data.py file
|_______-web.db # sqlite database
|_______-CrudModule.py # Module that reacts to Database and User Interface commands.
|_______-test.log # Log file (currently unused)
|-BatchInsert.py # Insert fake data into database
|-Caching.py # Caching mechanism for fast retrieval (to be used after Threading). Unused.
|-ishell.py # Interaction Module 2
|-Library.py # Module that facilitates Radix Sort and Binary Search
```