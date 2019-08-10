class Account:
    def __init__(self,accno,name,balance):
        self._accno = accno
        self._name = name
        self._balance = balance
    
    def get__accno(self):
        return self._accno

    def set__accno(self, _accno) :
        self._accno = _accno

    def get__name(self):
        return self._name
    
    def set__name(self, _name) :
        self._name = _name

    def get__balance(self):
        return self._balance
    
    def set__balance(self, _balance) :
        self._balance = _balance

    def deposit(self,amount):
        self._balance += amount
    
    def showInfo(self):
        print(f'{self._accno} : {self._name} : {self._balance} ')

P1 = Account(1001, "Suresh", 5000)
P1.deposit(4000)
print(P1.get__accno())
print(P1.get__balance())
P1.showInfo()


    