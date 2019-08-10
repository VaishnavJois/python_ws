class Employee:

    def __init__(self,empno,ename, qual,sal,dept_name):
        self.empno = empno
        self.ename = ename
        self.qual = qual
        self.sal = sal
        self.dept_name = dept_name

    def show_info(self):
        print(f'{self.empno} - {self.ename} - {self.qual} - {self.sal}')

    def increment_sal(self,inc_amt):
        self.sal += inc_amt
        print(f'Employee : {self.ename} salary after increment = {self.sal}')

    