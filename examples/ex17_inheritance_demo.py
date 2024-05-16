class Person:  # class Person(object):
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Name   : {self.name}')
        print(f'Email  : {self.email}')


class Student(Person):
    def __init__(self, **kwargs) -> None:
        # Person.__init__(self, **kwargs)
        super().__init__(**kwargs)
        self.rollno = kwargs.get('rollno')
        self.gpa = kwargs.get('gpa')

    def print(self):
        print(f'Roll#  : {self.rollno}')
        # Person.print(self)
        super().print()
        print(f'GPA    : {self.gpa}')
        

class Employee(Person):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.empno = kwargs.get('empno')
        self.salary = kwargs.get('salary')

    def print(self):
        print(f'Emp#   : {self.empno}')
        super().print()
        print(f'Salary : {self.salary}')


def main():
    s1 = Student(name='Kishore', email='kishore@xmpl.com', rollno=9181, gpa=4.9)
    s1.print()
    print()

    e1 = Employee(empno=1234, salary=45000, name='Kiran', email='kiran@xmpl.com')
    e1.print()
    

if __name__ == '__main__':
    main()
