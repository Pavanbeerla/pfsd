class Base1:
    def fn1(self):
        print("Base class")


class Base2:
    def fn2(self):
        print("Base2 class")


class Dervied:
    def fn3(Base1,Base2):
        print("Dervied classes")


ob=Dervied()
ob.fn3

