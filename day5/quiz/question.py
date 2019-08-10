class Question:

    def __init__(self,qdata,op1,op2,op3,op4,ans):
        self.qdata = qdata
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.ans = ans

    def __str__(self):
        return f'{self.qdata}\nA.{self.op1}\nB.{self.op2}\nC.{self.op3}\nD.{self.op4}'
