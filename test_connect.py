import psycopg2

try:
    conn = psycopg2.connect(
        user='webdb',
        password='webdb',
        host='192.168.0.10',
        port='5432',
        database='webdb'
    )
except Exception as e:
    print('error: {0}'.format(e))
finally:
    conn and conn.close()
