class Stack:
    def __init__(self):
        self.st = []

    def push(self):
        ele = int(input('Enter the element to be pushed: '))
        self.st.append(ele)
        print('Element pushed')

    def is_empty(self):
        if len(self.st)==0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            d = self.st.pop()
            print(f'Deleted element is {d}')
    
    def search(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            c = 0
            s = int(input('Enter the element to be searched: '))
            for i in self.st:
                c += 1
                if s == i:    
                    print(f'Key {s} found at location {c}')
                    break
            
            print('Key not found')

    def show(self):
        if not self.is_empty():
            for i in self.st:
                print(i,end=' ',sep=',')
        else:
            print('Nothing to show')
    

if __name__ == "__main__":
    s = Stack()
    print()
    opt_dict = {1:s.push , 2:s.pop , 3:s.search , 4:s.show , 5:exit}
    
    while True:
        print('1.Push 2.Pop 3.Search 4.Display 5.EXIT')
        try:
            choice = int(input('Enter your choice:'))
            ref = opt_dict[choice]
            ref()
        except (KeyError,ValueError):
            print('Enter a valid choice')
    