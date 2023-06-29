class Service:
    def perform_operation(self):
        raise NotImplementedError


class ServiceImplementation(Service):
    def perform_operation(self):
        print("Performing operation")


class Client:
    def __init__(self, service):
        self.service = service

    def do_work(self):
        self.service.perform_operation()


# Пример использования

service = ServiceImplementation()
client = Client(service)
client.do_work()
