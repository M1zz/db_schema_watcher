# -*- coding: utf-8 -*-
#!/bin/sh

from collector import get_tabel_name, get_table_schema
from config import DATABASE_CONFIG
import pymysql
import csv
from shutil import copyfile
from diff_print import diff_writer, diff_count
from sender import send_message


def main():
    print("start collect!")
    # collect
    config = DATABASE_CONFIG
    db = pymysql.connect(host=config['host'], port=config['port'], user=config['user'],
                         passwd=config['passwd'], db=config['db'], charset='utf8')

    copyfile(config['new'], config['old'])

    all_table_name = get_tabel_name(db)
    all_table_name.sort()
    schema = get_table_schema(all_table_name, db)
    new_schema_writer(config['new'], schema)

    diff_writer()
    if diff_count() > 1:
        print("send")
        send_message()

    print("end process")

    db.close()


def new_schema_writer(filename, schema):
    try:
        f = open(filename, 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)

        for row_data in schema:
            wr.writerow(row_data)
        f.close()
        return True
    except:
        return False


if __name__ == "__main__":
    main()
