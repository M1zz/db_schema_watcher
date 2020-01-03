# -*- coding: utf-8 -*-
#!/bin/sh
"""
    디비 테이블명 모두 가져오는 쿼리
"""


def get_tabel_name(db):
    try:
        cursor = db.cursor()
        sql = """
            SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'wadiz_db'
            """
        cursor.execute(sql)
        result = cursor.fetchall()

        all_table_name = []

        for item in result:
            all_table_name.append(item[0])
        return all_table_name
    except:
        return False

"""
    테이블 스키마 가져오는쿼리
"""


def get_table_schema(all_table_name, db):
    try:
        cursor = db.cursor()
        schema = []
        for table_name in all_table_name:
            sql = """
            show full columns from
                    """ + table_name
            cursor.execute(sql)
            result = cursor.fetchall()

            for item in result:
                schema.append((table_name, item))

        return schema
    except:
        return False
