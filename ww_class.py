from ezdxf.xref import detach


class SnAEmp:  # pass
    raise_percent = 40
    batch_size = 0

    def __init__(self, name, level, ):
        self.name = name
        self.level = level
        self.identifier = name + '@' + str(level)
        self.email = name + '@gmail.com'
        self.pay = 10 if level <= 4 else 15

        SnAEmp.batch_size += 1  # class level not instance

    def details(self):
        returnable = ('{} and {} and {} and {}'.format(
            self.email, self.name, self.level, self.identifier)
        )
        return returnable

    def raise_rating(self):
        self.pay = int(self.pay * self.raise_percent // 100)  # instance raise
        # self.pay = int(self.pay * SnAEmp.raise_percent // 100)  # class raise modular


print(SnAEmp.batch_size)

emp1 = SnAEmp('gamma', 2)
print(emp1.email, emp1.name, emp1.identifier, emp1.level)
print('{}, {}'.format(emp1.email, emp1.name))

print('mimmicking getter method\n', emp1.details())  # from instance
print('mimmicking getter method\n', SnAEmp.details(emp1))  # from # class

print(SnAEmp.batch_size)
