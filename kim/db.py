import pymysql

conn = pymysql.connect(host = 'localhost',
                       user = 'who',
                       password = '0000',
                       db = 'who_r_u',
                       charset = 'utf8')

def select():
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM quiz WHERE prob_id = %d'
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
    finally:
        conn.close()