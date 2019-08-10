from employee import Employee

def exer1():
    emp_1 = Employee(1,"Weirdo","M.Tech",50000,"CS")
    emp_2 = Employee(2,"Niffa","B.Tech",69696,"CS")

    emp_1.show_info()

    emp_2.show_info()

    emp_1.increment_sal(2000)

    emp_1.show_info()

    emp_2.show_info()

exer1()

lst_emp = []

def load_emp():
    with open("empdata.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            #print(data)
            ndata = data.strip('\n').split(',')
            empno = int(ndata[0])
            empname = ndata[1]
            qual = ndata[2]
            sal = int(ndata[3])
            dept = ndata[4]
            em = Employee(empno,empname,qual,sal,dept)
            lst_emp.append(em)
        print(f'Total count of employees: {len(lst_emp)}')


def showDeptName():
    dnames = set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)

def showAllQual():
    q = set(map(lambda emp:emp.qual,lst_emp))
    for qq in q:
        print(qq)

def maxSal():
    max1 = max(list(map(lambda m:m.sal , lst_emp)))

    allp = list(filter(lambda x:x.sal==max1,lst_emp))

    for p in allp:
        p.show_info()


def showTotalSalByDeptName():
    pass

def showEmpCountByQual():
    pass

def showEmpCountByDeptName():
    pass


print('***Employee')
load_emp()
print('***Department names:')
showDeptName()
print('***All qualifications')
showAllQual()
print('***Max salary')
maxSal()
