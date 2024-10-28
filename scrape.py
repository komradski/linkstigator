import sqlite3

database = 'db.sqlite3'

# conn = sqlite3.connect(database)

# import sqlite3

def organization_all():
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM modeltest_organization')
            rows = cur.fetchall()
            # for row in rows:
            #     print(row)
    except sqlite3.Error as e:
        print(e)
    return rows

def link_all():
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM modeltest_link')
            rows = cur.fetchall()
            # for row in rows:
            #     print(row)
    except sqlite3.Error as e:
        print(e)
    return rows

for x in link_all():
    print(x)