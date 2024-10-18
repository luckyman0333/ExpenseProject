import sqlite3, argparse, os


#json_path = ["db_card.json", "db_registration.json", "db_user.json"]

parser = argparse.ArgumentParser(description="Create sqlite3 db for hrtime.")
parser.add_argument('action')
parser.add_argument('-d', '--dbpath', help="Destination path for database (where DB should be).")
args = parser.parse_args()

# print(args.dbpath)

action = args.action
db_path = args.dbpath


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
    
    conn = sqlite3.connect(db_path)

    if conn is not None:
        c = conn.cursor()
        c.execute(sql_create_worker_table)
        c.execute(sql_create_card_table)
        c.execute(sql_create_registration_table)
        conn.commit()
    
    conn.close()


match action:
    case "reinit":
        if os.path.exists(db_path): os.remove(db_path)
        print("> Droped DB.")
        create_db()
        print("> Created DB.")
        
    case "init":
        create_db()
        print("> Created DB.")
        
    case _:
        pass
        