class Employee:
    def __init__(self, empno=None, name=None, salary=None) -> None:
        self.empno = empno
        self.name = name
        self.salary = salary

    def print(self):
        print(f'ID      : {self.empno}')
        print(f'Name    : {self.name}')
        print(f'Salary  : Rs. {self.salary}')
        print()

    def __iadd__(self, value):
        if type(value) == str:
            self.name += value
        elif type(value) in (int, float):
            self.salary += value
        
        return self
    
    def __gt__(self, value):
        if value is not None and type(value) in (int, float):
            return self.salary > value
        if value is not None and type(value) is Employee:
            return self.salary > value.salary
        
        raise ValueError('Invalid value supplied. Please try with number or Employee object')


def main():
    e1 = Employee(1122, 'Rajesh', 45000)
    e2 = Employee(6271, 'Umesh', 55000)

    e1 += ' Kumar'  # expectation --> RHS should be concatenated to e1.name
    e2 += 2500  # expectation --> RHS should be added to the salary

    e1.print()
    e2.print()

    if e1 > e2:  # if e2 < e1:
        print(f'{e1.name} earns more than {e2.name}')
    else:
        print(f'{e1.name} does not earn more than {e2.name}')

    e1.f1(10, 20)



if __name__ == '__main__':
    main()

