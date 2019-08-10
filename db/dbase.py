import sqlite3

host_name = "data.db"
def create_table():
    try:

        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()

        cursor.execute("create table student(regno integer primary key, name text, sem integer, placed integer)")
        
    except Exception as e:
        print(e)
    finally:
        conn.close()
#create_table()


def add_student(regno,name,sem,placed):
    try:
        con1 = sqlite3.connect(host_name)
        cur1 = con1.cursor()
        
        cur1.execute("insert into student(regno,name,sem,placed)values(?,?,?,?)",(regno,name,sem,placed))
        con1.commit()
    except Exception as e:
        print(e)
    finally:
        con1.close()

#add_student(100,'VR',7,0)
#add_student(101,'John Wick',7,1)
#add_student(102,'Baba Yaga',7,1)
def show_students():
    try:
        con2 = sqlite3.connect(host_name)
        cur2 = con2.cursor()
        cur2.execute("select regno,name,sem,placed from student")
        rows = cur2.fetchall()
        for row in rows:
            status = "Placed" if row[3] == 1 else "Not found"
            print(f'{row[0]},{row[1]},{row[2]} and {status}')
    except Exception as e:
        print(e)
    finally:
        con2.close()

show_students()


def update_student(regno, placed):
    try:
        con3 = sqlite3.connect(host_name)
        cur3 = con3.cursor()
        cur3.execute("update student set placed=? where regno=?",(placed,regno))
        con3.commit()
    except Exception as e:
        print(e)
    finally:
        con3.close()

update_student(100,1)
show_students()