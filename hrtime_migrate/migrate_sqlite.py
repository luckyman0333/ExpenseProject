import sqlite3, os, json, sys
from sqlite3 import Error

#json_path = ["db_card.json", "db_registration.json", "db_user.json"]

database = "hrtime.db"
pre_path = ".\\hrtime_migrate\\"
pre_path_json = ".\\hrtime_migrate\\"
db_with_prepath = "{}{}".format(pre_path, database)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def drop_db():
    """ delete sqlite3 database
    """
    if os.path.exists(db_with_prepath):
        try:
            os.remove(db_with_prepath)
        except Exception as e:
            print(e)


def create_db():
    """ create sqlite3 database with tables without data
    """
    sql_create_worker_table = """ CREATE TABLE IF NOT EXISTS Worker (
                                        id integer PRIMARY KEY,
                                        first_name text,
                                        last_name text,
                                        work_type text,
                                        act text,
                                        section text,
                                        teta_nr text
                                    ); """

    sql_create_card_table = """CREATE TABLE IF NOT EXISTS Card (
                                    id integer PRIMARY KEY,
                                    rfid text,
                                    card_nr text,
                                    id_worker integer,
                                    FOREIGN KEY (id_worker) REFERENCES Worker (id)
                                );"""

    sql_create_registration_table = """CREATE TABLE IF NOT EXISTS Registration (
                                    id integer PRIMARY KEY,
                                    datetime text,
                                    direction text,
                                    id_worker integer,
                                    id_card integer,
                                    FOREIGN KEY (id_worker) REFERENCES Worker (id),
                                    FOREIGN KEY (id_card) REFERENCES Card (id)
                                );"""
    
    # create a database connection
    conn = create_connection(db_with_prepath)

    # create tables
    if conn is not None:
        # create tables
        create_table(conn, sql_create_worker_table)
        create_table(conn, sql_create_card_table)
        create_table(conn, sql_create_registration_table)
    else:
        print("Error! cannot create the database connection.")
    
    conn.commit()
    #close the connection
    conn.close()



#############################################################
def transform_json(filename, table_name_in_json):
    """ transform data from json to database insert
    :param list_of_dics: [ {a : aa, b : bb}, ... ]
    :return: list of list of data for migration [ [a,b,c], ... ]
    """
    path = "{}{}".format(pre_path_json, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            source_data = json.load(json_file)
            list_of_dics = source_data[table_name_in_json]
            migrate_datas = []
            for dic_row in list_of_dics:
                row_values = []
                for k, v in dic_row.items(): 
                    row_values.append(v)
                migrate_datas.append(row_values)
            return migrate_datas
    
    else: 
        print("File not exist on path: {}".format(path))
        return None


def migrate_json(target):
        
        #create a database connection
        conn = create_connection(db_with_prepath)

        # create tables
        if conn is not None:
            # migrate datas
            if target in ["card", "all"]:
                migration_data = transform_json("db_card.json", "card")
                if not migration_data == None:
                    conn.executemany('INSERT INTO Card VALUES(?,?,?,?);', migration_data)

            if target in ["user", "worker", "all"]:
                migration_data = transform_json("db_user.json", "user")
                if not migration_data == None:
                    conn.executemany('INSERT INTO Worker VALUES(?,?,?,?,?,?,?);', migration_data)

            if target in ["registration", "all"]:
                migration_data = transform_json("db_registration.json", "registration")
                if not migration_data == None:
                    conn.executemany('INSERT INTO Registration VALUES(?,?,?,?,?);', migration_data)
        else:
            print("Error! cannot create the database connection.")
        
        conn.commit()
        #close the connection
        conn.close()

#drop_db()
#create_db()
#migrate_json("card")
#migrate_json("user")
#migrate_json("registration")
#migrate_json("all")
if len(sys.argv)>1:
    if sys.argv[1] == "recreate":
        drop_db()
        create_db()

    elif sys.argv[1] == "migrate":
        migrate_json("all")
    
    elif sys.argv[1] == "drop":
        drop_db()
    
    else: print("Set arg recreate, drop or migrate.")
else: print("Set arg recreate, drop or migrate.")