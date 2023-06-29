# Продукт, который мы хотим построить
class Pizza:
    def __init__(self):
        self.crust = ""
        self.toppings = []
        self.sauce = ""

    def set_crust(self, crust):
        self.crust = crust

    def add_topping(self, topping):
        self.toppings.append(topping)

    def set_sauce(self, sauce):
        self.sauce = sauce

    def list_ingredients(self):
        print("Pizza ingredients:")
        print("Crust:", self.crust)
        print("Toppings:", ', '.join(self.toppings))
        print("Sauce:", self.sauce)


# Абстрактный Строитель
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_crust(self):
        pass

    def build_toppings(self):
        pass

    def build_sauce(self):
        pass

    def get_pizza(self):
        return self.pizza


# Конкретные Строители
class MargheritaPizzaBuilder(PizzaBuilder):
    def build_crust(self):
        self.pizza.set_crust("Thin crust")

    def build_toppings(self):
        self.pizza.add_topping("Cheese")
        self.pizza.add_topping("Tomatoes")
        self.pizza.add_topping("Basil")

    def build_sauce(self):
        self.pizza.set_sauce("Marinara sauce")


class PepperoniPizzaBuilder(PizzaBuilder):
    def build_crust(self):
        self.pizza.set_crust("Thick crust")

    def build_toppings(self):
        self.pizza.add_topping("Cheese")
        self.pizza.add_topping("Pepperoni")
        self.pizza.add_topping("Mushrooms")

    def build_sauce(self):
        self.pizza.set_sauce("Tomato sauce")


# Директор
class PizzaDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_crust()
        self.builder.build_toppings()
        self.builder.build_sauce()


# Клиентский код
def main():
    director = PizzaDirector()

    builder = MargheritaPizzaBuilder()
    director.set_builder(builder)

    director.construct_pizza()
    pizza = director.builder.get_pizza()

    pizza.list_ingredients()


if __name__ == '__main__':
    main()
