class TrafficTower:
    def __init__(self):
        self.aircrafts = []

    def register_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def send_message(self, sender, message):
        for aircraft in self.aircrafts:
            if aircraft != sender:
                aircraft.receive_message(message)


class Aircraft:
    def __init__(self, callsign, tower):
        self.callsign = callsign
        self.tower = tower

    def send_message(self, message):
        self.tower.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.callsign} received a message: {message}")


# Пример использования

tower = TrafficTower()

aircraft1 = Aircraft("Flight 001", tower)
aircraft2 = Aircraft("Flight 002", tower)
aircraft3 = Aircraft("Flight 003", tower)

tower.register_aircraft(aircraft1)
tower.register_aircraft(aircraft2)
tower.register_aircraft(aircraft3)

aircraft1.send_message("Hello, this is Flight 001. Requesting landing instructions.")
