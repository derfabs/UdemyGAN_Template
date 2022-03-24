class Game:
    def __init__(self):
        self.bin_ich_pleite = False
        self.kontostand = 10

    def play_game(self):
        while self.bin_ich_pleite is False:
            print("Ich bin nicht pleite!", self.kontostand)
            self.kontostand -= 1
            if self.kontostand <= 0:
                self.bin_ich_pleite = True


my_game1 = Game()
my_game1.play_game()

my_game2 = Game()
my_game2.play_game()
