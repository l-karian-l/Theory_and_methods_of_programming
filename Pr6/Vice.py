class Image:
    def display(self):
        raise NotImplementedError


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")


class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def display(self):
        if self.image is None:
            self.image = RealImage(self.filename)
        self.image.display()


# Пример использования

image = ImageProxy("image.jpg")
# При вызове метода display() происходит загрузка и отображение изображения
image.display()
# При повторном вызове метода display() изображение загружается только один раз
image.display()
