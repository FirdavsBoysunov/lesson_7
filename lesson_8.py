import psycopg2

db_params = {
    'database': 'lesson5',
    'user': 'postgres',
    'password': '112',
    'host': 'localhost',
    'port': '5432'
    }


    

class DBConnect:
    def __init__(self, db_connect) -> None:
        self.db_connect = db_connect
    
    
    def __enter__(self):
        self.db_conn = psycopg2.connect(**db_params)

        self.cur = self.db_conn.cursor()
        return self.db_conn, self.cur
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.db_conn:
            self.db_conn.close

        if self.cur:
            self.cur.close
##===================================

def select_query():
    with DBConnect(db_params) as (conn, cur):
        select_query = '''select * from student;'''
        cur.execute(select_query)
        rows = cur.fetchall()
        for i in rows:
            print(i)

# select_query()
##=======================================

# with DBConnect(db_params) as (conn, cur):
#     insert_into = '''insert into student(name, data)
#     values ('Tom', '{"address": "Qashqadaryo", "friends": ["Toor", "Alesa", "Nodir"], "phone_number": "+998944444455"}');
#     '''
#     cur.execute(insert_into)
#     conn.commit()
#     select_query() 

## ============================================

# with DBConnect(db_params) as (conn, cur):
#     update_query = '''update student set name = 'Toms' where id = 5;'''
#     cur.execute(update_query)
#     conn.commit()
#     select_query()

## ========================================

# with DBConnect(db_params) as (conn, cur):
#     delete_query = '''delete from student where id = 5;'''
#     cur.execute(delete_query)
#     conn.commit()
#     select_query()
