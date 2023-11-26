# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for Item6 in rows:
        persons.append(dict(Item6))
print(persons)

logins = []
with open(os.path.join(__location__, 'login.csv')) as f:
    rows = csv.DictReader(f)
    for Item5 in rows:
        logins.append(dict(Item5))


# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []
    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None
# add in code for a Table class
import copy
class Table:
    def __init__(self, table_name, table):
        self.__table_name = table_name
        self.__table = table

    @property
    def new_name(self, new_name):
        self._new_name = new_name

    @new_name.setter
    def new_name(self, new_name):
        self._new_name = new_name

    def join(self, other_table, common_key):
        joined_table = Table(self.__table_name + '_join_' + other_table.table_name, [])
        for Item1 in self.__table:
            for Item2 in other_table.table_name:
                if Item1[common_key] == Item2[common_key]:
                    dict1 = copy.deepcopy(Item1)
                    dict2 = copy.deepcopy(Item2)
                    dict1.update(dict2)
                    joined_table.__table.append(dict1)
        return joined_table

    def filter(self, condition):
        filter_table = Table(self.__table_name + '_filtered_', [])
        for Item3 in self.__table:
            if condition(Item3):
                filter_table.__table.append(Item3)
        return filter_table

    def select(self, attribute_list):
        select_table = Table(self.__table_name + '_selected_', [])
        fills = []
        for Item4 in self.__table:
            dict_fill = {}
            for key in Item4:
                if key in attribute_list:
                    dict_fill[key] = Item4[key]
            fills.append(dict_fill)
        return select_table


    def __str__(self):
        return self.__table_name + ':' + str(self.__table)


table1 = Table('persons', persons)
table2 = Table('logins', logins)
print(table2)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
