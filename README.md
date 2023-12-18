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
#### Action

1.1.Find and send invitation to
other student to join and work.

#### Method
- send_request 
- search

## class Table

## Percentage
- 40 %
- 
#### Action

1.2.See and modify the project details.

#### Method

- look
- update

## class Table

## Percentage
- 80 %

#### Action

1.3.Send request message to advisor.

#### Method

- send_request

## class Table

## Percentage
- 30 %

#### Action

1.4.Summit the final project report.

#### Method

- summit

## class Table

## Percentage
- 70 %

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Member student
#### Action

1.1.See and modify own project details.

#### Method

- look
- update

## Percentage
- 60 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Student
#### Action

1.1.See the invitation message from the lead.

#### Method

- look

## Percentage
- 70 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Advisor faculty
#### Action

1.1.Send the request to be a supervisor.

#### Method

- send_request

## class Table

## Percentage
- 20 %

#### Action

1.2.Send accept or deny response.

#### Method

- send_request
- accept or deny

## class Table

## Percentage
- 20 %

#### Action

1.3.See details of all the project.

#### Method

- look

## class Table

## Percentage
- 80 %

#### Action

1.4.Evaluate projects.

#### Method

- update
- insert

## class Table

## Percentage
- 40 %

#### Action

1.5.Approve project.

#### Method

- send_approve

## class Table

## Percentage
- 20 %

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### Admin
#### Action

1.1.Managing database.

#### Method

- update
- insert

## Percentage
- 60 %

## class Table

## missing part
- Code didn't show the option and suddenly 
- exit of it code and some part of it didn't work

---
### normal faculty
#### Action

1.1.See request to be supervisor.

#### Method

- look
- accept or deny

## Percentage
- 50 %

## class Table

#### Action

1.2.Evaluate project

#### Method

- update
- insert

## Percentage
- 50 %

## class Table

#### Action

1.3.Approve the project

#### Method

- send_approve

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
