# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file
import csv, os
import copy

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_csv_file(filename):
    file_path = os.path.join(__location__, filename)
    data = []
    with open(file_path) as file:
        rows = csv.DictReader(file)
        for row in rows:
            data.append(dict(row))
    return data


def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# add in code for a Database class
class Database:
    def __init__(self):
        self.tables = []

    def insert_table(self, table):
        self.tables.append(table)

    def search_table(self, table_name):
        for table in self.tables:
            if table.get_table_name() == table_name:
                return table
        return None
# add in code for a Table class


class Table:
    def __init__(self, table_name, table_data):
        self.table_name = table_name
        self.table_data = table_data

    def join(self, other_table, common_key):
        joined_table = Table(f"{self.table_name}_join_{other_table.table_name}", [])
        for item1 in self.table_data:
            for item2 in other_table.table_data:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table_data.append(dict1)
        return joined_table

    def filter(self, condition):
        filter_table = Table(f"{self.table_name}_filtered", [])
        for item3 in self.table_data:
            if condition(item3):
                filter_table.table_data.append(item3)
        return filter_table

    def select(self, attribute_list):
        select_table = Table(f"{self.table_name}_selected", [])
        for item4 in self.table_data:
            dict_fill = {key: item4[key] for key in item4 if key in attribute_list}
            select_table.table_data.append(dict_fill)
        return select_table

    def insert_entry(self, entry):
        self.table_data.append(entry)

    def update_entry(self, entry_key, entry_value, condition):
        for item in self.table_data:
            if condition(item):
                item[entry_key] = entry_value

    def get_table_name(self):
        return self.table_name

    def __str__(self):
        return f"{self.table_name}:{str(self.table_data)}"


# Create a Database instance
persons = read_csv_file('persons.csv')
login = read_csv_file('login.csv')
project = read_csv_file('project.csv')
advisor_pending_request = read_csv_file('advisor_pending_request.csv')
member_pending_request = read_csv_file('member_pending_request.csv')
# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
