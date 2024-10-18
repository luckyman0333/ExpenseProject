import sqlite3, os, json, argparse


parser = argparse.ArgumentParser(description="Migrate data from json to sqlite3.")
parser.add_argument('action')
parser.add_argument('-d', '--dbpath', help="Destination path for database (where DB should be).")
parser.add_argument('-f', '--file',   help="Name of file to migrate. Can insert more than one with repeat -f.", action="append")
args = parser.parse_args()

# print(args.dbpath)
# print(args.file)

action = args.action
db_path = args.dbpath
files_to_migrate = args.file


def migrate_json(json_path, c):
    """ take data from json and create database insert format
    list_of_dics: [ {a : aa, b : bb}, ... ]
    list of list of data for migration [ [a,b,c], ... ]
    """
    migrate_datas = []

    with open(json_path, 'r', encoding='utf-8') as json_file:
        source_data = json.load(json_file)
        table = source_data['destination_tabel']
        columns_order = source_data['destination_columns_order']
        data = source_data['data']
        
        for dic_row in data:
            row_values = []
            for k in columns_order:
                row_values.append(dic_row[k])
            migrate_datas.append(row_values)

    c.executemany('INSERT INTO {} VALUES(?{});'.format(table, ",?"*(len(columns_order)-1)), migrate_datas)


def run_migration():
    
    # # Json structure should be like:
    #
    #     {
    #     "destination_tabel": "Card",
    #     "destination_columns_order": ["id", "rfid", "card_nr", "id_user"],
    #     "data": [
    #         {
    #             "id" : 1,
    #             "rfid" : "2B003E5CCB94",
    #             "card_nr" : "4111697",
    #             "id_user" : 12332
    #         },
    ##

    if os.path.exists(db_path):

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        for json_path in files_to_migrate:
            if os.path.exists(json_path):
                print("> Migrate file: {}".format(json_path))
                migrate_json(json_path, c)
            else:
                print("> File not exist. Skip migration on: {}.".format(json_path))

        conn.commit()
        conn.close()
        print("> Migration complete!")

    else:
        print("> DB not exist!")


match action:
    case "migrate":
        run_migration()

    case _:
        pass