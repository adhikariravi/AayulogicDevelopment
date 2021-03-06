## Aayulogic Development Week0: Apr16-Apr23

### Description of the Program

The program was developed using python v3.6.3
Please refer to the python version with `root@system ~# python --version`

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

 ```
 root@system ~# python3 BatchInsert.py 50000 
 ```

### Dependencies

 The program relies on two external libraries:
 ```
 |- psycopg2
 |- faker
 ```
 Install the dependencies with:

 ```
 root@system ~# pip3 install psycopg2-binary faker
 ```
  
## Configuration

 The following file needs to be modified for establising the database connection:
 
 ./config/Config.py
 
```
 class PsqlConnectionParameters:
    USERNAME='postgres'
    PASSWORD='postgres'
    DATABASE='milrows'
    HOST='127.0.0.1'
    PORT='5432'

class SqliteConnectionParameters:
    DATABASE='config/web.db'
``` 
Modify the selection of database from file ./src/config/CrudModule.py inside __init__ method in CrudModule class.
```
#self.dbEngine='SQLITE' 
self.dbEngine='POSTGRES'
```


## Folder Structure

```
|-README.md                          # This README file
|-src                                # Root Directory of the project
|_____-sortDataRadix.py              # Helper function to read and sort data retrieved from the |_____atabase
|_____-argshell.py                   # Interaction Module 1
|_____-test_Crud.py                  # Helper program to test the connectivity of CrudModule
|_____-test_Connectivity.py	         # Helper program to test the connectivity of Database.
|_____-config                        # The files containing database connection modules
|____________-load_json_data.py      # The file that loads json data into sqlite.
|____________-Config.py              # The file that defines database connectivity parameters
|____________-Connection.py          # The database interaction Module
|____________-row200.json            # json dump of 200 rows of data. Used for inserting with |_____oad_json_data.py file
|____________-web.db                 # sqlite database
|____________-CrudModule.py          # Module that reacts to Database and User Interface commands.
|____________-test.log               # Log file (currently unused)
|_____-BatchInsert.py                # Insert fake data into database
|_____-Caching.py                    # Caching mechanism for fast retrieval (to be used after |_____hreading). Unused.
|_____-ishell.py                     # Interaction Module 2
|_____-Library.py                    # Module that facilitates Radix Sort and Binary Search
```