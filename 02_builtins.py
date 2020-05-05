from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()

game = MyGame()

print(base.render)
print(__builtins__.camera)

game.run()

