class Beverage:
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        raise NotImplementedError()

    def pour(self):
        print("Pouring into cup")

    def add_condiments(self):
        raise NotImplementedError()


class Coffee(Beverage):
    def brew(self):
        print("Brewing coffee")

    def add_condiments(self):
        print("Adding milk and sugar")


class Tea(Beverage):
    def brew(self):
        print("Steeping tea")

    def add_condiments(self):
        print("Adding lemon")


# Пример использования

coffee = Coffee()
print("Making coffee...")
coffee.prepare()

print("\n")

tea = Tea()
print("Making tea...")
tea.prepare()