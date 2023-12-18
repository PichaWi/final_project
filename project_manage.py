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

    def manage_database(tables):
        print("Database tables loaded:", [table.get_table_name() for table in tables.tables])

        for table in tables.tables:
            print(f"\nDetails for {table.get_table_name()}:")
            print(table.table_data)

        table_name_to_update = input("Enter the name of the table you want to update: ")

        if tables.search_table(table_name_to_update):
            print(f"Current data for {table_name_to_update}:")
            print(tables.search_table(table_name_to_update).table_data)

            updated_data = input("Enter the updated data (comma-separated values): ")
            updated_data_list = updated_data.split(',')

            tables.search_table(table_name_to_update).update_table(updated_data_list)
            print(f"{table_name_to_update} updated successfully.")
        else:
            print(f"Table {table_name_to_update} not found.")


    def faculty_activities(tables):
        project_table = tables.search_table('Project')

        # See requests to be a supervisor
        supervisor_requests = project_table.get_supervisor_requests()
        print("Supervisor requests:")
        print(supervisor_requests)
        response_to_supervisor_request = input("Enter your response to a supervisor request (accept/deny): ")
        project_table.respond_to_supervisor_request(response_to_supervisor_request)

        # Evaluate a project
        project_id_to_evaluate = input("Enter the ID of the project you want to evaluate: ")
        evaluation_score = input("Enter your evaluation score (out of 10): ")
        # Assuming the existence of an 'evaluate_project' function in your Table class
        project_table.evaluate_project(project_id_to_evaluate, evaluation_score)

        # Approve a project
        project_id_to_approve = input("Enter the ID of the project you want to approve: ")
        project_table.approve_project(project_id_to_approve)

        print("Faculty activities completed.")


# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

    if val and val[1] == 'admin':
        manage_database(tables)
#see and do admin related activities
    elif val and val[1] == 'student':
        student_table = tables.search_table('persons')
        student_id = val[0]

        # 1. See if there are pending requests to become members of already created projects
        member_requests = tables.search_table('member_pending_request').filter(lambda x: x['member_id'] == student_id)

        if member_requests:
            print("Pending requests to become members:")
            print(member_requests.table_data)

            # 2. Accept or deny the requests
            for request in member_requests.table_data:
                decision = input(f"Do you want to accept the request for project {request['project_id']}? (yes/no): ")

                if decision.lower() == 'yes':
                    # Update Member_pending_request table (remove the accepted request)
                    tables.search_table('member_pending_request').table_data.remove(request)

                    # Update Project table (set member status to 'accepted')
                    project_table = tables.search_table('project')
                    project_id = request['project_id']
                    project_table.update_entry('ID', project_id, lambda x: x['ID'] == project_id,
                                               {'member_status': 'accepted'})

                    print(f"Request for project {project_id} accepted.")
                else:
                    # Update Member_pending_request table (remove the denied request)
                    tables.search_table('member_pending_request').table_data.remove(request)
                    print(f"Request for project {request['project_id']} denied.")

        # 3. If more members needed, send out requests and update the member_pending_request table
        project_needs_members = tables.search_table('project').filter(lambda x: x['member_status'] == 'needed')

        for project in project_needs_members.table_data:
            if project['lead_id'] == student_id:
                # Skip projects where the student is already a lead
                continue

            # Check if the student is not yet a member
            if not any(member['project_id'] == project['ID'] for member in student_table.table_data):
                # Add a request to Member_pending_request table
                new_member_request = {'project_id': project['ID'], 'member_id': student_id}
                tables.search_table('member_pending_request').insert_entry(new_member_request)

                print(f"Request sent to join project {project['ID']}.")

    #see and do student related activities
    elif val and val[1] == 'member':
        member_table = tables.search_table('persons')

        id_count = len(set(item['ID'] for item in member_table.table_data))
        print(f"The 'persons' table has {id_count} unique IDs.")

        project_table = tables.search_table('project')

        member_project_id = tables.search_table('ID')
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
        # see and do lead related activities
        lead_project_id = tables.search_table('persons')

        # 1. See project status (pending member, pending advisor, or ready to solicit an advisor)
        status = tables.search_table('project').get_project_status(lead_project_id)
        print(f"Project status: {status}")

        # 2. See and modify project information
        # Display current project information
        print("Current project information:")
        print(tables.search_table('project').filter(lambda x: x['ID'] == lead_project_id).table_data)

        # Modify project information
        new_information = {'description': 'Updated description', 'deadline': '2023-12-31'}
        success = tables.search_table('project').modify_project_information(lead_project_id, new_information)

        if success:
            print("Project information modified successfully")
        else:
            print("Project not found")

        # 3. See who has responded to the requests sent out
        # Get responses to requests
        responses = tables.search_table('project').get_responses_to_requests(lead_project_id)
        print(f"Responses to requests: {responses}")

        # 4. Send out requests to potential members (Member_pending_request table needs to be updated)
        # Assuming 'member_pending_request' is the table for member pending requests
        member_pending_request_table = tables.search_table('member_pending_request')

        # Update Member_pending_request table with new requests
        new_member_requests = [{'project_id': lead_project_id, 'member_id': '456'},
                               {'project_id': lead_project_id, 'member_id': '789'}]
        member_pending_request_table.table_data.extend(new_member_requests)

        # 5. Send out requests to a potential advisor (Advisor_pending_request table needs to be updated)
        # Assuming 'advisor_pending_request' is the table for advisor pending requests
        advisor_pending_request_table = tables.search_table('advisor_pending_request')

        # Update Advisor_pending_request table with a new request
        new_advisor_request = {'project_id': lead_project_id, 'advisor_id': '101'}
        advisor_pending_request_table.table_data.append(new_advisor_request)

    #see and do lead related activities
    elif val and val[1] == 'faculty':
        faculty_activities(tables)
    #see and do faculty related activities
    elif val and val[1] == 'advisor':
        project_table = tables.search_table('Project')

        # Send a request to be a supervisor
        supervisor_request = input("Enter your request to be a supervisor: ")
        project_table.send_supervisor_request(supervisor_request)

        # Send request to see the current work and situation of a project
        project_id_to_view = input("Enter the ID of the project you want to view: ")
        project_table.send_project_view_request(project_id_to_view)

        # Send accept or deny response to lead
        lead_response = input("Enter your response to the lead (accept/deny): ")
        project_table.send_lead_response(lead_response)

        # See details of all projects
        all_projects = project_table.get_all_projects_details()
        print("Details of all projects:")
        print(all_projects)

        # Evaluate a project
        project_id_to_evaluate = input("Enter the ID of the project you want to evaluate: ")
        evaluation_score = input("Enter your evaluation score (out of 10): ")
        project_table.evaluate_project(project_id_to_evaluate, evaluation_score)

        # Approve a project
        project_id_to_approve = input("Enter the ID of the project you want to approve: ")
        project_table.approve_project(project_id_to_approve)

        print("Advisor activities completed.")
#see and do advisor related activities

# once everything is done, make a call to the exit function
    exit(tables, data_directory)
