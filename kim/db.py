import pymysql

conn = pymysql.connect(host = 'localhost',
                       user = 'who',
                       password = '0000',
                       db = 'who_r_u',
                       charset = 'utf8')


def choice(phase, num, gender, age, depart):
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM aki WHERE phase = %s AND num = %s AND gender = %s AND age = %s AND depart = %s'
            cursor.execute(sql, [phase, num, gender, age, depart])
            row = cursor.fetchall()
            return row
    finally:
        conn.close()

