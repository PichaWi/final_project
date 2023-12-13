# import database module
import os
from database import Database, Table, read_csv, write_csv


# define a function called initializing

def initializing(data_directory):
    tables = Database()
    for filename in os.listdir(data_directory):
        if filename.endswith(".csv"):
            table_name = os.path.splitext(filename)[0]
            table_data = read_csv(os.path.join(data_directory, filename))
            table = Table(table_name, table_data)
            tables.insert_table(table)
    return tables


# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database


# define a function called login

def login(users_table):
    name_in = input('Your username: ')
    pass_in = input('Your password: ')

    for user in users_table.table_data:
        if user['username'] == name_in and user['password'] == pass_in:
            return user['ID'], user['role']

    return None

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit(tables, data_directory):
    for table in tables.tables:
        write_csv(os.path.join(data_directory, f"{table.get_table_name()}.csv"), table.table_data)

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

if __name__ == "__main__":
    data_directory = 'C:\\Code for work\\Final_project'
    tables = initializing(data_directory)
    val = login(tables.search_table('login'))

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

    if val[1] and val== 'admin':
        pass
#see and do admin related activities
    elif val[1] and val == 'student':
        pass
#see and do student related activities
    elif val[1] and val == 'member':
        pass
#see and do member related activities
    elif val[1] and val == 'lead':
        pass
#see and do lead related activities
    elif val[1] and val == 'faculty':
        pass
    #see and do faculty related activities
    elif val[1] and val == 'advisor':
        pass
#see and do advisor related activities

# once everything is done, make a call to the exit function
    exit(tables, data_directory)
