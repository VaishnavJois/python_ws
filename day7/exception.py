'''
BaseException
TypeError
ValueError
ZeroDivisionError
'''

def firstType():
    n1 = int(input('Enter n1: '))
    n2 = int(input('Enter n2: '))
    try:
        print(n1//n2)
        print(n1**n2)
        print('Sum is :'+n1+n2)
    except ZeroDivisionError:
        print('{n2} cannot be zero')
    except ValueError:
        print('Please enter only Numbers..')
    except Exception as e:
        print(f'Something went wrong : {e}')

#firstType()

###################################################################################


def secondType():
    try:
        f = open('data.txt')
        n1 = 100
        n2 = 'a'
        print(n1/n2)
    except ZeroDivisionError:
        print('Division by zero error..')
    except TypeError:
        print('type error encountered..')
    except FileNotFoundError:
        print('File not found..')
    except Exception as i:
        print(i)
    finally:
        try:
            f.close()
        except:
            print('Nothing to close')
        print('Finally block executed..')

secondType()

###################################################################################

def thirdType():

    def castvote(age):
        assert age>=18, 'Age cannot be less than 18'
        print('Thanks for voting')

    try:
        age = int(input('Enter age: '))
        castvote(age)
    except AssertionError as a:
        print(f'assss {a}')

    else:
        print('Thanks for being 18+')
    finally:
        print('End')


thirdType()

###################################################################################

#using class that inherits exception class

def forthType():
    class MaxLimitError(Exception):

        def __init__(self,message):
            self.message = message

        def __str__(self):
            return f'{self.__class__.__name__} : {self.message}'

    c = 0
    def login(uname,pwd):
        global c
        if uname == 'root' and pwd == 'root':
            print('Login successful')
        else:
            print('Dirty credentials..!')
        c += 1
        if c>2:
            raise MaxLimitError('You have reached maximum number of attempt to login...')
    try:
        login('a','root')
        login('a','root')
        login('a','root')
        login('root','root')
    except Exception :
        print('One or more statements were not executed')

forthType()

###################################################################################

def fithType():
    class B(Exception):
        print('B class')

    class C(B):
        print('C class')

    class D(C):
        print('D class')

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")  #superclass should be handled last
fithType()    

###################################################################################