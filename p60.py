class A():
    def fn1(self):
        print("base class")

class B(A):
    def fn2(self):
        print("dervied class1")


class C(A):
    def fn3(self):
        print("dervied class2")



ob=C()
ob.fn3()
ob.fn1()
