class Employee:
    def accept(self, visitor):
        visitor.visit(self)


class Engineer(Employee):
    def work(self):
        print("Engineer is working")


class Manager(Employee):
    def work(self):
        print("Manager is working")


class Visitor:
    def visit(self, element):
        raise NotImplementedError


class VacationVisitor(Visitor):
    def visit(self, element):
        if isinstance(element, Engineer):
            print("Engineer is on vacation")
        elif isinstance(element, Manager):
            print("Manager is on vacation")


class PromotionVisitor(Visitor):
    def visit(self, element):
        if isinstance(element, Engineer):
            print("Engineer is promoted")
        elif isinstance(element, Manager):
            print("Manager is promoted")


# Пример использования

engineer = Engineer()
manager = Manager()

vacation_visitor = VacationVisitor()
promotion_visitor = PromotionVisitor()

engineer.accept(vacation_visitor)
engineer.accept(promotion_visitor)

manager.accept(vacation_visitor)
manager.accept(promotion_visitor)
