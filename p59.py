class A:
    def fn1(self):
        print("base class")

class B(A):
    def fn2(self):
        print("dervied class")

class C(A):
    def fn3(self):
        print("dervied class 1")



ob=B()
ob.fn2()
ob.fn1()
