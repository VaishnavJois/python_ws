import time
import random as rn
import dbcontext as db
from models import Internship , Student, Registration

from beautifultable import BeautifulTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
            print(f"Internship is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_internships():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
    except Exception as e:
        print(str(e))

def search_internship_by_name(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship where iname like '%'?'%'",(name,))
            
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
           
    except Exception as e:
        print(e)

def change_status_internship(n_id,n_status):
    try:
        with db.DbContext() as connection:
            cur = connection.cursor()
            cur.execute("update internship set status=? where id=?",(n_status,n_id))
            print(f'{n_id} status updated to {n_status}')
    except Exception as e:
        print(e)

def delete_internship(d):
    try:
        with db.DbContext() as connection:
            cur = connection.cursor()
            cur.execute("delete internship where id=?",(d,))
            print(f'{id} deleted')
    except Exception as e:
        print(e)

def add_student_internship(iid,usn,status):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into registration(iid,usn,status) values(?,?,?)",(iid,usn,status))
            print(f"Student is registered successfully to the internship with usn:{usn}")
    except Exception as e:
        print(str(e))

def view_all_reg_student():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select iid,usn,status from registration")
            rows = cursor.fetchall()
            student_reg_lst = [Registration(*row) for row in rows]
            _view_reg_list(student_reg_lst)
    except Exception as e:
        print(str(e))

def search_student_by_name(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select usn,name,sem,placed from student where name=?",(name,))
            rows = cursor.fetchone()
            st_lst = [Student(*row) for row in rows]
            _view_student_list(st_lst)
    except Exception as e:
        print(e)


def update_student(sid,sem):
    try:
        with db.DbContext() as conn:
            cur = conn.cursor()
            cur.execute("update student set sem=? where usn=?",(sem,sid))
    except Exception as e:
        print(e)


def delete_student(sid):
    pass


def company_ws_count():
    #internship table
    try:
        with db.DbContext() as connection:
            cursor  = connection.cursor()
            cursor.execute("select distinct(company), count(*) from internship group by company")
            rows = cursor.fetchall()
            table = BeautifulTable()
            table.column_headers = ["COMPANY", "# of workshops"]
            for row in rows:
                table.append_row([row[0],row[1]])
            #c_count = [Internship(*row) for row in rows]
            print(table)
            
    except Exception as e:
        print(e)

def student_ws_count():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select s.usn,s.name, count(*) from registration r join student s on (s.usn=r.usn) group by r.usn")
            rows = cursor.fetchall()
            table = BeautifulTable()
            table.column_headers = ["USN","NAME","COUNT"]
            for row in rows:
                table.append_row(row)
            print(table)
    except Exception as e:
        print(e)
def ws_student_reports():
    pass

def reg_stu_internship(usn):
    pass
    #registering student to register table
    #status = 0
    try:
        with db.DbContext() as connection:
            cursor  = connection.cursor()
            iid = _get_new_id()
            cursor.execute("insert into registration(iid,usn,status) values(?,?,?)",(iid,usn,0))
            print(f'Student with usn:{usn} registered successfully with id:{iid}')
    except Exception as e:
        print(e)

def update_stu_intership_status(n_sts,n_usn):
    try:
        with db.DbContext() as connection:
            cursor  = connection.cursor()
            cursor.execute("update registration set status=? where usn=?",(n_sts,n_usn))
            print(f'Student with usn:{n_usn} updated the status to {n_sts}')
    except Exception as e:
        print(e)
    #register table


def _view_internship_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
        for l in lst:
            status = "Completed" if l.status == 0 else "Going on" 
            table.append_row([l.id, l.iname, l.company, l.i_year,status])
        print(table)
    else:
        print(f"There are no Intership programms, yet to add...")

def _view_student_list(s):
    if s and len(s) > 0:
        table = BeautifulTable()
        table.column_headers = ["USN", "NAME", "SEM", "PLACED"]
        for l in s:
            table.append_row([l.usn,l.name,l.sem,l.placed])
        print(table)

def _view_reg_list(s_reg):
    if s_reg and len(s_reg) > 0:
        table = BeautifulTable()
        table.column_headers = ["IID", "USN", "STATUS"]
        for l in s_reg:
            status = "Completed" if l.status == 0 else "Going on"
            table.append_row([l.iid,l.usn,status])
        print(table)