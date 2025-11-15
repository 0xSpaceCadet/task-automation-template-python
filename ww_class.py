from ezdxf.xref import detach


class SnAEmp: # pass
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.identifier = name + '@' + str(level)
        self.email = name + '@gmail.com'

    def details(self):
        returnable = ('{} and {} and {} and {}'.format(
            self.email, self.name, self.level, self.identifier)
        )
        return returnable

emp1 = SnAEmp('gamma', 2)
print(emp1.email, emp1.name, emp1.identifier, emp1.level)

print('{}, {}'.format(emp1.email, emp1.name))

print('mimmicking getter method\n\n', emp1.details())
