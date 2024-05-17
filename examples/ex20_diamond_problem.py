class A:
    def f1(self):
        print('A.f1() called')


class B(A):
    def f1(self):
        print('B.f1() called')


class C(A):
    def f1(self):
        print('C.f1() called')


class D(B, C):
    def f1(self):
        print('D.f1() called')


if __name__ == '__main__':
    d1 = D()
    d1.f1()
    print(D.mro())
    C.f1(d1)
    A.f1(d1)
