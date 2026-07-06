def add(a,b):
    return a+b

def multiply( a, b ):
        result=a*b
        return result

class Calculator:
    def __init__(self,start=0):
        self.value=start
    def add(self,x):
        self.value+=x
        return self.value
