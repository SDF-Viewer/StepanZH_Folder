class A:
    def __init__(self, a, b):
        self.a=a
        self.b=b
class B(A):
    def __init__(self, a, b):
        A.__init__()
        self.c = a + b
    def f(self):
        return self.a+self.b

B = B(1, 4)
print(B.c)
