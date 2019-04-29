import pymysql

conn = pymysql.connect(host = 'localhost',
                       user = 'who',
                       password = '0000',
                       db = 'who_r_u',
                       charset = 'utf8')


def choice(phase, num, gender, age, depart, depart_it, last_name, jeong_in_name):
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT NAME FROM aki WHERE phase = %s AND num = %s AND gender = %s AND age = %s AND depart = %s AND depart_it = %s AND last_name = %s AND jeong_in_name = %s'
            cursor.execute(sql, [phase, num, gender, age, depart, depart_it, last_name, jeong_in_name])
            row = cursor.fetchall()
            return row
    finally:
        conn.close()

