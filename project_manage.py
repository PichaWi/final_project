# import database module
import os, csv
from database import Database, Table, read_csv_file, write_csv

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# define a function called initializing

def initializing(data_directory):
    tables = Database()
    for filename in os.listdir(data_directory):
        if filename.endswith(".csv"):
            table_name = os.path.splitext(filename)[0]
            table_data = read_csv_file(os.path.join(data_directory, filename))
            table = Table(table_name, table_data)
            tables.insert_table(table)

    # Debugging print statements
    print("Tables loaded:", [table.get_table_name() for table in tables.tables])

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

    print("Login failed. Invalid credentials or user not found.")
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
    data_directory = 'C:\\Code for work\\Final_project\\final_project'
    tables = initializing(data_directory)
    login_data = read_csv_file(os.path.join(data_directory, 'login.csv'))
    login_table = tables.search_table('login')
    val = login(login_table)


# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

    if val and val[1] == 'admin':
        pass
#see and do admin related activities
    elif val and val[1] == 'student':
        pass
#see and do student related activities
    elif val and val[1] == 'member':
        member_table = tables.search_table('persons')

        # Display the count of unique IDs in the 'persons' table
        id_count = len(set(item['ID'] for item in member_table.table_data))
        print(f"The 'persons' table has {id_count} unique IDs.")

        # Assuming 'project' table has project information
        project_table = tables.search_table('project')

        # Member-specific activities
        member_project_id = '123'  # Replace with the actual project ID for the member
        status = project_table.get_project_status(member_project_id)
        print(f"Project status: {status}")

        # Modify project information
        new_information = {'description': 'Updated description', 'deadline': '2023-12-31'}
        success = project_table.modify_project_information(member_project_id, new_information)

        if success:
            print("Project information modified successfully")
        else:
            print("Project not found")

        # Get responses to requests
        responses = project_table.get_responses_to_requests(member_project_id)
        print(f"Responses to requests: {responses}")

#see and do member related activities
    elif val and val[1] == 'lead':
        pass
#see and do lead related activities
    elif val and val[1] == 'faculty':
        pass
    #see and do faculty related activities
    elif val and val[1] == 'advisor':
        pass
#see and do advisor related activities

# once everything is done, make a call to the exit function
    exit(tables, data_directory)
