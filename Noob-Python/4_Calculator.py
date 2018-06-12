#! /usr/bin/env python3

class cal():
    def __init__(self, a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a/self.b


a= int(input("Enter the First Number: "))
b = int(input("Enter the Second NUmber: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0: Exit")
