#Write a recursive and non-recurssive function to calculate fibinacci numbers

class Fibonacci:
    def __init__(self, n:int, mode:int):
        if mode=='recurssive':
            print(self.recurssive(n))
        else:
            print(self.iterative(n))
    
    def recurssive(self, n: int):
        if n==0:
            return 0
        if n==1: 
            return 1
        return self.recurssive(n-1)+self.recurssive(n-2)


print(Fibonacci(10, 'recurssive'))
