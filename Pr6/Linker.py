from abc import ABC, abstractmethod

# Абстрактный базовый класс компонента
class Component(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Конкретный компонент - раздел
class Section(Component):
    def __init__(self, name):
        self.name = name
        self.subcomponents = []

    def add_component(self, component):
        self.subcomponents.append(component)

    def remove_component(self, component):
        self.subcomponents.remove(component)

    def display_info(self):
        print(f"Section: {self.name}")

        for component in self.subcomponents:
            component.display_info()

# Конкретный компонент - элемент контента
class ContentItem(Component):
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Content item: {self.name}")

# Пример использования

# Создаем разделы
section1 = Section("Introduction")
section2 = Section("Body")
section3 = Section("Conclusion")

# Создаем элементы контента
content1 = ContentItem("Introduction content")
content2 = ContentItem("Body content 1")
content3 = ContentItem("Body content 2")
content4 = ContentItem("Conclusion content")

# Добавляем элементы контента в разделы
section1.add_component(content1)
section2.add_component(content2)
section2.add_component(content3)
section3.add_component(content4)

# Добавляем разделы в главный раздел
document = Section("Document")
document.add_component(section1)
document.add_component(section2)
document.add_component(section3)

# Обходим всю иерархию и выводим информацию о каждом компоненте
document.display_info()
