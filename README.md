# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv

---

# List of file in this repository
## 1.project_manage.py, 
### this contain three def and two more def in main
#### 1.def initializing 
- this contain code that will read the csv file that will come from database and insert
- the table for it

#### 2.def login
- this contain to ask you to login by ask about username and password if there are
- that username it will continue in each role but if there none will exit code

#### 3.def exit
- this contain code to exit from the program and will save everything that other 
- member save

#### 4.def manage_database 
- this will manage by updating the table and list inside in database

#### 5.def faculty_activities
- this contain code for the faculty part like approve or evaluate part and response part
- from the faculty

## 2.database.py
### this contain two class and two more def 
#### 1.class Database
- this class make a simple task like insert and search function for table

#### 2.class Table
- this class contain some simple table function like filter, join and select 
- for the other this will work with if and elif code in project_manage.py 
- there insert and update entry that will update that if there are new ID
- and get def like get response and status of function and modify def if someone modify the table

#### 3.def read_csv_file
- this code duty is to read the new csv file that will come to the table

#### 4.def write_csv
- this code is for write a new table to database

---

## Csv file that are here
- 1.login.csv
- 2.persons.csv
- 3.member_pending.csv
- 4.project.csv
- 5.advisor_pending_request.csv

---

# How to run this file
- this code will run by first ask the person to put
- the username then the password if it wrong it will exit
- and if it there are this person in login table it will continue
- to the if and elif code part to check the role duty
- and show that what you can do and this code will auto 
- input the new csv file and update it

---

## Role

---
### Lead student
#### Method

1.1.Find and send invitation to
other student to join and work.

--Lead student have to find a member for a project
      work by sending invitation to them to join. 

## class Table

## Percentage
- 40 %

1.2.See and modify the project details.

--Lead student can see all the project detail and
      can modify it.

## class Table

## Percentage
- 80 %

1.3.Send request message to advisor.

--Send request message to advisor to ask or tell
      about the project report for now.

## class Table

## Percentage
- 30 %

1.4.Summit the final project report.

--Lead student have to be the one who have to 
summit the final project report to faculty to check.

## class Table

## Percentage
- 70 %

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Member student
#### Method
1.1.See and modify own project details.

--Member can see the current project details
and modify they own project detail that they make
into it.

## Percentage
- 60 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Student
#### Method
1.1.See the invitation message from the lead.

--See the invitation from lead student and can 
accept or deny the invitation to join and became 
member.

## Percentage
- 70 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Advisor faculty
#### Method
1.1.Send the request to be a supervisor.

--Send request to see or the project current work
and situation of it.

## class Table

## Percentage
- 20 %

1.2.Send accept or deny response.

--Can send accept or deny response to lead to know
if the response is correct or not.

## class Table

## Percentage
- 20 %

1.3.See details of all the project.

--Can see all the detail of project as like lead
student see.

## class Table

## Percentage
- 80 %

1.4.Evaluate projects.

--Can evaluate the project by they self.

## class Table

## Percentage
- 40 %

1.5.Approve project.

--Can approve the project that lead student have send.

## class Table

## Percentage
- 20 %

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Admin
#### Method
1.1.Managing database.

--Can managing the database and update all the 
details and all the tables there.

## Percentage
- 60 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### normal faculty
#### Method
1.1.See request to be supervisor.

--Can see the request from the advisor faculty
and can accept or deny that response.

## Percentage
- 50 %

## class Table

1.2.Evaluate project

--Can evaluate the project 

## Percentage
- 50 %

## class Table

1.3.Approve the project

--Can approve the project that have been send.

## Percentage
- 50 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---

# The missing feature in this file
- If you can see the missing part of the role code
- there are all the same because the exit program and 
- option of it doesn't work and before it is almost time '
- to send the work I now notice that all the problem come from
- the part in each role that some of them I didn't
- give part to go and it stuck and not run because it didn't knwo
- where to go so that make a lot of it doesn't work.
