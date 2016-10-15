import sqlite3
import csv
from pprint import pprint

sqlite_file = 'mydb.db'    # name of the sqlite database file
conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

# Create the table, specifying the column names and data types:

### Create nodes table #############################################
cur.execute('''
    CREATE TABLE nodes(id INTEGER PRIMARY KEY, lat REAL, lon REAL,user TEXT,uid INTEGER,
                        version INTEGER, changeset TEXT, timestamp TEXT)
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('nodes.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['lat'], i['lon'], i['user'].decode("utf-8"), i['uid'], i['version'], i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

### Create nodes_tag table #############################################
cur.execute('''
    CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT,type TEXT, FOREIGN KEY (id) REFERENCES nodes (id))
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('nodes_tags.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['key'].decode("utf-8"),i['value'].decode("utf-8"), i['type'].decode("utf-8")) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO nodes_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()


### Create ways table #############################################
cur.execute('''
    CREATE TABLE ways(id INTEGER PRIMARY KEY, user TEXT,uid INTEGER,
                        version INTEGER, changeset TEXT, timestamp TEXT)
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('ways.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['user'].decode("utf-8"), i['uid'], i['version'], 
            i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO ways(id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

### Create ways_nodes table #############################################
cur.execute('''
    CREATE TABLE ways_nodes(id INTEGER, node_id INTEGER, position INTEGER,
                            FOREIGN KEY (id) REFERENCES ways (id),
                            FOREIGN KEY (node_id) REFERENCES nodes (id))
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('ways_nodes.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['node_id'], i['position']) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO ways_nodes(id, node_id, position) VALUES (?, ?, ?);", to_db)
# commit the changes
conn.commit()

### Create ways_tags table #############################################
cur.execute('''
    CREATE TABLE ways_tags(id INTEGER, key TEXT, value TEXT, type TEXT,
                            FOREIGN KEY (id) REFERENCES ways (id))
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('ways_tags.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['key'].decode("utf-8"), i['value'].decode("utf-8"),i['type'].decode("utf-8")) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO ways_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

### Create relations table #############################################
cur.execute('''
    CREATE TABLE relations(id INTEGER PRIMARY KEY, user TEXT, uid INTEGER, version INTEGER,
                           changeset TEXT, timestamp TEXT)
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('relations.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['user'].decode("utf-8"), i['uid'], i['version'], 
            i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO relations(id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

### Create ways_nodes table #############################################
cur.execute('''
    CREATE TABLE relations_members(id INTEGER, member_id INTEGER, role TEXT,
                                    type TEXT, position INTEGER,
                                    FOREIGN KEY (id) REFERENCES relations (id))
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('relations_members.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['member_id'], i['role'].decode("utf-8"), i['type'].decode("utf-8"),
            i['position']) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO relations_members(id, member_id, role, type, position) VALUES (?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

### Create relations_tags table #############################################
cur.execute('''
    CREATE TABLE relations_tags(id INTEGER, key TEXT, value TEXT, type TEXT,
                            FOREIGN KEY (id) REFERENCES relations (id))
''')
# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('relations_tags.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['key'].decode("utf-8"), i['value'].decode("utf-8"),i['type'].decode("utf-8")) for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO relations_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

conn.close()