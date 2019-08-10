from car import Car

lst = []
def BMW():
    bmw = Car("KA013060",5)
    lst.append(bmw)
    bmw.start()
    bmw.start()
    bmw.change_gear()
    bmw.stop()
    bmw.change_gear()
    bmw.stop()
    bmw.change_gear()
    bmw.start()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    #bmw.stop()

def McLaren():
    Mc = Car("KA017619",7)
    lst.append(Mc)
    Mc.start()
    #Mc.stop()

BMW()
McLaren()

for i in lst:
    i.showInfo()

c= len(list(filter(lambda x:x.is_started and x.c_gear,lst)))
print(f'Number of cars that has started : {c}')
