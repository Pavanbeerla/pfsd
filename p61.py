class A():
    def fn1(self):
        print("base class")

class B(A):
     def fn2(self):
         print("dervied class")


class C(A,B):
    def fn3(self):
        print("new dervied class")



class D(A):
    def fn4(self):
        print("dervied of D")

class E(A):
    def fn5(self):
        print("derived of E")


ob=E()
ob.fn5()
ob.fn1()
