from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

game = MyGame()
game.run()

