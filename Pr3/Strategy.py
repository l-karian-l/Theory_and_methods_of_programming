import random

class GameStrategy:
    def play(self):
        raise NotImplementedError()

class RockStrategy(GameStrategy):
    def play(self):
        print("Player chooses Rock")

class ScissorsStrategy(GameStrategy):
    def play(self):
        print("Player chooses Scissors")

class PaperStrategy(GameStrategy):
    def play(self):
        print("Player chooses Paper")

class Game:
    def __init__(self, strategy):
        self.strategy = strategy

    def play_game(self):
        self.strategy.play()
        self.strategy = random.choice([RockStrategy(), ScissorsStrategy(), PaperStrategy()])
        self.strategy.play()

# Пример использования

game = Game(RockStrategy())
game.play_game()
