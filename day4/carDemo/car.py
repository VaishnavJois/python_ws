class Car:
    c_gear = 0
    def __init__(self, reg_no , no_gears):
        self.reg_no = reg_no
        self.no_gears = no_gears
        self.is_started = False

    def start(self):
        if not self.is_started :
            print(f'Car with regno : {self.reg_no} started')
            self.is_started = True
        else:
            print('Car already started')
    def stop(self):
        if self.is_started:
            print(f'Car with regno : {self.reg_no} stopped')
            self.is_started = False
        else:
            print('Car already stopped')
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f'Car with regno : {self.reg_no} changed the gear to {self.c_gear}')
            else:
                print('Already in top gear')
        else:
            print('Car stoppped, cannot change the gear')

    def showInfo(self):
        print(f'Car with regno: {self.reg_no} , Gear status :{self.c_gear} ')
