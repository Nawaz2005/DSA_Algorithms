class a:
    def __init__(self):
        self.stack=list()
        self.max=int(input("ente the size"))
        self.top=-1
    def push(self,data):
        if self.top==self.max-1:
            print("over")
        else:
            self.top+=1
            self.stack.append(data)
    def pop(self):
        if self.top==-1:
            print("under")
        else:
            self.ad=self.stack.pop()
            print("del is:",self.ad)
            self.top-=1
    def display(self):
        if self.top==-1:
            print("emp")
        else:
            print(self.stack)
    def peek(self):
        if self.top==-1:
            print("emp")
        else:
            print(self.stack[self.top])

s=a()
while True:
    k=int(input("enter choice:"))
    if k==1:
        data=int(input("enter to add"))
        s.push(data)
    elif k==2:
        s.pop()
    elif k==3:
        s.display()
    elif k==4:
        s.peek()
    elif k==5:
        break
    else:
        print("invalid ")
